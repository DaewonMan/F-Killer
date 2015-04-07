###############################################################################
#              
#                                 C++ Mudule
#  
#  1. 함수,변수 통일화작업                                        <2015.03.31>
#  2. 클래스 통일화작업                                           <2015.04.01>
#  3. 템플릿 통일작업                                             <2015.04.02> 
###############################################################################

# 템플릿을 하나의 문자로 통일
def tplate_Union(st):
    st = st.replace("<class ","ㅌ")  #(예시) template <class T>
    st = st.replace("< class ","ㅌ") #(예시) template<class T>
    st = st.replace("<typename ","ㅌ")  #(예시) template <typedef T>
    st = st.replace("< typename ","ㅌ") #(예시) template<typedef T>
    st = st.replace(",class ",",")  #(예시) template <class T",class T>"
    st = st.replace(", class ",",") #(예시) template<class T", class T>"
    st = st.replace(",typename ",",")  #(예시) template <typedef T",typedef T>"
    st = st.replace(", typename ",",") #(예시) template<typedef T", typedef T>"
    l = len(st)
    tempSt = st
    catch = 0
    for x in range(0,l):
        temptpt = ""
        if st[x] == "ㅌ" or catch == x:
            temp = x+1
            while st[temp] == " ": 
                temp += 1
            # 클래스명 추출
            while 1:
                if st[temp] == " ":  
                    temp += 1    
                    continue 
                elif st[temp] == ">":  #(예시) T> 일때 T만 추출
                    break
                elif st[temp] == ",":   #(예시) <class T, class T> 콤마 전 T 추출
                    catch = temp  # 콤마의 인덱스 할당
                    break                  
                # 클래스명 한문자씩 저장                                    
                temptpt += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 템플릿명 통일           
        if temptpt != "": 
            #(예시) typename<T>
            t = "<" + temptpt + ">"            
            tempSt = tempSt.replace(t,"<템>")                         
            #(예시) "T "tname or "T &"" tname
            t = " " + temptpt + " "            
            tempSt = tempSt.replace(t," 템 ")
            t = "\t" + temptpt + " "            
            tempSt = tempSt.replace(t,"\t템 ")
            t = " " + temptpt + "&"            
            tempSt = tempSt.replace(t," 템&")
            t = "\t" + temptpt + "&"            
            tempSt = tempSt.replace(t,"\t템&")
            t = "\n" + temptpt + " "            
            tempSt = tempSt.replace(t,"\n템 ")
            #(예시) (T tname, T tname)
            t = "(" + temptpt + " "            
            tempSt = tempSt.replace(t,"(템 ")
            t = "," + temptpt + " "            
            tempSt = tempSt.replace(t,",템 ")
            t = "(" + temptpt + "&"            
            tempSt = tempSt.replace(t,"(템&")
            t = "," + temptpt + "&"            
            tempSt = tempSt.replace(t,",템&")
            #(예시) <class T, class T>
            t = "ㅌ" + temptpt + ">"            
            tempSt = tempSt.replace(t,"ㅌ템>")
            t = "ㅌ" + temptpt + ","            
            tempSt = tempSt.replace(t,"ㅌ템,")
            t = "," + temptpt + ">"            
            tempSt = tempSt.replace(t,",템>")
            #(예시) return T(-1);
            t = " " + temptpt + "("            
            tempSt = tempSt.replace(t," 템(")                   
    tempSt = tempSt.replace("ㅌ","<")        
    return tempSt

