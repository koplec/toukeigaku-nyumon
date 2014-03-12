# iii)はRで描画する
e1 <- 0.198
s1 <- 0.357

e2 <- 0.055
s2 <- 0.203

rho <- 0.18

x <- seq(0,1,by=0.1)
y1 <- x*e1 + (1-x)*e2
y2 <- (x*s1)^2 + ((1-x)*s2)^2 + 2*x*(1-x)*s1*s2*rho

#グラフ描画 1行2列にまとめて描画する
par(mfrow=c(1,2))
plot(x, y1, type="l", ylab="expect")
plot(x, y2, type="l", ylab="variance")
