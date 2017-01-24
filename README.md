# Weather.com automation scripts

## Purpose

This is automated test for Weather.com website that fulfills following requirements:

TEST CASE 1: LOGIN TO THE APPLICATION
- Open https://weather.com/ page
- Press Sign Up link
- Enter email and password in order to register
- Press Sign Up button
- Enter your location (city) and choose suggestion from the list
- Press Done button
- Check that you're logged in
- Logout

TEST CASE 2: UPDATE ACCOUNT DATA
- Login to the application using credentials of previously created account
- Go to My profile > Edit profile
- Update your data (first name, username, birthdate) 
- Press save button
- Check that your data was updated successfully 
- Logout

TEST CASE 3: DELETE ACCOUNT
- Login to the application
- Delete account
- Check that you're not able to login with user/pass for deleted account

## Prerequisites

- Python 3
- Chrome web browser (<https://www.google.com/chrome/browser/desktop/>)
- Chrome Selenium webdriver (<https://sites.google.com/a/chromium.org/chromedriver/downloads>) in your PATH
- python selenium 2.53 (<https://pypi.python.org/pypi/selenium>)
- python faker library (<https://pypi.python.org/pypi/Faker>)

Last two are handled by `requirements.txt`; Chrome and webdriver must be installed manually.

## Installation (Windows)

Install Python 3 miniconda from <http://conda.pydata.org/miniconda.html>.

Open command prompt (`cmd.exe`) and run following commands:

    conda create -n weather-automation python=3
    activate weather-automation
    pip install -r requirements.txt

Download Chrome Selenium webdriver from <https://sites.google.com/a/chromium.org/chromedriver/downloads>,
unzip it and place `chromedriver.exe` in root of conda virtual environment
(if you have installed conda for current user only, it should be
`%HOMEDIR%\Miniconda3\envs\weather-automation\ `).

## Installation (Linux)

    apt-get install chromium python3-selenium chromedriver faker

## Running

Open command prompt and run following commands:

    activate weather-automation
    python ManageAccount.py

## Limitations

- Weather.com uses various techniques to figure out user location and provide local weather data.
  Unfortunately, some locations receive another home page than others, which means that entry point
  will vary depending on computer location, ISP and browser settings. What's worse, some locations
  do not provide user management capabilities at all, which is required for our test scripts.
  We use non-existing page as entry point, which is the only one that consistently provides
  all functionality that we require.

- The way that requirements were created makes test scenarios coupled together. We must execute
  them in particular order, or they will fail (due to user not existing yet/already). We abuse
  unittest habit of executing test scenarios in alphabetical order, but this is deemed to fail
  eventually. In real world, we should probably run tests in well-defined test harness that
  conforms to certain expectations, such as "user exists" (most likely by spinning off docker
  image for each test).

- New users sometimes get cities that are not in Weather.com database, causing first scenario 
  to stall. We could choose city from list of known working items, but current fuzzy approach
  would probably give more value for real development team (as occasional failure for existing
  city is something that we should probably work on).

- When running on your local machine, mouse cursor inside Chrome window may break Selenium
  ActionChain and cause test to fail. This happens only for scripts that require user to hover
  mouse cursor over certain element and should probably be fixed on website side (mobile devices
  have no hover event).

- Occasionally you might get `selenium.common.exceptions.WebDriverException: Message: unknown 
  error: unhandled inspector error: {"code":-32000,"message":"Cannot find context with specified id"}`
  error message. This is chromedriver issue that cannot be worked around on our side
  (see <https://bugs.chromium.org/p/chromedriver/issues/detail?id=1224> and
  <http://stackoverflow.com/q/41429723/3552063>).
