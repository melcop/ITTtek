import joypy
import pandas as pd
from matplotlib import pyplot as plt

# Lav et dataset af random numre
data = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [7, 8, 9, 10, 11, 12]})

# Lav en joy plot
fig, axes = joypy.joyplot(data, ylim='own')

# tilføj labels og titler
plt.xlabel("Value")
plt.ylabel("Variable")
plt.title("Joy Plot of two Variables")

# Vis plottet
plt.show()