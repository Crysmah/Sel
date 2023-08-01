from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.adorama.com/")

# Find the search input field using the appropriate locating strategy
search = driver.find_element(By.NAME, "searchinfo")

search.send_keys("radeon rx graphics card")
search.send_keys(Keys.RETURN)

try:
    names = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "Products_title__t1ag6"))
    )
    prices = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "Products_price__YsZAR"))
    )

    with open("output.txt", "w") as file:
        for name, price in zip(names, prices):
            output_line = f"{name.text} {price.text}\n"
            print(output_line)
            file.write(output_line)

except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(5)
    driver.quit()
