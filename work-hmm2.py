import numpy as np
import pandas as pd
from pandas import DataFrame,Series

class HMM:
    def __init__(self, A, B, Pi, O):
        self.A = np.array(A)  # 状态转移概率矩阵
        self.B = np.array(B)  # 观测概率矩阵
        self.Pi = np.array(Pi) # 初始状态概率矩阵
        self.O =  np.array(O)  # 观测序列
        self.N = self.A.shape[0] # 状态取值个数
        self.M = self.B.shape[1] # 观测值取值个数

    def printhmm(self):
        print("==================================================")
        print(u"HMM content: N (状态数量)=%s   M (观察数量)=%s "%(self.N,self.M))
        print(u"hmm.A(转移矩阵) ")
        print(self.A)
        print(u" hmm.B(发射矩阵) ")
        print(self.B)
        print(u"hmm.pi(初始状态分布)")
        print(self.Pi)
        print("==================================================")
    
    def viterbi(self):
        n = len(self.O)  #观测序列和状态序列的长度
        Y = np.zeros(n)  #初始化状态序列
        
        delta = np.zeros((n,self.N))
        psi = np.zeros((n,self.N))
        
        #初始化
        for i in range(self.N):
            delta[0,i] = self.Pi[i] * self.B[i,self.O[0]]
            psi[0,i] = 0
        #递推
        for t in range(1,n):
            for i in range(self.N):
                delta[t,i] = self.B[i,self.O[t]] * np.array([delta[t-1,j] * self.A[j,i] for j in range(self.N)]).max()
                psi[t,i] = np.array([delta[t-1,j] * self.A[j,i] for j in range(self.N)]).argmax()
       # print(psi)
        #终止
        Y[n-1] = delta[n-1,:].argmax()
        print(Y[n-1])
        if(Y[n-1]==0):
            print("优")
        if(Y[n-1]==1):
            print("良")
        if(Y[n-1]==2):
            print("差")
        
        #回朔
        for t in range(n-2,-1,-1):
            Y[t] = psi[int(t+1),int(Y[t+1])]
            
        return Y

def normalization(m):

    l = len(m)
    matrix = [4,4,4,4,4]
    c1 = -10
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0

    for i in range(l):
        if(c3<=m[0] <25*(i+1)):
            matrix[0]=l-1-i
            break
        else:
            c3=25*(i+1)
    for i in range(l):
        if(c4<=m[1] <13*(i+1)):
            matrix[1]=l-1-i
            break
        else:
            c3=13*(i+1)
    for i in range(l):
        if(c5<=m[2] <0.67*(i+1)):
            matrix[2]=l-1-i
            break
        else:
            c5=0.67*(i+1)
    for i in range(l):
        if(c6<=m[3] <26.7*(i+1)):
            matrix[3]=l-1-i
            break
        else:
            c6=26.7*(i+1)
    for i in range(l):
        if(c1<=m[4] <9*(i+1)-10):
            matrix[4]=l-1-i
            break
        else:
            c1=9*(i+1)-10

    for i in range(l):
        if(matrix[i]>4):
            matrix[i]=4

    return matrix
        

if __name__ == '__main__':
    #初始化HMM模型参数
    A = [[0.62,0.38,0],[0.22,0.71,0.07],[0.2,0.2,0.6]]
    #B = [[0,0.53,0,0,0.47],[0,0,0.51,0.14,0.35],[0.41,0,0.36,0.23,0]]#第一次测试20
    #B = [[0.17,0.33,0.17,0.08,0.25],[0.11,0.13,0.36,0.19,0.21],[0.37,0.08,0.26,0.23,0.06]]#第二次测试20
    B = [[0,0.5,0,0,0.5],[0,0,0.5,0.1,0.4],[0.4,0,0.4,0.2,0]]#第三次测试23
    Pi = [0.33,0.33,0.34]
    #观测序列 

    datafile='E:\\xhyxx\\work2\\AQI-12.xlsx'#文件所在位置
    data = pd.read_excel(datafile)#datafile是excel文件，所以用read_excel,如果是csv文件则用read_csv
    examDf = DataFrame(data)
 
    #数据清洗,要哪些列取哪些列
    new_examDf = examDf.iloc[:,6:11]
    data = new_examDf.values
    #print(data[0,:])

    for i in range(31):

        v = data[i,:]
        O = normalization(v)
    #O = [3,4,5,2,5,3]
        print(v)
        
        print('----------------viterbi 算法-----------------------',i+1)
        hmm = HMM(A,B,Pi,O)
        Y = hmm.viterbi()
        