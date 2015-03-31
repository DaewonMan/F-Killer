###############################################################################
#              
#                                 C++ Mudule
#
#                                                              <2015.03.31>
###############################################################################

# 클래스를 하나의 문자로 통일
def class_Union(st):
    st = st.replace("class ","@")
    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempClass = ""
        if st[x] == "@":
            temp = x+1
            # 클래스 다음 빈칸 건너 뛰기
            while st[temp] == " " or st[temp] == "*": 
                temp += 1
            # 클래스명 추출
            while 1:
                if st[temp] == "\n":    
                    break
                elif st[temp] == ";":   
                    break              
                # 클래스명 한문자씩 저장                                    
                tempClass += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 클래스명 통일           
        if tempClass != "":                          
            t = tempClass + "::"            
            tempSt = tempSt.replace(t,"ㅋ::")
            t = tempClass + "."            
            tempSt = tempSt.replace(t,"ㅋ.")
            t = tempClass + ";"            
            tempSt = tempSt.replace(t,"ㅋ;")
            t = tempClass + "["            
            tempSt = tempSt.replace(t,"ㅋ[")
            t = tempClass + "\n"            
            tempSt = tempSt.replace(t,"ㅋ\n")
            t = tempClass + "("            
            tempSt = tempSt.replace(t,"ㅋ(")
            # 클래스의 객체 생성시
            t = tempClass + " "            
            tempSt = tempSt.replace(t,"ㅋ ")
            t = tempClass + "*"            
            tempSt = tempSt.replace(t,"ㅋ*")
    tempSt = tempSt.replace("@","")

    # 클래스 객체 하나의 문자로 통일
    st = tempSt
    l = len(st)
    for x in range(0,l):
        tempClass = ""
        if st[x] == "ㅋ":
            temp = x+1
            # 클래스명 다음 빈칸 건너 뛰기
            while st[temp] == " " or st[temp] == "*": 
                temp += 1
            # 클래스 객체 추출
            while 1:
                if st[temp] == ";":    
                    break
                elif st[temp] == "=":   
                    break
                elif st[temp] == "(":   
                    break     
                elif st[temp] == " ":
                    temp += 1   
                    continue
                # 객체가 아닐시 저장하고 있던 스트링 초기화    
                elif st[temp] == "\n":
                    tempClass = ""   
                    break
                elif st[temp] == ":":
                    tempClass = ""   
                    break                          
                # 클래스 객체 한문자씩 저장                                    
                tempClass += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 클래스 객체명 통일           
        if tempClass != "":
            t = tempClass + ";"            
            tempSt = tempSt.replace(t,"ㅋ;")                                  
            t = "]" + tempClass            
            tempSt = tempSt.replace(t,"]ㅋ")
            t = tempClass + "="            
            tempSt = tempSt.replace(t,"ㅋ=")
            t = tempClass + " "            
            tempSt = tempSt.replace(t,"ㅋ ")
            t = tempClass + "("            
            tempSt = tempSt.replace(t,"ㅋ(")
            t = tempClass + "."            
            tempSt = tempSt.replace(t,"ㅋ.")

    return tempSt


