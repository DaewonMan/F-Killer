###############################################################################
#              
#                               Python Mudule
#
#   1. 함수 통일화 작업                        <2015.03.03>
#   2. 변수 통일화 작업                        <2015.03.13>
###############################################################################

# 함수를 하나의 문자로 통일
def func_Union(st):
    st = st.replace("\ndef ","\n@")
    st = st.replace("\tdef ","\t@")
    st = st.replace(" def "," @")
    st = st.replace("\treturn ","\t")
    st = st.replace(" return "," ")
    st = st.replace("\tpass\n","\n")
    st = st.replace(" pass\n","\n")
    l = len(st)
    tempSt = st
    for x in range(0,l):
        tempFunc = ""
        if st[x] == "@":
            temp = x+1
            # 
            while st[temp] == " ": 
                temp += 1
            # 함수명 추출
            while 1:
                if st[temp] == "(":    
                    break    
                elif st[temp] == ":":
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
            """       
            t = ")" + tempFunc            
            tempSt = tempSt.replace(t,")함")
            
            t = " " + tempFunc            
            tempSt = tempSt.replace(t," 함")
            """
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
    tempSt = tempSt.replace("@함","함")        
    return tempSt 
# 변수를 하나의 문자로 통일  
def vble_Union(st):
    # 기존의 특수문자 제거
    st = st.replace("~","")
    st = st.replace("^",".symmetric_difference:")
    # 변수를 잡아내는데 포인트 변경    
    st = st.replace("==","@")
    st = st.replace("\t","")
    # for문 안에 변수를 찾기위해 특수문자 변환
    st = st.replace("for ","^")
    st = st.replace(" in ","~")

    st = st.replace(" ","")
    l = len(st)        
    tempSt = st
    cc = []
    for x in range(0,l):
        for_switch = 0
        tempVb = ""
        mVb = []
        # 변수명 추출
        if st[x] == "\n" or x == 0 or st[x] == "함":
            if x == l-1:
                break
            temp = x+1    
            #elif x != 0:    
            #    temp += 1
            #변수를 할당하는 과정        
            while 1:
                if st[temp] == "\n":
                    mVb = []
                    tempVb = ""
                    for_switch = 0
                    break
                elif st[temp] == ":":
                    mVb = []
                    tempVb = ""
                    for_switch = 0
                    break           
                elif st[temp] == '"':
                    temp += 1
                    continue
                elif st[temp] == " ":
                    temp += 1
                    continue
                # 함수안의 변수 찾기    
                elif st[temp] == "(":
                    temp += 1
                    continue     
                # for문일때    
                elif st[temp] == "^":
                    temp += 1
                    for_switch = 1
                    continue
                #for문 안에 변수 획득    
                elif for_switch == 1:
                    if st[temp] == "~":
                        mVb.append(tempVb)
                        tempVb = ""
                        for_switch = 0
                        break                    
                #변수,변수일때 찾아내기                               
                elif tempVb != "":
                    if st[temp] == ",":
                        mVb.append(tempVb)
                        tempVb = ""
                        temp += 1
                        continue
                    # 변수만 찾아서 탈출    
                    elif st[temp] == "=":
                        mVb.append(tempVb)
                        tempVb = ""       
                        break
                    #함수안의 변수 다 찾아서 탈출    
                    elif st[temp] == ")":
                        mVb.append(tempVb)
                        tempVb = ""       
                        break               
                   
                tempVb += st[temp]
                if st[temp] in ["+","-","*","/","%","!",">","<","@"]:
                    tempVb = ""
                temp += 1    
                if temp == l-1:
                    break
        for x in range(0, len(mVb)):
            cc.append(mVb[x])

    cc = set(cc)         
    # 변수명 통일           
    for x in cc:
        t = x
        t += " "         
        tempSt = tempSt.replace(t,"변 ")
        t = " "
        t += x         
        tempSt = tempSt.replace(t," 변")

        t = x
        t += ":"         
        tempSt = tempSt.replace(t,"변:")
        
        t = x
        t += "~" 
        tempSt = tempSt.replace(t,"변~")
                    
        t = x
        t += "="
        tempSt = tempSt.replace(t,"변=")
                    
        t = "=" 
        t += x  
        tempSt = tempSt.replace(t,"=변")

        t = x 
        t += "&" 
        tempSt = tempSt.replace(t,"변&")
        t = "&" 
        t += x
        tempSt = tempSt.replace(t,"&변")

        t = x
        t += "|" 
        tempSt = tempSt.replace(t,"변|")
        t = "|"
        t += x
        tempSt = tempSt.replace(t,"|변")

        t = x
        t += ">" 
        tempSt = tempSt.replace(t,"변>")
        t = ">" 
        t += x
        tempSt = tempSt.replace(t,">변")

        t = x
        t += "<" 
        tempSt = tempSt.replace(t,"변<")
        t = "<" 
        t += x
        tempSt = tempSt.replace(t,"<변")

        t = x
        t += "+" 
        tempSt = tempSt.replace(t,"변+")
        t = "+" 
        t += x
        tempSt = tempSt.replace(t,"+변")

        t = x
        t += "-" 
        tempSt = tempSt.replace(t,"변-")
        t = "-"
        t += x
        tempSt = tempSt.replace(t,"-변")

        t = x
        t += "/" 
        tempSt = tempSt.replace(t,"변/")
        t = "/" 
        t += x
        tempSt = tempSt.replace(t,"/변")

        t = x
        t += "*" 
        tempSt = tempSt.replace(t,"변*")
        t = "*" 
        t += x
        tempSt = tempSt.replace(t,"*변")

        t = x
        t += "%" 
        tempSt = tempSt.replace(t,"변%")

        t = x
        t += "!" 
        tempSt = tempSt.replace(t,"변!")
    
        t = ","
        t += x            
        tempSt = tempSt.replace(t,",변")
        t = x
        t += ","            
        tempSt = tempSt.replace(t,"변,")
        ###
        t = x
        t += "."            
        tempSt = tempSt.replace(t,"변.")
        # 변수 다음 배열이 온 경우
        t = x
        t += "["            
        tempSt = tempSt.replace(t,"변[")
        # 배열 인덱스로 변수 쓰일 경우
        t = x
        t += "]"            
        tempSt = tempSt.replace(t,"변]")
        """
        #if switch == 1:
        #    t = mVb + "("            
        #    tempSt = tempSt.replace(t,"변(")
        """        
        t = x
        t += ")"            
        tempSt = tempSt.replace(t,"변)")

        t = x
        t += "@"            
        tempSt = tempSt.replace(t,"변@")
        t = "@"
        t += x            
        tempSt = tempSt.replace(t,"@변")

        t = x
        t += "\n"            
        tempSt = tempSt.replace(t,"변\n")    

    tempSt = tempSt.replace("@","==")
    tempSt = tempSt.replace("^","for ")
    tempSt = tempSt.replace("~"," in ")                    
    return tempSt
 
