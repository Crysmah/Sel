from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def scrape_newegg(output_file):
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.newegg.com/p/pl?d=radeon+rx+graphics+card")

        names = driver.find_elements(By.CLASS_NAME, "item-title")
        prices = driver.find_elements(By.CLASS_NAME, "price-current")

        with open(output_file, "w") as file:
            for name, price in zip(names, prices):
                # Cut off anything that follows a "(" character in the product price
                clean_price = price.text.split("(")[0].strip()
                output_line = f"{name.text} {clean_price}\n"
                print(output_line)
                file.write(output_line)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    output_file = "output.txt"
    scrape_newegg(output_file)
