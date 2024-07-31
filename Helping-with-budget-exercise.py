# List of monthly spending amounts
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

# Initialize counters for different spending categories
low = 0     # Counts months with low spendings (less than 1000)
normal = 0  # Counts months with normal spendings (between 1000 and 2500)
high = 0    # Counts months with high spendings (more than 2500)

# Loop through each month's spending
for month in spendings:
    # Check if the spending is less than 1000
    if month < 1000.0:
        low += 1  # Increment low counter
    # Check if the spending is between 1000 and 2500
    elif month <= 2500.0:
        normal += 1  # Increment normal counter
    # If spending is greater than 2500
    else:
        high += 1  # Increment high counter

# Print out the number of months in each category
print('Numbers of months with low spendings: ' + str(low) +
      ', normal spendings: ' + str(normal) +
      ', high spendings: ' + str(high) + '.')
