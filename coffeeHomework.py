import plotly.express as px
import csv 
import numpy as np 
def getDataSource():
    marks=[]
    days=[]
    with open ("percentage.csv") as sfile:
        df=csv.DictReader(sfile)
        for row in df:
            marks.append(float(row["Coffee in ml"]))
            days.append(int(row["sleep in hours"]))
        return{"x":marks,"y":days}

def findCorrelation(ds):
    correlation=np.corrcoef(ds["x"],ds["y"])
    print("correlation ",correlation[0,1])

ds=getDataSource()
findCorrelation(ds)
with open ("percentage.csv") as sfile:
    df=csv.DictReader(sfile)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()