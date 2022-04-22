import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    studentmarks=[]
    dayspresent=[]
    with open (data_path) as f:
        df=csv.DictReader(f)
        for row in df:
            studentmarks.append(float(row['Marks In Percentage']))
            dayspresent.append(float(row['Days Present']))
        return{"x":studentmarks,"y":dayspresent}    
        
def findcorelation(data_source):
    corelation=np.corrcoef(data_source['x'],data_source['y'])
    print (corelation[0,1])
def setup():
    data_path='present.csv'
    data_source=getDataSource(data_path)
    findcorelation(data_source)
setup()