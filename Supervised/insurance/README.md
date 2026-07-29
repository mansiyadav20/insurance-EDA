# Insurance Dataset Analysis (EDA + Preprocessing)

##  Overview
This project focuses on performing "Exploratory Data Analysis (EDA)" and "data preprocessing" on an insurance dataset.  
The goal is to understand the data, extract insights, and prepare it for machine learning models.


## Dataset Information
The dataset contains the following features:

- **age**: Age of the individual  
- **sex**: Gender (male/female)  
- **bmi**: Body Mass Index  
- **children**: Number of dependents  
- **smoker**: Smoking status  
- **region**: Residential area  
- **charges**: Medical insurance cost (Target Variable)


##  Exploratory Data Analysis (EDA)

The following steps were performed:

## Basic Data Inspection
 Used "head()" and "tail()" to view data
 Used "info()" to check data types and null values
 Used "describe()" to understand statistical summary(like mean median or sd)

### Data Visualization
- **Histogram with KDE**
  - To understand distribution of numerical features
  - KDE (Kernel Density Estimation) smooths the distribution curve

- **Boxplot**
  - Used to detect outliers in the dataset

- **Count Plot**
  - Used to analyze frequency of categorical variables  
  (e.g., number of males vs females)

- **Heatmap (Correlation Matrix)**
  - Used to understand relationships between numerical features


##  Data Cleaning

- Created a copy of dataset using "copy()" to preserve original data
- Removed duplicate rows using `drop_duplicates()`

###  Encoding Categorical Variables
- **One-Hot Encoding**
  - Converted categorical columns into multiple binary (dummy) columns

- **Label Encoding**
  - Converted categorical values into numerical form (0, 1, etc.)

##  Feature Engineering

- Created new features to improve model performance
- Goal: Help the model understand patterns more effectively

##  Feature Scaling

To ensure all features are on the same scale:

###  Methods Used:
- Normalization
- Standardization

###  Standardization Formula:
\[
X = \frac{X - \mu}{\sigma}
\]

- `fit()` calculates mean (μ) and standard deviation (σ)
- `transform()` applies scaling to each value

 This prevents the model from being biased toward features with larger values


##  Feature Selection

- Identified important features affecting the target variable (**charges**)

###  Pearson Correlation (using scipy)
- Found that **smoker** has the highest correlation (~0.78) with charges


## Statistical Testing

###  Chi-Square Test
- Used to analyze relationships between categorical variables
- Helps determine dependency between features



## Key Insights

- Smoking significantly increases insurance charges
- BMI and age also impact medical costs
- Some features have weaker influence on the target variable


##  Tools & Libraries

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scipy  


##  How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/mansiyadav20/insurance-EDA.git
2. Open the project in VS Code / Jupyter Notebook
3. Run the notebook step-by-step