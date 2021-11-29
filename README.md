# Classification_Project



## Project Objectives
- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook Final Report.

- Create modules (acquire.py, prepare.py) that make your process repeateable and your report (notebook) easier to read and follow.

- Ask exploratory questions of your data that will help you understand more about the attributes and drivers of customers churning. Answer questions through charts and statistical tests.

- Construct a model to predict customer churn using classification techniques, and make predictions for a group of customers.

- Refine your work into a Report, in the form of a jupyter notebook, that you will walk through in a 5 minute presentation to a group of collegues and managers about the work you did, why, goals, what you found, your methdologies, and your conclusions.

- Be prepared to answer panel questions about your code, process, findings and key takeaways, and model.

## Business Goals
- Find drivers for customer churn at Telco. Why are customers churning?

- Construct a ML classification model that accurately predicts customer churn.

- Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?

# Audience
-Your target audience for your notebook walkthrough is your direct manager and their manager. This should guide your language and level of explanations in your walkthrough.

# Deliverables
- Jupyter Notebook Report
- README.md file containing the project information
- CSV file with customer_id, probability of churn, and prediction of churn
- Acquire and prepare files
- Notebook walkthrough presentation
<hr style="border:2px solid black"> </hr>

<hr style="border:2px solid black"> </hr>


# Key Findings:

### The customer churn rate is the highest within the 6 months of tenure

### Month to month customers serve as the highest churn rate for services
  - We want to maintain this service so we dug deeper into the customers data

### Fiber customers are more likely to churn than DSL 

### Customers who use manual payments are more likely to churn than automatic payments


<hr style="border:2px solid black"> </hr>

# Hypothesis Testing:

### Created 3 chi^2 hypothesis tests

#### Hypothesis 1: Determine if there is a relationship between DSL and churn
  - There is a relationship between DSL and churn
  
#### Hypothesis 2: Determine if there is a relationship between Fiber Optic and churn
  - There is a relationship between Fiber and churn

#### Hypothesis 3: Determine if there is a relationship between payment type and churn
  - There is a relationship between manual payments and churn

### Takeaways: We tested and graphed our data analysis


<hr style="border:2px solid black"> </hr>

# Modeling:

### Created 4 modeling tests: (Decision Tree, Random Forest, 2x Linear Regression)
 - All tested above our baseline prediction model
 - We used the features : 'payment_type', 'month_to_month', 'partner', 'dependents', 'senior_citizen' in our model
 - These were used in a Decision Tree and Random Forest testing model
 - For Linear Regression we substituted 'payment_type' with DSL for one model and fiber for the other
 - Our Linear Regression fiber model trained the best and used it to test our data with improved accuracy

<hr style="border:2px solid black"> </hr>

# Project Takeaways:

### We were able to create a model that predicted a 76.7% chance whether or not a customer would churn based on a few features
### Our data dived into causes for churn such as DSL vs Fiber and manual vs automatic payments
### With this information we now have a strong model to use for the company and have better categorized customers to help reduce the churn rate


<hr style="border:2px solid black"> </hr>
## Data Dictionary 

## Project Specifications
- Plan
- Acquire
- Prepare
- Explore
- Model Evaluate

## Conclusion


# Data Dictionary
| Feature                    | Datatype               | Description                                                           |
|:---------------------------|:-----------------------|:----------------------------------------------------------------------|
| customer_id                | 7043 non-null: object  | Identification number for customer                 |
| gender                     | 7043 non-null: object  | Customer gender, male or female                    |
| senior_citizen             | 7043 non-null: int64   | Yes or No, is the customer a senior citizen        |
| partner                    | 7043 non-null: object  | Yes or No, does the customer customer has a parter |
| dependents                 | 7043 non-null: object  | Number of dependents a customer has                |
| tenure                     | 7043 non-null: int64   | Months a customer has been with the company        |
| phone_service              | 7043 non-null: object  | Phone Service plan, Yes or No                      |
| multiple_lines             | 7043 non-null: object  | Multiple lines, Yes or No                          |
| internet_service_type_id   | 7043 non-null: int64   | 1, 2, 3                                            |
| online_security            | 7043 non-null: object  | Yes, no, or no internet service                    |
| online_backup              | 7043 non-null: object  | Yes, no, or no internet service                    |
| device_protection          | 7043 non-null: object  | Yes, no, or no internet service                    |
| tech_support               | 7043 non-null: object  | Yes, no, or no internet service                    |
| streaming_tv               | 7043 non-null: object  | Yes, no, or no internet service                    |
| streaming_movies           | 7043 non-null: object  | Yes, no, or no internet service                    |
| contract_type_id           | 7043 non-null: int64   | 1, 2, 3                                            |
| paperless_billing          | 7043 non-null: object  | Yes or no, customer uses paperless billing         |
| payment_type_id            | 7043 non-null: int64   | 1, 2, 3, 4                                         |
| monthly_charges            | 7043 non-null: float64 | Monthly charges the customer pays                  |
| total_charges              | 7043 non-null: object  | Total charges the customer has paid                |
| churn                      | 7043 non-null: object  | Yes or no, whether or not the customer has churned |
| contract_type_id.1         | 7043 non-null: int64   | 1, 2, 3                                            |
| contract_type              | 7043 non-null: object  | Month-to-month, One year, Two year                 |
| internet_service_type_id.1 | 7043 non-null: int64   | 1, 2, 3                                            |
| internet_service_type      | 7043 non-null: object  | DSL, Fiber Optic, or None                          |
| payment_type_id.1          | 7043 non-null: int64   | 1, 2, 3, 4                                         |
| payment_type               | 7043 non-null: object  | E-check, mailed check, bank transfer, credit card  |
