import numpy as np
import pandas as pd


###################################################
## Building Relational tables
###################################################

# Population (in millions)
population_dict = {'California': 38,
                    'Texas': 26,
                    'New York': 20,               
                    'Florida': 19,                  
                    'Illinois': 13}

# Area in square kilometers
area_dict = {'California': 423967,
            'Texas': 695662,
            'New York': 141297,
            'Florida': 170312,
            'Illinois': 149995}

largestcity_dict = {'California': 'Los Angeles',
            'Texas': 'Houston',
            'New York': 'New York',
            'Florida': 'Jacksonville',
            'Illinois': 'Chicago'}

# Just one column in a table
print('************** JUST 1 COLUMN ****************')
population = pd.Series(population_dict)
print(population)
print(population['California':'New York'])


print('************** WIDER DATAFRAME ****************')

# Combine DataFrame from several Series
area = pd.Series(area_dict)
city = pd.Series(largestcity_dict)
USStateDF = pd.DataFrame({'population': population,
                    'area': area, 'city':city})
print(USStateDF)


print('************** GENERATED DATAFRAME ****************')
data = [{'a': i, 'b': 2 * i} for i in range(5)]
numberDF = pd.DataFrame(data)
print(numberDF)


########################################################
## Project operation
########################################################

print('************** BEFORE PROJECT ****************')

print(USStateDF)

print('************** AFTER PROJECT ****************')

ProjectedDF = USStateDF[['population', 'city']]

print(ProjectedDF)




########################################################
## Union of two dataframes
########################################################

print('************** UNION ****************')
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
ser3 = pd.concat([ser1, ser2])
print(ser3)




########################################################
## (Inner) Join of two dataframes
########################################################

print('************** INNER JOIN ****************')

df1 = pd.DataFrame({
    'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
    'department': ['Accounting', 'Engineering','Engineering', 'HR']})
df2 = pd.DataFrame({
    'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
    'date': [2004, 2008, 2012, 2014]})
                    
df3 = pd.merge(df1, df2)
print(df3)






