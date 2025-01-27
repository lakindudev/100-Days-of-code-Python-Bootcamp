from selenium import webdriver
from selenium.webdriver.common.by import By

#keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Instant-pot-plus-60-Programmable/dp/B075CYMYK6/?th=1")

price_dollar = driver.find_element(By.CLASS_NAME,value="a-size-medium")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-size-medium")

print(f"The price is {price_dollar.text}")

#driver.close()
driver.quit()