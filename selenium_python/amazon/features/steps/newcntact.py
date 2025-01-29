from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://www.barchart.com/futures")

    # Wait for the grid's parent div to load
    grid_wrapper = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.barchart-table-sticky-200"))
    )
    print("Grid wrapper located.")

    # Scroll the grid into view to ensure content is loaded dynamically
    driver.execute_script("arguments[0].scrollIntoView(true);", grid_wrapper)

    # Wait for the <bc-data-grid> to load within the wrapper
    data_grid = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "bc-data-grid"))
    )
    print("bc-data-grid element located.")

    # Example: Locate column header "Contract Name" inside the grid
    contract_name_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'bc-datatable-header-tooltip') and text()='Contract Name']"))
    )
    print("Contract Name header found!")

    # Print the outer HTML of the grid for verification
    print("Outer HTML of bc-data-grid:")
    print(data_grid.get_attribute("outerHTML"))

except Exception as e:
    print("Error:", e)

finally:
    # Quit the driver
    driver.quit()
