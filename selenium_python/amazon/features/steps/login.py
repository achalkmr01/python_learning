from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import pandas as pd
import matplotlib.pyplot as plt

driver = webdriver.Chrome()
driver.get("https://www.barchart.com/futures")

# ////Summary
# driver.title → Retrieves the <title> tag's value in the <head> section.
# Element locators (e.g., find_element) → Retrieve text or attributes of elements in the body, like <span> or <div>.
title = driver.title

title_element = driver.find_element(By.XPATH,"//*[@id=\"main-content-column\"]/div/div[1]/div/div[1]/div/h1/span").text;


if title_element == "Futures Market Overview":
       print("Thank You For Title")
else:
      print(f"sorry text is not found {title_element}")
try:
    # Wait for the element to be visible
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='main-content-column']/div/div[3]/div[2]/div/div")))

    # Get the text content of the element
    element_text = element.text
    rows = element_text.split("\n")  # Split the content into lines

    # Header row and number of columns
    header = ['Contract Name', 'Last', 'Change', 'High', 'Low', 'Volume', 'Time']
    num_columns = len(header)

    # Transform rows into a table structure
    table = [header]  # Start with the header
    for i in range(num_columns, len(rows), num_columns):
        table.append(rows[i:i + num_columns])

    # Create an Excel workbook and worksheet
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "market_data"  # Ensure this matches your read_excel call

    # Write data to the Excel file
    for row in table:
        worksheet.append(row)  # Append each row to the worksheet

    # Save the workbook
    excel_file = "market_data.xlsx"
    workbook.save(excel_file)
    print(f"Data saved to {excel_file}")

    # Save the workbook with the sheet name "Raw Data"


    # Read data back with correct sheet name
    df = pd.read_excel(excel_file, sheet_name="market_data")

    # Proceed with the rest of the operations...

    # Load the Excel data into a DataFrame
    # df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Step 2: Data Cleaning and Analysis
    # Convert necessary columns to numeric
    df['High'] = pd.to_numeric(df['High'], errors='coerce')
    df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
    df['Change'] = pd.to_numeric(df['Change'].str.replace('+', ''), errors='coerce')
    df['Last'] = pd.to_numeric(df['Last'], errors='coerce')

    # Task (a): Create the "Mean" column
    df['Mean'] = (df['High'] + df['Low']) / 2

    # Task (b): Plot "High," "Low," and "Mean" in a single linear graph
    plt.figure(figsize=(10, 6))
    plt.plot(df['Contract Name'], df['High'], label='High', marker='o')
    plt.plot(df['Contract Name'], df['Low'], label='Low', marker='o')
    plt.plot(df['Contract Name'], df['Mean'], label='Mean', marker='o')
    plt.xlabel('Contract Name')
    plt.ylabel('Values')
    plt.title('High, Low, and Mean Values')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Task (c): Find the row with the largest "Change"
    largest_change_row = df.loc[df['Change'].idxmax()]
    largest_change_contract = largest_change_row['Contract Name']
    largest_change_last = largest_change_row['Last']
    print(f"Contract with largest Change: {largest_change_contract}")
    print(f"Last value of largest Change: {largest_change_last}")

    # Step 3: Save updated DataFrame back to Excel
    updated_file = "updated_market_data.xlsx"
    with pd.ExcelWriter(updated_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name=excel_file)
    print(f"Updated data saved to {updated_file}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()