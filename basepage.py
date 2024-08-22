from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class seleniumextended():

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def wait_and_get_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_and_find_element_visibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def wait_and_get_text(self, locator):
        return self.wait_and_get_element(locator).text

    def wait_and_click(self, locator):
        self.wait_and_get_element(locator).click()

    def wait_and_input_text(self, locator, value):
        self.wait_and_get_element(locator).clear()
        self.wait_and_get_element(locator).send_keys(value)

    def scroll_to_element(self, locator):
        element = self.wait_and_get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_get_inner_text(self,locator):
        return self.wait_and_get_element(locator).text

    def wait_hover_and_click(self, locator1, locator2):
        wait = WebDriverWait(self.driver, 10)
        ele1 = wait.until(EC.visibility_of_element_located(locator1))

        self.actions.move_to_element(ele1).pause(2).perform()
        wait.until(EC.visibility_of_element_located(locator2)).click()