# 클래스를 하나의 문자로 통일
def class_Union(st):
    st = st.replace("class ","ㅋ")
    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempClass = ""
        if st[x] == "ㅋ":
            temp = x+1
            # 클래스 다음 빈칸 건너 뛰기
            while st[temp] == " " or st[temp] == "*": 
                temp += 1
            # 클래스명 추출
            while 1:
                if st[temp] == "\n": # class 클래스명    
                    break
                elif st[temp] == ";": #(예시) template <class T> class 클래스명;
                    break
                elif st[temp] == "<": #(예시) 클래스명"<"템>   
                    break
                elif st[temp] == " ": 
                    temp += 1   
                    continue                              
                # 클래스명 한문자씩 저장                                    
                tempClass += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 클래스명 통일           
        if tempClass != "":
            #(예시) class 클래스
            t = " " + tempClass + "\n"            
            tempSt = tempSt.replace(t," 클\n")  
            t = " " + tempClass + " "            
            tempSt = tempSt.replace(t," 클 ")
            t = "\t" + tempClass + " "            
            tempSt = tempSt.replace(t,"\t클 ")
            #(예시) class 클래스
            t = "ㅋ" + tempClass + " "            
            tempSt = tempSt.replace(t,"ㅋ클 ")
            t = "ㅋ" + tempClass + "\n"            
            tempSt = tempSt.replace(t,"ㅋ클\n") 
            #(예시) 클래스명::                          
            t = tempClass + "::"            
            tempSt = tempSt.replace(t,"클::")
            t = "::" + tempClass + "("            
            tempSt = tempSt.replace(t,"::클(")  #(예시) 클래스명<T>"::클래스명(")
            #
            t = tempClass + "."            
            tempSt = tempSt.replace(t,"클.") #(예시) 클래스명.클래스명()
            t = tempClass + ";"            
            tempSt = tempSt.replace(t,"클;")
            t = tempClass + "["            
            tempSt = tempSt.replace(t,"클[")
            t = tempClass + "\n"            
            tempSt = tempSt.replace(t,"클\n")
            t = tempClass + "("            
            tempSt = tempSt.replace(t,"클(")
            """
            t = tempClass + "*"            
            tempSt = tempSt.replace(t,"클*")
            """
            #(예시) 클래스명<T>
            t = tempClass + "<"            
            tempSt = tempSt.replace(t,"클<") #(예시) "class 클래스명<"T>
            t = tempClass + " <"            
            tempSt = tempSt.replace(t,"클 <") #(예시) "class 클래스명 <"T>
            t = "\t" + tempClass + "<"            
            tempSt = tempSt.replace(t,"\t클<") #(예시) "\t클래스명<"T>
            t = "\t" + tempClass + " <"            
            tempSt = tempSt.replace(t,"\t클 <") #(예시) "\t클래스명 <"T>
            t = "(" + tempClass + "<"            
            tempSt = tempSt.replace(t,"(클<") #(예시) "(클래스명<"T> * 템플릿객체, ........)
            t = "," + tempClass + "<"            
            tempSt = tempSt.replace(t,",클<") #(예시) (.......",클래스명<"T>..)
            
    tempSt = tempSt.replace("ㅋ","")
    
    # 클래스 객체 하나의 문자로 통일
    st = tempSt
    l = len(st)
    switch = 0
    for x in range(0,l):
        tempClass = ""
        if st[x] == "클" or switch == 1:
            temp = x+1
            # 클래스명 다음 빈칸 건너 뛰기
            while st[temp] == " " or st[temp] == "*": 
                temp += 1
            # 클래스 객체 추출
            while 1:
                if st[temp] == ";":
                    switch = 0
                    break
                elif st[temp] == "=":
                    switch = 0   
                    break
                elif st[temp] == "(":
                    switch = 0   
                    break
                elif st[temp] == ")":
                    switch = 0   
                    break     
                elif st[temp] == " ":
                    temp += 1   
                    continue
                # (예시) 클래스명 "<T> * " 클래스객체명    
                elif st[temp] == "<":
                    switch = 1
                    temp += 1   
                    continue
                elif st[temp] == ">":
                    switch = 0
                    temp += 1   
                    continue
                elif st[temp] == "*":
                    temp += 1   
                    continue            
                # 객체가 아닐시 저장하고 있던 스트링 초기화    
                elif st[temp] == "\n":
                    switch = 0
                    tempClass = ""   
                    break
                elif st[temp] == ":":
                    switch = 0
                    tempClass = ""   
                    break
                elif switch == 1: #(예제) 클래스명<int> 객체명; 중에 <int> 뛰어 넘기
                    temp += 1   
                    continue                              
                # 클래스 객체 한문자씩 저장                                    
                tempClass += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 클래스 객체명 통일           
        if tempClass != "":
            t = tempClass + ";"            
            tempSt = tempSt.replace(t,"객;")                                  
            t = "]" + tempClass            
            tempSt = tempSt.replace(t,"]객")
            t = tempClass + "-"            
            tempSt = tempSt.replace(t,"객-") #(예제) 객체->객체;
            t = tempClass + "="            
            tempSt = tempSt.replace(t,"객=")
            t = tempClass + " "            
            tempSt = tempSt.replace(t,"객 ")
            t = " " + tempClass            
            tempSt = tempSt.replace(t," 객")
            t = "(" + tempClass            
            tempSt = tempSt.replace(t,"(객") #(예제) if(객체!=0)
            t = " " + tempClass + "("            
            tempSt = tempSt.replace(t," 객(")
            t = "\t" + tempClass + "("            
            tempSt = tempSt.replace(t,"\t객(")    
            t = tempClass + "."            
            tempSt = tempSt.replace(t,"객.")
            #(예제) (클래스명<T> * 객체명)
            t = " " + tempClass + ")"            
            tempSt = tempSt.replace(t," 객)")
            t = "*" + tempClass            
            tempSt = tempSt.replace(t,"*객")
    
    return tempSt


