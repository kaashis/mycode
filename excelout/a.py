import pandas as pd

excel_file ="/home/student/mycode/hockey.xls"

hockey=pd.read_excel(excel_file)
#hockey is now an object called a DF

print(hockey.head())

# who are the tallest hockey players?
height= hockey.sort_values(["HtIn"], ascending = False)

print(height.head(10))

height.to_excel("editedhockey.xls", index = False)

x=height.to_dict()

print(x)
