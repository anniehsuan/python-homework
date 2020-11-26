# Unit 10—A Yen for the Future

## Background

The financial departments of large companies often have to make foreign currency transactions when doing international business, while hedge funds are also interested in anything that will provide an edge in predicting currency movements. Hence, both are always eager to gain a better understanding of the future direction and risk of various currencies. 

In this assignment, you will test the many time series tools that you have learned in order to predict future movements in the value of the Canadian dollar versus the Japanese yen.


1. Time series forecasting
2. Linear regression modelling

- - -

### Files
## Analysis on Jupyter Notebook:

[Time-Series Starter Notebook](time_series_analysis.ipynb)

[Linear Regression Starter Notebook](regression_analysis.ipynb)

## Data Sources:

[CAD/JPY Data CSV File](cad_jpy.csv)

- - -

### Instructions

#### Time-Series Forecasting

Load historical CAD-JPY exchange rate data and apply time series analysis and modelling to determine if there is any predictable behaviour.



1. Plotting the Settle price to check for long or short-term patterns.
   
    * Do you see any patterns, long-term and/or short?

2. Decomposition using a Hodrick-Prescott filter (decompose the settle price into trend and noise).
    
     *  Do you see any patterns, long-term and/or short?

3. Forecasting returns using an ARMA model.
    
    * Based on the p-value, is the model a good fit?

4. Forecasting the exchange rate price using an ARIMA model.
    
    * What does the model forecast will happen to the Japanese Yen in the near term?

5. Forecasting volatility with GARCH.
   
    * What does the model forecast will happen to volatility in the near term?

Use the results of the completed time series analysis and modelling to answer the following questions:

1. Based on your time series analysis, would you buy the yen now?
2. Is the risk of the yen expected to increase or decrease?
3. Based on the model evaluation, would you feel confident in using these models for trading?

#### Linear Regression Forecasting

In this notebook, you will build a Scikit-Learn linear regression model to predict CAD/JPY returns with *lagged* CAD/JPY futures returns and categorical calendar seasonal effects (e.g., day-of-week or week-of-year seasonal effects).

Follow the steps outlined in the regression_analysis starter notebook to complete the following:

1. Data preparation (creating returns and lagged returns, and splitting the data into training and testing data)
2. Fitting a linear regression model.
3. Making predictions using the testing data.
4. Out-of-sample performance.
5. In-sample performance.

Use the results of the linear regression analysis and modelling to answer the following question:

* Does this model perform better or worse on out-of-sample data compared to in-sample data?

- - -
