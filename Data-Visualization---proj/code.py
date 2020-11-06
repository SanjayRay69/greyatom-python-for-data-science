# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status = data['Loan_Status'].value_counts()

#Creating a new variable to store the value counts
loan_status.plot(kind = 'bar')
plt.xlabel("Status of Loan Approval")
plt.ylabel("Total Count of Loans")
plt.title("Loan Approved/Not Approved Chart")
#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind = 'bar', stacked = False, figsize=(15,10))
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation = 45)
plt.title("Property Area Vs Loan Status chart")
plt.show()


#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind = 'bar', stacked = True, figsize = (15, 10))

plt.title("Education Vs. Loan Approval Status Chart")
#Changing the x-axis label
plt.xlabel("Education Status")
#Changing the y-axis label
plt.ylabel("Loan Status")
#Rotating the ticks of X-axis
plt.xticks(rotation = 45)
plt.show()
# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density', label='Graduate')
plt.show()
#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')
plt.show()
#For automatic legend display
plt.legend(loc = 'best')

# Step 5
#Setting up the subplots
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3, ncols = 1, figsize = (10, 5))
#Plotting scatter plot
data.plot.scatter('ApplicantIncome', 'LoanAmount', ax = ax_1)
#Setting the subplot axis title
ax_1.set_title("Applicant Income")

#Plotting scatter plot
data.plot.scatter('CoapplicantIncome', 'LoanAmount', ax = ax_2)

#Setting the subplot axis title
ax_2.set_title("Coapplicant Income")

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot.scatter('TotalIncome', 'LoanAmount', ax = ax_3)
ax_3.set_title("Total Income")
#Plotting scatter plot
plt.show()


#Setting the subplot axis title