# 함수를 하나의 문자로 통일
def func_Union(st):
    st = st.replace("char ","ㅅ")
    st = st.replace("short ","ㅅ")
    st = st.replace("int ","ㅅ")
    st = st.replace("long ","ㅅ")
    st = st.replace("long long ","ㅅ")
    st = st.replace("flaot ","ㅅ")
    st = st.replace("double ","ㅅ")
    st = st.replace("long double ","ㅅ")
    st = st.replace("void ","ㅅ")
    st = st.replace("string ","ㅅ")

    # 식별자 다음 포인터 온 경우
    st = st.replace("char*","ㅅ*")
    st = st.replace("short*","ㅅ*")
    st = st.replace("int*","ㅅ*")
    st = st.replace("long*","ㅅ*")
    st = st.replace("long long*","ㅅ*")
    st = st.replace("flaot*","ㅅ*")
    st = st.replace("double*","ㅅ*")
    st = st.replace("long double*","ㅅ*")

    st = st.replace("#include","")
    st = st.replace("return ","")
    st = st.replace("void","")
    # ㅋ:: 인경우 함수를 찾아내는데 혼동 막기위해
    st = st.replace("ㅋ::","::")

    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempFunc = ""
        if st[x] == "ㅅ":
            temp = x+1
            # 식별자 다음 빈칸 및 포인터일때 건너 뛰기
            while st[temp] == " " or st[temp] == "*": 
                temp += 1
            # 함수명 추출
            while 1:
                if st[temp] == "(":    
                    break    
                elif st[temp] == ";":
                    tempFunc = ""
                    break    
                elif st[temp] == "\n":
                    tempFunc = ""
                    break
                elif st[temp] == "ㅎ":
                    temp += 1
                    continue
                elif st[temp] == ":":
                    temp += 1
                    continue            
                # 함수를 한문자씩 저장                                    
                tempFunc += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 함수명 통일           
        if tempFunc != "":                          
            t = tempFunc + "("            
            tempSt = tempSt.replace(t,"ㅎ(")
                    
            t = ")" + tempFunc            
            tempSt = tempSt.replace(t,")ㅎ")

            t = " " + tempFunc            
            tempSt = tempSt.replace(t," ㅎ")
            t = tempFunc + " "            
            tempSt = tempSt.replace(t,"ㅎ ")

            t = "+" + tempFunc            
            tempSt = tempSt.replace(t,"+ㅎ")
            t = "-" + tempFunc            
            tempSt = tempSt.replace(t,"-ㅎ")
            t = "/" + tempFunc            
            tempSt = tempSt.replace(t,"/ㅎ")
            t = "*" + tempFunc            
            tempSt = tempSt.replace(t,"*ㅎ")
            t = "=" + tempFunc            
            tempSt = tempSt.replace(t,"=ㅎ")
            t = "%" + tempFunc            
            tempSt = tempSt.replace(t,"%ㅎ")
            t = "," + tempFunc            
            tempSt = tempSt.replace(t,",ㅎ")
            t = tempFunc + "ㅎ"            
            tempSt = tempSt.replace(t,"ㅎ")   # 미해결

            tempSt = tempSt.replace("ㅅㅎ","ㅎ")
            # 함수 포인터인 경우 
            tempSt = tempSt.replace("ㅅ* ㅎ","* ㅎ")
            tempSt = tempSt.replace("ㅅ *ㅎ"," *ㅎ")
            tempSt = tempSt.replace("ㅅ * ㅎ"," * ㅎ")

    # 함수 찾아내는데 방해요소 원상태로        
    tempSt = tempSt.replace("::","ㅋ::")        
    return tempSt

