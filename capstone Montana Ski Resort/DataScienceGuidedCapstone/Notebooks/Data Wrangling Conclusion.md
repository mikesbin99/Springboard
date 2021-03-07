Loaded Ski Resort Data - Data Wrangling

Question

**Q: 3** Write a summary statement that highlights the key processes and findings from this notebook. This should include information such as the original number of rows in the data, whether our own resort was actually present etc. What columns, if any, have been removed? Any rows? Summarise the reasons why. Were any other issues found? What remedial actions did you take? State where you are in the project. Can you confirm what the target feature is for your desire to predict ticket price? How many rows were left in the data? Hint: this is a great opportunity to reread your notebook, check all cells have been executed in order and from a "blank slate" (restarting the kernel will do this), and that your workflow makes sense and follows a logical pattern. As you do this you can pull out salient information for inclusion in this summary. Thus, this section will provide an important overview of "what" and "why" without having to dive into the "how" or any unproductive or inconclusive steps along the way.

Summary
    
Data exploration phase began with 330 rows of data.  We had no more than 50% of missing data in any one column.  16% of our target variables (either ticket price) were missing.  Since all of the ticket prices by state were varied depending on which state they were in, it was deemed acceptable to ignore the missing 16% of target variables.  

Removed outliers after examining distributions.  Corrected some obvious errors in tabulation of the data.  Shelved the idea of chasing down the missing values and processed what we have.

Determined that we isolate TerrainParks, SkiableTerrain_ac, daysOpenLastYear, NightSkiing_ac as the likely features.  Passed on other features that were related to these, either not as important (ski lift related info) or how many runs (skiable area stronger).

Key features identified, we took approach to find aggregations per state.  We also obtained state metrics to augment our data in the future to provide some relative scaling based on these features.  This was the apporach deemed valuable based off the relative differences between pricing approaches. Two key state features are population and state area which we applied to each aggregation of resort.

We identified that weekday and weekend prices were linearly related, so we chose either of the columns depending on which feature was present.


- Data columns Summary (total 27 columns):
     
     #   Column             Non-Null Count  Dtype     Approach (key features *)
    ---  ------             --------------  -----     --------
     0   Name               330 non-null    object      
     1   Region             330 non-null    object    Suspect and not mutually exclusive
     2   state              330 non-null    object    Suspect and not mutually exclusive  CONCLUSION: IGNORE
     3   summit_elev        330 non-null    int64     Altitude-relatedfeatures CONCLUSION: These are not relevant.
     4   vertical_drop      330 non-null    int64     Altitude-relatedfeatures CONCLUSION: These are not relevant.
     5   base_elev          330 non-null    int64     Altitude-relatedfeatures CONCLUSION: These are not relevant.
     6   trams              330 non-null    int64     Chairlift-related features CONCLUSION: These are not relevant.
     7   fastEight          164 non-null    float64   Missing 50% of the data, not a strong determinant of value CONCLUSION: Drop
     8   fastSixes          330 non-null    int64     Chairlift-related features CONCLUSION: These are not relevant.
     9   fastQuads          330 non-null    int64     Chairlift-related features CONCLUSION: These are not relevant.
     10  quad               330 non-null    int64     Chairlift-related features CONCLUSION: These are not relevant.
     11  triple             330 non-null    int64     Not a focus
     12  double             330 non-null    int64     Not a focus
     13  surface            330 non-null    int64     Not a focus
     14  total_chairs       330 non-null    int64     Chairlift-related features CONCLUSION: These are not relevant.
     15  Runs               326 non-null    float64   Related to total skiing area, not as valuable as a feature
     16  TerrainParks       279 non-null    float64   * Park 'perk', worth keeping
     17  LongestRun_mi      325 non-null    float64   Not a focus
     18  SkiableTerrain_ac  327 non-null    float64   * Park 'perk', worth keeping - related to total area that is usable
     19  Snow Making_ac     284 non-null    float64   Not a focus
     20  daysOpenLastYear   279 non-null    float64   * Feature worth keeping
     21  yearsOpen          329 non-null    float64   Not a focus
     22  averageSnowfall    316 non-null    float64   Not a focus
     23  AdultWeekday       276 non-null    float64   Target Features  Wide range between states
     24  AdultWeekend       279 non-null    float64   Target Features  CONCLUSION: Keep longer column, both are linearlly related 
     25  projectedDaysOpen  283 non-null    float64   Not a focus
     26  NightSkiing_ac     187 non-null    float64   * Park 'perk', worth keeping - skiing at night could be exclusive 
     
- Missing Data    
    count	%
    fastEight	        166	50.303030
    NightSkiing_ac	    143	43.333333
    AdultWeekday	    54	16.363636
    AdultWeekend	    51	15.454545
    daysOpenLastYear	51	15.454545
     
- Target Data
  Our resort was not missing any values.

Exploration
- Started with initial 330 rows
- Examine our resort - no missing data and present
- Counted missing data in our set
-- fastEight missing 166 entries (50% gone)
-- Target quantity missing in 15-16% cases
-- Dropped
    - 
-- Price Distributions for Each State to establish range
   * Difference in somes states range of Weekday and Weekend Prices and some were missing
       * After examining we decide to keep the longer of the two after we realize there's linear relationship
       * Make determination after we examine numerics
           * Found many outliers, dumped those - not going to focus on what is missing


Categorical Exploration
- Examined meanings of Region and State- Are they mutually exclusive?
- Appears to be no encoded values (they are real)
- Found duplicate resort names - some could be a chain

Examined count of Resorts in each state
- Boxplot of states and picked Weekday prices
- New York had the most resorts...how do we pick states to help determine pricing. NY has large population, demand high?

Examine weekend and weekday prices
- Look at averages of resorts by state
- Melted dataframe to Ticket and Price
- Boxplot and determined range was 25 to 100 dollars

Numeric Features
- Dealing with 16% of resorts missing prices
- Examine distributions for numeric features and examine outliers Spot Checking
    * SkiableTerrain_ac because values are clustered down the low end
        - Extreme high values..one is Silverton Mountain.  Assignment says this is a mistake but internet proves otherwise
        - Reset this value, reexamine. Long Tail
    * Snow Making_ac for the same reason
        - Strange values.  Also no ticket data, decided to drop this entry
    * fastEight because all but one value is 0 so it has very little variance, and half the values are missing,
    * fastSixes raises an amber flag; it has more variability, but still mostly 0,
    * trams also may get an amber flag for the same reason,
 
Determine State-Wide Summary Statistics for our Market Segment
    * Focus on TerrainParks (total of terrain parks)
    * SkiableTerrain_ac (Total Skiable Area), 
    * daysOpenLastYear
    * NightSkiing_ac (Night skiing availablity)
    
Named Aggregation to see aggregations on these columns to determine State statistics
    * How many resorts in the state
    * Total Skiable Area in State
    
Numeric quantity related to park density could be beneficial
    
 
Augment with Population Data from Wikipedia
    * Develop summary statistics
    * Correct and clean column names
    
  
Examine relationship between ticket prices
     * Linear relationship
     * Keep the column that had the most entries
     
Conspicuously missing Values - leave these alone