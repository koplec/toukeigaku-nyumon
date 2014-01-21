# 誕生日の問題
# r人の集団中に、同じ誕生日の人が少なくとも2人以上いる確率は、
# P_r = 1 - (1 - 1/365)*(1 - 2/365)* ... * (1 - (r-1)/365)であることを示せ。
# また、r =5,15,20~25,30,35,40,50,60に対してPrを計算せよ

# plot図を書いてみる

import pylab as pl


def q(r):
    u"""
    r人の集団中に1人も誕生日が同じ人がいない確率
    """
    if r <= 2:
        return 1.0 - 1.0/365
    elif r>=366:
        return 0.0
    else:
        return (1.0 - (r-1)/365)*q(r-1)
    

def p(r):
    u"""
    r人の集団中に誕生日が同じ人が2人以上いる確率
    q(r)の排反事象
    """
    return 1.0 - q(r)

r=2
probs = []
while r<=370:
    prob = p(r)
    probs.append(prob)
    print("P(",r,")=",prob)
    r = r + 1

#プロット図

# 線の描画
pl.plot(probs)
# ラベル
pl.xlabel("number")
pl.ylabel("prob")
pl.title("04-04")
pl.show()
