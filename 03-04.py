# 3.4 ブートストラップ
# (1) [1,11]に属する整数の乱数を発生させる手続きを考えよ
# (2) (1)を11回繰り返し実行し、11個のランダムな番号を得たのち、表3.1, 図3.1のデータからその番号を取り出し、
# (重複する番号があれば重複して取出し、そのデータはその個数だけあると考える）、相関係数rを計算せよ
# (3) (2)を200回繰り返し、相関係数の値r1,r2,...,r200を得たのち、そのヒストグラムを作れ。
# 以上の統計手法をブートストラップと呼ぶ

import random
import math
import numpy as np

##(1)の手続き
def rand11():
    data11 = []
    for i in range(11):
        a = random.randint(1,11)
        data11.append(a)
    
    return np.array(data11)

##11回繰り返す
data11 = rand11()
print("生成した11個の乱数は以下の通り")
print(data11)

##表3.1のデータ
# x:男兄弟の身長（インチ）
# y:女兄弟の身長（インチ）
table = {
    "x":np.array([71,68,66,67,70,71,70,73,72,65,66]), 
    "y":np.array([69,64,65,63,65,62,65,64,66,59,62])
}
print("表3.1のデータ")
print(table)

##11個のランダムな番号から相関係数を計算する
## 相関係数は、r_xy = \sum(x_i-\bar(x))(y_i-\bar(y))/n / \sqrt(\sum(x_i-\bar(x))^2/n) \sqrt(\sum(x_i-\bar(x))^2/n)
## 平均と分散の計算手続きを書く
# 平均
def avg(lst):
    total = sum(lst)
    return total / len(lst)

# 分散
def div(x_lst, y_lst):
    x_av = avg(x_lst)
    y_av = avg(y_lst)
    return sum(list(map(lambda x, y: (x-x_av)*(y-y_av), x_lst, y_lst))) / len(x_lst)

#相関係数
def corr(x_lst, y_lst):
    xy_div = div(x_lst, y_lst)
    x_div = div(x_lst,x_lst)
    y_div = div(y_lst, y_lst)
    return xy_div/(math.sqrt(x_div)*math.sqrt(y_div))

x_avg = avg(table["x"])
print("xの平均値は、", x_avg)
y_avg = avg(table["y"])
print("yの平均値は、", y_avg)

x_div = div(table["x"], table["x"])
y_div = div(table["y"], table["y"])
xy_div = div(table["x"], table["y"])

print("表3.1から純粋に求めた相関係数は、", xy_div/(math.sqrt(x_div)*math.sqrt(y_div)))
print(" 相関係数の関数から求めると、", corr(table["x"], table["y"]))


print("(2)11個の乱数から求めた相関係数を計算する")
print("まず、データを抜き出す")
print("乱数は",data11)

x_11 = []
y_11 = []

for r in data11:
    x = table["x"][r-1]
    y = table["y"][r-1]
    x_11.append(x)
    y_11.append(y)
        
x_11 = np.array(x_11)
y_11 = np.array(y_11)
print("x_11=",x_11)
print("y_11=",y_11)
print("これらから相関係数を求めると、", corr(x_11, y_11))

print("(3)data11を200個作って、相関係数を200個作成してヒストグラムを作る")
#(2)の結果から、乱数を与えた時に相関係数を計算する関数を作る
def calcCorr(data11):
    x_11 = []
    y_11 = []

    for r in data11:
        x = table["x"][r-1]
        y = table["y"][r-1]
        x_11.append(x)
        y_11.append(y)
        
    x_11 = np.array(x_11)
    y_11 = np.array(y_11)
    return corr(x_11, y_11)

#11個の乱数を作る手続きはすでに作成したので
corrs = []
for count in range(200):
    data11 = rand11()
    r = calcCorr(data11)
    corrs.append(r)
    print("r_", count, " = ", r)

    
corrs = np.array(corrs)

