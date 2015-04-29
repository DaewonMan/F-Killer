###############################################################################
#              
#                           C Language Mudule
#    함수,변수명 통일
#    define명 통일   
#    구조체명 통일                                                <2015.04.28>
###############################################################################
def str_Union(st):
    st = st.replace("\nstruct ","\nㄱ")
    st = st.replace(" struct "," ㄱ")
    st = st.replace("\tstruct ","\tㄱ")

    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempStr = ""
        if st[x] == "ㄱ":
            temp = x+1
            # 
            while st[temp] == " ": 
                temp += 1
            # 구조체명 추출
            while 1:
                if st[temp] == "\n":    
                    break    
                elif st[temp] == " ":
                    break
                elif st[temp] == "구":
                    tempStr = ""
                    break        
                # 구조체를 한문자씩 저장                                    
                tempStr += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 구조체명 통일           
        if tempStr != "":                          
            t = "ㄱ" + tempStr            
            tempSt = tempSt.replace(t,"ㄱ구")
    tempSt = tempSt.replace("ㄱ","")

    # typedef로 구조체 재정의        
    tempSt = tempSt.replace("\ntypedef ","\nㅌ")
    tempSt = tempSt.replace(" typedef "," ㅌ")
    tempSt = tempSt.replace("\ttypedef ","\tㅌ")

    st = tempSt
    l = len(st)
    cnt = 0 # 괄호갯수 체크
    for x in range(0,l):
        tempStr = ""
        if st[x] == "ㅌ":
            temp = x+1
            while st[temp] == " " or st[temp] == "구" or st[temp] == "\n": 
                temp += 1

            # 구조체명 추출
            while 1:
                if st[temp] == "{":
                    cnt += 1
                     
                    
                if st[temp] == " ":
                    temp += 1    
                    continue
                elif st[temp] == "\t":
                    temp += 1    
                    continue
                elif st[temp] != "}" and cnt != 0:
                    temp += 1    
                    continue        
                elif st[temp] == "}":
                    cnt -= 1
                    temp += 1
                    continue
                elif st[temp] == ";":
                    break            
                # 괄호밖에 구조체명추출    
                if cnt == 0: 
                    # 구조체명을 한문자씩 저장                                    
                    tempStr += st[temp] 
                    temp += 1
                if temp == l-1:
                    break                        

        # 구조체명 통일           
        if tempStr != "":                          
            t = tempStr + ";"            
            tempSt = tempSt.replace(t,"구;")
            t = tempStr + " "            
            tempSt = tempSt.replace(t,"구 ")
    tempSt = tempSt.replace("ㅌ","")
            
    # 구조체 구조체명 찾아서 통일
    st = tempSt
    l = len(st)
    for x in range(0,l):
        tempStr = ""
        if st[x] == "구":
            temp = x+1
            # 
            while st[temp] == " " or st[temp] == "*": 
                temp += 1
            # 구조체명 추출
            while 1:
                if st[temp] == ";":    
                    break
                elif st[temp] == "=":
                    break
                elif st[temp] == "\n":
                    break             
                elif st[temp] == " ":
                    temp += 1
                    continue
                # 구조체명을 한문자씩 저장                                    
                tempStr += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # 구조체명 통일           
        if tempStr != "":                          
            t = tempStr + ";"            
            tempSt = tempSt.replace(t,"구;")
            t = tempStr + "."            
            tempSt = tempSt.replace(t,"구.")
            t = "." + tempStr            
            tempSt = tempSt.replace(t,".구")
            t = " " + tempStr + " "            
            tempSt = tempSt.replace(t," 구 ")
            t = "\t" + tempStr + " "            
            tempSt = tempSt.replace(t,"\t구 ")
            t = " " + tempStr + "="            
            tempSt = tempSt.replace(t," 구=")
            t = "&" + tempStr            
            tempSt = tempSt.replace(t,"&구")
            
    return tempSt


