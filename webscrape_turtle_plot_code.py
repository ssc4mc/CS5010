#Webscrape Data Visualization
#Summer Chambers & Latifa Hasan
#ssc4mc , lmh3ge

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sea_turtle_wiki.csv")
print(data)

Green_T = data["Green Sea Turtle"]
Logger_T = data["Loggerhead Sea Turtle"]
Leather_T = data["Leatherback Sea Turtle"]

tax = data["Taxonomic Rank"]

fig, ax = plt.subplots()
ax.plot(tax, Green_T, label="Green")
ax.plot(tax, Logger_T, label="Loggerhead")
ax.plot(tax, Leather_T, label="Leatherback")
ax.legend()

plt.show()
