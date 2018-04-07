import sys
import numpy as np
import copy
args = sys.argv
if(len(args)!=3):
    sys.exit(1)
line = int(args[1])
if((line<1)|(line>10)):
    sys.exit(1)
row = int(args[2])
if((row<1)|(row>10)):
    sys.exit(1)

if((line==1)|(row==1)):#明らかに一通りの時終わる
    print(1)
    exit(0)

matrix = np.zeros([line+2,row+2])

for i in range(line+2):
    for j in range(row+2):
        if((i==0)|(i==line+1)|(j==0)|(j==row+1)):
            matrix[i][j] = 1

pos = [1,1]#現在位置
pos_n = [1,1]#次の位置
pos_b = [1,1]#前の位置
start = 0
route = 0

goal = 0
rev_flag = 0
move_list = [[0,1],[1,0],[-1,0],[0,-1]]
trail=[]
while start!=2:
    pos = copy.deepcopy(pos_n)
    matrix[pos[0],pos[1]] = 1
    trail.append(pos)

    pos_n=[0,0]#pos_nの初期化
    route = 0#routeの初期化

    if(rev_flag==1):
        matrix[pos_b[0],pos_b[1]]=0#逆走中はひとつ前の位置の記録を消す
        for mov in move_list[move_list.index([pos_b[0]-pos[0],pos_b[1]-pos[1]])+1:]:#行先探し
            if(matrix[pos[0]+mov[0],pos[1]+mov[1]]==0):
                route += 1
                if(pos_n==[0,0]):
                    pos_n = [pos[0]+mov[0],pos[1]+mov[1]]#次の位置
    else:
        for mov in [[0,1],[1,0],[-1,0],[0,-1]]:#行先探し
            if(matrix[pos[0]+mov[0],pos[1]+mov[1]]==0):
                route += 1
                if(pos_n==[0,0]):
                    pos_n = [pos[0]+mov[0],pos[1]+mov[1]]#次の位置
    
    if(route==0):
        if(rev_flag != 1):
            if(np.sum(matrix)==(line+2)*(row+2)):#一筆書き成功カウント
                goal+=1
        
        pos_b = trail.pop()#現在位置をひとつ前の位置として記憶
        pos_n = trail.pop()#ひとつ前に戻る
        if(pos_n==[1,1]):#初期位置に移動した回数が2回で終了
            start += 1

        rev_flag = 1#逆走はじめ

    else:
        rev_flag = 0#逆走やめる 
print (goal)