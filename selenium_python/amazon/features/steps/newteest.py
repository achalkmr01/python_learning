from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver (Make sure you have the correct path to your chromedriver)
driver = webdriver.Chrome()

try:
    # Open the page
    driver.get("https://www.barchart.com/futures")  # Replace with your URL

    # Step 1: Get all iframes on the page
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Total iframes found: {len(iframes)}")

    # Step 2: Iterate through each iframe
    for i, iframe in enumerate(iframes):
        print(f"Iframe {i + 1}:")

        # Print iframe attributes
        print(f"  - src: {iframe.get_attribute('src')}")
        print(f"  - id: {iframe.get_attribute('id')}")
        print(f"  - name: {iframe.get_attribute('name')}")
        print(f"  - class: {iframe.get_attribute('class')}")

        # Step 3: Switch to the iframe
        driver.switch_to.frame(iframe)


        try:
            # Wait until the element is present in the main document
            shadow_host = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#_root"))
            )
            print("Element found.")
        except TimeoutException:
            print("Element not found in the main document within the timeout period.")


        except NoSuchElementException:
            print(f"Element not found in iframe {i + 1}")

        # Step 5: Switch back to the main content after each iframe check
        driver.switch_to.default_content()

finally:
    # Close the browser after the operation
    time.sleep(5)  # Add a delay if you want to see the results
    driver.quit()
