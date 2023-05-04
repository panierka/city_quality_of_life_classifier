# Fuzzy classifier of the life quality in cities

Fuzzy classifier implemented from scratch that creates quality of life prediction in the city based on input - observation with assessment of 
many aspects of life in given city. 

Entire classification task is logically divided on a few steps:
- initial configuration - defining antecedents (categories of variables and specific functions with typical arguments for each category),
                          consequents (categories of final classification and function with typical arguments for each category),
                          rules (system of principles that make a lingustic decision based on input features in the linguistic form),
- fuzzification - for each category for every attribute we define membership functions, which are later calculated at points taken from input vector. 
                  The category with highest function value is chosen. Result of fuzzification is the vector of linguistic values, each corresponding to the 
                  different attribute,
- inference - those maximal function values are used to calculate level of every rule's fulfillment (here Norms should be used as a way of interpreting logical
              operations on logistic values in terms of numerical ones). In fact, to every possible linguistic value of outcome corresponds its highest
              activated rule value, which is numerical interpretation of rule's logical operation,
- defuzzification - creation of the single function that combines all membership functions and maximas of their rule activation results. Selected defuzzification
                    method, based on this function's set of values, generates the final outcome.
                    
After finishing constructing fuzzy classifier, other algorithms were implementated to compare the quality of classification with accuracy and precision rates
(KNN, Naive Bayes, Softset).

## Details of the most interesting parts of the system:

Inference's system of rules - essence of the designing appropriate system of rules was to divide complete set of 12 features into 2 groups: essentials and
non-essentials. Some of the life aspects are just more important than others and impact the life by far more. 5 qualities was selected as essentials (Housing, 
Cost of Living, Safety, Healthcare, Travel Connectivity). System was characterized by 3 main principles:
1) at least 3 essential qualities are on the certain level -> final verdict should be on this level,
2) 2 essential and at least 2 non-essential qualities are on the certain level -> final verdict should be on this level,
3) 1 essential and at least 5 non-essential qualities are on the certain level -> final verdict should be on this level.

Data were obtained from Kaggle.

## Used Norms:
- Manger's Norm,
- Zadeh's Norm,
- Łukasiewicz's Norm.

## Applied membership functions:
- triangular, 
- trapezoidal.

## Defuzzification methods:
- First of Maxima,
- Middle of Maxima,
- Last of Maxima,
- centroid middle of area.

## Team:
- [panierka](https://github.com/panierka) - fuzzification, inference and defuzzification layers
- [jdylik](https://github.com/jdylik) - KNN, Naive Bayes, Softset implementations, system of rules design
