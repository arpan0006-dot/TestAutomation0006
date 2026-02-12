
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.ac=ActionChains(driver)

    def find_element(self, locator):
        element =self.wait.until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self,locator,text):
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.find_element(locator).text

    def double_click(self,locator):
        element=self.wait.until(EC.element_to_be_clickable(locator))
        self.ac.double_click(element).perform()

    def move_to_element(self,locator):
        element=self.find_element(locator)
        self.ac.move_to_element(element).perform()


   def select_all(self, locator):

      elements = self.find_elements(locator)
      for element in elements:
           if not element.is_selected():
              element.click()


         identifier=element.get_attribute("value") or element.text
        print(f"Element <{identifier}> Selected: {element.is_selected()}")


   def deselect_all(self, locator):
       elements = self.find_elements(locator)
       for element in elements:
         if element.is_selected():
              element.click()

       identifier=element.get_attribute("value") or element.text
       print(f"Element <{identifier}> Deselected: {not element.is_selected()}")







