###############################################################################
#              
#                                 Java Mudule
#
#
# 참조변수,인스턴스 통일                                           <2015.04.30>    
###############################################################################
# 클래스를 하나의 문자로 통일
def class_Union(st):
    st = st.replace(" class "," ㅋ")
    st = st.replace("\tclass ","\tㅋ")
    st = st.replace(" new "," 뉴 ")
    st = st.replace("=new ","=뉴 ")
    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempClass = ""
        if st[x] == "ㅋ":
            temp = x+1
            # 클래스 다음 빈칸 건너 뛰기
            while st[temp] == " ": 
                temp += 1
            # 클래스명 추출
            while 1:
                if st[temp] == "\n": # class 클래스명    
                    break
                elif st[temp] == " ": 
                    break
                elif st[temp] == "\t": 
                    break                                 
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
            t = "\t" + tempClass + "\n"            
            tempSt = tempSt.replace(t,"\t클\n")
            #(예시) class 클래스
            t = "ㅋ" + tempClass + " "            
            tempSt = tempSt.replace(t,"ㅋ클 ")
            t = "ㅋ" + tempClass + "\n"            
            tempSt = tempSt.replace(t,"ㅋ클\n") 
            #
            t = " " + tempClass + "("            
            tempSt = tempSt.replace(t," 클(")
            t = "\t" + tempClass + "("            
            tempSt = tempSt.replace(t,"\t클(")
            t = "(" + tempClass + " "            
            tempSt = tempSt.replace(t,"(클 ")

    tempSt = tempSt.replace("ㅋ","")
    
    # new로인해 생성된 클래스명 통일    
    st = tempSt
    l = len(st)
    for x in range(0,l):
        tempClass = ""
        if st[x] == "뉴":
            temp = x+1
            # 클래스명 다음 빈칸 건너 뛰기
            while st[temp] == " ": 
                temp += 1
            # 클래스명 추출
            while 1:
                if st[temp] == "클":
                    tempClass = "" 
                    break
                elif st[temp] == "(":   
                    break          
                elif st[temp] == " ":
                    temp += 1   
                    continue
                # 클래스가 아닐시 저장하고 있던 스트링 초기화    
                elif st[temp] == "\n":
                    tempClass = ""   
                    break                            
                # 클래스명 한문자씩 저장                                    
                tempClass += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 클래스명 통일           
        if tempClass != "":
            # 
            t = " " + tempClass + " "            
            tempSt = tempSt.replace(t," 클 ")
            t = "\t" + tempClass + " "            
            tempSt = tempSt.replace(t,"\t클 ") 
            #
            t = " " + tempClass + "("            
            tempSt = tempSt.replace(t," 클(")
            t = "\t" + tempClass + "("            
            tempSt = tempSt.replace(t,"\t클(")
            t = "(" + tempClass + " "            
            tempSt = tempSt.replace(t,"(클 ")

    # 클래스 참조변수를 하나의 문자로 통일

    st = tempSt
    l = len(st)
    for x in range(0,l):
        tempClass = ""
        if st[x] == "클":
            temp = x+1
            # 참조변수명 다음 빈칸 건너 뛰기
            while st[temp] == " ": 
                temp += 1
            # 참조변수명 추출
            while 1:
                if st[temp] == "=": 
                    break
                elif st[temp] == "(":   
                    break
                elif st[temp] == ";":   
                    break              
                elif st[temp] == " ":
                    temp += 1   
                    continue
                # 참조변수가 아닐시 저장하고 있던 스트링 초기화
                elif st[temp] == "[":
                    tempClass = ""   
                    break    
                elif st[temp] == "\n":
                    tempClass = ""   
                    break                            
                # 참조변수명 한문자씩 저장                                    
                tempClass += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 클래스 참조변수명 통일           
        if tempClass != "":
            t = " " + tempClass + " "            
            tempSt = tempSt.replace(t," 참 ")
            t = " " + tempClass + "="            
            tempSt = tempSt.replace(t," 참=")
            t = " " + tempClass + "."            
            tempSt = tempSt.replace(t," 참.")
            t = "(" + tempClass + "."            
            tempSt = tempSt.replace(t,"(참.")
            t = "\t" + tempClass + " "            
            tempSt = tempSt.replace(t,"\t참 ")
            t = "\t" + tempClass + "="            
            tempSt = tempSt.replace(t,"\t참=")
            t = "\t" + tempClass + "."            
            tempSt = tempSt.replace(t,"\t참.")
            t = "(" + tempClass + ")"            
            tempSt = tempSt.replace(t,"(참)")
            t = " " + tempClass + ")"            
            tempSt = tempSt.replace(t," 참)")
            t = " " + tempClass + ";"            
            tempSt = tempSt.replace(t," 참;")
        
    return tempSt
