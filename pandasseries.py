import pandas as pd
l = [10,20,30,40,50,60]
series = pd.Series(l)
series[1:5] = 70
print(series)

d = {1:"Mango",2:"Apple",3:"Guava",4:"Kiwi"}
e = {1:"esb", 2:"rpi", 3:"arduino"}
seriesd = pd.Series(d)
seriese = pd.Series(e)
print(d.get(2))
resultlist = seriesd[1:4] + seriese[1:3]
print(resultlist)