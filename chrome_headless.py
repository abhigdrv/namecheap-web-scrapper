from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

print(driver.title)

driver.quit()