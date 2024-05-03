from Datas import dataP2
from Locator import locatorP2


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class PIMmodule:

    def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)
       self.act = ActionChains(self.driver)


    def boot(self):
        self.driver.get(dataP2.Webdata().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def quit(self):
        self.driver.quit()

    def enterText(self, locator, textValue):
        element = self.wait.until(EC.visibility_of_element_located((By.NAME, locator)))
        element.clear()
        element.send_keys(textValue)

    def clickButton(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator))).click()



    def pim(self):

        self.boot()

        # Username = 7
        # Password = 8
        # First Name = 9
        # Last Name = 10
        # DOB = 11
        # Test Results = 14

        # Rows - 6 to 8

        for row in range(6, 7):
            username = dataP2.Webdata().readData(row, 7)
            password = dataP2.Webdata().readData(row, 8)
            fname = dataP2.Webdata().readData(row,9)
            lname = dataP2.Webdata().readData(row, 10)

            try:
                self.enterText(locatorP2.WebLocators().usernameLocator, username)
                self.enterText(locatorP2.WebLocators().passwordLocator, password)
                self.clickButton(locatorP2.WebLocators().loginButtonLocator)

                try:
                    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    alert.accept()
                except TimeoutException:
                    print("No alert to accept.")

                self.clickButton(locatorP2.WebLocators().PIMButtonLocator)
                self.clickButton(locatorP2.WebLocators().addButtonLocator)
                self.enterText(locatorP2.WebLocators().firstNameLocator, fname)
                self.enterText(locatorP2.WebLocators().lastNameLocator,lname)
                self.clickButton(locatorP2.WebLocators().saveButtonLocator)

                try:

                   message_locator = (By.ID, "oxd-toaster_1")
                   WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(message_locator))
                   popup_message = self.driver.find_element(*message_locator).text
                   print("Popup message:", popup_message)
                except TimeoutException:
                   print("Popup message did not appear within the expected time.")

                dataP2.Webdata().writeData(row, 14, "SUCCESS")



            except NoSuchElementException as e:

                print("An error occurred:", e)

    def pim1(self):
        try:
            for row in range(7, 8):

                driving = dataP2.Webdata().readData(row, 11)

                self.clickButton(locatorP2.WebLocators().PIMButtonLocator)
                for _ in range(9):
                    self.act.send_keys(Keys.DOWN).perform()

                self.clickButton(locatorP2.WebLocators().editButtonLocator)

                driving_element = self.driver.find_element(By.XPATH, locatorP2.WebLocators().drivingLicenseLocator)
                driving_element.clear()
                driving_element.send_keys(driving)
                for _ in range(4):
                    self.act.send_keys(Keys.DOWN).perform()
                self.clickButton(locatorP2.WebLocators().save2ButtonLocator)

                try:

                    message_locator = (By.ID, "oxd-toaster_1")
                    WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(message_locator))
                    popup_message = self.driver.find_element(*message_locator).text
                    print("Popup message:", popup_message)
                except TimeoutException:
                    print("Popup message did not appear within the expected time.")

                dataP2.Webdata().writeData(row, 14, "SUCCESS")


        except NoSuchElementException as e:

            print("An error occurred:", e)



    def pim2(self):
        try:
            for row in range(8, 9):
                fname = dataP2.Webdata().readData(row,9)
                self.clickButton(locatorP2.WebLocators().PIMButtonLocator)
                for _ in range(9):
                    self.act.send_keys(Keys.DOWN).perform()
                self.clickButton(locatorP2.WebLocators().deleteButtonLocator)
                self.clickButton(locatorP2.WebLocators().yesDeleteLocator)

                try:

                    message_locator = (By.ID, "oxd-toaster_1")
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(message_locator))
                    popup_message = self.driver.find_element(*message_locator).text
                    print("Popup message:", popup_message)
                except TimeoutException:
                    print("Popup message did not appear within the expected time.")

                dataP2.Webdata().writeData(row, 14, "SUCCESS")

        except NoSuchElementException as e:

            print("An error occurred:", e)


obj = PIMmodule()
obj.pim()
obj.pim1()
obj.pim2()
obj.quit()


"""
Output- 
No alert to accept.
Popup message: Success
Successfully Saved
×
Popup message: Success
Successfully Updated
×
Popup message: Success
Successfully Deleted
×
"""

