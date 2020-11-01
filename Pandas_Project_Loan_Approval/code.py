# --------------
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
categorical_var.shape
numerical_var.shape
banks = bank.drop('Loan_ID', axis = 1)
print(banks.isnull().sum())
bank_mode = banks.mode()
for x in banks.columns.values:
        banks[x]=banks[x].fillna(value=bank_mode[x].iloc[0])
banks.shape
banks.isnull().sum().values.sum()
avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount', aggfunc=np.mean)
print(avg_loan_amount['LoanAmount'][1])
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].count()
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].count()
Loan_Status = 614
percentage_se = loan_approved_se/Loan_Status * 100
print(percentage_se)
percentage_nse = loan_approved_nse/Loan_Status * 100
print(percentage_nse)
def year_term(Loan_Amount_Term):
    term = Loan_Amount_Term/12
    return term
loan_term = banks['Loan_Amount_Term'].apply(year_term)
big_loan_term = loan_term.loc[lambda x : x>=25].count()
print(big_loan_term)
loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
mean_values.iloc[1,0]


