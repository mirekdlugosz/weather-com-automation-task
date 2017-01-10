import os

from faker import Faker


class User:
    def __init__(self):
        self.__user_config_dir = os.path.join(os.path.dirname(__file__), "users")
        self.email = ''
        self.password = ''
        self.city = ''
        self.accept_toc = ''

    def new(self, save_on_disk=False):
        fake = Faker()
        self.email = fake.safe_email()
        self.password = fake.password()
        self.city = fake.city()
        self.accept_toc = True

        if save_on_disk:
            self.__save_to_file()

        return self

    def from_file(self, filename=None):
        if filename is None:
            pass
        file = os.path.join(self.__user_config_dir, filename)
        with open(file, 'r', encoding='utf-8') as fh:
            for line in fh:
                item, value = line.split(" ", 1)
                setattr(self, item, value.strip())
        return self

    def __save_to_file(self):
        file = os.path.join(self.__user_config_dir, self.email)
        with open(file, 'w', encoding='utf-8') as fh:
            for item, value in vars(self).items():
                fh.write("{} {}\n".format(item, value))