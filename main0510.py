#####################################################################
#
#  1. 스페이스,엔터,탭제거하기                        <2015.01.27>
#  2. simpleset, ngram 모듈 저장                      <2015.01.29>
#  3. 리스트에 서브스트링 할당                        <2015.01.30>
#  4. 합집합과 교칩합 구함                            <2015.02.01>
#  5. 자른 스트링 정수변환 후 리스트저장              <2015.02.03>
#  6. 문자열을 저장한 리스트를 set으로 변환           <2015.02.05>
#  7. 주석 제거                                       <2015.02.11>
#  8. 주석 제거(수정)                                 <2015.02.15>
#  9. 변수명 통일                                     <2015.02.16>
#  10. 함수명 통일                                    <2015.02.23>
#  11. 여러개의 파일 불러오기                         <2015.02.26>
#  12. 포인터, 배열 변수 통일                         <2015.02.27>
#  13. 각 언어마다 파일 불러오게 구현                 <2015.03.03>
#####################################################################
# 막대형 그래프 출력
def graphPrint():
    fig = plt.subplots(1,1)
    data = Series(jc,index = psmIndex)
    data.plot(kind='bar')
# 불러온 파일을 하나의 스트링으로 변환
def convertString(ofile,lg):
    st = "\n"
    for x in ofile:
        st += x
    # 기존의 있었던 특수문자 제거
    st = st.replace("$","")
    st = st.replace("@","")    
    # 주석을 특수 문자로 변환
    if lg == ("4"):
        #파이썬 일때만 다르게 변환
        st = st.replace("'''","^")
        st = st.replace('"""','^')
    else:    
        st = st.replace("//","@")
        st = st.replace("/*","$")
        st = st.replace("*/","$")    
    return st
# 주석 제거(행단위, 블록단위), (모든언어 사용 가능)
def commmentRemove(st,first,last):
    tempSt = ""
    l = len(st)
    front = l
    rear = l
    switch = 0
    for x in range(0,l):
        if st[x] == first and switch == 0:
            front = x
            rear = x+1
            while st[rear] != last:
                rear += 1
                if rear == l-1:
                    break
        if front <= x and x <= rear:           
            tempSt += ""
            if x == rear:
                tempSt += "\n"
                switch = 0
            else:    
                switch = 1    
        else:
            tempSt += st[x]
            switch = 0                 
    return tempSt
#스페이스,엔터,탭 제거 ,(모든언어 사용가능)
def emptyRemove(st):
    st = st.replace(" ","")
    st = st.replace("\t","")
    st = st.replace("\n","")
    st = st.replace(";","")
    st = st.replace(",","")
    #st = st.replace("(","")
    #st = st.replace(")","")
    #st = st.replace("{","")
    #st = st.replace("}","")
    return st
#문자열 끊어 리스트에 삽입(0번 ~ k-4번), (모든언어 사용가능)
def insertList(st):
    strList = []
    l = len(st)
    pivot = 0
    for x in range(5, l+1):
        temp = ""
        for i in range(pivot, x):
            temp += st[i]
        strList.append(temp)
        pivot += 1
 #문자열 끊어 리스트에 삽입(k-3번 ~ k번)   
    for pivot in range(l-4, l):
        temp = ""
        rear = 0
        n = 0
        for x in range(pivot, l): 
            temp += st[x]
            n += 1
        for y in range(n, 5):
            temp += st[rear]
            rear += 1
        strList.append(temp)    
    return strList         
###################### main ###########################################
import fileinput
from glob import glob

from pandas import Series, DataFrame
import pandas as pd

# 검사할 언어 선택
print("1. C")
print("2. C++")
print("3. JAVA")
print("4. PYTHON")
lgg = input("검사할 언어의 번호를 입력하시오 : ")

# 여러개의 파일 불러오기
try:
    if lgg == ("1"):
        fnames = glob('C:/Python34/gproject/Problem/c_test/20*.c')    
    elif lgg == ("2"):
        fnames = glob('C:/Python34/gproject/Problem/task/20*.cpp')
    elif lgg == ("3"):
        fnames = glob('C:/Python34/gproject/Problem/cmpjava/20*.java')
    elif lgg == ("4"):
        fnames = glob('C:/Python34/gproject/Problem/py_test/20*.py')
    else:
        print("1에서 4까지의 번호를 입력하시오!")            
except ValueError:
    print("It looks like you input a value that wasn't a number!")

f1,f2 = "",""
switch = -1
cnt = 1

fileIndex = []
fnameIndex = []
jc = []

# 파일 불러와 인덱스번호에 할당
for line in fileinput.input(fnames):
    if fileinput.isfirstline():
        switch += 1
        fnameIndex.append(fileinput.filename()[34:])

    if switch % 2 == 0:
        if cnt % 2 == 0:
            fileIndex.append(f2)
            f2 = ""
            cnt += 1
        f1 += line
    elif switch % 2 == 1:
        if cnt % 2 == 1:
            fileIndex.append(f1)
            f1 = ""
            cnt += 1
        f2 += line

if cnt % 2 == 0:
    fileIndex.append(f2)
else:
    fileIndex.append(f1)

