import scipy.misc as scm
import pylab as pl
# 45組から15組を選択する場合の数 45_C_15を計算する

c = scm.comb(45,15,True) #第3引数は整数で返す指定（精度）
print("45組から15組を選択する場合の数:", c)

p = c * ((1/3)**15) * ((2/3)**30)
print("45組のうちが15組が向かい合って座り、30組が隣り合って座る全確率は、", p)

# 計算すると12.5%くらい　本当にありそうか知りたいので、周辺を見てみる

#45組からn組を選択した場合の確率を求める
def prob(n):
    c = scm.comb(45, n, True)
    p = (1/3)**n
    q = (2/3)**(45-n)
    return c*p*q

probs = []
n=1
while n<=45:
    p = prob(n)
    probs.append(p)
    print("n=",n," =>",p)
    n = n + 1

pl.plot(probs)
# ラベル
pl.xlabel("number")
pl.ylabel("prob")
pl.title("04-05")
pl.show()
