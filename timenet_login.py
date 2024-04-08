from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class timenet_login:
    def __init__(self, driver):
        self.driver = driver

    # Define your dictionary with web elements
    elements = {
        'button_0': (By.XPATH, '//button[@aria-label="0"]'),
        'button_1': (By.XPATH, '//button[@aria-label="1"]'),
        'button_2': (By.XPATH, '//button[@aria-label="2"]'),
        'button_3': (By.XPATH, '//button[@aria-label="3"]'),
        'button_4': (By.XPATH, '//button[@aria-label="4"]'),
        'button_5': (By.XPATH, '//button[@aria-label="5"]'),
        'button_6': (By.XPATH, '//button[@aria-label="6"]'),
        'button_7': (By.XPATH, '//button[@aria-label="7"]'),
        'button_8': (By.XPATH, '//button[@aria-label="8"]'),
        'button_9': (By.XPATH, '//button[@aria-label="9"]'),
        'button_backspace': (By.XPATH, '//button[@aria-label="borrar"]'),
        'button_aceptar': (By.XPATH, '//button[@aria-label="Aceptar"]')
        # Add more elements as needed
    }

    def get_element(self, key) -> WebElement:
        # Retrieve the web element using the key from the dictionary
        return self.driver.find_element(*self.elements[key])

    def wait_for_element_presence(self, key, timeout=10):
        # Wait for the presence of the specified element
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.elements[key])
        )

    def click_button(self, digit):
        # Wait for the page to load before interacting with the button
        self.wait_for_element_presence(f'button_{digit}')

        # Click the button with the specified digit
        key = f'button_{digit}'
        button = self.get_element(key)
        button.click()

    # Add more methods to interact with other elements as needed
