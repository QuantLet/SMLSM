import pandas as pd

#This code produces the descriptive table and correlation matrix from the master thesis "Supervised Machine Learning Sentiment Measures"
#File data_whole_AAPL2016.csv can be used to test the code. For actual table from thesis, download the data set from the Blockchain Research Center 
#and use the other code in this quantlet to estimate the sentiment measures. Overall table structure based on Frankel, Jennings and Lee (2021).

#Read data 
data = pd.read_csv("DATA FILE PATH")

#Get descriptive statistics of variables used in panel data regression
data_des = data[["r_{ab}","NASDAQ", "TURNOVER", "log(SIZE)", "BTM", "PREFALPHA", "HIV4 TONE", "LM TONE", "r_{ab} RF12", "r_{ab} RFFin", "r_{ab} FinNN"]]
des_table = data_des.describe().loc[["mean", "std", "25%", "50%", "75%"]]
print(des_table)

#Get correlation matrix of sentiment measures 
data_full_cor = data_full[["HIV4 TONE", "LM TONE", "r_{ab} RF12", "r_{ab} RFFin", "r_{ab} FinNN"]]
corr_matrix = data_full_cor.corr()
print(corr_matrix)

#References
#Blockchain Research Center, https://blockchain-research-center.com/
#Frankel, R., Jennings, J., and Lee, J. (2021). Disclosure sentiment: Machine learning vs. dictionary methods. Management Science