i_len = len(fileIndex)            
psmIndex = []
pivot = 0

# 전체 표절률
totalPlsm = [] 
for x in range(0, i_len):
    totalPlsm.append("") 
# 전체 파일 비교
for x in range(pivot, i_len-1): 
    for y in range(x+1, i_len):

        #불러온 파일 스트링화
        str1 = convertString(fileIndex[x],lgg)
        str2 = convertString(fileIndex[y],lgg)

        #주석문 제거
        if lgg == ("4"):
            #파이썬일 경우
                # #주석문 제거(행단위)
            str1 = commmentRemove(str1,'#','\n')
            str2 = commmentRemove(str2,'#','\n')
            
                # """주석문 제거(블록단위)
            str1 = commmentRemove(str1,'^','^')    
            str2 = commmentRemove(str2,'^','^')
        else:    
                # //주석문 제거(행단위)
            str1 = commmentRemove(str1,'@','\n')
            str2 = commmentRemove(str2,'@','\n')
            
                # /*~*/주석문 제거(블록단위)
            str1 = commmentRemove(str1,'$','$')    
            str2 = commmentRemove(str2,'$','$')
            
        # 각 언어의 맞는 모듈 불러오기
        if lgg == ("1"):
            import c_modules0428 as c
            #구조체명 통일
            str1 = c.str_Union(str1)
            str2 = c.str_Union(str2)
            #함수명 통일
            str1 = c.func_Union(str1)
            str2 = c.func_Union(str2)
            #변수명 통일
            str1 = c.vble_Union(str1)
            str2 = c.vble_Union(str2)
            #define명 통일
            str1 = c.def_Union(str1)
            str2 = c.def_Union(str2)
        elif lgg == ("2"):
            import cpp_modules0428 as cpp
            #템플릿명 통일
            str1 = cpp.tplate_Union(str1)
            str2 = cpp.tplate_Union(str2)
            #클래스명 통일
            str1 = cpp.class_Union(str1)
            str2 = cpp.class_Union(str2)
            #함수명 통일
            str1 = cpp.func_Union(str1)
            str2 = cpp.func_Union(str2)
            #변수명 통일
            str1 = cpp.vble_Union(str1)
            str2 = cpp.vble_Union(str2)
            #define명 통일
            str1 = cpp.def_Union(str1)
            str2 = cpp.def_Union(str2)
        elif lgg == ("3"):
            import java_modules0429 as java
            #클래스명 통일
            str1 = java.class_Union(str1)
            str2 = java.class_Union(str2)
            #함수명 통일
            str1 = java.func_Union(str1)
            str2 = java.func_Union(str2)
            #변수명 통일
            str1 = java.vble_Union(str1)
            str2 = java.vble_Union(str2)
        elif lgg == ("4"):
            import py_modules0408 as py
            #함수명 통일
            str1 = py.func_Union(str1)
            str2 = py.func_Union(str2)
            #변수명 통일
            str1 = py.vble_Union(str1)
            str1 = py.vble_Union(str1)
            str2 = py.vble_Union(str2)
            str2 = py.vble_Union(str2)            
            
        #스페이스,개행,탭 제거
        #str1 = emptyRemove(str1)
        #str2 = emptyRemove(str2)
        
        #출력파일 저장
        f1 = open('C:/python34/gproject/result/test1.txt','w')
        f1.write(str1)
        f1.close

        f2 = open('C:/python34/gproject/result/test2.txt','w')
        f2.write(str2)
        f2.close
        
        #리스트를 set으로 변환 후 할당
        set1 = set(insertList(str1))
        set2 = set(insertList(str2)) 
        #교집합과 합집합 
        set_Is = set1 & set2
        set_Un = set1 | set2
        #교집합과 합집합 갯수
        cnt_Is = len(set_Is)
        cnt_Un = len(set_Un)
        #자카르트 인덱스
        j_Index = cnt_Is / cnt_Un
        #print(j_Index, " (Jaccard index)")
        
        #교집합과 합집합 출력, 갯수 출력
        #print(set_Is)
        #print(set_Un)
        #print(cnt_Is)
        #print(cnt_Un)

        # K-Gram으로 잘라서 할당된 string
        #print(set1)
        #print(set2)
        
        #print(fnameIndex[x], fnameIndex[y], " (Compare files)")
        #print("\n")

        #모든 파일 비교해서 가장 큰 표절률 할당
        if totalPlsm[x] == "" or totalPlsm[x] < j_Index:
            totalPlsm[x] = j_Index
        if totalPlsm[y] == "" or totalPlsm[y] < j_Index:
            totalPlsm[y] = j_Index

        if j_Index >= 0.75:
            psmIndex.append(fnameIndex[x])
            psmIndex.append(fnameIndex[y])
            jc.append(j_Index)
            jc.append(j_Index)
print("\n")
print("표절이 의심되는 파일들 : ")
print(set(psmIndex))
print("\n")
print("        총 : ",i_len,"개의 파일들에 대한 표절률")
fig = plt.subplots(1,1)
data = Series(totalPlsm,index = fnameIndex)
data.plot(kind='bar')


















# Plagiarism Checker
## F - Killer

