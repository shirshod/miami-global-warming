## Global Warming in Miami — Temperature Modeling and Predictions

By: Shirsho Dasgupta (2022)

The code reads daily temperature — minimum, maximum, mean, dewpoint temperatures — for Miami-Dade County from 1983 to 2022. It then calls a pre-defined module to compute the heat index — a measure of what the temperature "feels like" for each of the days.
Finally, it counts the number of days above certain heat index thresholds — which would make it a health risk for humans to be exposed to the sun for prolonged periods. Read about the thresholds here. 

The code also aims to predict the daily temperatures into 2053. To do this three time series predictive models were first tested: Prophet, Neural Prophet and Holtz-Winter model. The second Neural Prophet model was found to have the least error-margins among the three. 


#### Notes and Observations:

1. None of the models were able to properly account for the variations in daily temperatures in winter.
2. It is better to restrict predictions to 3-5 years using these models — the more into the future the model went, the more the predictions became dependent on prior predictions, magnifying error margins. 
