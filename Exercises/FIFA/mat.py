import matplotlib.pyplot as plt

# Sample data
data = [7, 2, 15, 9, 12, 4, 11, 8, 13, 6]

# Create boxplot
plt.boxplot(data)

# Customize labels and title
plt.xlabel("Data")
plt.ylabel("Value")
plt.title("Boxplot with Matplotlib")

plt.show()