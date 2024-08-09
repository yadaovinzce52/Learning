import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey = len(data[data['Primary Fur Color'] == 'Gray'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])

color_dict = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [grey, red, black]
}

colors_csv = pandas.DataFrame(color_dict)
colors_csv.to_csv('squirrel_count.csv')