# 함수를 하나의 문자로 통일
def func_Union(st):
    st = st.replace("char ","식")
    st = st.replace("short ","식")
    st = st.replace("int ","식")
    st = st.replace("long ","식")
    st = st.replace("long long ","식")
    st = st.replace("flaot ","식")
    st = st.replace("double ","식")
    st = st.replace("long double ","식")
    st = st.replace("void ","식")
    st = st.replace("string ","식")
    st = st.replace("bool ","식")

    # 식별자 다음 포인터 온 경우
    st = st.replace("char*","식*")
    st = st.replace("short*","식*")
    st = st.replace("int*","식*")
    st = st.replace("long*","식*")
    st = st.replace("long long*","식*")
    st = st.replace("flaot*","식*")
    st = st.replace("double*","식*")
    st = st.replace("long double*","식*")

    st = st.replace("#include","")
    st = st.replace("return ","")
    st = st.replace("void","")
    # 클:: 인경우 함수를 찾아내는데 혼동 막기위해
    #st = st.replace("클::","::")

    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempFunc = ""
        if st[x] == "식" or st[x] == "템":
            temp = x+1
            # 식별자 다음 빈칸 및 포인터일때 건너 뛰기
            while st[temp] == " " or st[temp] == "*" or st[temp] == "&": 
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
                elif st[temp] == ">":
                    tempFunc = ""
                    break    
                elif st[temp] == "함":
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
            tempSt = tempSt.replace(t,"함(")
                    
            t = ")" + tempFunc            
            tempSt = tempSt.replace(t,")함")

            t = " " + tempFunc            
            tempSt = tempSt.replace(t," 함")
            t = tempFunc + " "            
            tempSt = tempSt.replace(t,"함 ")

            t = "+" + tempFunc            
            tempSt = tempSt.replace(t,"+함")
            t = "-" + tempFunc            
            tempSt = tempSt.replace(t,"-함")
            t = "/" + tempFunc            
            tempSt = tempSt.replace(t,"/함")
            t = "*" + tempFunc            
            tempSt = tempSt.replace(t,"*함")
            t = "=" + tempFunc            
            tempSt = tempSt.replace(t,"=함")
            t = "%" + tempFunc            
            tempSt = tempSt.replace(t,"%함")
            t = "," + tempFunc            
            tempSt = tempSt.replace(t,",함")
            t = tempFunc + "함"            
            tempSt = tempSt.replace(t,"함")   # 미해결

            tempSt = tempSt.replace("식함","함")
            # 함수 포인터인 경우 
            tempSt = tempSt.replace("식* 함","* 함")
            tempSt = tempSt.replace("식 *함"," *함")
            tempSt = tempSt.replace("식 * 함"," * 함")

    # 함수 찾아내는데 방해요소 원상태로        
    #tempSt = tempSt.replace("::","클::")        
    return tempSt

