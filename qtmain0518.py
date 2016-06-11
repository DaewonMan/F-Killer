#####################################################################
#
#                           UI
#
#  1. ui 틀 그리기                                    <2015.05.15>
#####################################################################

#################################### QT MAIN ############################################################
## 모듈 불러오기 ##
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, uic
from PyQt5 import *

import main0518 as mn
from main0518 import *

import fileinput
from glob import glob

from pandas import Series, DataFrame
import pandas as pd

import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
######################################################

class MainWindow(QtWidgets.QDialog):
    indexNumber = 0
    radioValue = 0
    lggSelect = ""
    aRoute = ""
    
    tPlsm = []
    fIex = []
    flen = 0

    wF = []
    pIex = []
    iList = []
    
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("ui.ui", self)
        self.buttonOpen.clicked.connect(self.directoryOpen)
        self.indexSpinBox.valueChanged.connect(self.changedValue)
        self.radio_c.toggled.connect(self.radioChanged1)
        self.radio_cpp.toggled.connect(self.radioChanged2)
        self.radio_java.toggled.connect(self.radioChanged3)
        self.radio_python.toggled.connect(self.radioChanged4)
        self.startButton.clicked.connect(self.startClicked)

        self.pushButton.clicked.connect(self.buttonClicked)
        self.graphButton.clicked.connect(self.graphClicked)
        self.graphButton2.clicked.connect(self.graphClicked2)
        
    # 디렉토리 열기
    def directoryOpen(self):
        self.directoryName = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.DirectoryNameLabel.setText(self.directoryName)
    # 자카르트 인덱스 값 설정         
    def changedValue(self, event):
        self.indexNumber = self.indexSpinBox.value()
        
    # 검사할 언어의 라디오 버튼 선택  
    def radioChanged1(self):
        self.radioValue = 1
        self.lggSelect = '/*.c'
    def radioChanged2(self):
        self.radioValue = 2
        self.lggSelect = '/*.cpp'
    def radioChanged3(self):
        self.radioValue = 3
        self.lggSelect = '/*.java'
    def radioChanged4(self):
        self.radioValue = 4
        self.lggSelect = '/*.py'
    # 검사 시작 버튼    
    def startClicked(self):
        self.aRoute = self.directoryName + self.lggSelect
        self.coiedFile, self.tPlsm, self.fIex, self.flen, self.wF, self.pIex, self.iList  = mn.main(self.radioValue, glob(self.aRoute), self.indexNumber)
        self.textDisplay.setText(self.coiedFile)
        
        #self.tPlsm = mn.totalPlsm
        #self.fIex = mn.fnameIndex
    def buttonClicked(self):
        allFile = "\t" + "File Name           Plagiarism Rate" + "\t\t\t" + "File Name           Plagiarism Rate" + "\n"
        for x in range(0,len(self.tPlsm)):
            if (x+1) % 2 == 0:
                allFile += self.fIex[x] + "       "
                allFile += str(self.tPlsm[x]) + "%" + "\n"
            else:    
                allFile += "\t" + self.fIex[x] + "       "
                allFile += "\t" + str(self.tPlsm[x]) + "%" + "\t\t\t\t"

        self.printLabel.setText(allFile)    
    # 카테고리별 출력       
    def graphClicked(self):
        pos_list = np.arange(len(self.fIex))
        
        plt.title("Plagiarism rate for " + str(self.flen) + " files")
        plt.xlabel("File Name")
        plt.ylabel("Plagiarism Rate (%)")
        plt.ylim(0,100)
        plt.bar(pos_list, self.tPlsm, color = 'b', align = 'center')
        plt.xticks(pos_list, self.fIex, rotation = -50)
        plt.show()
        

    def graphClicked2(self):
        # 같은 토큰이있는지 알아내는 로직
        inCnt = 0        
        for x in range(0,len(self.wF)):
            cntList = [] # 표절한 토큰수
            for z in range(0,len(self.wF[x])):
                cntList.append(0)    
                for y in range(0,len(self.iList[x])):
                    if self.wF[x][z] == self.iList[x][y]:
                        cntList[z] += 1
                   
            if len(self.wF[x]) != 0:
                inCnt += 1
                plt.subplot2grid((5, 2),(inCnt,0),rowspan = 1,colspan = 3)
                pos_list = np.arange(len(self.wF[x])) 
                plt.title("Plagiarism Sector of " + str(self.pIex[x]))
                plt.xlim(0,len(self.wF[x]))
                plt.bar(pos_list, cntList, color = 'k', align = 'center')
                plt.show()

        
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(None)
    window.show()
    app.exec()
