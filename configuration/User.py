import os
import random

from faker import Faker


class User:
    def __init__(self):
        self.__user_config_dir = os.path.join(os.path.dirname(__file__), "users")
        self.email = ''
        self.password = ''
        self.city = ''
        self.first_name = ''
        self.username = ''
        self.birthdate = ''
        self.accept_toc = ''

    def new(self, save_on_disk=False):
        fake = Faker()
        self.email = fake.safe_email()
        self.password = fake.password(special_chars=False)
        self.city = fake.city()
        self.first_name = fake.first_name()
        self.username = self.email
        self.birthdate = fake.date_time_between(start_date="-36y", end_date="-13y").strftime("%m / %d / %Y")
        self.accept_toc = True

        if save_on_disk:
            self.__save_to_file()

        return self

    def from_file(self, filename=None):
        if filename is None:
            files = [f for f
                     in os.listdir(self.__user_config_dir)
                     if os.path.isfile(os.path.join(self.__user_config_dir, f))
                     and not f.startswith('.')
                     ]
            filename = random.choice(files)

        self.__file = os.path.join(self.__user_config_dir, filename)

        with open(self.__file, 'r', encoding='utf-8') as fh:
            for line in fh:
                item, value = line.split(" ", 1)
                setattr(self, item, value.strip())
        return self

    def delete_file(self):
        try:
            os.remove(self.__file)
        except (OSError, AttributeError) as e:
            pass

    def __save_to_file(self):
        file = os.path.join(self.__user_config_dir, self.email)
        with open(file, 'w', encoding='utf-8') as fh:
            for item, value in vars(self).items():
                if not item.startswith("_"):
                    fh.write("{} {}\n".format(item, value))
