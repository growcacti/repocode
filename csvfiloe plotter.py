import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv("your_file.csv")

# Extract the data for plotting
x = data["x"]
y = data["y"]

# Plot the data
plt.plot(x, y)

# Customize the plot
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Title of the Plot")
plt.legend(["Data"])

# Display the plot
plt.show()
