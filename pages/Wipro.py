import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.flipkart.com/")


try:
    driver.find_element(By.XPATH, "//span[@role='button']").click()
except:
    pass

# click mobiles
driver.execute_script("arguments[0].click();",
                      driver.find_element(By.XPATH, "//div[contains(text(),'Mobiles')]"))

time.sleep(2)


found = False


for _ in range(10):
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(1)

    elements = driver.find_elements(By.XPATH, "//a[contains(@href,'mobile-phones-mystery-box-store')]")

    if elements:
        driver.execute_script("arguments[0].scrollIntoView();", elements[0])
        print("Found")
        found = True
        break


if not found:
    print("Not Found ")