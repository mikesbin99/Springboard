Preprocesing and Training Summary

Keeping in mind that our future work must be at least better than picking something like the average ticket price....

Remove our resort from data since this is the target.

Train / Test Split - chose a 70/30 test split

Keeping baseline model guess in mind (just use the mean!) get that number (63 dollars)

Metrics

Performed R2, Mean Absolute Error, and Mean Squared Error utilized in sklearn metrics


Attempted to impute missing values with median

Scaled units to zero mean and unit variance.
Trained model using linear regression
Assessed model performance with R2, 80% of variance on train set and over 70% on test set.
That gave us ~9 error.

BAsed on error we estimate a ticket price withing 9 dollars of real prices, and lower than the 19 we were using as the average.

Attempted to impute missing data with mean (which were higher)

Moved this operation to sklearn pipeline to simplify code.
    1. Simple Imputation with median (or mean)
    2. Scale our data to zero mean and unit variance
    3. Perform linear regression model
    
Performed predictions and compared to manual method, to confirm we were performing same tasks, which we validated.

Suspect overfitting of the data since we used all. To remedy, used SelectKBest features and rerun pipeline using 10 features. This was worse. Attempt with 15 features.

Attempt Cross validation to remedy
Perform a grid search to determine which is the best value of k
The least variablilty was a value of 8 for k
After using the best estimator attribute, we determine that the vertical_drop feature was best.

We attempt a random forest model within a new pipeline.  We changed imputing strategy, with and without feature scaling

The random forest mimiced the linear model in terms of feature importance
1) fastQuads
2) Runs
3) Snow making capability in acreage
4) Vertical Drop

Potential for increased hyperparameter tuning but we proceed minimizing business cost

The random forest model has lower cross-valdation mean absolute error by a dollar, and has less variablility.

We test this new model with different data sizes to weigh options of collecting more data.  This experiment has shown we have enough data with sample of 40-50

Summary of Summary

**Q: 1** Write a summary of the work in this notebook. Capture the fact that you gained a baseline idea of performance by simply taking the average price and how well that did. Then highlight that you built a linear model and the features that found. Comment on the estimate of its performance from cross-validation and whether its performance on the test split was consistent with this estimate. Also highlight that a random forest regressor was tried, what preprocessing steps were found to be best, and again what its estimated performance via cross-validation was and whether its performance on the test set was consistent with that. State which model you have decided to use going forwards and why. This summary should provide a quick overview for someone wanting to know quickly why the given model was chosen for the next part of the business problem to help guide important business decisions.

Formed a hypothetical minimum-effort base case of a potential model price by taking average of all competing ticket prices.  We determined that was 63 dollars.  This is good to remember before we start attempting models.

We first attempted a linear model, and suspected we overfit.  We did a cross validation to find out which were our best features by adding SelectKBest to our pipeline.  This actually did worse for mean absolute error (9.5, 11.2) vs (8.55, 9.41) vs using all the data (k=10).

Slightly changing k improved the mean absolute error.  Realized we need cross-validation to evaluate our model performance.  Peforming grid search and plotting different k values, we determined that k of 8 provided us our lowest error.  Searching for the features using get_support(), we found that vertical_drop, Snow Making_ac, total_chairs, and fastQuads were best features.  These aligned with our foray into the pair plots and correlations discovered during EDA.

This iterative process of testing features for the linear model was not as efficient as choosing Random Forest Regressor.  This allows us to skip the ad-hoc iteration and skip to a cross validation that will choose the best parameters.  We changed just a few hyperparameters, but more work could be done to fine tune the model given longer project investigation...we kept this simple as a theoretical exercise.

The results of the random forest were consistent with the linear model, that the same 4 features were dominant and should be focus of pricing model. We chose the random forest model due to lower cross-validation error and less variability, which the model error beat the linear regression by 1$.

We assessed whether it would be beneficial to collect more data, but realized the cross validation score did not increase significantly once we reached a sample of 40-50 instances.

We concluded this operation by saving the best model in 'ski_resort_pricing_model.pkl' as a serialized pickle object.

