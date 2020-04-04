a <- 10
b <- 4
c <- 12
m <- 8

res1 <- (a*c - b*c) %% m
res2 <- (a - b) %% m 
print(sprintf("res.A = (%d,%d)", res1, res2))





a <- 4
b <- 2
c <- 7
d <- 5
m <- 3

res1 <- (a - c) %% m
res1A <- (a -b) %% m
res2 <- (c - d) %% (m-1)
res3 <- (a^c - b^d) %% m
print(sprintf("res.B = (%d[%d],%d,%d)", res1, res1A, res2,res3))