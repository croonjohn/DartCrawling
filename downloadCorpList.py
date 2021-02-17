### 필요한 모듈
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

### 회사고유번호 데이터 불러오기
url = 'https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=b32ba8d8ed48d5f400fd33bc64eba9861b3dbac1'
with urlopen(url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('corp_num')