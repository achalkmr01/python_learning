from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Navigate to the target page
    driver.get("https://www.barchart.com/futures")  # Replace with the actual URL containing the shadow DOM

    # Wait for the shadow host element to be present
    shadow_host = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#table-guid-bcc8197b-4b1a-82f5-3bf6-bbd80bf7ac98"))
    )
    print(shadow_host)
    # Use JavaScript to access the shadow root
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

    # Find the element inside the Shadow DOM
    shadow_element = shadow_root.find_element(By.CSS_SELECTOR, "#_root")

    # Perform actions with the target element
    print("Text inside shadow DOM element:", shadow_element.text)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    time.sleep(5)  # Pause for debugging or visual confirmation
    driver.quit()