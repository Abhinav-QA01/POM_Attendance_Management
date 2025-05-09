import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverManager:
    _driver = None
    keep_browser_open = True

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            # Use the Selenium server URL from the environment variable
            remote_url = os.environ.get('SELENIUM_REMOTE_URL', 'http://localhost:4444/wd/hub')
            print(f"Using remote Selenium server at {remote_url}")

            # Configure Chrome options
            options = Options()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

            # Connect to the remote Selenium server
            cls._driver = webdriver.Remote(
                command_executor=remote_url,
                options=options
            )

            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if not cls.keep_browser_open and cls._driver is not None:
            cls._driver.quit()
            cls._driver = None