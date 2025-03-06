#pandas is a open sourse data analysis library written in python

#series - it is a one dimensional array with indexes it stores a single coloumn or row of data in a dataframe
# DATA TUPE ON INIVUAL COLOUMN IS CALLED A SERIES

#DATAFRAME- it is a tabluar spreadsheetlike structure representing rows each of which contains one or multiple coloumns


import numpy as np
import pandas as pd
 
dict1={
    "name":['sanket' ,'rohan'],
    "marks":[20 ,30],
    "city":['kolkata', 'Delhi']
}

#DATAFRAME
df=pd.DataFrame(dict1)   #data frame is a a excel sheet  is line will convert the dict1 data into a excel sheet

# print(df)
# df.to_csv('table.csv') #covert it to csv file

# df.to_csv('table.csv_noindex', index=False)

# df.head (2) #starting 2 rows
# df.tail(2)#ending 2 rows

# df.describe() #will count mean and basically give a statisticall analyisis of the numeric data

# table= pd.read_csv('table.csv') #to read a particular csv file

# print(table['marks'][0]) #to print particular element from a table

# table['marks'][0]=50#update statement
# print(table['marks'][0]) 


#SERIES
import numpy as np
import pandas as pd
# ser=pd.Series(np.random.rand(34))
# print(ser)

# type(ser)



newdf=pd.DataFrame(np.random.rand(334, 5), index=np.arange(334)) #craeting a dataframe  using random function and givinng them a proper index
# print(newdf)
type(newdf)
print(type(newdf)) 
newdf.dtypes

newdf[0][0]="sanket" 

newdf.loc[0,0]























