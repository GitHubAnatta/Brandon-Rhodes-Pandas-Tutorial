# Conventional way to import pandas
import pandas as pd 

# to get a dataframe from a csv
df = pd.read_csv('data/titles.csv')

# find how many rows in a dataframe
len(df)

# return the head or tail of a dataframe
df.head()
df.head(10) #specify how many you want
df.tail()


#########################################

#PART 1

# Columns are called series when you pull them out

# to create a series
df['title']

# you can do math on series like you are doing it on 1 number and it will do it all
# example: the following will subtract 1900 from all the years
years_adj = df['year'] - 1900

# if col name plays nice, you can do dot notation too
years = df.year

# you can return booleans
df.year > 1985

# you can filter  using the square bracket notation and a boolean operation
#this returns all the years less than 1985
df[df.year < 1985] 

# you cannot do this however
#returns error
df[df.year < 1980 and df.year >= 1990]
#the truth value of a series is ambiguius

# but you can use & instead.  Because python you must use paretheses
df[(df.year < 1980) & (df.year >= 1990)]
# | for or
df[(df.year < 1980) | (df.year >= 1990)]

# you can sort dataframes by a collumn 
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
macbeth_by_year = df[df.title == 'MacBeth'].sort_values(by=['year'],ascending=True) #true is default

# you can grab dataframes that are or not null (like NaN for example)
df_null = h[h.n.isnull()]
df_notNull = h[h.n.notnull()]


############################################################################################


#PART 2

#string methods do not work on dataframes
#this returns an error
df.title.startswith('the')

#however if we use .str we can use string methods
df.title.str.startswith('the')

#we can use value_counts to figure out how many times a specific value appears
df.year.value_counts()

#you can plot series using .plot()
df.year.value_counts().plot()

#this will suck though because the pandas index is not sorted
#we can sort by index 
df.year.value_counts().sort_index().plot

#you can plot using something other than index
df.plot(x='year', y='n', kind='scatter')

#you can get multiple collums
df[['year','n']]

