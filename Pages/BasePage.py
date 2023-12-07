from selenium.webdriver.common.by import By
from Utilities import configReader
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=By.XPATH, value=configReader.readconfig("locators", locator)).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(by=By.ACCESSIBILITY_ID, value=configReader.readconfig("locators", locator)) \
                .click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(by=By.ID, value=configReader.readconfig("locators", locator)).click()
        
    
    def send_values(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=By.XPATH, value=configReader.readconfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(by=By.ACCESSIBILITY_ID, value=configReader.readconfig("locators", locator)) \
                .send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(by=By.ID, value=configReader.readconfig("locators", locator)).send_keys(value)
        
    def get_element_Text(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(by=By.XPATH, value=configReader.readconfig("locators", locator)).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(by=By.ACCESSIBILITY_ID, value=configReader.readconfig("locators",
                                                                                                        locator)).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element(by=By.ID, value=configReader.readconfig("locators", locator)).text

        return text


    def take_screenshot(self, image_name_path):
        screenshot_path = os.path.join(os.path.dirname(__file__) , '..', 'screenshots', image_name_path)
        self.driver.get_screenshot_as_file(screenshot_path)
    
    
    def CountElementsOnPage(self, locator):
        global count
        if str(locator).endswith("_XPATH"):
            count = self.driver.find_elements(by=By.XPATH, value=configReader.readconfig("locators", locator))
        elif str(locator).endswith("_ACCESSIBILITYID"):
            count = self.driver.find_elements(by=By.ACCESSIBILITY_ID,
                                              value=configReader.readconfig("locators", locator))
        elif str(locator).endswith("_CLASSNAME"):
            count = self.driver.find_elements(by=By.CLASS_NAME,
                                              value=configReader.readconfig("locators", locator))
        elif str(locator).endswith("_ID"):
            count = self.driver.find_elements(by=By.ID, value=configReader.readconfig("locators", locator))
        
        return count

    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    
    def clear_textbox(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=By.XPATH, value=configReader.readconfig("locators", locator)).clear()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(by=By.ACCESSIBILITY_ID, value=configReader.readconfig("locators",
                                                                                                        locator)).clear()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(by=By.ID, value=configReader.readconfig("locators", locator)).clear()
