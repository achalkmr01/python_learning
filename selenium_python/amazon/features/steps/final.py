from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Setup WebDriver (ensure ChromeDriver is installed)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open your webpage
driver.get("https://www.barchart.com/futures")

# Give time for the page to load, especially for dynamic content like shadow DOMs
driver.implicitly_wait(5)

# Locate the shadow root of the data grid element
data_grid_element = driver.find_element(By.CSS_SELECTOR, "bc-data-grid")

# Access the shadow root
shadow_root = data_grid_element.shadow_root

# Locate the root element inside the shadow DOM
root_element = shadow_root.find_element(By.CSS_SELECTOR, "#_root")
print("Root Element:", root_element)

# Locate the grid element
grid_element = root_element.find_element(By.CSS_SELECTOR, "div#_grid")
print("Grid Element:", grid_element)

# Column headers as per your request
headers = ["Contract Name", "Last", "Change", "High", "Low", "Volume", "Time"]

# Find all rows in the grid
rows = root_element.find_elements(By.CSS_SELECTOR, "set-class.row")

# Prepare data for DataFrame
data = []

# Loop through each row and extract the text content from its cells
for index, row in enumerate(rows):
    # Extract text content from the row's cells
    cells = row.find_elements(By.CSS_SELECTOR, "div._cell")
    row_text = [cell.text.strip() for cell in cells]

    # If the row has more than 7 columns, discard the extra column(s)
    if len(row_text) > len(headers):
        row_text = row_text[:len(headers)]  # Keep only the first 7 columns

    # Check if the row has the correct number of columns (7 in this case)
    if len(row_text) == len(headers):
        data.append(row_text)  # Add the row data to the list
        print(f"Row {index + 1} Text: {' | '.join(row_text)}")
    else:
        print(f"Row {index + 1} has an unexpected number of columns: {len(row_text)}")

# Save the extracted data to an Excel file
df = pd.DataFrame(data, columns=headers)  # Create a DataFrame with headers
df.to_excel(r"G:\passion\python_learning\futures_data.xlsx", index=False)

print("Data saved to futures_data.xlsx")

# Close the browser after scraping
driver.quit()
