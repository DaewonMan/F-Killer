###############################################################################
#              
#                           C Language Mudule
#
#                                                              <2015.03.02>
###############################################################################



# 함수를 하나의 문자로 통일
def func_Union(st):
    st = st.replace("char ","@")
    st = st.replace("short ","@")
    st = st.replace("int ","@")
    st = st.replace("long ","@")
    st = st.replace("long long ","@")
    st = st.replace("flaot ","@")
    st = st.replace("double ","@")
    st = st.replace("long double ","@")
    st = st.replace("void ","@")

    # 식별자 다음 포인터 온 경우
    st = st.replace("char*","@*")
    st = st.replace("short*","@*")
    st = st.replace("int*","@*")
    st = st.replace("long*","@*")
    st = st.replace("long long*","@*")
    st = st.replace("flaot*","@*")
    st = st.replace("double*","@*")
    st = st.replace("long double*","@*")

    st = st.replace("#include","")
    st = st.replace("return ","")
    st = st.replace("void","")

    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempFunc = ""
        if st[x] == "@":
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
                elif st[temp] == "#":
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
            tempSt = tempSt.replace(t,"#(")
                    
            t = ")" + tempFunc            
            tempSt = tempSt.replace(t,")#")

            t = " " + tempFunc            
            tempSt = tempSt.replace(t," #")
            t = tempFunc + " "            
            tempSt = tempSt.replace(t,"# ")

            t = "+" + tempFunc            
            tempSt = tempSt.replace(t,"+#")
            t = "-" + tempFunc            
            tempSt = tempSt.replace(t,"-#")
            t = "/" + tempFunc            
            tempSt = tempSt.replace(t,"/#")
            t = "*" + tempFunc            
            tempSt = tempSt.replace(t,"*#")
            t = "=" + tempFunc            
            tempSt = tempSt.replace(t,"=#")
            t = "%" + tempFunc            
            tempSt = tempSt.replace(t,"%#")
            t = "," + tempFunc            
            tempSt = tempSt.replace(t,",#")
            t = tempFunc + "#"            
            tempSt = tempSt.replace(t,"#")   # 미해결

            tempSt = tempSt.replace("@#","#")
            # 함수 포인터인 경우 
            tempSt = tempSt.replace("@* #","* #")
            tempSt = tempSt.replace("@ *#"," *#")
            tempSt = tempSt.replace("@ * #"," * #")
    return tempSt

# 변수를 하나의 문자로 통일  
def vble_Union(st):
    l = len(st)
    tempSt = st
    switch = 0
    for x in range(0,l):
        tempVb = ""
        # 변수명 추출
        if st[x] == "@":
            temp = x+1
            # 식별자 다음 빈칸 및 포인터일때 건너 뛰기
            while st[temp] == " " or st[temp] == "*": 
                temp += 1
            #변수를 할당하는 과정        
            while 1:
                if st[temp] == ";":
                    switch = 0
                    break
                elif st[temp] == "\n":
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
                elif st[temp] == "$":
                    temp += 1
                    continue 
                elif st[temp] == "=":
                    break
                elif st[temp] == ",":
                    break    
                elif st[temp] == ")":   # 함수의 인자값으로 괄호안에서 변수 선언시
                    break
                """    
                elif st[temp] == "(":
                    break
                """    
                    
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
                elif st[temp] == "$":
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
            tempSt = tempSt.replace(t,"$;")
            
            t = tempVb + " " 
            tempSt = tempSt.replace(t,"$ ")

            t = tempVb + "="
            tempSt = tempSt.replace(t,"$=")
            t = "=" + tempVb 
            tempSt = tempSt.replace(t,"=$")

            t = tempVb + "&" 
            tempSt = tempSt.replace(t,"$&")
            t = "&" + tempVb
            tempSt = tempSt.replace(t,"&$")

            t = tempVb + "|" 
            tempSt = tempSt.replace(t,"$|")
            t = "|" + tempVb
            tempSt = tempSt.replace(t,"|$")

            t = tempVb + ">" 
            tempSt = tempSt.replace(t,"$>")
            t = ">" + tempVb
            tempSt = tempSt.replace(t,">$")

            t = tempVb + "<" 
            tempSt = tempSt.replace(t,"$<")
            t = "<" + tempVb
            tempSt = tempSt.replace(t,"<$")

            t = tempVb + "+" 
            tempSt = tempSt.replace(t,"$+")
            t = "+" + tempVb
            tempSt = tempSt.replace(t,"+$")

            t = tempVb + "-" 
            tempSt = tempSt.replace(t,"$-")
            t = "-" + tempVb
            tempSt = tempSt.replace(t,"-$")

            t = tempVb + "/" 
            tempSt = tempSt.replace(t,"$/")
            t = "/" + tempVb
            tempSt = tempSt.replace(t,"/$")

            t = tempVb + "*" 
            tempSt = tempSt.replace(t,"$*")
            t = "*" + tempVb
            tempSt = tempSt.replace(t,"*$")

            t = tempVb + "%" 
            tempSt = tempSt.replace(t,"$%")
            #t = "%" + tempVb
            #tempSt = tempSt.replace(t,"%$")

            t = tempVb + ","            
            tempSt = tempSt.replace(t,"$,")
            t = "," + tempVb            
            tempSt = tempSt.replace(t,",$")

            # 변수 다음 배열이 온 경우
            t = tempVb + "["            
            tempSt = tempSt.replace(t,"$[")
            """
            if switch == 1:
                t = tempVb + "("            
                tempSt = tempSt.replace(t,"$(")
            """        
            t = tempVb + ")"            
            tempSt = tempSt.replace(t,"$)")

            # 만약 변수안에 변수명이 포함된 경우
            t = tempVb + "$"            
            tempSt = tempSt.replace(t,"$")
            
    tempSt = tempSt.replace("@","")              
    return tempSt