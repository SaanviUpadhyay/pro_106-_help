
import plotly.express as px
import csv
import numpy as np

def plotFig(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)

        fig = px.scatter(df , x="Days Present" , y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    days_present= []
    marks       = []

    with open(data_path) as f :
        csv_reader = csv.DictReader(f)

        for row in csv_reader :
            days_present.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))

    return {
              "x" : days_present ,
              "y" : marks
           }

def correlation(data_Source):
    correlation = np.corrcoef(
                                 data_Source["x"] , 
                                 data_Source["y"]
                             )
    print("Correlation coefient is " , correlation[0,1])

 
def main():
    data_path = "Student Marks vs Days Present.csv"
    correlation(data_path)
    plotFig(data_path)

main()
