# 키워드 추출 및 유사도 분석을 위한 hssh 패키지
<i>한성과학고등학교 2022학년도 과제연구 - 2702 김수진</i>

python 패키지 <b>hssh</b>는 pandas의 DataFrame형태로 입력된 문서군에서 키워드를 추출하고 코사인 유사도를 이용해 유사한 문서를 찾을 수 있게 합니다.

## 목차
* [기능](https://github.com/Sujin-Github/Study2022/blob/main/README.md#%ED%82%A4%EC%9B%8C%EB%93%9C-%EC%B6%94%EC%B6%9C-%EB%B0%8F-%EC%9C%A0%EC%82%AC%EB%8F%84-%EB%B6%84%EC%84%9D%EC%9D%84-%EC%9C%84%ED%95%9C-hssh-%ED%8C%A8%ED%82%A4%EC%A7%80)
* [설치](https://github.com/Sujin-Github/Study2022/blob/main/README.md#%ED%82%A4%EC%9B%8C%EB%93%9C-%EC%B6%94%EC%B6%9C-%EB%B0%8F-%EC%9C%A0%EC%82%AC%EB%8F%84-%EB%B6%84%EC%84%9D%EC%9D%84-%EC%9C%84%ED%95%9C-hssh-%ED%8C%A8%ED%82%A4%EC%A7%80)
* [사용 - Document 클래스](https://github.com/Sujin-Github/Study2022/blob/main/README.md#document-%ED%81%B4%EB%9E%98%EC%8A%A4-hsshdefclassdocument)
* [사용 - Paper 클래스](https://github.com/Sujin-Github/Study2022/blob/main/README.md#paper-%ED%81%B4%EB%9E%98%EC%8A%A4-hsshdefclassdocument)
* [예시](https://github.com/Sujin-Github/Study2022/blob/main/README.md#%EC%98%88%EC%8B%9C)

## 기능
* <b>문서군에서</b>
	* 빈도수를 기반으로 문서군 단어집 생성
	* 단어별 역문서 빈도(inverse document frequency, IDF) 계산
	* 역문서 빈도를 기반으로 단어집에서 부적절한 단어 삭제
	* 문서군의 각 문서별 키워드 추출
	* 문서군의 각 문서간 유사도 계산
	
* <b>문서에서</b>
	* 문서군의 단어집을 이용, 단어 빈도 (term frequency, TF) 계산
	* 키워드 추출

## 설치
```python
pip install hssh
```
/ <b>hssh</b>는 numpy, pandas, konlpy 등을 필요로합니다.

## 사용
### Document 클래스 (hssh.DefClass.Document)
### Document(dataframe, analysis_by) 

* `dataframe` : 문서군이 저장된 데이터프레임을 받습니다. header가 있어야합니다.   
* `analysis_by` : 형태소 분석을 할 열의 칼럼명을 받습니다.   

<br>

* `.dataframe` : 원본 dataframe   
* `.df` : analysis_by를 칼럼으로 하는 series. 데이터의 양을 줄이기 위해 사용   
* `.voca_dict` : 문서군에서 등장하는 명사를 { '단어' : '등장 횟수' }의 형태로 횟수가 많은 순부터 내림차순으로 정리한 딕셔너리   
* `.voca_list` : 문서군에서 등장하는 명사를 등장 횟수가 많은 순부터 내림차순으로 정리한 리스트 (`Document.voca_dict`의 key값)   
* `.idf_dict` : 단어집의 단어들의 IDF를 { '단어' : 'idf값' }의 형태로 정리한 딕셔너리   

<br>

* `.modify_voca([cut])` : IDF가 cut 이하인 단어를 voca_list와 voca_dict에서 삭제 후 삭제되는 단어를 출력. 기본 1.5
* `.keywords([index_by,[cut]])` : 문서군 내 문서의 TF-IDF값을 { '문서 이름' : [ ( 단어1 , TF-IDF1) , ... ] ... } 형태로 정리. '문서 이름'은 dataframe에서 index_by를 칼럼명으로 하는 칼럼에 해당하는 값으로 지정. index_by기본 '제목', cut 기본 2.
* `.cos_sim([index_by])` : 코사인 유사도를 이용해 구한 각 문서간 유사도를 데이터프레임으로 정리. dataframe에서 index_by 칼럼을 칼럼/인덱스명으로 지정. 기본 '제목'
<br><br>

### Paper 클래스 (hssh.DefClass.Document)
### Paper(content,document)

* `content`: 분석을 할 내용입니다. 문자열(str)을 받습니다.
* `document` : 문서가 포함된 Document 클래스를 받습니다.
	
* `.txt` : 원본 content
* `.doc` : 원본 document
* `.tf` : `document.voca_list` 기준의 TF 값을 저장한 numpy array
* `.tftdf` : `document.voca_list` 기준의 TF-IDF 값을 저장한 numpy array로, 단어별 TF와 IDF의 값.
* `.keywords` : `keywords_f`의 실행값 (하단)

* `.keywords_f([cut])` : TF-IDF 값이 cut 이상인 단어만 내림차순으로 [ ( '단어1' , TF-IDF값1 ) , ... ] 형태로 반환. 실행한 후 .keywords에 저장. cut 기본값 2.


## 예시

#### cf. 예시 데이터 가져오기
```python
import urllib

urllib.request.urlretrieve('https://raw.githubusercontent.com/Sujin-Github/Study2022/main/SampleData/2021_%EC%9A%B0%EC%88%98%EB%85%BC%EB%AC%B8_%EC%B4%88%EB%A1%9D.csv', "SampleData.csv")
#Sampledf=pd.read_csv('SampleData.csv',sep=',',encoding='cp949')
```
`출력` ('SampleData.csv', <http.client.HTTPMessage at 0x19b2298a040>)

* <i>예시 데이터는 한성과학고등학교 2021학년도 30기(1학년) 우수논문의 제목, 연구자, 초록 등이 포함된 csv 파일로 위 코드를 통해서나 현재 페이지의 [SampleData 폴더](https://github.com/Sujin-Github/Study2022/tree/main/SampleData)에서 다운받을 수 있습니다. 논문 작성자의 허락을 받은 파일로 용도(학습, 테스트) 외 사용을 금합니다.</i>


<br>

#### import 및 데이터 확인
```python
from hssh.DefClass import *

sampledf=pd.read_csv('SampleData.csv',sep=',',encoding='cp949')
```
```python
sampledf
```
`출력 (상단 3개만 표시)`   
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>과목</th>
      <th>제목</th>
      <th>연구자1</th>
      <th>연구자2</th>
      <th>초록</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>화학</td>
      <td>안토시아닌계 색소를 이용한 천연염색에서 염색성과 탄닌의 작용에 대한 탐구</td>
      <td>1604 이영채</td>
      <td>1701 유희진</td>
      <td>합성염료는 인체에 유해한 성분이 다수 포함되어 있으며 염색폐수에 의한 환경오염 문제...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>화학</td>
      <td>Luminol을 이용한 혈흔탐지법의 화학적 억제 방법 탐구</td>
      <td>1407 김세윤</td>
      <td>1417 탁한진</td>
      <td>본 연구에서는 첫째로 혈액의 공기 중 노출 시간과 혈액과 루미놀 시약 사이 발광 반...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>화학</td>
      <td>금속증착물에 따른 염료감응 태양전지 셀의</td>
      <td>1406 공성민</td>
      <td>1412 신준환</td>
      <td>본 연구는 화석 연료를 대체할 친환경 발전 공법 중 광감응 염료를 이용한 염료감응형...</td>
    </tr>
   </tbody>
  </table>
</div>
   
   
### Document
```python
sampledata=hssh.DefClass.Document(sampledf,'초록')
```
```python
sampledata
```
`출력` <hssh.DefClass.Document at 0x19b46920be0>

<br>

```python
sampledata.voca_dict
```
`출력 (일부만 표시)  `    
{'연구': 49, '수': 47, '것': 42,'때': 36,'결과': 26, ...

<br>

```python
sampledata.voca_list      
```
`출력 (일부만 표시)`   
['연구', '수', '것', '때', '결과', ...
      
<br>

```python
sampledata.idf_dict
```
`출력 (일부만 표시)`   
    {'연구': 0.0769610411361284,
     '수': 0.03774032798284711,
     '것': 0.3513978868378886,
     '때': 0.30010459245033816,
     '결과': 0.5232481437645479,
     '이용': 0.5232481437645479, ...
         
<br>
  
### Document 함수
```python
print(len(sampledata.voca_list),'\n')
sampledata.modify_voca()
print('\n\n',len(sampledata.voca_list))
```
`출력`   
969     
연구 것 결과 이 효율 효과 두 중 사용 경우 변화 때문 방법 정도 자 관계 탐구 지 분석 세 작 위 순 환경 물 의 등 내 차 한 점 가지 양 높이 포 대 적 다양 리 종 전 2 그 법 시 5 형 유 바 각 변 안 일 3 코 간 합 식 제 미 데 증 면    
906
     
 <br>
 
 ```python
sampledata.keywords()
```
`출력(일부만 표시)`   
    {'안토시아닌계 색소를 이용한 천연염색에서 염색성과 탄닌의 작용에 대한 탐구': [('염색', 30.761144082707073),
      ('적양배추', 20.82151748355507),
      ('견뢰도', 18.218827798110688),
      ('견뢰', 18.218827798110688),
      ('배', 13.49119162856183),
      ('블루베리', 10.986122886681098),
      ...
      ('시료', 2.1972245773362196),
      ('원인', 2.1972245773362196),
      ('제시', 2.1972245773362196)],
      ...
      
      <br>
      
```python
sampledata.keywords('연구자1',5)
```
`출력 (일부만 표시)`   
    {'1604 이영채': [('염색', 30.761144082707073),
      ('적양배추', 20.82151748355507),
      ('견뢰도', 18.218827798110688),
      ('견뢰', 18.218827798110688),
      ('배', 13.49119162856183),
      ('블루베리', 10.986122886681098)     
      ...
      ('시료', 2.1972245773362196),
      ('원인', 2.1972245773362196),
      ('제시', 2.1972245773362196)],
      ...
      
<br>

```python
sampledata.cos_sim()
```
`출력(일부만 표시)` <br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>제목</th>
      <th>안토시아닌계 색소를 이용한 천연염색에서 염색성과 탄닌의 작용에 대한 탐구</th>
      <th>Luminol을 이용한 혈흔탐지법의 화학적 억제 방법 탐구</th>
      <th>금속증착물에 따른 염료감응 태양전지 셀의</th>
      <th>Minkowski Distance로 정의된 휴리스틱 함수의 p값에 따른 서울 시내 도로망에서의 A* 알고리즘 성능 비교</th>
      <th>CNN을 통한 프레임 기반 동영상 부분 화질 향상 실현</th>
      <th>원 위를 구르는 뢸로 삼각형의 자취 그래프 분석</th>
      <th>필승 알고리즘이 존재하기 위한 최소 노드수의 실험적 증명</th>
      <th>KAN바코드의 오류 검출률 향상을 위한 weight와 modulo에 대한 탐구</th>
      <th>격자 그래프에서 두 사람이 만날 확률에 대한 연구</th>
      <th>다각형의 변에 접하여 구르는 원이 나타내는 성질에 대한 연구</th>
      <th>...</th>
      <th>무선충전 도로의 코일모양과 입력에 따른 충전량 비교</th>
      <th>단풍나무 씨앗의 특성을 이용한 느린 낙하장치에 대한 탐구</th>
      <th>천연염료와 매염제에 따른 염료 감응형 태양전지의 효율성</th>
      <th>온도에 따른 용수철의 히스테리시스 손실에 대한 연구</th>
      <th>진동에 따른 알갱이 입자의 유체성 탐구</th>
      <th>바람이 부는 환경에서 나선형 화살깃의 휘어진 각도가 화살의 비행에 미치는 영향</th>
      <th>북극의 빙하군 특정</th>
      <th>태양굴뚝의 원리를 활용한 친환경 건축물에서의 환기 및 냉방 효과 연구</th>
      <th>함수량 및 월별 강수량이 포항 지역 액상화에 미치는 영향 탐구</th>
      <th>여러 변인에 대한 진동수주형 파력발전의 효율 분석</th>
    </tr>
    <tr>
      <th>제목</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>안토시아닌계 색소를 이용한 천연염색에서 염색성과 탄닌의 작용에 대한 탐구</th>
      <td>NaN</td>
      <td>0.006785</td>
      <td>0.060295</td>
      <td>0.012280</td>
      <td>0.008513</td>
      <td>0.006366</td>
      <td>0.000680</td>
      <td>0.008157</td>
      <td>0.000140</td>
      <td>0.007621</td>
      <td>...</td>
      <td>0.019908</td>
      <td>0.012359</td>
      <td>0.236983</td>
      <td>0.010303</td>
      <td>0.012621</td>
      <td>0.005223</td>
      <td>0.008494</td>
      <td>0.002529</td>
      <td>0.005486</td>
      <td>0.012529</td>
    </tr>
    <tr>
      <th>Luminol을 이용한 혈흔탐지법의 화학적 억제 방법 탐구</th>
      <td>0.006785</td>
      <td>NaN</td>
      <td>0.006011</td>
      <td>0.004026</td>
      <td>0.009829</td>
      <td>0.013649</td>
      <td>0.000933</td>
      <td>0.000607</td>
      <td>0.000196</td>
      <td>0.019698</td>
      <td>...</td>
      <td>0.010306</td>
      <td>0.013251</td>
      <td>0.002627</td>
      <td>0.008205</td>
      <td>0.017748</td>
      <td>0.004772</td>
      <td>0.003015</td>
      <td>0.032259</td>
      <td>0.007604</td>
      <td>0.004399</td>
    </tr>
  </tbody>
</table>
<p>27 rows × 27 columns</p>
</div>

<br>

### Paper

```python
paper1=Paper(sampledata.df.iloc[0],sampledata)
paper2=Paper(sampledata.df.iloc[1],sampledata)
```
```python
paper1.txt
```
`출력`    
'합성염료는 인체에 유해한 성분이 다수 포함되어 있으며 염색폐수에 의한 환경오염 문제가 대두되고 있다. 이에 따라 천연염색의 중요성이 대두되고 있는 한편 그에 대한 연구는 활발히 진행되고 있지 않다. 따라서 본 연구에서는 안토시아닌계 색소를 이용한 천연 염색의 염색성과 이에 따른 최적 방안에 대해 탐구했다. 블루베리, 적양배추, 포도를 이용하여 견직물을 염색하였으며 염색 전후 흡광도 차이, 세탁 견뢰도, 물 견뢰도, 픽셀 견뢰도를 측정하여 최적의 염색 조건에 대해 알아보았다. 그 과정에서 새로운 분석 방법을 적용함으로써 방법론적인 내용을 중점적으로 탐구하였다. 두 번째로 블루베리와 포도 속 탄닌의 매염제로써의 작용에 대해 알아보기 위해 염액을 여러 비율로 혼합하여 염색하였다. 탐구 결과, 단일 염색의 경우 포도, 블루베리, 적양배추 순으로 염색 전후 흡광도 차가 크게 나타났고 이는 이 순서대로 염색이 많이 되었음을 의미한다. 그리고 적양배추에 다른 색소들을 섞어 측정한 결과 적양배추 단일 염액을 이용해 염색했을 때보다 염색이 많이 되었다. 그리고 세탁 견뢰도는 단일 용액은 블루베리, 적양배추, 포도 순으로 높은 것을 확인할 수 있었다. 물 견뢰도의 경우 측정 결과 적양배추의 비율이 높을수록 물 견뢰도가 높게 나온다는 것을 알 수 있고 픽셀 견뢰도 측정 결과 R,B의 값이 높았는데 이는 안토시아닌의 영향으로 해석된다. 적양배추를 섞은 혼합 용액의 경우 특정 비율 (1:4)에서 G가 우세하게 나타났다. 이러한 결과를 종합한 결과 안토시아닌계 색소를 활용한 최적의 염색 방법은 블루베리와 적양배추를 1:4 비율로 섞은 용액이라 할 수 있다.'

<br>

### Paper 함수

```python
paper1.keywords_f()
```
`출력 (일부만 표시)`   
[('염색', 30.761144082707073),
 ('적양배추', 20.82151748355507),
 ('견뢰도', 18.218827798110688),
 ('견뢰', 18.218827798110688),
 ('배', 13.49119162856183),
 ('블루베리', 10.986122886681098),
 ('포도', 10.410758741777535),<br>...<br>
 ('중요', 2.1972245773362196),
     ('폐수', 2.1972245773362196),
     ('측정한', 2.1972245773362196),
     ('매염제', 2.1972245773362196)]
 
 <br>
 
 ```python
paper1.keywords_f(5)
```
`출력 (일부만 표시)`      
[('염색', 30.761144082707073),
     ('적양배추', 20.82151748355507),
     ('견뢰도', 18.218827798110688),
     ('견뢰', 18.218827798110688),
     ('배', 13.49119162856183),
     ('블루베리', 10.986122886681098),
     ('포도', 10.410758741777535),<br>...<br>
     ('견뢰도,', 5.2053793708887675),
     ('픽셀', 5.2053793708887675),
     ('염액', 5.2053793708887675),
     ('혼합', 5.2053793708887675)]
