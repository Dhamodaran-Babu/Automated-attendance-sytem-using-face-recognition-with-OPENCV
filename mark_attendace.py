# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:13:52 2020

@author: Dhamodaran
"""

from datetime import date
import pandas as pd
from calendar import month as MM
from pathlib import Path



def attendance_marker(present_people):
    today=date.today()
    today_str=today.strftime("%d-%b-%Y")
    day,month,year=today_str.split("-")
    day=int(day)
    filename=month+""+year+".csv"  
    filename=Path(filename)
    df=pd.DataFrame()
    if filename.exists():
        df=pd.read_csv(filename)
        df.index=df['student_id']
        df.loc[df.student_id==int(present_people),str(day)]=int(1)
        print(df[str(day)])
        print(df)
        df.to_csv(filename,index=False)
    
    else:
        mm_cal=MM(today.year,today.month)
        max_date=mm_cal[len(mm_cal)-3]+mm_cal[len(mm_cal)-2]
    
        columns=[]
        for i in range(1,int(max_date)+1):
            columns.append(i) 
        df=pd.DataFrame(columns=columns)
        
        names=pd.read_csv('students details.csv',header=None)
        names.columns=['student_id','name']
        names.index=names['student_id']
        names.drop(columns='student_id')
        df=pd.concat([names,df],axis=1) 
    
        df.loc[df.student_id==int(present_people),day]=1
        print(df[day])
        df.to_csv(filename,index=False)
    
attendance_marker(5)
    
