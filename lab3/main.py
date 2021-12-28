from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string

rnd = "Joys" + "".join(random.choices(string.ascii_lowercase, k=3))

keys = {
    "firstname": rnd,
    "lastname": rnd,
    "reg_email__": rnd + "@gmail.com",
    "reg_passwd__": "123" + rnd
}

print(rnd)

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://www.fb.com")

if driver.current_url == "https://www.facebook.com/":
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="open-registration-form-button"]')))
    
    create_button = driver.find_element(By.XPATH, '//*[@data-testid="open-registration-form-button"]')
    create_button.click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "firstname")))

    driver.find_element(By.NAME, "firstname").send_keys(keys["firstname"])
    driver.find_element(By.NAME, "lastname").send_keys(keys["lastname"])
    driver.find_element(By.NAME, "reg_email__").send_keys(keys["reg_email__"])
    driver.find_element(By.NAME, "reg_email_confirmation__").send_keys(keys["reg_email__"])
    driver.find_element(By.NAME, "reg_passwd__").send_keys(keys["reg_passwd__"])

    Select(driver.find_element(By.NAME, "birthday_day")).select_by_value('1')
    Select(driver.find_element(By.NAME, "birthday_month")).select_by_value('1')
    Select(driver.find_element(By.NAME, "birthday_year")).select_by_value('1980')

    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='2']").click()

    driver.find_element(By.NAME, "websubmit").click()

    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, "conf_dialog_middle_components")))

else:
    print("Don't redirected")