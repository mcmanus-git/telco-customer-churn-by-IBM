# Project Overview  

This project is part of the
[Holiday Community App-Building Challenge](https://community.plotly.com/t/holiday-community-app-building-challenge/70393)
put on by [Plotly](https://plotly.com/dash/).

The goal of the challenge is to utilize customer churn data provided by IBM to predict customer churn for a fictional 
telecommunication company.  

The winning apps were judged on the following categories:

1. Ability to provide insight on the relationship between churn and customers’ characteristics
2. App Design
3. Data exploration and data analysis routines (e.g. numerical methods, machine learning, prediction, classification, optimization)


# Data  

The [raw data](https://raw.githubusercontent.com/plotly/datasets/master/telco-customer-churn-by-IBM.csv) provided for 
the Plotly App-Building Challenge was provided by 
[IBM](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113).  

## Description  

The dataset provided for the App-Building Challenge is fictitions customer churn data provided by IBM.  

### Column Descriptions  
#### Demographics
**CustomerID**: A unique ID that identifies each customer.  
**Gender**: The customer’s gender: Male, Female  
**Senior Citizen**: Indicates if the customer is 65 or older: Yes, No  
**Partner**: Indicates if the customer is married: Yes, No  
**Dependents**: Indicates if the customer lives with any dependents: Yes, No. Dependents could be children, parents, 
grandparents, etc.  

#### Services
**Tenure in Months**: Indicates the total amount of months that the customer has been with the company by the end of the
quarter specified above.  
**Phone Service**: Indicates if the customer subscribes to home phone service with the company: Yes, No  
**Multiple Lines**: Indicates if the customer subscribes to multiple telephone lines with the company: Yes, No  
**Internet Service**: Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic, 
Cable.  
**Online Security**: Indicates if the customer subscribes to an additional online security service provided by the 
company: Yes, No  
**Online Backup**: Indicates if the customer subscribes to an additional online backup service provided by the company: 
Yes, No  
**Device Protection Plan**: Indicates if the customer subscribes to an additional device protection plan for their 
Internet equipment provided by the company: Yes, No  
**Tech Support**: Indicates if the customer subscribes to an additional technical support plan from the company with 
reduced wait times: Yes, No  
**Streaming TV**: Indicates if the customer uses their Internet service to stream television programing from a third 
party provider: Yes, No. The company does not charge an additional fee for this service.  
**Streaming Movies**: Indicates if the customer uses their Internet service to stream movies from a third party 
provider: Yes, No. The company does not charge an additional fee for this service.  
**Contract**: Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year.  
**Paperless Billing**: Indicates if the customer has chosen paperless billing: Yes, No  
**Payment Method**: Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check  
**Monthly Charge**: Indicates the customer’s current total monthly charge for all their services from the company.  
**Total Charges**: Indicates the customer’s total charges, calculated to the end of the quarter specified above.  

#### Status
**Churn Label**: Yes = the customer left the company this quarter. No = the customer remained with the company. 
Directly related to Churn Value.  


