#%pip install openpyxl
import pandas as pd

def find_minimum_difference_color(row, processed_colors):
    min_diff_color = None
    min_difference = float('inf')

    for color, difference in row.items():
        if color not in processed_colors and difference < min_difference:
            min_difference = difference
            min_diff_color = color

    return min_diff_color

def find_order_of_colors(matrix, starting_color, production_colors):
    order = [starting_color]
    processed_colors = {starting_color}

    current_color = starting_color

    while len(processed_colors) < len(production_colors):
        try:
            row = matrix.loc[current_color]
        except KeyError:
            print(f"KeyError: {current_color} not found in the matrix.")
            break

        next_color = find_minimum_difference_color(row, processed_colors)

        if next_color is not None:
            order.append(next_color)
            processed_colors.add(next_color)
            current_color = next_color
        else:
            break

    return order

# Read data from the Excel file containing the order of colors
order_df = pd.read_excel('Production_Plan.xlsx', header=None, names=['Color'])

# Read data from the Excel file containing the symmetric matrix
df = pd.read_excel('Spectrophotometer_Matrix.xlsx', index_col=0)

# Read data from the Excel file containing the lightest to darkest color shades
shades_df = pd.read_excel('Light_to_Dark.xlsx', header=None, names=['Color'])

# Get the list of colors from both files
shades_colors = shades_df['Color'].tolist()
production_colors = order_df['Color'].tolist()

# Choose the lightest color from the production file that exists in both files 
#as the starting color
common_colors = set(shades_colors).intersection(production_colors)
if common_colors:
    starting_color = min(common_colors, key=shades_colors.index)
else:
    print("No common colors found between the shades and production files.")
    starting_color = None

# Print the starting color for debugging
print("Starting Color:", starting_color)

# Create a new matrix based on the production colors
new_matrix = df.loc[production_colors, production_colors]

# Find the order of colors based on minimum differences for the specified 
#production colors
color_order = find_order_of_colors(new_matrix, starting_color, production_colors)

# Display the order of colors on the screen
print("Order of Colors based on Minimum Differences:")
print(color_order)

# Save the output to a new Excel file
output_df = pd.DataFrame({'Color': color_order})
output_df.to_excel('COLOR_ORDER_OUPUT.xlsx', index=False)

print(f"Order of Colors based on Minimum Differences saved to 'color_order_output.xlsx'.")