# 변수를 하나의 문자로 통일  
def vble_Union(st):
    l = len(st)
    tempSt = st
    switch = 0
    for x in range(0,l):
        tempVb = ""
        # 변수명 추출
        if st[x] == "식" or st[x] == "템":
            temp = x+1
            # 식별자 다음 빈칸 및 포인터일때 건너 뛰기
            while st[temp] == " " or st[temp] == "*" or st[temp] == "&": 
                temp += 1
            #변수를 할당하는 과정        
            while 1:
                if st[temp] == ";":
                    switch = 0
                    break
                elif st[temp] == "\n": # int gjlk, fglk, fgldj ........,gjkjflkgjkl; 개행을 넘어버리는 경우 어쩔 ? 
                    switch = 0
                    break
                elif st[temp] == ">": #
                    tempVb = ""
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
                elif st[temp] == "변":
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
                elif st[temp] == "변":
                    temp += 1
                    continue    
                elif st[temp] == "=":
                    break
                elif st[temp] == ",":
                    break    
                elif st[temp] == ")":    # 함수의 인자값으로 괄호안에서 변수선언시
                    break
                elif st[temp] == "템":
                    tempVb = ""
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
            tempSt = tempSt.replace(t,"변;")
            
            t = tempVb + " " 
            tempSt = tempSt.replace(t,"변 ")

            t = tempVb + "="
            tempSt = tempSt.replace(t,"변=")
            t = "=" + tempVb 
            tempSt = tempSt.replace(t,"=변")

            t = tempVb + "&" 
            tempSt = tempSt.replace(t,"변&")
            t = "&" + tempVb
            tempSt = tempSt.replace(t,"&변")

            t = tempVb + "|" 
            tempSt = tempSt.replace(t,"변|")
            t = "|" + tempVb
            tempSt = tempSt.replace(t,"|변")

            t = tempVb + ">" 
            tempSt = tempSt.replace(t,"변>")
            t = ">" + tempVb
            tempSt = tempSt.replace(t,">변")

            t = tempVb + "<" 
            tempSt = tempSt.replace(t,"변<")
            t = "<" + tempVb
            tempSt = tempSt.replace(t,"<변")

            t = tempVb + "+" 
            tempSt = tempSt.replace(t,"변+")
            t = "+" + tempVb
            tempSt = tempSt.replace(t,"+변")

            t = tempVb + "-" 
            tempSt = tempSt.replace(t,"변-")
            t = "-" + tempVb
            tempSt = tempSt.replace(t,"-변")

            t = tempVb + "/" 
            tempSt = tempSt.replace(t,"변/")
            t = "/" + tempVb
            tempSt = tempSt.replace(t,"/변")

            t = tempVb + "*" 
            tempSt = tempSt.replace(t,"변*")
            t = "*" + tempVb
            tempSt = tempSt.replace(t,"*변")

            t = tempVb + "%" 
            tempSt = tempSt.replace(t,"변%")
            #t = "%" + tempVb
            #tempSt = tempSt.replace(t,"%변")

            t = tempVb + ","            
            tempSt = tempSt.replace(t,"변,")
            t = "," + tempVb            
            tempSt = tempSt.replace(t,",변")

            # 변수 다음 배열이 온 경우
            t = tempVb + "["            
            tempSt = tempSt.replace(t,"변[")
            """
            if switch == 1:
                t = tempVb + "("            
                tempSt = tempSt.replace(t,"변(")
            """        
            t = tempVb + ")"            
            tempSt = tempSt.replace(t,"변)")

            # 만약 변수안에 변수명이 포함된 경우
            t = tempVb + "변"            
            tempSt = tempSt.replace(t,"변")
            
    tempSt = tempSt.replace("식","")              
    return tempSt