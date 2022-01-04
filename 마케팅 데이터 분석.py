#!/usr/bin/env python
# coding: utf-8

# # <center>올인원 패키지 : 머신러닝과 데이터분석 A-Z</center>

# ### # Domain Knowledge 2 : 광고성과지표
# | 광고성과지표 | = | 계산식 |
# |:---------- |---------- |:---------- |
# |CTR(Click Through Rate)|=|클릭수 / 노출수 * 100|
# |CPM(Cost Per Mile)|=|광고비용 / 노출수 * 1000|
# |CPC(Cost Per Click)|=|광고비용 / 클릭수|
# |CPA(Cost Per Action)|=|광고비용 / 구매수|

# In[3]:


imp=10000 #노출수
clk=100  #클릭수
conv=10  #구매수
cost=100000 #광고비용


# In[4]:


# ctr
ctr = clk/imp *100


# In[5]:


#ctr 출력
ctr


# In[6]:


# cpm
cpm = cost/imp *1000


# In[7]:


#cpm 출력
cpm


# In[8]:


# cpc
cpc = cost/clk


# In[9]:


#cpc 출력
cpc


# In[10]:


# cpa 
cpa = cost/conv


# In[11]:


#cpa 출력
cpa


# # Matplotlib 
# ###    - 시각화 라이브러리

# ### # 데이터 분석과정과 시각화

# - 머신러닝의 과정
#  1. 데이터 수집
#  2. 데이터 전처리 
#  3. 데이터 탐색 ★
#  4. 모델 선택
#  5. 모델 평가 및 적용

# ### # 시각화의 필요성
# 1. 대량의 데이터 파악 가능
# 2. 데이터의 패턴 파악 가능

# In[12]:


import matplotlib.pyplot as plt


# In[13]:


import pandas as pd
from pandas import DataFrame
from pandas import Series


# In[14]:


# matplotlib 한글 폰트 출력코드
# 출처 : 데이터공방( https://kiddwannabe.blog.me)

import matplotlib
from matplotlib import font_manager, rc
import platform

try : 
    if platform.system() == 'Windows':
    # 윈도우인 경우
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else:    
    # Mac 인 경우
        rc('font', family='AppleGothic')
except : 
    pass
matplotlib.rcParams['axes.unicode_minus'] = False   


# In[15]:


import pandas as pd
from pandas import DataFrame
from pandas import Series


# In[17]:


df=pd.read_excel("C:/Users/USER/Desktop/패스트캠퍼스-project/01. 광고 데이터를 활용한 데이터 분석 Project/Data/네이버보고서.xls",skiprows=[0])


# In[18]:


df


# In[19]:


((((df['노출수'].sort_values())/1000).reset_index()).drop('index',axis=1)).plot(figsize=[13,5])
plt.yticks([0,2000,4000,6000,8000,10000],[0,'2,000,000','4,000,000','6,000,000','8,000,000','10,000,000'])
plt.title('노출수 plot',fontsize=20)
plt.show() 
# 노출수에 대한 전반적인 것을 시각화하여 볼 수 있음


# <br><br><br>
# ![matplotlib.JPG](attachment:matplotlib.JPG)
# <br>
# - 시각화 라이브러리 matplotlib
# - matplotlib은 pandas의 데이터프레임, 시리즈 자료구조와 함께 사용 가능 
# - 따라서 데이터 처리와 동시에 시각화도 함께 진행할 수 있음
# - 아나콘다(anaconda)를 설치했다면 별도의 설치과정이 필요 없음

# In[20]:


# matplotlib import
import matplotlib.pyplot as plt


# In[21]:


# pandas, DataFrame, Series import
import pandas as pd
from pandas import DataFrame
from pandas import Series


# In[22]:


# matplotlib 한글 폰트 출력코드
# 출처 : 데이터공방( https://kiddwannabe.blog.me)

import matplotlib
from matplotlib import font_manager, rc
import platform

try : 
    if platform.system() == 'Windows':
    # 윈도우인 경우
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else:    
    # Mac 인 경우
        rc('font', family='AppleGothic')
except : 
    pass
matplotlib.rcParams['axes.unicode_minus'] = False   


# ### # 데이터프레임 시각화

# In[23]:


#데이터프레임 변수 생성
dict_data={"철수":[1,2,3,4],"영희":[2,3,4,5],"민수":[3,4,5,6],"수진":[4,5,6,7]}
df=DataFrame(dict_data)


# In[24]:


df


# ### # 차트 그리기

# In[25]:


# 선그래프 
df.plot()
plt.show()


# In[26]:


# 막대그래프
df.plot.bar()
plt.show()


