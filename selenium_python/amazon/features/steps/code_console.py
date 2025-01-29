let
dataGrid = document.querySelector("bc-data-grid");
if (dataGrid) {
let shadowRoot = dataGrid.shadowRoot; // Access the shadowRoot
let rootElement = shadowRoot.querySelector("#_root"); // Access the root element inside shadowRoot
console.log("Root Element:", rootElement);

if (rootElement) {
let gridElement = rootElement.querySelector("div#_grid");
console.log("Grid Element:", gridElement);

// Fetch all rows
let rows = rootElement.querySelectorAll("set-class.row");

// Loop through each row and print its text content
rows.forEach((row, index) = > {
console.log(`Row ${index + 1}:`, row);

// Extract
text
content
from the row

's cells
let
cells = row.querySelectorAll("div._cell");
let
rowText = Array.
from

(cells).map(cell= > cell.textContent.trim()).join(" | ");
console.log(`Row ${index + 1}
Text: ${rowText}
`);

// Check if the
row is selected
if (row.classList.contains("selected"))
{
    console.log(`Selected
Row ${index + 1}
Text: ${rowText}
`);
}
});
} else {
    console.log("Root element (#_root) not found in shadowRoot.");
}
} else {
    console.log("bc-data-grid element not found.");
}
