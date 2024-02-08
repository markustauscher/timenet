from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class home_page:
    def __init__(self, driver):
        self.driver = driver

    # Define your dictionary with web elements
    elements = {
        'marcajes': (By.XPATH, '//button[@aria-label="Marcajes"]'),
        'calendario': (By.XPATH, '//button[@aria-label="Calendario"]'),
        'mensajes': (By.XPATH, '//button[@aria-label="Mensajes"]'),
        'solicitudes': (By.XPATH, '//button[@aria-label="Solicitudes"]'),
        'documentos': (By.XPATH, '//button[@aria-label="Documentos"]'),
        'cerrar': (By.XPATH, '//button[@aria-label="Cerrar"]'),
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

    def click_button(self, name):
        # Wait for the page to load before interacting with the button
        self.wait_for_element_presence(f'{name}')

        # Click the button with the specified digit
        key = f'{name}'
        button = self.get_element(key)
        button.click()

    # Add more methods to interact with other elements as needed
