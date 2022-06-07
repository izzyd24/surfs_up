# surfs_up
This project explores data storage and retrieval via the following tools: 
Python SQL toolkit (SQLAlchemy), Object Relational Mapper, pandas, numpy, SQLlite, Python 3.9.2, Flask, Jupyter Notebook
## Intent
Produce an analyis of temperature trends in Oahu, Hawaii. Specifically, summary statistics of temperature data were requested for the months of June and December, and then determine if an ice-cream shop would be a model that can be sustained around the year. 
## Results Deliverable 1
Determine the Summary Statistics for June

## Results Deliverable 2
Determine the Summary Statistics for December 

## Key Differences and Suggestions
1. The average temperature in June is about 74-75 degrees or about 4 degrees higher than average temperature from December. 
Suggestion: If we see a decrease in temperature by nearly 5% from June to December, we recommend to expand the summary stats to all months of the year to ensure there are no outlier/close shop scenarios. 
2. June temperatures have a normal bell curve, and December seems to have more variability. 
Suggestion: Map out via Matplotlib library for each month, and compare the distribution curves. We ideally want to see a tight curve with a normal distribution, and an emphasis on small stdevs to ensure we can forecast demand according to weather temperatures. 
Broader Suggestion: Review other important variables that are correlated with optimal beach and surfing weather. If we only rely on weather, we may miss other indicators or trends that lead to ice-cream consumption. Currently, our 'hunch' that weather leads to a level of ice-cream consumption is true, but we need to dig further and make sure we have accounted for all external factors/variables---perhaps location or driving distance would be an interesting factor.
