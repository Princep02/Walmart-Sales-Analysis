#pip install pandas
#pip install pandas-profiling
import pandas as pd
from ydata_profiling import ProfileReport

df=pd.read_csv('Data.csv.csv')
print (df)

#Generate a report
profile=ProfileReport(df, title="Data profile")
profile.to_file(output_file="Data_report.html")
