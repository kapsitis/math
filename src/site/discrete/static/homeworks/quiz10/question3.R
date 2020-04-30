A <- 4
B <- 5
C <- 6
bb1 <- c(1+A, 2+A+B, 3+A+B+C,  4+(2*A+B+C),  5 + 2*A +2*B + C, 6 + 2*A+2*B+2*C)
bb2 <- bb1 %% 16

bb4 <- rep(0,times=16)
for (i in 1:16) {
  if ((i-1) %in% bb2) {
    bb4[i] <- 1
  }
}


