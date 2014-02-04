### 計算が合わない。。。

takarakuji = {200:1300000, 
              1000: 26000, 
              10000: 1300, 
              100000: 645,
              140000: 130,
              200000: 903,
              1000000: 130,
              10000000: 19,
              40000000: 7}

sum = 0
num = 13000000 #1300万通の宝くじが発行される

for key ,value in takarakuji.items():
    print("key=",key," value=",value)
    sum += key*value

avg = sum / num

print("期待値は",avg)
