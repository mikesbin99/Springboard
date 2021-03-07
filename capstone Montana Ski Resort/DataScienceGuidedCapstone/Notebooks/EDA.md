

**Q: 1** Write a summary of the exploratory data analysis above. 

We reloaded the artifacts from the Data Wrangling Exercise, 'ski_data_cleaned' and 'state_summary'

What numerical or categorical features were in the data? 

We examined state area, population, total skiable area, night skiing area, and resorts per state to get a better understanding of the ski resort markets.  Who should we compare ourselves with?

State Area - Montana ranks third
State Population - Near bottom in population
Resorts per state - Don't rank in the top 5
Skiiable Area - In the top 5
Night Skiing Area - Not in the top 5. What is the nature of this feature?
Days Open per year - not in top 5

Montana is a niche because of its large size, large skiiable areas, but not very populated.  Density determined as a useful metric to scale the competition so the approach was to derive these features.

Calculated resorts per 100k capita and per 100k square miles which allowed us to removed total population and size to better scale differences between states.  The distributions of these population and densities were examined and simllar, both containing long tails.  

The density metric for population per resort was high for Montana, but the density in state size remained low due to size of Montana.

The next focus was reducing the dimensionality of the data, and PCA was performed,  This only works with numeric data, so we moved the states to the label column to prevent from having to encode them.  We want to focus on the primary features from 7 dimensions.  We first scaled the data down to prevent skewed results.  This removed the labels so we stuck the columns back onto the scaled DataFrame.  We validated the scaling to ensure the process happened correctly.

Looking at the variance ratio, over 95% of the variability is explained in the first two components.

-Was there any pattern suggested of a relationship between state and ticket price? 

The relationship between state and ticket price was tough to understand after recombining the two principle component columns and arranging them into quartiles.  After switching to seaborn to simplify the visualization, still no clear grouping.  We understand what features to keep, but it is clear we need more features to separate the states from one another.

We merged the data back together, and computed the following features:
* ratio of resort skiable area to total state skiable area
* ratio of resort days open to total state days open
* ratio of resort terrain park count to total state terrain park count
* ratio of resort night skiing area to total state night skiing area

We dropped original quantities that created these ratios.  Armed with relative scaled features, we look at a correlation heatmap and identify potential correlations between ticket prices and features.  Night skiing, snow making equipment, total chairs, and vertical drop were correlated to ticket prices.  Correlation does not tell the entire story, so we created matrix of scatterplots to determine if there were any relationships.

Because of the relationship between numbers of chairs and runs to prices, the ratio between chairs of runs might be beneficial.  This is an index of how people can traverse the resort and get skiing quickly.

What did this lead us to decide regarding which features to use in subsequent modeling? What aspects of the data (e.g. relationships between features) should you remain wary of when you come to perform feature selection for modeling? 

At the conclusion of the EDA we saved our new features to .csv.



