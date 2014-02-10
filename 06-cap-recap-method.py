#捕獲・採捕獲法の例
# ある湖の中にいる魚1000匹のうち、200匹には尾部に赤い色の標識を人為的につけて放流されている。
# いま池から魚を5匹捕ったとき、そのうち標識がつけた魚が1匹である確率はどれくらいか？
# 0匹の場合はどれくらいか

import scipy.misc as scm
import pylab as pl

# 全体の場合の数
all = scm.comb(1000, 5, True) #1000_C_5

# 1匹が赤色の魚の場合の数
num_1 = scm.comb(800, 4, True) * scm.comb(200, 1, True)

prob_1 = num_1 / all
print("1匹の場合の確率は、", prob_1)


# 赤の魚が0匹の場合の数
num_0 = scm.comb(800, 5, True)

prob_0 = num_0 / all
print("0匹の場合の確率は、", prob_0)
