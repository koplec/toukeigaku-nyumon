# 06-02
# ポアソン分布
#
import math

avg = 2.5
def prob(x):
    return math.exp(-avg) * math.pow(avg, x) / math.factorial(x)


print("x=0~4の確率を求める")

sum = 0
for x in range(0, 5):
    p = prob(x)
    print("x=",x,"prob=",p)
    sum += p

print("x>=5の確率は", (1 - sum))


import pylab as pl
print("ポアソン分布をプロットする")
probs = []
for x in range(0, 10):
    p = prob(x)
    probs.append(p)
    print("x=",x,"prob=",p)
    sum += p

pl.plot(probs)

# ラベル
pl.title("06-02")
pl.xlabel("number")
pl.ylabel("prob")

pl.show()
