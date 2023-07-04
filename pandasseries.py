import pandas as pd
l = [10,20,30,40,50,60]
series = pd.Series(l)
series[1:5] = 70
print(series)

d= {1:"Mango",2:"Apple",3:"Guava",4:"Kiwi"}
seriesd = pd.Series(d)
seriesd[2:4]
print(seriesd)