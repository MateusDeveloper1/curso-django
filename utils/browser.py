from time import sleep
from selenium import webdriver
import os

def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    if os.environ.get("SELENIUM_HEADLESS") == 1:
        chrome_options.add_argument(option)

    browser = webdriver.Chrome(options=chrome_options)
    return browser


if __name__ == '__main__':
    browser = make_chrome_browser()
    browser.get('http://www.udemy.com/')
    sleep(5)
    browser.quit()
