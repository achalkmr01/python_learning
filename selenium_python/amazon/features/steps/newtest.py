from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://www.barchart.com/futures")

    # # Wait for the grid wrapper
    # grid_wrapper = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "div.barchart-table-sticky-200"))
    # )
    # print("Grid wrapper located.")
    #
    # # Scroll to grid wrapper to trigger content loading
    # driver.execute_script("arguments[0].scrollIntoView(true);", grid_wrapper)
    #
    # # Wait for bc-data-grid to be present
    # data_grid = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "bc-data-grid"))
    # )
    # print("bc-data-grid element located.")
    #
    # # Wait for the headers to be present in the DOM (increase timeout)
    # table_headers = WebDriverWait(driver, 40).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bc-datatable-header-tooltip"))
    # )
    #
    # # Hover over each header to show the tooltip and print the tooltip text
    # action_chains = ActionChains(driver)
    #
    # for index, header in enumerate(table_headers):
    #     action_chains.move_to_element(header).perform()
    #     tooltip_text = header.get_attribute("data-tooltip")
    #     print(f"Header {index + 1}: {tooltip_text if tooltip_text else '[No Tooltip]'}")
    # Locate the shadow root
    shadow_host = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.barchart-table-sticky-200"))
    )
    # shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    shadow_root = driver.execute_script("arguments[0].scrollIntoView(true);", shadow_host)
    # Wait and interact with the element inside the shadow DOM
    shadow_element = WebDriverWait(driver, 10).until(
        lambda d: shadow_root.find_element(By.XPATH, "//*[@id='_root']")
    )
#
# except TimeoutException as te:
#     print("Timeout Error: Element not found or content not fully loaded.")
# except Exception as e:
#     print("Unexpected Error:", e)
finally:
    # Always close the browser
    driver.quit()