# 함수를 하나의 문자로 통일
def func_Union(st):
    st = st.replace("char ","식")
    st = st.replace("short ","식")
    st = st.replace("int ","식")
    st = st.replace("long ","식")
    st = st.replace("long long ","식")
    st = st.replace("float ","식")
    st = st.replace("double ","식")
    st = st.replace("long double ","식")
    st = st.replace("void ","식")

    # 식별자 다음 포인터 온 경우
    st = st.replace("char*","식*")
    st = st.replace("short*","식*")
    st = st.replace("int*","식*")
    st = st.replace("long*","식*")
    st = st.replace("long long*","식*")
    st = st.replace("float*","식*")
    st = st.replace("double*","식*")
    st = st.replace("long double*","식*")

    st = st.replace("#include","")
    st = st.replace("return ","")
    st = st.replace("void","")

    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempFunc = ""
        if st[x] == "식":
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
                elif st[temp] == "함":
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
                elif st[temp] == "변":
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
                elif st[temp] == "변":
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

def def_Union(st):
    st = st.replace("#define ","정")
    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempdef = ""
        if st[x] == "정":
            temp = x+1
            while st[temp] == " ": 
                temp += 1
            # define명 추출
            while 1:
                if st[temp] == " ":  
                    break     
                # define명 한문자씩 저장                                    
                tempdef += st[temp] 
                temp += 1
                if temp == l-1:
                    break

        # define명 통일           
        if tempdef != "": 
            t = tempdef + ";"         
            tempSt = tempSt.replace(t,"변;")
            
            t = tempdef + " " 
            tempSt = tempSt.replace(t,"변 ")

            t = tempdef + "="
            tempSt = tempSt.replace(t,"변=")
            t = "=" + tempdef 
            tempSt = tempSt.replace(t,"=변")

            t = tempdef + "&" 
            tempSt = tempSt.replace(t,"변&")
            t = "&" + tempdef
            tempSt = tempSt.replace(t,"&변")

            t = tempdef + "|" 
            tempSt = tempSt.replace(t,"변|")
            t = "|" + tempdef
            tempSt = tempSt.replace(t,"|변")

            t = tempdef + ">" 
            tempSt = tempSt.replace(t,"변>")
            t = ">" + tempdef
            tempSt = tempSt.replace(t,">변")

            t = tempdef + "<" 
            tempSt = tempSt.replace(t,"변<")
            t = "<" + tempdef
            tempSt = tempSt.replace(t,"<변")

            t = tempdef + "+" 
            tempSt = tempSt.replace(t,"변+")
            t = "+" + tempdef
            tempSt = tempSt.replace(t,"+변")

            t = tempdef + "-" 
            tempSt = tempSt.replace(t,"변-")
            t = "-" + tempdef
            tempSt = tempSt.replace(t,"-변")

            t = tempdef + "/" 
            tempSt = tempSt.replace(t,"변/")
            t = "/" + tempdef
            tempSt = tempSt.replace(t,"/변")

            t = tempdef + "*" 
            tempSt = tempSt.replace(t,"변*")
            t = "*" + tempdef
            tempSt = tempSt.replace(t,"*변")

            t = tempdef + "%" 
            tempSt = tempSt.replace(t,"변%")
            #t = "%" + tempdef
            #tempSt = tempSt.replace(t,"%변")

            t = tempdef + ","            
            tempSt = tempSt.replace(t,"변,")
            t = "," + tempdef            
            tempSt = tempSt.replace(t,",변")

            # 변수 다음 배열이 온 경우
            t = tempdef + "["            
            tempSt = tempSt.replace(t,"변[")
            #
            t = "[" + tempdef + "]"            
            tempSt = tempSt.replace(t,"[변]")
            """
            if switch == 1:
                t = tempdef + "("            
                tempSt = tempSt.replace(t,"변(")
            """        
            t = tempdef + ")"            
            tempSt = tempSt.replace(t,"변)")

            # 만약 변수안에 변수명이 포함된 경우
            t = tempdef + "변"            
            tempSt = tempSt.replace(t,"변")
            
    tempSt = tempSt.replace("정","")                         
            
    return tempSt      