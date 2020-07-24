#Webscrape Homework
#Summer Chambers & Latifa Hasan
#ssc4mc , lmh3ge

#Import Packages
from bs4 import BeautifulSoup
import requests
import pandas as pd

#get urls with request package
url = "https://en.wikipedia.org/wiki/Green_sea_turtle"
page = requests.get(url)

url2 = "https://en.wikipedia.org/wiki/Loggerhead_sea_turtle"
page2 = requests.get(url2)

url3 = "https://en.wikipedia.org/wiki/Leatherback_sea_turtle"
page3 = requests.get(url3)

#use BeautifulSoup to read html code
soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')
soup3 = BeautifulSoup(page3.content, 'html.parser')

#initiate index column
col1 = []

#Loop through taxonomic ranks on first wiki page
for i in range(6,16):
    
    #access tags wwith taxonomic rank text
    col1.append(soup.findAll('table')[0].tbody.findAll('tr')[i].td.text.strip())
    
#initiate columns for various turtles
Green_sea_turtle = []
Loggerhead_sea_turtle = []
Leatherback_sea_turtle = []
    
#Loop through scientific names for various wiki pages
for i in range(6, 15):
    
    #access tags with scientific name text
    Green_sea_turtle.append(soup.findAll('table')[0].tbody.findAll('tr')[i].findAll('td')[1].a.text)
    Loggerhead_sea_turtle.append(soup2.findAll('table')[0].tbody.findAll('tr')[i].findAll('td')[1].a.text)
    Leatherback_sea_turtle.append(soup3.findAll('table')[0].tbody.findAll('tr')[i].findAll('td')[1].a.text)

#Last index (species) was housed in a different tag, remove extra characters
Green_sea_turtle.append(soup.findAll('table')[0].tbody.findAll('tr')[15].findAll('td')[1].div.i.b.text.replace('\xa0', ' '))
Loggerhead_sea_turtle.append(soup2.findAll('table')[0].tbody.findAll('tr')[15].findAll('td')[1].div.i.b.text.replace('\xa0', ' '))
Leatherback_sea_turtle.append(soup3.findAll('table')[0].tbody.findAll('tr')[15].findAll('td')[1].div.i.b.text.replace('\xa0', ' '))


#compile columns into mega-list
list_of_lists = [col1, Green_sea_turtle, Loggerhead_sea_turtle, Leatherback_sea_turtle]

print(list_of_lists)

#create pandas dataframe from mega-list 
df = pd.DataFrame(list_of_lists)

#transpose dataframe so columns become rows
df = df.T

#label our columns
df_new = df.rename(columns={0: "Taxonomic Rank", 1: "Green Sea Turtle", 2: "Loggerhead Sea Turtle", 3: "Leatherback Sea Turtle"})

#set first column to be index
df_new.set_index('Taxonomic Rank', inplace=True)

print(df_new)

#write dataframe to csv file
df_new.to_csv('sea_turtle_wiki.csv')