# 변수를 하나의 문자로 통일  
def vble_Union(st):
    l = len(st)
    tempSt = st
    switch = 0
    for x in range(0,l):
        tempVb = ""
        # 변수명 추출
        if st[x] == "ㅅ":
            temp = x+1
            # 식별자 다음 빈칸 및 포인터일때 건너 뛰기
            while st[temp] == " " or st[temp] == "*": 
                temp += 1
            #변수를 할당하는 과정        
            while 1:
                if st[temp] == ";":
                    switch = 0
                    break
                elif st[temp] == "\n": # int gjlk, fglk, fgldj ........,gjkjflkgjkl; 개행을 넘어버리는 경우 어쩔 ? 
                    switch = 0
                    break
                # 배열의 []를 건너 뛰기    
                elif st[temp] == "[":
                    while st[temp] != "]":
                        temp += 1
                    temp += 1
                    switch = 0
                    continue        
                elif st[temp] == " ":
                    temp += 1
                    continue
                elif st[temp] == "ㅂ":
                    temp += 1
                    continue 
                elif st[temp] == "=":
                    break
                elif st[temp] == ",":
                    break    
                elif st[temp] == ")":   # 함수의 인자값으로 괄호안에서 변수 선언시
                    break
                # 함수앞 식별자 있을때 건너 뛰기    
                elif st[temp] == "(":
                    tempVb = ""
                    break
                    
                    
                tempVb += st[temp] 
                temp += 1
                switch = 1
                if temp == l-1:
                    break
        # 식별자 다음 변수 다음 "," 나올시             
        elif switch == 1 and st[x] == ",":
            temp = x+1
            while 1:
                if st[temp] == ";":
                    switch = 0
                    break
                elif st[temp] == "\n":
                    switch = 0
                    break    
                elif st[temp] == " ":
                    temp += 1
                    continue
                elif st[temp] == "ㅂ":
                    temp += 1
                    continue    
                elif st[temp] == "=":
                    break
                elif st[temp] == ",":
                    break    
                elif st[temp] == ")":    # 함수의 인자값으로 괄호안에서 변수선언시
                    break
                # 변수를 한문자씩 저장                        
                tempVb += st[temp] 
                temp += 1
                switch = 1
                if temp == l-1:
                    break
        elif st[x] == "\n":
            switch = 0            
                           
        # 변수명 통일           
        if tempVb != "":                          
            t = tempVb + ";"         
            tempSt = tempSt.replace(t,"ㅂ;")
            
            t = tempVb + " " 
            tempSt = tempSt.replace(t,"ㅂ ")

            t = tempVb + "="
            tempSt = tempSt.replace(t,"ㅂ=")
            t = "=" + tempVb 
            tempSt = tempSt.replace(t,"=ㅂ")

            t = tempVb + "&" 
            tempSt = tempSt.replace(t,"ㅂ&")
            t = "&" + tempVb
            tempSt = tempSt.replace(t,"&ㅂ")

            t = tempVb + "|" 
            tempSt = tempSt.replace(t,"ㅂ|")
            t = "|" + tempVb
            tempSt = tempSt.replace(t,"|ㅂ")

            t = tempVb + ">" 
            tempSt = tempSt.replace(t,"ㅂ>")
            t = ">" + tempVb
            tempSt = tempSt.replace(t,">ㅂ")

            t = tempVb + "<" 
            tempSt = tempSt.replace(t,"ㅂ<")
            t = "<" + tempVb
            tempSt = tempSt.replace(t,"<ㅂ")

            t = tempVb + "+" 
            tempSt = tempSt.replace(t,"ㅂ+")
            t = "+" + tempVb
            tempSt = tempSt.replace(t,"+ㅂ")

            t = tempVb + "-" 
            tempSt = tempSt.replace(t,"ㅂ-")
            t = "-" + tempVb
            tempSt = tempSt.replace(t,"-ㅂ")

            t = tempVb + "/" 
            tempSt = tempSt.replace(t,"ㅂ/")
            t = "/" + tempVb
            tempSt = tempSt.replace(t,"/ㅂ")

            t = tempVb + "*" 
            tempSt = tempSt.replace(t,"ㅂ*")
            t = "*" + tempVb
            tempSt = tempSt.replace(t,"*ㅂ")

            t = tempVb + "%" 
            tempSt = tempSt.replace(t,"ㅂ%")
            #t = "%" + tempVb
            #tempSt = tempSt.replace(t,"%ㅂ")

            t = tempVb + ","            
            tempSt = tempSt.replace(t,"ㅂ,")
            t = "," + tempVb            
            tempSt = tempSt.replace(t,",ㅂ")

            # 변수 다음 배열이 온 경우
            t = tempVb + "["            
            tempSt = tempSt.replace(t,"ㅂ[")
            """
            if switch == 1:
                t = tempVb + "("            
                tempSt = tempSt.replace(t,"ㅂ(")
            """        
            t = tempVb + ")"            
            tempSt = tempSt.replace(t,"ㅂ)")

            # 만약 변수안에 변수명이 포함된 경우
            t = tempVb + "ㅂ"            
            tempSt = tempSt.replace(t,"ㅂ")
            
    tempSt = tempSt.replace("ㅅ","")              
    return tempSt