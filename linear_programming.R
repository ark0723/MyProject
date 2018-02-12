#4-3

library(linprog)
cvec=c(18,29,25)
bvec=c(1500,600,-1000,-200,-400)
amat=matrix(c(0.5,0.2,0.75,0.2,0.4,0.2,-1,0,0,0,-1,0,0,0,-1),ncol=3,byrow=TRUE)
solveLP(cvec,bvec,amat,maximum=T)

#4-4
library(linprog)
cvec=c(29000,21000,13000,-14000,-6000,2000)
bvec=c(-10,-40,-35)
amat=matrix(c(-1,0,0,1,0,0,-1,-1,0,1,1,0,-1,-1,-1,1,1,1),ncol=6,byrow=TRUE)
solveLP(cvec,bvec,amat,maximum=F)

920000+480000