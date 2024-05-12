## Global Warming in Miami — Temperature Modeling and Predictions

By: Shirsho Dasgupta (2022)

The code reads daily temperature — minimum, maximum, mean, dewpoint temperatures — for Miami-Dade County from 1983 to 2022. It then calls a pre-defined module to compute the heat index — a measure of what the temperature "feels like" for each of the days.
Finally, it counts the number of days above certain heat index thresholds — which would make it a health risk for humans to be exposed to the sun for prolonged periods. Read about the thresholds here. 

The code also aims to predict the daily temperatures into 2053. 
To do this three time series predictive models were first tested: Prophet, Neural Prophet and Holtz-Winter model. The second Neural Prophet model was found to have the least error-margins among the three. A separate block of code then tested for the best parameters for the model to implement. The mean and dewpoint temperatures for future dates were calculated after deploying Neural Prophet with the best parameters. Finally, using the predicted values, the heat indices for those future dates were also computed/predicted. 


#### Notes and Observations:

1. This code can only be used for stories where the focus is on rising summer temperatures (and not stories about winter months) becauses while these models' predictions are more or less within error-margins for the summer months, none of the models were able to properly account for the variations in daily temperatures in winter.
2. It is better to restrict predictions to 3-5 years using these models — the more into the future the model went, the more the predictions became dependent on prior predictions, magnifying error margins. 
