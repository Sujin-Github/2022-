# 키워드 추출 및 유사도 분석을 위한 hssh 패키지
<i>한성과학고등학교 2022학년도 과제연구</i>

python 패키지 <b>hssh</b>는 pandas의 DataFrame형태로 입력된 문서군에서 키워드를 추출하고 코사인 유사도를 이용해 유사한 문서 찾을 수 있게 합니다.

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
#### 
