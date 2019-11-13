#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime
import time


# In[ ]:


from firebase_admin import db
from requests import get
from firebase import firebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# In[ ]:


cred = credentials.Certificate("E:/557(公路比賽)/data/roaddata-f23ec-firebase-adminsdk-yuiau-072e4f0be2.json")
firebase_admin.initialize_app(cred)


# In[ ]:


t1 = 1
def timer(n):
    global t1
    while True:
        NO2022 = pd.read_csv('C:/DATA/NO2022.csv', encoding='utf-8')
        NO2022 = NO2022.rename(columns = {'Index_name':'id', 'StopName':'name', 'Lat':'lat', 'Lon':'lon'})
        data = pd.read_csv('spd.csv', encoding='big5')
        tm = data['Time'][0]
        if tm == t1:
            print('No')
        else:
            # 相機經緯度
            data['sx'] = data['Start'].str.split(',', expand=True)[0]
            data['sy'] = data['Start'].str.split(',', expand=True)[1]
            data['ex'] = data['End'].str.split(',', expand=True)[0]
            data['ey'] = data['End'].str.split(',', expand=True)[1]
            # 轉資料型態
            data['sx'] = data['sx'].astype('float')
            data['ex'] = data['ex'].astype('float')
            data['sy'] = data['sy'].astype('float')
            data['ey'] = data['ey'].astype('float')

            sample1={}
            sample2={}
            for q in range(len(NO2022)):
                AB = []
                for d in range(len(data)):
            #         位於區間(A, B)
                    if ((data['ex'][d]<=NO2022['lat'][q]<=data['sx'][d]) or (data['sx'][d]<=NO2022['lat'][q]<=data['ex'][d])):
                        if ((data['ey'][d]<=NO2022['lon'][q]<=data['sy'][d]) or (data['sy'][d]<=NO2022['lon'][q]<=data['ey'][d])):
                            AB.append(data['SectionName'][d])
                            if len(AB)>1:
                                sample1[NO2022['id'][q]] = AB
                            else:
                                sample2[NO2022['id'][q]] = data['SectionName'][d]
            if len(sample1)>0:
                df_557_1=pd.Series(sample1).apply(pd.Series).stack().apply(pd.Series).reset_index().drop('level_1',1)
                df_557_1.columns=['id','SectionName']

                df_557_2=pd.DataFrame({
                    'id':list(sample2.keys()),
                    'SectionName':list(sample2.values())
                })

                df_557=df_557_1.append(df_557_2, ignore_index=True)
            else:
                df_557=pd.DataFrame({
                    'id':list(sample2.keys()),
                    'SectionName':list(sample2.values())
                })

            data1=pd.merge(data,df_557,on=['SectionName'],how='left')

            data1=data1[data1['id'].notnull()]
            data1['id']=data1['id'].astype(int)
            data1=pd.merge(data1,NO2022,on=['id'],how='left')

            data1.sort_values(['AvgSpd'],inplace=True)
            data1.reset_index(drop=True,inplace=True)
            data1.drop_duplicates(['Time','id'],keep='last',inplace=True)

            # 算差距取最小值
            s1 = []
            s2 = []
            s3 = []
            for q in range(len(NO2022)):
                A = np.square(NO2022['lat'][q]-data['sx']) + np.square(NO2022['lon'][q]-data['sy'])
                A_S = np.sqrt(A)
                B = np.square(NO2022['lat'][q]-data['ex']) + np.square(NO2022['lon'][q]-data['ey'])
                B_S = np.sqrt(B)
                A_S_MIN = min(A_S)
                B_S_MIN = min(B_S)
                if A_S_MIN > B_S_MIN:
                    MIN =B_S_MIN
                elif A_S_MIN < B_S_MIN:
                    MIN = A_S_MIN
                else:
                    MIN = A_S_MIN
                s1.append(A_S)
                s2.append(B_S)
                s3.append(MIN)

            x1 = {}
            x2 = {}
            for i1 in range(len(s3)):
                M = []
                for i2 in range(len(data)):
                    if s1[i1][i2] == s3[i1]:
                        M.append(data['SectionName'][i2])
                        if len(M)>1:
                            x1[NO2022['id'][i1]] = M
                        else:
                            x2[NO2022['id'][i1]] = data['SectionName'][i2]
            #             print(i1, i2, M)
                    if s2[i1][i2] == s3[i1]:
                        M.append(data['SectionName'][i2])
                        if len(M)>1:
                            x1[NO2022['id'][i1]] = M
                        else:
                            x2[NO2022['id'][i1]] = data['SectionName'][i2]
            #             print(i1, i2, M)

            df_min_1=pd.Series(x1).apply(pd.Series).stack().apply(pd.Series).reset_index().drop('level_1',1)
            df_min_1.columns=['id','SectionName']

            df_min_2=pd.DataFrame({
                'id':list(x2.keys()),
                'SectionName':list(x2.values())
            })

            df_min=df_min_1.append(df_min_2, ignore_index=True)

            data2=pd.merge(data,df_min,on=['SectionName'],how='left')

            data2=data2[data2['id'].notnull()]
            data2['id']=data2['id'].astype(int)
            data2=pd.merge(data2,NO2022,on=['id'],how='left')

            data2.sort_values(['AvgSpd'],inplace=True)
            data2.reset_index(drop=True,inplace=True)
            data2.drop_duplicates(['Time','id'],keep='first',inplace=True)

            check = data1.append(data2, ignore_index=True)
            check = check.drop_duplicates(['id'])
            check.reset_index(inplace=True, drop=True)

            check = check[['id', 'name', 'Time', 'SectionName', 'AvgSpd', 'Rank']]
            print(check)
            #連接資料庫
            engine = create_engine('mysql+pymysql://root:a83w.6j06@127.0.0.1:3306/traffic')
            con = engine.connect()
            #寫入資料庫
            check.to_sql('082022', engine, if_exists='append')
            #寫入firebase
            c = check[['id', 'Time', 'Rank']]
            c['id'] = c['id'].astype('str')

            for fk in range(len(c)):
                db = firestore.client()
                doc_ref = db.collection('road_spd').document('NO2022').collection(c['id'][fk]).document('Rank')
                fkd = {'Time':c['Time'][fk], 'Rank':c['Rank'][fk]}
                doc_ref.set(fkd)
                print(fkd)
        t1 = tm
        time.sleep(n)


# In[ ]:


timer(300)


# In[ ]:





# In[ ]:




