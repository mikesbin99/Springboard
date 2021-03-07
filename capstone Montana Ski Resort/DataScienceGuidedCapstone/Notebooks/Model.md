**Q: 1** Write a summary of the results of modeling these scenarios. Start by starting the current position; how much does Big Mountain currently charge? What does your modelling suggest for a ticket price that could be supported in the marketplace by Big Mountain's facilities? How would you approach suggesting such a change to the business leadership? Discuss the additional operating cost of the new chair lift per ticket (on the basis of each visitor on average buying 5 day tickets) in the context of raising prices to cover this. For future improvements, state which, if any, of the modeled scenarios you'd recommend for further consideration. Suggest how the business might test, and progress, with any run closures.

Based off model evaluation, we have determined that Big Mountain Resort desired modeled price is $95.87, actual price is $81.00.
Even with the expected mean absolute error of $10.39, this suggests there is room for an increase.

This comes with risk.  First wa are assuming all other resorts use best data science practice in determining their own prices.  This is our best strategy given our dataset.  Second, this assumes raising prices will not alter the ridership.  Third, we are missing more information from other ski resorts.  Do they have the same operating costs and thus a complementatry data science approach at their strategy?

After building the model, we reevaluated our model using all available data with the exception of our own resort.  This is to keep with the original plan and objective of the project, to find an appropriate readjusted ticket price.

Our key features were empirically determined to be the following:
vertical_drop - generally taken from the lift-served point
Snow Making_ac
total_chairs
fastQuads
Runs
LongestRun_mi
trams
SkiableTerrain_ac

These features that we determined help determine ski resort prices.  Based off these features, we believe that we are significantly underpriced the market in relation to the ski resort space.  TThis pricing strategy is not comissurate with our facilities, which we can show are top notch.

We can make snow on large runs with high vertical drop and we have the seats to handle these customers.  We should sieze opportunity to reflect our prices as such.

Unfortunately, we must also propose and analyze potential scenarios for decreasing revenue.  We expect 350k visitors over the course of the season and is used for estimates

Let us examine the 4 scenarios that are proposed for reducing costs and increasing revenue
1) Scenario 1 - Closing down 10 of the least used runs 
    - CONCLUSION - closing runs does not impact the price greatly.  The modeled price does not decrease costs enough to warrant   drop in ticket prices.  The number of runs is a strength and shouldn't be altered.
2) Scenario 2 - Adding a run, increase the vertical drop by 150 feet, and adding a lift
    - CONCLUSION - increases support for ticket price by $1.99, and could amount to $3.46 million increase in revenue
3) Scenario 3 - Repeat Scenario 2 but add 2 acres of snow making
    - CONCLUSION - scenario yields similar results as scenario 2, adding just 2 acres of snow doesn't make difference.  
4) Scenario 4 - Increase longest run by 0.2 miles and adding 4 acres of snow making capability to it
    - CONCLUSION - Makes no difference in the cost model


**Q: 2** What next? Highlight any deficiencies in the data that hampered or limited this work. The only price data in our dataset were ticket prices. You were provided with information about the additional operating cost of the new chair lift, but what other cost information would be useful? Big Mountain was already fairly high on some of the league charts of facilities offered, but why was its modeled price so much higher than its current price? Would this mismatch come as a surprise to the business executives? How would you find out? Assuming the business leaders felt this model was useful, how would the business make use of it? Would you expect them to come to you every time they wanted to test a new combination of parameters in a scenario? We hope you would have better things to do, so how might this model be made available for business analysts to use and explore?

We believe missing revenue, demand, total volume of customers, operating costs, capital assets from other resorts could have provided more insight into the details of ski resort pricing.  We also missed prices of other key features, like hotel stay, gear rental, parking, facility amenities.

The modeled price significantly higher, but we believe we have uncovered why:

- We are currently the highest priced resort in Montana, but near the center based on all resorts in the United States. 
- We are in the upper majority for the most empirically determined feature, the vertical drop.  
- We have one of the highest area covered by snow makers in acreage. This is insurance to the customer that we can provide skiing   opportunity despite weather conditions.  This is why adding snow in small increments have not changed the cost strategy.
- We also rank near the top in amount of chairs available to seat those customers. Our lift technology is in the upper leagues as   well, as we have 3 fast quad lifts..most resorts do not have these.
- We have one of the longest ski runs in the market.  This is why scenario makes no difference-we have the long, high quality runs and adding more does little to the cost model.
- A weaker but less important feature is trams.  We share in the majority of the market as 250 of the 254 resorts queried have no trams either.
- Finally, we have some of the largest skiable are in all sampled markets.

Based off our evidence, we are significantly underpriced based off the quality of our facilities.  We can make this model available to executives in a digestable format via dashboards for your experimentation.
