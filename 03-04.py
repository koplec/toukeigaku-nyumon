# 3.4 ブートストラップ
# (1) [1,11]に属する整数の乱数を発生させる手続きを考えよ
# (2) (1)を11回繰り返し実行し、11個のランダムな番号を得たのち、表3.1, 図3.1のデータからその番号を取り出し、
# (重複する番号があれば重複して取出し、そのデータはその個数だけあると考える）、相関係数rを計算せよ
# (3) (2)を200回繰り返し、相関係数の値r1,r2,...,r200を得たのち、そのヒストグラムを作れ。
# 以上の統計手法をブートストラップと呼ぶ

import random

##(1)の手続き
def rand11():
    return random.randint(1,11)

##11回繰り返す
data = []
for i in range(11):
    a = rand11()
    data.append(a)

print("生成した乱数は以下の通り")
print(data)

##表3.1のデータ
# x:男兄弟の身長（インチ）
# y:女兄弟の身長（インチ）
table = {
    "x":[71,68,66,67,70,71,70,73,72,65,66], 
    "y":[69,64,65,63,65,62,65,64,66,59,62]
}
print("表3.1のデータ")
print(table)

##11個のランダムな番号から相関係数を計算する
## 相関係数は、r_xy = \sum(x_i-\bar(x))(y_i-\bar(y))/n / \sqrt(\sum(x_i-\bar(x))^2/n) \sqrt(\sum(x_i-\bar(x))^2/n)
## 分散から求める
