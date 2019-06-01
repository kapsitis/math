ff <- function(n) {
  return (n + (-7*n + 3)/(n^2 + 7))
}

xx <- seq(0, 12, by=0.1)
yy <- ff(xx)

plot(xx,yy, type="l", col="red")
points(xx,xx, type="l", col="blue")
grid()
