import pandas as pd

#Preprocessing - cleaning the data
df = pd.read_csv('/home/fatemeh/satellite-cnn/derived/SCNN (Train From Scratch)/src/Maps/counties_FIPS.txt', sep="        ", header=None)
df.columns = ["FIPS" , "county"]
df["county"] = [df["county"].iloc[i].replace(' County','') for i in range(0, len(df))] #removing "County in the NAMES column"
temp = []
for i in range(len(df)):
    temp.append(str(df['FIPS'].iloc[i]))
df['FIPS'] = temp

#converting 4digit FIPS to 5digit
def convert_2_5digit(fips):
    return "".join(['0',str(fips)])
for row in range(len(df)):
    if len(str(df['FIPS'][row])) ==4:
        df['FIPS'][row] = convert_2_5digit(df['FIPS'][row])
df.to_csv("counties_FIPS.csv", sep=',',index=True)
#df=pd.read_csv("counties_FIPS.csv")
#del df['Unnamed: 0']
