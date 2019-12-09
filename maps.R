library(maps)
library(dplyr)

data(county.fips)
dat = read.csv("/Users/fatemeh/Desktop/Maps/Final_data.csv", header = TRUE)
GeoID<- as.vector(dat['GEOID'])
#vals<- abs(GeoID)
x <- abs(rnorm(3074)*10)
vals <- x

dataframe <- data.frame(fips=c(GeoID), 
                        values=c(vals) )

#df_pop_county <- data.frame(region=county.fips$fips)
#df_pop_county$value <- county.fips$fips
y <- dataframe$values
dataframe$color <- rainbow(n=1, y / max(y))

## merge population data with county.fips to make sure color column is
## ordered correctly.
#counties <- county.fips %>% left_join(df_pop_county, by=c('fips'='region'))
map("county", fill=TRUE, col=dataframe$color)