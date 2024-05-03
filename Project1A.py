from Datas import dataP1
from Locator import locatorP1

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginPage:

     def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)


     def boot(self):
        self.driver.get(dataP1.Webdata().url)


     def quit(self):
        self.driver.quit()

     def enterText(self, locator, textValue):
        element = self.wait.until(EC.visibility_of_element_located((By.NAME, locator)))
        element.clear()
        element.send_keys(textValue)

     def clickButton(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator))).click()



     def login(self):
         try:

            self.boot()

            # Username = 7
            # Password = 8
            # Test Results = 14

            # Rows - 2 to 5

            for row in range(2, 6):

                username = dataP1.Webdata().readData(row, 7)
                password = dataP1.Webdata().readData(row, 8)

                try:
                    self.enterText(locatorP1.WebLocators().usernameLocator, username)
                    self.enterText(locatorP1.WebLocators().passwordLocator, password)
                    self.clickButton(locatorP1.WebLocators().loginButtonLocator)

                    try:
                        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                        alert = self.driver.switch_to.alert
                        alert.accept()
                    except TimeoutException:
                        print("No alert to accept.")

                    if self.driver.current_url == dataP1.Webdata().dashboardURL:
                        print("Successfully LoggedIn")
                        dataP1.Webdata().writeData(row, 14, "PASSED")

                        # Logout
                        self.clickButton(locatorP1.WebLocators().topRightLocator)
                        self.clickButton(locatorP1.WebLocators().logoutButtonLocator)

                    else:
                        try:

                            error_locator = (By.XPATH, locatorP1.WebLocators().errorMessageLocator)
                            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(error_locator))
                            error_message = self.driver.find_element(*error_locator).text
                            print("Error message:", error_message)
                        except TimeoutException:
                            print("No Error message")

                        dataP1.Webdata().writeData(row, 14, "FAILED")




                except NoSuchElementException as e:

                    print("An error occurred:", e)

         except NoSuchElementException as e:
             print(e)
         finally:
             self.quit()

obj = LoginPage()
obj.login()

""""
Output- 
No alert to accept.
Successfully LoggedIn
No alert to accept.
Error message: Invalid credentials
No alert to accept.
Error message: Invalid credentials
No alert to accept.
Error message: Invalid credentials
"""






