import pandas as pd
import numpy as np
import math
data = pd.read_csv('Maps/Final_data.csv')
images_of_counties = {i: [] for i in data['GEOID'].values.tolist()}
counties_lats = data['INTPTLAT'].values.tolist()
counties_lngs = data['INTPTLONG'].values.tolist()
#images_of_counties[29201]
#images_of_counties.values()[0].append(1)

def L1_distance(v1, v2):
    return sum([abs(x-y) for (x,y) in zip(v1,v2)])
#Euclidean_distance((1,2),(3,4))

images = pd.read_csv('images.csv')
images_lats = images['lats'].values.tolist()
images_lngs = images['lngs'].values.tolist()

for i in range(len(images)):
    euclidean_distances = []
    for j in range(len(data)):
        tmp = Euclidean_distance((images_lngs[i], images_lats[i]), (counties_lngs[j], counties_lats[j]))
        euclidean_distances.append(tmp)
    index = euclidean_distances.index(min(euclidean_distances))
    print(index)
    images_of_counties[data['GEOID'].iloc[index]].append(images['popdiff'][i])
    #print(index)
    #print("\n")
    #print(images_of_counties[data['GEOID'].iloc[index]])
x = images_of_counties
values = []
for i in range(len(images_of_counties.values())):
    if len(images_of_counties.values()[i]) == 0:
        values.append(0)
    if len(images_of_counties.values()[i]) !=0:
        values.append(sum(images_of_counties.values()[i])/len(images_of_counties.values()[i]))
final_data = pd.DataFrame({'fips': data['fips'].values.tolist(),
                          'values': values})
final_data.to_csv("final_data.csv", sep=',',index=True)
data = pd.read_csv('final_data.csv')
del data['Unnamed: 0']
pallete = ['#f7fcf5', '#e5f5e0', '#c7e9c0', '#a1d99b', '#74c476', '#41ab5d', '#238b45', '#005ad2c', '#00441b']
colors = ['#ffffff']*len(data)
maximum =data['values'].max()
#normalizing values
for i in range(len(data)):
    if data['values'].iloc[i] == 0:
        data['values'].iloc[i] = 1
        data['values'].iloc[i] = data['values'].iloc[i]/maximum
    else:
        data['values'].iloc[i] = data['values'].iloc[i]/maximum
minimum, maximum = data['values'].min(), data['values'].max()
step = (maximum - minimum)/9
steps = []
for i in range(9):
    steps.append([minimum+i*step, minimum+(i+1)*step])
steps[8][1]+=1

def get_value(indx):
    val = data['values'].iloc[indx]
    pal = 0
    for i in range(len(steps)):
        if val <= steps[i][1] and val >= steps[i][0]:
            pal = i
    return pal

non_white_counts = 0
white_counts = 0
for j in range(len(data)):
    if data['values'].iloc[j] == 0:
        white_counts += 1
        pass
    else:
        index = get_value(j)
        colors[j] = pallete[index]
        non_white_counts +=1
#print(non_white_counts)
#print(white_counts)
#colors.count("#ffffff")
data['colors'] = colors
data.to_csv("plottable.csv", sep=',',index=True)

