from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
      
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("user-agent=SeKonBot/1.0 (https://zazepa.pl/bot.html)")
driver = webdriver.Chrome(options = options)

driver.get("https://zazepa.pl/v2/")
driver.implicitly_wait(20)
products = driver.find_elements(by = By.CLASS_NAME, value = "product")
print("Znalezionych produktów:", len(products))
body_html = driver.find_element(by = By.XPATH, value = "/html/body")
print(body_html.text)
driver.quit()