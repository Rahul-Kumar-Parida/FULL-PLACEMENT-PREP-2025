# # 1)
# tup1=(1,2,3,"a")
# tup2= (5,6,7)
# print(tup1+tup2)
# print(tup2+tup1)

# import numpy as np
# arr = np.zeros((5, 5))  
# print(arr)

import pandas as pd
# data={'Name':['Rahul','Rohit'], 'Age':[25,30]}
# df= pd.DataFrame(data)
# print(df)

# data=[2,3,4,5]
# sr=pd.Series(data)
# print(sr)

# data={'Dept':['MCA','IT','MCA','IT'],'Salary':[3000,4000,5000,2000]}
# df=pd.DataFrame(data)
# res=df.groupby('Dept')['Salary'].sum()
# print(res)

# df=pd.DataFrame()
# marks=[34,56,78,90]
# subject=["OOPS","SQL","C++","JAVA"]
# df["subject"]=subject
# df["marks"]=marks
# print(df)

# lis=[["Mca",23],["IT",46],["CSE",56]]
# df1=pd.DataFrame(lis,columns=["Dept","Marks"])
# print(df1)

# data={"Name":["Rahul","Rohit","Sangram"],"Age":[23,12,24]}
# df2=pd.DataFrame(data)
# print(df2)

# d1={'ID': [1, 2, 3], 'Name': ['Amit', 'Neha', 'Raj']}
# d2={'ID': [1, 2, 3], 'Age': [23,24,25]}
# df1=pd.DataFrame(d1)
# df2=pd.DataFrame(d2)
# res=df1.set_index('ID').join(df2.set_index("ID"))
# print(res)


# d1={'ID': [1, 2, 3], 'Name': ['Amit', 'Neha', 'Raj']}
# d2={'ID': [3,4,5], 'Name': ["Real","Sarkar","Gaming"]}
# df1=pd.DataFrame(d1)
# df2=pd.DataFrame(d2)
# res=pd.concat([df1,df2],ignore_index=True)
# print(res)

# d1={'ID': [1, 2, 3], 'Name': ['Amit', 'Neha', 'Raj']}
# d2={'ID': [1, 2, 4], 'Age': [23,24,25]}
# df1=pd.DataFrame(d1)
# df2=pd.DataFrame(d2)
# res=pd.merge(df1,df2, on="ID", how='inner')
# print(res)

# df = pd.DataFrame({'Col1': [1.0, 2.0, None], 'Col2': ['A', 'B', 'C']})  
# res=df.dropna()
# print(res)

# d1={'ID': [1, 2, 3], 'Name': ['Amit', 'Neha', 'Raj']}
# df1=pd.DataFrame(d1)
# print(df1)
# df1.set_index("ID", inplace=True)
# print(df1)
# print(df1.loc[2])


# import numpy as np  
# from scipy import stats 

# arr = np.array([1, 5, 1, 100, 4, 48])
# mean=np.mean(arr)
# median=np.median(arr)
# mod=stats.mode(arr)
# print(mean," ",median," ",mod)


# my_dict = {"name": "John", "age": 25, "city": "New York"}
# print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])


# str="rahul Kumar"
# print(str.capitalize())

# lst=[1,2,3,4,5]
# lst.insert(3,5)
# print(lst)
# lst=[1,1,2,2,2,3,4,5]
# nwlst=list(set(lst))
# n=list(dict.fromkeys(lst))
# print(n)

# lst=[]
# for i in range(1,6):
#     lst.append(i**2)
# print(lst)

# ls=[x**2 for x in range(1,6)]
# print(ls)

# with open(r"D:\Users\rahul\PYTHON\PYTHON INTERVIEW QUESTIONS\Dbms.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)


# num=[1,2,3,4]
# lst=list(map(lambda x:x**2, num))
# print(lst)

# class example:
#     def __init__(self,name):
#         self.name=name

# obj=example("Jhon")
# print(obj.name)


# text="Rahul Kumar Parida"
# words=text.split()
# print(words)

def add(a,b):
    """This is sum"""
    return a+b
print(add.__doc__)