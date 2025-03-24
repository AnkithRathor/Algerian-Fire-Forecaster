import streamlit as st


def show_about_page():
    st.markdown(
        """
    # **Table of Contents**
    
    - Introduction
    - Objective
    - Data Collection
    - About the Dataset
    - Python libraries used
    - Project Work flow
        1. Data Exploration
        2. Data Wrangling
        3. Exploratory Data Analysis
        4. Model Building
        5. Prediction
    - Limitations
    - Conclusion

    ## **Introduction**

    * 'Algerian Fire Forecaster' - A cutting-edge project leveraging Machine Learning and Python to predict wildfire risks in Algeria.
    * This project analyzes key factors like Temperature, Relative Humidity, Wind speed, Rain level,Fine Fuel Moisture Code, Duff Moisture Code, Drought Code, Initial Spread Index, Buildup Index and predicts Fire Weather Index.
    * By fusing meteorological data with machine learning, this project aims to provide timely insights for effective firefighting and emergency response, offering a proactive approach to wildfire management in Algeria.

    ## **Objective** 

    * The objective of this project is to utilize Python and machine learning techniques for predicting the Fire Weather Index (FWI) in different locations across Algeria.

    ## **Data Collection**

    * The data for this project was collected from Kaggle, a popular platform for data science competitions and datasets.
    * Check out the raw dataset [here](https://github.com/AnkithRathor/Algerian-Fire-Forecaster/blob/main/data/raw_data/Algerian_forest_fires_dataset_UPDATE.csv)
    * Check out the cleaned dataset [here](https://github.com/AnkithRathor/Algerian-Fire-Forecaster/blob/main/data/cleaned_data/Algerian_forest_fires_dataset_cleaned.csv)

    ## **About the Dataset**

    ### Data Set Information:
    - The dataset includes 244 instances that regroup a data of two regions of Algeria,namely the Bejaia region located in the northeast of Algeria and the Sidi Bel-abbes region located in the northwest of Algeria.

    - 122 instances for each region.

    - The period from June 2012 to September 2012. The dataset includes 11 attribues and 1 output attribue (class) The 244 instances have been classified into fire(138 classes) and not fire (106 classes) classes.

    ### Attribute Information:

    - Date : (DD/MM/YYYY) Day, month ('june' to 'september'), year (2012)

    Weather data observations:

    * Temp : temperature noon (temperature max) in Celsius degrees: 22 to 42
    * RH : Relative Humidity in %: 21 to 90
    * Ws :Wind speed in km/h: 6 to 29
    * Rain: total day in mm: 0 to 16.8 FWI Components
    * Fine Fuel Moisture Code (FFMC) index from the FWI system: 28.6 to 92.5
    * Duff Moisture Code (DMC) index from the FWI system: 1.1 to 65.9
    * Drought Code (DC) index from the FWI system: 7 to 220.4
    * Initial Spread Index (ISI) index from the FWI system: 0 to 18.5
    * Buildup Index (BUI) index from the FWI system: 1.1 to 68
    * Fire Weather Index (FWI) Index: 0 to 31.1
    * Classes: two classes, namely Fire and not Fire


    ## **Libraries Used:**

    Employed the following libraries for comprehensive data analysis:

    * **Pandas** for versatile data manipulation.
    * **NumPy** for efficient numerical operations.
    * Leveraged **Scikit-Learn** for machine learning tasks and predictive modeling.
    * Utilized **Matplotlib.Pyplot** and **Seaborn** for creating insightful visualizations.
    * Integrated **Regex** for advanced text pattern matching.

    ## **Project Work flow**

    **1. Data Exploration**
    - Dive into an in-depth exploration of the dataset to gain insights into its structure, features, and distributions.

    **2. Data Wrangling**
    - Perform data cleaning, handle missing values, and transform the data into a suitable format for analysis.

    **3. Exploratory Data Analysis**
    - Conduct EDA to uncover patterns, trends, and relationships within the data using visualizations and statistical analyses.

    **4. Model Building**
    
    - Feature Selection Based on Correlation:
        - Identify and select relevant features by assessing their correlation with the target variable.    
    - Feature Scaling or Standardization:
        - Normalize features to a consistent scale, ensuring fair comparisons between them.
    - Linear Regression:
        - Implement linear regression as a baseline model to understand the basic relationships between variables.
    - Lasso Regression:
        - Introduce Lasso regression to enhance feature selection and mitigate overfitting.
    - Ridge Regression:
        - Employ Ridge regression to address multicollinearity and stabilize model performance.
    - ElasticNet Regression:
        - Combine L1 and L2 regularization using ElasticNet to benefit from both variable selection and regularization.

    **5. Prediction**
    - Leverage the trained models to make predictions on new data, assessing their performance and reliability.


    ## Limitations
    * The model was trained exclusively using data from the 'Bejaia' and 'Sidi-Bel Abbes' Regions.
    * The training dataset spans from June 2012 to September 2012.
    * Exclusion of 'Drought Code (DC)' and 'Buildup Index (BUI)' input values is recommended due to their high correlation with 'Duff Moisture Code (DMC).'
    * The training prioritizes region-specific insights, focusing on the unique characteristics of 'Bejaia' and 'Sidi-Bel Abbes' during the specified time period.

    ## **Conclusion**

    * In conclusion, the 'Algerian_Fire_Forecaster' project successfully utilized Python and machine learning techniques to predict the Fire Weather Index (FWI) for locations in Algeria.
    * By employing temperature, relative humidity (rh), wind speed (ws), rainfall (rain), Fine Fuel Moisture Code (FFMC), Duff Moisture Code (DMC), Initial Spread Index (ISI), fire classes, and regional parameters as input features, our model demonstrated the ability to assess the potential fire danger.
    * This project leverages the power of machine learning to enhance our understanding of fire weather dynamics in Algeria, ultimately contributing to more effective wildfire risk management strategies in the region.

  """
    )
