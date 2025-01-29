from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the webpage
    driver.get("https://www.barchart.com/futures")

    # Wait for the shadow host to appear
    shadow_host = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#_root._root"))
    )

    # Access the shadow root
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

    # Locate an element inside the shadow root
    grid_element = shadow_root.find_element(By.CSS_SELECTOR, "div#_grid._grid")
    print("Grid element found:", grid_element.get_attribute("class"))

finally:
    driver.quit()
