# Home Credit Group's Default Risk Prediction [@kaggle] (https://www.github.com/kaggle) Competition

## How capable of repaying a loan is each applicant?

---

### Description

Many people struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately, this population is often taken advantage of by untrustworthy lenders.

![Home Credit Group](https://storage.googleapis.com/kaggle-media/competitions/home-credit/about-us-home-credit.jpg)

[Home Credit](http://www.homecredit.net/) strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience, Home Credit makes use of a variety of alternative data--including telco and transactional information--to predict their clients' repayment abilities.

While Home Credit is currently using various statistical and machine learning methods to make these predictions, they're challenging Kagglers to help them unlock the full potential of their data. Doing so will ensure that clients capable of repayment are not rejected and that loans are given with a principal, maturity, and repayment calendar that will empower their clients to be successful.

### Evaluation

For this project, submissions were evaluated on [area under the ROC curve](http://en.wikipedia.org/wiki/Receiver_operating_characteristic) between the predicted probability and the observed target.

#### ROC curve calculation

The receiver operating characteristic (ROC) curve is a plot of the *true positive rate (TPR)* __against__ the *false positive rate (FPR)* at various threshold settings

$$ TPR = f(FPR)$$

where:

$$ TPR = \frac{TruePositives}{TruePositives + FalseNegatives}$$

$$ FPR = \frac{FalsePositives}{TrueNegatives + FalsePositives}$$

The area under the ROC curve (AUC for short) reduces the ROC curve to a single value, which represents the expected performance of the classifier. An AUC close to 1 indicates a good classifier.


# Dataset Description

| ***application\_{train\|test}** | ***bureau** | ***bureau\_balance** | ***credit\_card\_balance** | ***HomeCredit\_columns\_description** | ***installments\_payments** | ***POS\_CASH\_balance** | ***previous\_application** |
|---|---|---|---|---|---|---|---|
| * This is the main table, broken into two files for Train (with TARGET) and Test (without TARGET). | * All client's previous credits provided by other financial institutions that were reported to Credit Bureau (for clients who have a loan in our sample). | * Monthly balances of previous credits in Credit Bureau. | * Monthly balance snapshots of previous credit cards that the applicant has with Home Credit. | * This file contains descriptions for the columns in the various data files. | * Repayment history for the previously disbursed credits in Home Credit related to the loans in our sample. | * Monthly balance snapshots of previous POS (point of sales) and cash loans that the applicant had with Home Credit. | * All previous applications for Home Credit loans of clients who have loans in our sample. |
| * Static data for all applications. One row represents one loan in our data sample. | * For every loan in our sample, there are as many rows as number of credits the client had in Credit Bureau before the application date. | * This table has one row for each month of history of every previous credit reported to Credit Bureau – i.e the table has (#loans in sample \* # of relative previous credits \* # of months where we have some history observable for the previous credits) rows. | * This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample \* # of relative previous credit cards \* # of months where we have some history observable for the previous credit card) rows. |  | * There is a. one row for every payment that was made plus b. one row each for missed payment. | * This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample \* # of relative previous credits \* # of months in which we have some history observable for the previous credits) rows. | * There is one row for each previous application related to loans in our data sample. |
|  |  |  |  |  | * One row is equivalent to one payment of one installment OR one installment corresponding to one payment of one previous Home Credit credit related to loans in our sample. |  |  |

```mermaid
---
title: Dataset Setup
---

    style bureau stroke:#0f0
    style bureau_balance stroke:#0f0
    style previous_application stroke:#f00
    style POS_CASH_balance stroke:#fcfc58
    style installments_payments stroke:#fcfc58
    style credit_card_balance stroke:#fcfc58

erDiagram
    "application_{train|test}" {
        int SK_ID_CURR PK
    }
    bureau {
        int SK_ID_BUREAU PK
        int SK_ID_CURR FK
    }
    previous_application {
        int SK_ID_PREV PK
        int SK_ID_CURR FK
    }
    bureau_balance {
        int SK_ID_BUREAU FK "CPK"
        int MONTHS "CPK"
    }
    POS_CASH_balance {
        int SK_ID_PREV FK "CPK"
        int SK_ID_CURR FK "CPK"
        int MONTHS_BALANCE "CPK"
    }
    installments_payments {
        int SK_ID_PREV FK "CPK"
        int SK_ID_CURR FK "CPK"
        int NUM_INSTALMENT_NUMBER "CPK"
    }
    credit_card_balance {
        int SK_ID_PREV FK "CPK"
        int SK_ID_CURR FK "CPK" 
        int MONTHS_BALANCE "CPK"
    }



    "application_{train|test}" ||--o{ bureau : "SK_ID_CURR"
    "application_{train|test}" ||--o{ previous_application : "SK_ID_CURR"
    bureau ||--o{ bureau_balance : "SK_ID_BUREAU"
    previous_application ||--o{ POS_CASH_balance: "SK_ID_PREV"
    previous_application ||--o{ installments_payments : "SK_ID_PREV"
    previous_application ||--o{ credit_card_balance : "SK_ID_PREV"
```

### Citation

Anna Montoya, inversion, KirillOdintsov, and Martin Kotek. Home Credit Default Risk. https://kaggle.com/competitions/home-credit-default-risk, 2018. Kaggle.
