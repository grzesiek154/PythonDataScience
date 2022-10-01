from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import extruct

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("user-agent=SeKonBot/1.0 (https://zazepa.pl/bot.html)")
driver = webdriver.Chrome(options = options)
driver.get("https://zazepa.pl/v2/")

try:
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "summary"))
    )
    body_html = driver.find_element(by = By.XPATH, value = "/html/body")
    html = body_html.get_attribute("innerHTML")
    data = extruct.extract(html)
    for key in data:
        if len(data[key])>0:
            for element in data[key]:
                print(element)
        print("Liczba wykrytych elementów według standardu: " + key, len(data[key]))
finally:
    driver.quit()