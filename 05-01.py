#
# 手計算で求めた確率と1/k^2の大小関係をプロットする
#
import matplotlib.pyplot as plt
import numpy as np

def prob(a):
    print(a)
    if a < :
        return 1 - a/1.73
    else:
        return 0


k = np.arange(0.1, 2., 0.1)

plt.plot(k, prob(k), 'r--')
plt.xlabel("k")
plt.ylabel("p")
plt.title("05-01")

plt.show()