# 함수를 하나의 문자로 통일
def func_Union(st):
    for i in [" ","\t","(",","]:
        st = st.replace(i+"char ",i+"식")
        st = st.replace(i+"short ",i+"식")
        st = st.replace(i+"int ",i+"식")
        st = st.replace(i+"long ",i+"식")
        st = st.replace(i+"long long ",i+"식")
        st = st.replace(i+"float ",i+"식")
        st = st.replace(i+"double ",i+"식")
        st = st.replace(i+"long double ",i+"식")
        st = st.replace(i+"void ",i+"식")
        st = st.replace(i+"String ",i+"식")
        st = st.replace(i+"bool ",i+"식")

    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempFunc = ""
        if st[x] == "식":
            temp = x+1
            # 식별자 다음 빈칸 건너 뛰기
            while st[temp] == " ": 
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

            tempSt = tempSt.replace("식함","함")

    # new로인해 생성된 함수명 통일    
    st = tempSt
    l = len(st)
    for x in range(0,l):
        tempFunc = ""
        if st[x] == "뉴":
            temp = x+1
            # 함수명 다음 빈칸 건너 뛰기
            while st[temp] == " ": 
                temp += 1
            # 함수명 추출
            while 1:
                if st[temp] == "클":
                    tempFunc = "" 
                    break
                elif st[temp] == "함":
                    tempFunc = ""   
                    break     
                elif st[temp] == "(":
                    tempFunc = ""   
                    break          
                elif st[temp] == " ":
                    temp += 1   
                    continue
                elif st[temp] == "[":
                    break   
                # 함수가 아닐시 저장하고 있던 스트링 초기화    
                elif st[temp] == "\n":
                    tempFunc = ""   
                    break                            
                # 함수명 한문자씩 저장                                    
                tempFunc += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 함수명 통일           
        if tempFunc != "":
            # 
            t = " " + tempFunc + " "            
            tempSt = tempSt.replace(t," 함 ")
            t = "\t" + tempFunc + " "            
            tempSt = tempSt.replace(t,"\t함 ") 
            #
            t = " " + tempFunc + "["            
            tempSt = tempSt.replace(t," 함[")
            t = "\t" + tempFunc + "["            
            tempSt = tempSt.replace(t,"\t함[")
            t = "(" + tempFunc + " "            
            tempSt = tempSt.replace(t,"(함 ")

    # 함수의 인스턴스를 하나의 문자로 통일
    st = tempSt
    l = len(st)
    switch = 0
    for x in range(0,l):
        tempFunc = ""
        if st[x] == "함":
            temp = x+1
            # 인스턴스명 다음 빈칸 건너 뛰기
            while st[temp] == " ": 
                temp += 1
            # 인스턴스명 추출
            while 1:
                if st[temp] == "=":   
                    break
                elif st[temp] == ";":   
                    break              
                elif st[temp] == " ":
                    temp += 1   
                    continue
                #배열 건너뛰기    
                elif st[temp] == "[":
                    temp += 1
                    switch = 1   
                    continue
                elif st[temp] == "]":
                    temp += 1
                    switch = 0   
                    continue
                elif switch == 1:
                    temp += 1  
                    continue            
                # 인스턴스가 아닐시 저장하고 있던 스트링 초기화
                elif st[temp] == "(":
                    tempFunc = ""   
                    break    
                elif st[temp] == "\n":
                    tempFunc = ""   
                    break                            
                # 인스턴스명 한문자씩 저장                                    
                tempFunc += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 인스턴스명 통일           
        if tempFunc != "":
            
            t = "\t" + tempFunc + " "            
            tempSt = tempSt.replace(t,"\t인 ")
            t = " " + tempFunc + " "            
            tempSt = tempSt.replace(t," 인 ")

            t = "\t" + tempFunc + "="            
            tempSt = tempSt.replace(t,"\t인=")
            t = " " + tempFunc + "="            
            tempSt = tempSt.replace(t," 인=")

            t = tempFunc + "["            
            tempSt = tempSt.replace(t,"인[")
            
            t = " " + tempFunc + ";"            
            tempSt = tempSt.replace(t," 인;")                     
    return tempSt

# 변수를 하나의 문자로 통일  
def vble_Union(st):
    l = len(st)
    tempSt = st
    switch = 0
    for x in range(0,l):
        tempVb = ""
        # 변수명 추출
        if st[x] == "식":
            temp = x+1
            # 식별자 다음 빈칸 건너 뛰기
            while st[temp] == " ": 
                temp += 1
            #변수를 할당하는 과정        
            while 1:
                if st[temp] == ";":
                    switch = 0
                    break
                elif st[temp] == "\n": # 
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
            #
            t = "[" + tempVb + "]"            
            tempSt = tempSt.replace(t,"[변]")

            t = tempVb + ")"            
            tempSt = tempSt.replace(t,"변)")

    tempSt = tempSt.replace("식","")              
    return tempSt
