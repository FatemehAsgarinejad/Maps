import tables
import pandas as pd
import numpy as np
h5_file = tables.open_file("../../../../../restricted_images_national.h5")
table_train = h5_file.get_node("/{}".format("train")) #len=58263
table_validate = h5_file.get_node("/{}".format("validate")) #len=7744
table_test = h5_file.get_node("/{}".format("test")) #len= 13509

#table_train.colnames #Table[0][0:11] ['img0','img1','img_id','inc0','inc1','lat','lng','pop0','pop1','pop_centile','sol0','sol1']
#print(len(table_train[0]), len(table_train[0][0]), len(table_train[0][0][0]), len(table_train[0][0][0][0]))
#(12, 94, 94, 7)
#table.colnames #Table[0][0:11]
lats = [] #latitudes of points
lngs = [] #longitudes of points
pop0 = [] #Population of 2000 of points
pop1 =[] #Population of 2010 of points
popdiff = [] #Pop1 - Pop0
inc0 = [] #Income of 2000
inc1 =[] #Income of 2010 of points
incdiff = [] #inc1 - inc0 of points
for table in [table_train, table_validate, table_test]:
    for row in table:
        #row[3]=inc0, row[4]=inc1, row[5]=lat, row[6]=lng, row[7]=pop0, row[8]=pop1
        inc0.append(row[3])
        inc1.append(row[4])
        incdiff.append(row[4] - row[3])
        lats.append(row[5])
        lngs.append(row[6])
        pop0.append(row[7])
        pop1.append(row[8])
        popdiff.append(row[8]-row[7])
print("total {}".format(len(inc0)))
for feature in [inc0, inc1, incdiff, lats, lngs, pop0, pop1, popdiff]:
    print("len: {} | std: {} | max: {} | min: {} | mean: {}".format(len(feature), np.std(feature), max(feature), min(feature), np.mean(feature)))
df = pd.DataFrame(data={"inc0": inc0, "inc1": inc1, "incdiff": incdiff, "lats": lats, "lngs": lngs, "pop0": pop0, "pop1": pop1, "popdiff": popdiff })
df.to_csv("images.csv", sep=',',index=True)
df=pd.read_csv("images.csv")
df.head()
lats, lngs = df['lats'], df['lngs']
