# Capstone Project for Business Data Management
## IIT Madras Online BS Degree in Data Science and Applications (Diploma Level)
## July 2024
### DEFAULTER ANALYSIS AND CLASSIFICATION for Home Credit

The project focuses on an international non-bank financial company called Home Credit
Group. It provides financial solutions like loans and EMI based payments to both individual
customers and businesses which makes it a B2C as well as a B2B business.

Since the company’s main objective is to provide financial solutions to those who have no or
insufficient credit histories, the major problem which the business faces is to identify potential
defaulters who fail to repay the loan amount either partially or completely. On the other hand,
the loan approval criteria cannot be made too strict as the company may reject loans of valuable
non-defaulter customers.

The issues will be addressed by analyzing the data through different analytical procedures like
data cleaning, identifying important attributes for defaulter classification and tuning a machine
learning model on the data. For the customers that do have some credit history, efforts to
aggregate it and include past data in the analysis will also be made. Tools like MS Excel,
Python and its various libraries will extensively be used for data preprocessing, analysis and
visualization.

The most important features are related to the age of the customer, data from the external
sources which the company maintains, and number of ongoing previous loans. The machine
learning model fails to perform up to the mark due to high class imbalance. The company needs
to make its loan approval process stricter for younger customers.

The data has been collected from a Kaggle Competition called Home Credit Default Risk. The
link for the competition can be accessed here: [Home Credit Default Risk](https://www.kaggle.com/competitions/home-credit-default-risk/data)

The competition data was released by Home Credit Group itself on May 17, 2018.


### File Descriptions

* bureau.ipynb : contains code to aggregate, clean and extract the most important features from the bureau data that show significant trends with the customer repayment behavior.
* cleaning.ipynb : contains code to aggregate, clean and extract the most important features from the main data that show significant trends with the customer repayment behavior.
* credit_card.ipynb : contains code to aggregate, clean and extract the most important features from the credit card data that show significant trends with the customer repayment behavior.
* eda.ipynb final_sub.ipynb : contains some code to produce useful visualizations.
* further_cleaning.ipynb : contains code to further clean the processed data from all sources like imputations and removing highly correlated data.
* instalments.ipynb :  contains code to aggregate, clean and extract the most important features from the instalments data that show significant trends with the customer repayment behavior.
* models.ipynb : contains code to try different macine learning models to classify customers as defaulters or not.
* my_functions.py : contains helper functions for plotting and loading data.
* pos_cash.ipynb : contains code to aggregate, clean and extract the most important features from the point of sale data that show significant trends with the customer repayment behavior.
* prev_app.ipynb : contains code to aggregate, clean and extract the most important features from the previous application data that show significant trends with the customer repayment behavior.

#### `docs/` Directory

* 22f1001864_final.docx : The doc version of the final report
* 22f1001864_final.pdf : The final report submission for the project. Many details related to the methedologies are mentioned in this report.
* 22f1001864_proposal.docx : The doc version of the proposal document.
* 22f1001864_proposal.pdf : The proposal document
* 22f1001864_proposal(un).pdf : The unsigned version of the proposal document

#### `plots/` Directory

Contains the plots and visulaizations of the data analysis.