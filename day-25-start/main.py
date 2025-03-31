'''import csv

with open('weather_data.csv') as file:
    data = csv.reader(file)
    temperaturas = []
    for coluna in data:
        temp = coluna[1]
        temperaturas.append(temp)
        int_temp = list(map(int, temperaturas[1:]))
    print(int_temp)
'''
import pandas as pd
'''
data = pd.read_csv('weather_data.csv')
print(data)
temp = data['temp']
temp2 = list(temp)

media = 0                               #metodo 01:
for graus in temp2:
    media += graus
print(media/len(temp2))

media = sum(temp2) / len(temp2)         #metodo 02:
print(media)


#print(data['temp'].mean())              #Novo metodo

#print(data['temp'].max())               #Algumas series novas para serem usadas
#print(data['temp'].median())
#print(data['temp'].min())

#Pegar Dados em uma linha
#print(data[data.day == 'Monday'])
#print(data[data.temp == data.temp.max()])

#Pegar Dado dentro da linha
sunday = data[data.day == "Sunday"]
sunday_temp = sunday.temp[6]
print((sunday_temp * 9/5) + 32)

#Criar a Dataframe
data_dict = {
    "students": ["Amy","Joao","Ana"],
    "scores": [88, 40, 99]
}
new_data = pd.DataFrame(data_dict)
new_data.to_csv("new_data.csv")

n_data = pd.read_csv('new_data.csv')
print(n_data)
'''

big_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241031.csv')
color_squirls = big_data['Primary Fur Color']
print(color_squirls.value_counts())