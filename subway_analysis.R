# Load subway.csv file to a data frame
# Use read.table
getwd()
setwd('C:/Users/User/Downloads/subway')
df=read.table('subway.csv',sep=',',header=T, fileEncoding = 'utf8')

# (a) What is the average number of passengers of Sinchon station?
# The number should be stored in the variable 'ans_a'.
Line2Shin=subset(df, line=='2호선'&station_name=='신촌') 
Line2Shin
ans_a <- sum(Line2Shin[,4],Line2Shin[,5])/nrow(Line2Shin)
ans_a

# (b) Find top 10 subway stations in terms of the avg. number of passengers.
# The list of top 10 subway stations should be stored in the variable 'ans_b'.
# (Hint: you may use sort function like the following codes)
t <- c(1, 3, 2, 5, 4)
s <- sort(t, decreasing = T)
s

total<-rowSums(df[,4:5])
df_total<-cbind(df,total)
head(df_total)
install.packages('doBy')
library(doBy)
avg_passenger=summaryBy(total~station_name, df_total, FUN=mean)
shin2=subset(df_total, station_name=='신촌' & line=='2호선')
shinK=subset(df_total, station_name=='신촌' & line=='경의선')
yang5=subset(df_total, station_name=='양평'& line=='5호선')
yangJ=subset(df_total, station_name=='양평'& line=='중앙선')
head(shin2)
sum(shin2[,4],shin2[,5])/nrow(shin2)
sum(shinK[,4],shinK[,5])/nrow(shinK)
sum(yang5[,4],yang5[,5])/nrow(yang5)
sum(yangJ[,4],yangJ[,5])/nrow(yangJ)
location=c(which(avg_passenger$station_name=='신촌'|avg_passenger$station_name=='양평'))
avg_passenger=avg_passenger[-location,]
avg_passenger$station_name=as.character(avg_passenger$station_name)
avgshin2=c('신촌',sum(shin2[,6])/nrow(shin2))
avgshinK=c('신촌',sum(shinK[,6])/nrow(shinK))
avgyangJ=c('양평',sum(yangJ[,6])/nrow(yangJ))
avgyang5=c('양평',sum(yang5[,6])/nrow(yang5))
avg_passenger<-rbind(avg_passenger,avgshin2,avgshinK,avgyang5,avgyangJ)
str(avg_passenger)
avg_passenger$total.mean=as.numeric(avg_passenger$total.mean)
passenger=order(avg_passenger$total.mean,decreasing=T)
ans_b=head(avg_passenger[passenger,],10)
ans_b

# (c) Find top 3 subway lines in terms of the average number of passengers.
# The list of top 3 subway lines should be stored in the variable 'ans_c'.
head(df_total)
df_line=aggregate(total~line,df_total,FUN=mean)
avgline=df_line[order(df_line$total,decreasing=T),]
ans_c=avgline[1:3,]
ans_c
# (d) Draw scatter plots for the number of passengers of Nakseongdae station and Incheon Int'l Airport station.
Naksung=subset(df_total,station_name=='낙성대')
head(Naksung)
Naksung_passenger=Naksung[,c(1,6)]
Incheon=subset(df_total, station_name=='인천국제공항')
Incheon_passenger=Incheon[,c(1,6)]
head(Incheon_passenger)
par(mfrow=c(2,1))
plot(Naksung_passenger)
plot(Incheon_passenger)
