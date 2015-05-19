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
def main(lgg,fnames,jaccard_Index):
    import fileinput
    from glob import glob

    from pandas import Series, DataFrame
    import pandas as pd

    import numpy as np
    import matplotlib.pyplot as plt

    f1,f2 = "",""
    switch = -1
    cnt = 1

    fileIndex = []
    fnameIndex = []

    # 파일 불러와 인덱스번호에 할당
    for line in fileinput.input(fnames):
        if fileinput.isfirstline():
            switch += 1
            fnameIndex.append(fileinput.filename()[37:])

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

    f_len = len(fileIndex)            
    pivot = 0
    plaFile = ""
    #가공된 파일
    workedFile = []
    #교집합리스트
    isList = []
    #표절한 파일
    psmIndex = []
    psmIndex22 = []
    # 전체 표절률
    totalPlsm = [] 
    for x in range(0, f_len):
        workedFile.append("")
        isList.append("")
        psmIndex.append("")
        totalPlsm.append("") 
    # 전체 파일 비교
    for x in range(pivot, f_len-1): 
        for y in range(x+1, f_len):
            #더큰 자카르트인덱스를 할당하기위한 스위치
            newxFile = 0
            newyFile = 0 
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
            str1 = emptyRemove(str1)
            str2 = emptyRemove(str2)
            
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

            #모든 파일 비교해서 가장 큰 표절률 할당
            if totalPlsm[x] == "" or totalPlsm[x] < round(j_Index*100,2):
                newxFile = 1
                totalPlsm[x] = round(j_Index*100,2)
            if totalPlsm[y] == "" or totalPlsm[y] < round(j_Index*100,2):
                newyFile = 1
                totalPlsm[y] = round(j_Index*100,2)
            #자카르트 인덱스이상의 파일을 할당
            if j_Index >= jaccard_Index and newxFile == 1:
                newxFile = 0 #스위치
                psmIndex[x] = fnameIndex[x] #표절한파일할당
                isList[x] = list(set_Is) #교집합리스트할당
                workedFile[x] = insertList(str1) #가공된 파일할당
            if j_Index >= jaccard_Index and newyFile == 1:
                newyFile = 0 #스위치
                psmIndex[y] = fnameIndex[y] #표절한파일할당
                isList[y] = list(set_Is) #교집합리스트할당
                workedFile[y] = insertList(str2) #가공된 파일할당
    
    # 표절한 파일이 담긴 리스트에 공백 제거            
    for x in range(0,f_len):
        if psmIndex[x] != "":
            psmIndex22.append(psmIndex[x])
    # ui로 보낼 표절한파일 스트링        
    for x in range(0,len(psmIndex22)):
        plaFile += psmIndex22[x]
        if (x + 1) % 8 == 0:
            plaFile += "\n"
        else:
            plaFile += "  "
     
    return plaFile, totalPlsm, fnameIndex, f_len, workedFile, psmIndex, isList












# Plagiarism Checker
## F - Killer

