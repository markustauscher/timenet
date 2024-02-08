import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import requests

from home_page import home_page
from holidays import holidays
from marcajes_page import marcajes_page
from timenet_login import timenet_login


class MySeleniumScript(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays()
        # Replace the path with the actual path to your chromedriver.exe
        self.opt = Options()
        self.opt.add_argument("--disable-infobars")
        self.opt.add_argument("--headless")  # Add this line for headless mode
        self.opt.add_argument("start-maximized")
        self.opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        self.opt.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 2,
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.notifications": 2
        })

        self.driver_path = 'C:\\Users\\MarkusTauscher\\AppData\\Local\\Programs\\chromedriver\\chromedriver.exe'
        self.driver = None
        self.work_started_notify = 'https://maker.ifttt.com/trigger/notify/with/key/d54cU9V2D9LCVxgFslYSrs?value1=Work started'
        self.work_finished_notify = 'https://maker.ifttt.com/trigger/notify/with/key/d54cU9V2D9LCVxgFslYSrs?value1=Work finished'
        self.work_started_failed_notify = 'https://maker.ifttt.com/trigger/notify/with/key/d54cU9V2D9LCVxgFslYSrs?value1=FAILED to start Work'
        self.work_finished_failed_notify = 'https://maker.ifttt.com/trigger/notify/with/key/d54cU9V2D9LCVxgFslYSrs?value1=FAILED to finish Work'
        self.no_work_notify = 'https://maker.ifttt.com/trigger/notify/with/key/d54cU9V2D9LCVxgFslYSrs?value1=No Work Today'


    def setupPages(self):
        self.login_page = timenet_login(self.driver)
        self.home_page = home_page(self.driver)
        self.marcajes_page = marcajes_page(self.driver)

    def start_browser(self):
        self.driver = webdriver.Chrome(chrome_options=self.opt, executable_path=self.driver_path)

    def navigate_to_website(self, url='https://timenet-mcp.gpisoftware.com/check/f61518b2-4e5e-431d-a3d7-fc12ea26223c'):
        if not self.driver:
            raise Exception("Browser not started. Call start_browser() first.")

        self.driver.get(url)

    def get_page_title(self):
        if not self.driver:
            raise Exception("Browser not started. Call start_browser() first.")

        return self.driver.title

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def wait_for_text_in_element(self, element_locator, expected_text, timeout=10):
        # Wait for the specified text to be present in the element
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(element_locator, expected_text)
        )

    def is_weekend_or_holiday(self):
        # Check if today is a Saturday or Sunday
        if datetime.datetime.today().weekday() in [5, 6]:
            return True

        # Check if today is one of the specified public holidays
        madrid_holidays = self.holidays
        today = datetime.date.today()
        holidays = madrid_holidays.get_holidays()
        for holiday in holidays:
            if today == holiday['date']:
                return True

        return False

    def write_to_log(self, action, result):
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_datetime} - {action} - {result}\n"

        # Write the log message to the "logs.log" file
        with open("logs.log", "a") as log_file:
            log_file.write(log_message)

    def test_salida(self):

        if self.is_weekend_or_holiday():
            self.write_to_log("HOLIDAY", "NO LOG")
            self.skipTest("Skipping test on weekends or holidays")

        self.start_browser()
        self.setupPages()
        self.navigate_to_website()
        #time.sleep(10)
        title = self.get_page_title()
        print(title)
        self.login_page.click_button('9')
        time.sleep(0.2)
        self.login_page.click_button('4')
        time.sleep(0.2)
        self.login_page.click_button('5')
        time.sleep(0.2)
        self.login_page.click_button('4')
        time.sleep(2)
        self.home_page.click_button('marcajes')
        time.sleep(2)
        self.marcajes_page.click_button('salida')
        time.sleep(3)
        salir_element = self.marcajes_page.get_element('salir')
        text = salir_element.get_attribute('innerHTML')
        print(text)
        if (text == 'Acabas de salir de trabajar'):
            requests.post(self.work_finished_notify)
            self.write_to_log("FINISHED WORK", "SUCCESS")
        else:
            requests.post(self.work_finished_failed_notify)
            self.write_to_log("FINISHED WORK", "FAILED")

    def test_entrada(self):
        test_passed = False

        if self.is_weekend_or_holiday():
            self.write_to_log("HOLIDAY", "NO LOG")
            self.skipTest("Skipping test on weekends or public holidays")

        self.start_browser()
        self.setupPages()
        self.navigate_to_website()
        #time.sleep(10)
        title = self.get_page_title()
        print(title)
        self.login_page.click_button('9')
        time.sleep(0.2)
        self.login_page.click_button('4')
        time.sleep(0.2)
        self.login_page.click_button('5')
        time.sleep(0.2)
        self.login_page.click_button('4')
        time.sleep(2)
        self.home_page.click_button('marcajes')
        time.sleep(2)
        self.marcajes_page.click_button('entrada')
        time.sleep(2)
        empezar_element = self.marcajes_page.get_element('empezar')
        text = empezar_element.get_attribute('innerHTML')
        print(text)
        if (text == 'Acabas de empezar a trabajar'):
            test_passed = True

        if test_passed:
            requests.post(self.work_started_notify)
            self.write_to_log("STARTED WORK", "SUCCESS")
        else:
            requests.post(self.work_started_failed_notify)
            self.write_to_log("STARTED WORK", "FAILED")


if __name__ == "__main__":
    unittest.main()
