import pandas as pd

df = pd.read_csv('/home/fatemeh/satellite-cnn/derived/SCNN (Train From Scratch)/src/Maps/2019_Gaz_counties_national.txt', sep=",", header=None)
df.columns = ["USPS" , "GEOID" , "ANSICODE" , "NAME" , "ALAND" , "AWATER" , "ALAND_SQMI" , "AWATER_SQMI" , "INTPTLAT" , "INTPTLONG"]
df = df[["NAME", "GEOID","INTPTLAT" , "INTPTLONG"]]
Names = [df["NAME"].iloc[i].replace(' County','') for i in range(0, len(df))] #removing "County in the NAMES column"
Names = [Names[i].replace(' Municipio','') for i in range(0, len(Names))] #removing "County in the NAMES column"
df["NAME"] = Names
#df.to_csv("coordinates.csv", sep=',',index=True)

#Filtering the rows with specific values for columns
R = pd.read_csv('R_FIPS.csv')
#R.columns = ["num", "fips"]
#fips = R['fips'].tolist()

#[i for i, j in zip(fips, df['GEOID'].tolist()) if i == j]
#R.columns = ["num", "fips"]
#del R['num']
#fips = R['fips'].tolist()
#df = df[df['GEOID'].isin(fips)]
#fips = df['GEOID'].tolist()
#df.to_csv("Final_data.csv", sep=',',index=True)
#df['GEOID'].to_csv("R_FIPS.csv", sep=',',index=True)
#Adding states names to dataframe
abbr = pd.read_csv('/home/fatemeh/satellite-cnn/derived/SCNN (Train From Scratch)/src/Maps/state-abbrevs.csv', sep=",", header=None)
abbr.columns = [["STATE" ,"ABBR"]]
abbr.drop(0)
