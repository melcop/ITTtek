import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = pd.DataFrame({"values": [7, 2, 15, 9, 12, 4, 11, 8, 13, 6]})

# Create boxplot
data.plot.box()

# Customize labels and title
plt.xlabel("Data")
plt.ylabel("Value")
plt.title("Boxplot with Pandas")

plt.show()