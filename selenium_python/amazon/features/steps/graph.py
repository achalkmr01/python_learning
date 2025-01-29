import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
# print("Root Element:", root_element)

# Locate the grid element
grid_element = root_element.find_element(By.CSS_SELECTOR, "div#_grid")
# print("Grid Element:", grid_element)

# Find all rows in the grid
rows = root_element.find_elements(By.CSS_SELECTOR, "set-class.row")

# Prepare the header and data for the Excel file
header = ["Contract Name", "Last", "Change", "High", "Low", "Volume", "Time"]
data = []

# Loop through each row and extract the text content from its cells
for index, row in enumerate(rows):
    cells = row.find_elements(By.CSS_SELECTOR, "div._cell")

    # Print the entire row data for debugging purposes
    row_data = [cell.text.strip() for cell in cells]
    print(f"Row {index + 1}: {row_data}")  # Print all cell data in the row

    # If the row has the expected number of columns (7), extract the data
    if len(cells) == 7:
        data.append(row_data)
    elif len(cells) > 7:
        # If there are more than 7 columns, take the first 7 only (ignore extra ones)
        data.append(row_data[:7])
    else:
        print(f"Skipping Row {index + 1} due to unexpected number of columns: {len(cells)}")

# If no valid rows, notify the user and stop execution
if not data:
    print("No valid data extracted from the rows.")
else:
    # Save the data to a DataFrame
    df = pd.DataFrame(data, columns=header)

    # Convert columns to numeric (if possible)
    df["High"] = pd.to_numeric(df["High"], errors='coerce')
    df["Low"] = pd.to_numeric(df["Low"], errors='coerce')
    df["Mean"] = (df["High"] + df["Low"]) / 2  # Create the Mean column

    # Plot "High", "Low", and "Mean" in a single linear graph
    plt.figure(figsize=(10, 6))
    plt.plot(df["Contract Name"], df["High"], label="High", marker='o')
    plt.plot(df["Contract Name"], df["Low"], label="Low", marker='x')
    plt.plot(df["Contract Name"], df["Mean"], label="Mean", linestyle='--')
    plt.xlabel('Contract Name')
    plt.ylabel('Price')
    plt.title('High, Low, and Mean Values')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Find the row with the largest "Change"
    df["Change"] = pd.to_numeric(df["Change"], errors='coerce')  # Convert "Change" to numeric
    max_change_row = df.loc[df["Change"].idxmax()]  # Find the row with the largest "Change"

    # Display the "Contract Name" and "Last" of the row with the largest "Change"
    print(f"Contract with the largest Change: {max_change_row['Contract Name']}")
    print(f"Last value: {max_change_row['Last']}")

    # Save the DataFrame to Excel
    df.to_excel(r"G:\passion\python_learning\futures_data_with_analysis.xlsx", index=False)

# Close the browser after scraping
driver.quit()
