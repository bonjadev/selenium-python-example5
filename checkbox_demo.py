import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoCheckbox():
    def checkbox(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://thefutur.com/newsletter")
        driver.maximize_window()
        driver.implicitly_wait(10) #implicit waiting command

        #Scroll Down
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(2) #pause
        driver.execute_script("window.scrollBy(0, 430);")
        time.sleep(3) #pause
        #XPATH of the checkbox element on web page
        driver.find_element(By.XPATH, "//form[@id='wf-form-Email-Form']//div[@class='w-checkbox-input w-checkbox-input--inputType-custom wiz-form-checkbox']").click()
        time.sleep(5) #pause
        driver.close()

#object creation
checkbox = DemoCheckbox()
checkbox.checkbox()