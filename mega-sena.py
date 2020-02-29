import pandas as pd
# content = str(open("d_mega.htm",'r').read())
data = pd.read_csv("d_mega.csv")
for i in data.Concurso:
    print(i)
# print(data['1'])