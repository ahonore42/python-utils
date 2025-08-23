import requests
import re
from html import unescape

# Regex patterns
TABLE_PATTERN = re.compile(r"<table[^>]*>(.*?)</table>", re.DOTALL | re.IGNORECASE)
ROW_PATTERN = re.compile(r"<tr[^>]*>(.*?)</tr>", re.DOTALL | re.IGNORECASE)
CELL_PATTERN = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.DOTALL | re.IGNORECASE)
HTML_TAG_PATTERN = re.compile(r"<[^>]+>")
NUMBER_PATTERN = re.compile(r"\b\d+\b")
BLOCK_CHAR_PATTERN = re.compile(r"[█░]")

def decode_secret_message(url):
    """
    Decodes a secret message from a published Google Doc URL containing coordinate data.
    """
    try:
        # Fetch document
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Parse coordinate data
        coordinates = parse_coordinate_data(response.text)

        # Build and display grid
        if coordinates:
            build_and_print_grid(coordinates)
        else:
            print("No coordinate data found in document")

    except requests.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Processing error: {e}")


def parse_coordinate_data(html_content):
    """Parse coordinate data from HTML tables using pattern matching."""
    # Find all tables using compiled pattern
    tables = TABLE_PATTERN.findall(html_content)

    if not tables:
        print("No tables found in document")
        return []

    # Find target table with coordinate data
    target_table = None
    best_score = 0

    for i, table_content in enumerate(tables):
        # Quick check for block characters first
        block_matches = BLOCK_CHAR_PATTERN.findall(table_content)
        if not block_matches:
            continue

        # Count numbers only if we found block characters
        number_matches = NUMBER_PATTERN.findall(table_content)

        block_count = len(block_matches)
        number_count = len(number_matches)

        # Score based on data density
        score = block_count if number_count >= block_count else 0

        if score > best_score:
            best_score = score
            target_table = table_content

    if not target_table:
        print("No suitable coordinate data table found")
        return []

    # Extract and process rows
    rows = ROW_PATTERN.findall(target_table)
    coordinates = []

    for i, row in enumerate(rows):
        cells = CELL_PATTERN.findall(row)

        if len(cells) < 3:
            continue

        try:
            # Clean cells efficiently
            cleaned_cells = [
                unescape(HTML_TAG_PATTERN.sub("", cell).strip()) for cell in cells[:3]
            ]

            # Skip header detection
            if i == 0 and any(
                word in cleaned_cells[0].lower() for word in ["coordinate", "character"]
            ):
                continue

            # Parse coordinates
            x, char, y = int(cleaned_cells[0]), cleaned_cells[1], int(cleaned_cells[2])

            # Only store valid block characters
            if char in "█░":
                coordinates.append((x, y, char))

        except (ValueError, IndexError):
            continue

    return coordinates


def build_and_print_grid(coordinates):
    """Build and print 2D grid from coordinates efficiently."""
    if not coordinates:
        return

    # Calculate bounds in single pass
    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]

    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    # Create grid as dictionary for sparse representation
    grid = {}
    for x, y, char in coordinates:
        grid[(x - min_x, y - min_y)] = char

    # Print grid efficiently
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Build rows from bottom to top (y=0 at bottom)
    for row_idx in range(height - 1, -1, -1):
        row_chars = []
        for col_idx in range(width):
            row_chars.append(grid.get((col_idx, row_idx), " "))
        print("".join(row_chars).rstrip())


# # Example usage:
# if __name__ == "__main__":
#     # Test with the provided URL
#     url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"

#     decode_secret_message(url)
