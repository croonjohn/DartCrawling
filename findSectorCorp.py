### xml 모듈 import
import pickle
import time
import requests
import pandas as pd
import openpyxl



# 해당 업종, 상장구분의 기업들이 들어갈 list
total_company_list=[]
induty_code_list = ['2915','29150','41224']
corp_cls_list = ['Y','K','N','E']

def selectCorp(company, induty_code_tolook, corp_cls_tolook):
    for i in induty_code_tolook:
        if i == company['induty_code']:
            for j in corp_cls_tolook:
                if j == company['corp_cls']:
                    total_company_list.append(company)
                    return
                else: pass
        else: pass
    return


with open('total_company_list.txt','rb') as f:
    data=pickle.load(f)
    for i in data:
        #selectCorp(i, induty_code_list, corp_cls_list)
        total_company_list.append(i)


df = pd.DataFrame(total_company_list)
df.to_csv('DART전체기업리스트.csv', encoding='cp949')


