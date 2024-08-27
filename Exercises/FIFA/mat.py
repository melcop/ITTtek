import matplotlib.pyplot as plt

# Sample data
data = [2, 2, 15, 1, 9, 12, 4, 11, 8, 13, 6, 4]

# Create boxplot
plt.boxplot(data)

# Customize labels and title
plt.xlabel("Data")
plt.ylabel("Value")
plt.title("Boxplot with Matplotlib")

plt.show()