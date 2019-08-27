import numpy as np
import csv
import torch as t
        
def linearRegression(x,y,lr=0.01):
    w=np.random.randn(18,1)
    #for i in range(10):
    #x=np.asarray(x) 
    #x=snp.squeeze(x)
    print(x)
    #x.squeeze()
    #print(x.shape)
    print(w.shape)
        # pred_y=np.dot(train_x,w)
        # loss=pred_y-train_y
        # gradient=2*np.dot(train_x,loss)
        # w-=lr*gradient

    
if __name__=='__main__':
    #Extract Features
    with open("train.csv") as csvfile:
        reader=reader(csvfile) #DictReader 會自動省略第一列
        flag=True
        train_data=[]
        for i in range(18):
            train_data.append([])
        row_cnt=0
        for row in reader:
            if flag:
                flag=False
                continue
            train_data[row_cnt%18]=np.hstack((train_data[row_cnt%18],row[3:]))
            row_cnt+=1
    tmp=1
    train_x=[]
    train_y=[]
    train_data=np.squeeze(train_data)
    train_data=t.Tensor(train_data)
    print(train_data)
    #print(train_data[0][0:10])  
    data=np.zeros([18,10])
    #train_x維度怪怪
    for i in range(0,len(train_data[0])-10,10):
        train_x.append(train_data[0:18][i:i+10])
        print(train_x)
        break
    #    #print(train_data[:][i:i+10])
    #     train_y.append(train_data[9][i+10])
    #     tmp+=1
    #     if tmp==3:
    #         break
    # linearRegression(x=train_x,y=train_y)
