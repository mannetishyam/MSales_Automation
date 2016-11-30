import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
from pandas import *
import datetime
import openpyxl as pyxl
import os
import time
import urllib
def connected(host='http://google.com'):
    try:
        urllib.urlopen(host)
        return True
    except:
        return False
#Online sheet part
k=0
while k!='stop':
    if connected()==True:
         print "Connected to Internet"
         os.chdir("D:/Saarang 2017/Summer work/code")
         scope = ['https://spreadsheets.google.com/feeds']
         credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project 1-cc2490dd3c9e.json', scope)
         gc = gspread.authorize(credentials)
         sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1tKs8jyNr5sItjM8Hn5ZsDoFUk-kg7BwiFoIv5qVUowM/edit#gid=1479630181')
         worksheet =sh.sheet6
         ws =sh.get_worksheet(1)
         dat=datetime.date.today().strftime("%d-%m-%Y")
         df=pd.ExcelFile('sample.xls')
         df = df.parse("ikollege")
         tickets=['RG','RB','RF','PG','PSC','PGC','PPC','EG','EB','EF','CG','CC']
         A={}
         m=[]
         df1=pd.DataFrame(df)
         df['number']=1
         table=pivot_table(df1,values='number',index='Rock Show',columns='Total Purchase',aggfunc=np.sum)
         df=pd.DataFrame(table)
         df=df.fillna(0)
         df=df.astype(int)
         col=list(df.columns.values)
         ind=list(df.index.values)
         for i in ind:
              for j in col:
                   k=df.get_value(i,j)
                   if k!=0:
                        name=i[0]+j[0:10]
                        name=''.join(c for c in name if c.isupper())
                        A[name]=k
         Akeys=list(A)
         m=m+[dat]
         for l in range(len(tickets)):
              if tickets[l] in Akeys:
                   m=m+[A[tickets[l]]]
              else:
                   m=m+[0]
         print "Values are collected from sheet"
         g=worksheet.col_values(1)
         g=len(filter(bool, g))
         f=0
         if dat!=worksheet.cell(g,1).value:
             g=g+1
         print "Connecting to live sheet"
         tex='A'+str(g)+':M'+str(g)
         cell_list=worksheet.range(tex)
         for cell in cell_list:
             cell.value=m[f]
             f=f+1  
         worksheet.update_cells(cell_list)
         j=datetime.datetime.now().time().strftime("%H:%M")[:5]
         worksheet.update_acell('N'+str(g),j)
         if len(filter(bool, worksheet.col_values(15))) != g:
             l=0
         else:
             l=int(worksheet.cell(g,15).value)
         worksheet.update_cell(g,15,l+1)
         print "Upload complete"
         time.sleep(2)
         k='stop'
    else:
         print  "No internet Connection"
         time.sleep(5)
         print " Trying again......"
'''
inp=raw_input().strip()
def palindromes(text):
    text = text.lower()
    results = []
    for i in range(len(text)):
        print i
        for j in range(0, i):
            print "This is j "+str(j)
            chunk = text[j:i + 1]    
            print chunk
            if chunk == chunk[::-1]:
                results.append(chunk)
                #print results
    length=[len(i) for i in results]
    print results[length.index(max(length))]
palindromes(inp)

# Enter your code here. Read input from STDIN. Print output to STDOUT
yu,ym=map(int,raw_input().strip().split(' '))
S=str(raw_input().strip().replace(" ",""))
T=str(raw_input().strip().replace(" ",""))
def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])
    return lcs_set
print lcs(S,T)

'''


