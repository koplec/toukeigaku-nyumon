import numpy as np
import pylab as pl

## ホイヘンスの問題
## 2個のさいころを何回振れば、そのうちの1回は目の和が12になる確率が0.9を超えるか

# 目の和が12になる確率は、1/36
# 排反事象として、n回投げた時に1回も目の和が12にならない確率を考えると
def prob(n):
    a = 35/36
    return a**n

count = 1
probs = []
while True:
    p = 1 - prob(count)
    probs.append(p)
    print("count:",count,"=>",p)
    count = count+1
    if p > 0.9:
        break

#　練習として、プロット図も描いてみる

#線の描画
pl.plot(probs)
#点の描画
pl.plot(probs, "r*")
#いろいろ説明
pl.xlabel("count")
pl.ylabel("prob")
pl.title("04-02")
pl.show()
