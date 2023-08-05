import joypy
import pandas as pd
from matplotlib import pyplot as plt

# Lav et dataset af random numre
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})

# Lav en joy plot
fig, axes = joypy.joyplot(data, ylim='own')

# tilføj labels og titler
plt.xlabel("Value")
plt.ylabel("Variable")
plt.title("Joy Plot of two Variables")

# Vis plottet
plt.show()