# In[27]:


# 가로막대그래프
df.plot.barh()
plt.show()


# In[28]:


# 히스토그램
df.plot.hist()
plt.show()


# In[29]:


# 히스토그램 구간설정
df.plot.hist(bins = range(1,9,1)) #1부터 8까지 만들어 진다


# ### # 차트에 옵션 추가하기

# In[30]:


# 기본 막대그래프
df.plot.bar()
plt.show()


# In[31]:


# 그래프 크기 설정
df.plot.bar(figsize=[10,6])
plt.show()


# In[32]:


# 제목설정
df.plot.bar(figsize=[10,6])
plt.title('예제')
plt.show()


# In[33]:


# 제목 폰트 크기 설정
df.plot.bar(figsize=[10,6])
plt.title('예제',fontsize =18)
plt.show()


# In[34]:


# x축 이름 설정
df.plot.bar(figsize=[10,6])
plt.title('예제',fontsize =18)
plt.xlabel('xlabel')
plt.show()


# In[35]:


# x축 이름 및 폰트크기 설정
df.plot.bar(figsize=[10,6])
plt.title('예제',fontsize =18)
plt.xlabel('xlabel',fontsize =16)
plt.show()


# In[36]:


# y축 이름 및 폰트 크기 설정 
df.plot.bar(figsize=[10,6])
plt.title('예제',fontsize =18)
plt.xlabel('xlabel',fontsize =16)
plt.ylabel('ylabel',fontsize =16)
plt.show()


# In[37]:


# x축 눈금설정
# 설정할 눈금의 위치, 눈금의 이름, 폰트사이즈, 각도
df.plot.bar(figsize=[10,6])
plt.title('예제',fontsize =18)
plt.xlabel('xlabel',fontsize =16)
plt.ylabel('ylabel',fontsize =16)
plt.xticks([0, 1, 2],['첫째','둘째','셋째'], fontsize =10,rotation=0) #rotation 각도
plt.show()


# In[38]:


# y축 눈금설정
df.plot.bar(figsize=[10,6])
plt.title('예제',fontsize =18)
plt.xlabel('xlabel',fontsize =16)
plt.ylabel('ylabel',fontsize =16)
plt.xticks([0, 1, 2],['첫째','둘째','셋째'], fontsize =10,rotation=0) #rotation 각도
plt.yticks([1, 3, 5, 7],['첫째','셋째','다섯째','일곱번째'])
plt.show()


# In[39]:


# x축 범위설정
df.plot.bar(figsize=[10,6])
plt.title('예제',fontsize =18)
plt.xlabel('xlabel',fontsize =16)
plt.ylabel('ylabel',fontsize =16)
plt.xticks([0, 1, 2],['첫째','둘째','셋째'], fontsize =10,rotation=0) #rotation 각도
plt.yticks([1, 3, 5, 7],['첫째','셋째','다섯째','일곱번째'])
plt.xlim([-1,4])
plt.show()


# In[40]:


# y축 범위설정
df.plot.bar(figsize=[10,6])
plt.title('예제',fontsize =18)
plt.xlabel('xlabel',fontsize =16)
plt.ylabel('ylabel',fontsize =16)
plt.xticks([0, 1, 2],['첫째','둘째','셋째'], fontsize =10,rotation=0) #rotation 각도
plt.yticks([1, 3, 5, 7],['첫째','셋째','다섯째','일곱번째'])
plt.xlim([-1,4])
plt.ylim([-1,8])
plt.show()


# ### # 시리즈 시각화

# In[41]:


# 데이터프레임 열 = 시리즈
df['철수']


# In[42]:


# 선그래프
df['철수'].plot()
plt.show()


# In[43]:


# 막대그래프
df['철수'].plot.bar()
plt.show()


# In[44]:


# 가로막대그래프
df['철수'].plot.barh()
plt.show()


# In[45]:


# 히스토그램(구간설정)
df['철수'].plot.hist(bins = range(1, 6, 1))
plt.show()


# ### # 차트에 옵션 추가하기

# In[46]:


df['철수'].plot.bar()
plt.show()


# In[47]:


df['철수'].plot.bar()
df['철수'].plot.bar(figsize=[10,6])
plt.xlabel('xlabel',fontsize =16)
plt.ylabel('ylabel',fontsize =16)
plt.xticks([0, 1, 2],['첫째','둘째','셋째'], fontsize =10,rotation=0) #rotation 각도
plt.yticks([1, 3, 5, 7],['첫째','셋째','다섯째','일곱번째'])
plt.xlim([-1,4])
plt.ylim([-1,8])
plt.show()

