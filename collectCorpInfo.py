#### xml 모듈 import
#import xml.etree.ElementTree as ET
#import time
#import requests
#
#### xml 파일 읽기
#tree = ET.parse('corp_num/CORPCODE.xml')
#root = tree.getroot()
#
#
#
#### 기업 고유번호 모음 list 만들기
#code_list=[]
#for country in root.iter("corp_code"):
#    code_list.append(country.text)
#
#
#
#### 기업개황 검색 함수 만들기
#def load_data(corp_code):
#    
#    ### 본인의 인증키 입력
#    crtfc_key_1 = "b32ba8d8ed48d5f400fd33bc64eba9861b3dbac1"
#    crtfc_key_2 = "57a347d79473131eeccb4bad3661798bfa1d6f86"
#    crtfc_key_3 = "cdbff271a23305c862a7ba5e2e4b675001dfd3ad"
#    crtfc_key_4 = "7774c5c250b8b44952e958116f06dbe6197470ef"
#    crtfc_key_5 = "본인이 발급받은 인증키"
#    crtfc_key_6 = "본인이 발급받은 인증키"
#    crtfc_key_7 = "본인이 발급받은 인증키"
#    crtfc_key_8 = "본인이 발급받은 인증키"
#    crtfc_key_9 = "본인이 발급받은 인증키"
#    
#    ### 기업개황 요청 url
#    url = 'https://opendart.fss.or.kr/api/company.json?crtfc_key='+crtfc_key_3+'&corp_code='+corp_code
#
#    ### HTTP 요청
#    r = requests.get(url)
#
#    ### 요청한 데이터는 json형태이기 때문에 json으로 읽어줍니다.
#    company_data = r.json()
#
#    ### 기업개황을 요청했을 때 기업개황에 대한 자료를 반환합니다.
#    return company_data
#    
#    
#    
#### 데이터를 담아둘 list 생성
#company_list_1 = [] # company_list_1 0 ~ 9,000 
#company_list_2 = [] # company_list_2 9,000 ~ 18,000 
#company_list_3 = [] # company_list_3 18,000 ~ 27,000 
#company_list_4 = [] # company_list_4 27,000 ~ 37,000 
#company_list_5 = [] # company_list_5 37,000 ~ 47,000 
#company_list_6 = [] # company_list_6 47,000 ~ 57,000 
#company_list_7 = [] # company_list_7 57,000 ~ 67,000 
#company_list_8 = [] # company_list_8 67,000 ~ 77,000 
#company_list_9 = [] # company_list_9 77,000 ~ 83,571
#
#checker = 0
#
#### 반본문 실행
#for corp_code in code_list[77000:-1]:
#    company_dict = load_data(corp_code)
#    checker += 1
#    if checker == 999:
#        time.sleep(65)
#        checker = 0
#
#    ### list 변경할것
#    company_list_9.append(company_dict)
#    
#    
#    
#### pickle 모듈 import
#import pickle
#
#### pickle 모듈을 통해 list 저장
#with open('company_9.txt','wb') as f:
#       pickle.dump(company_list_9,f)

import pickle
### 기업개황 통합하기
# 모든 기업개황이 담길 list
total_company_list=[]

# for문을 이용해 통합
for num in range(1,10):
    file_name = 'company_'+str(num)+'.txt'
    with open(file_name,'rb') as f:
        data=pickle.load(f)
        total_company_list=total_company_list + data
        
# 통합 list 저장
with open('total_company_list.txt','wb') as f:  
    pickle.dump(total_company_list,f)