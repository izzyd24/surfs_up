# surfs_up
This project explores data storage and retrieval via the following tools: 
Python SQL toolkit (SQLAlchemy), Object Relational Mapper, pandas, numpy, SQLlite, Python 3.9.2, Flask, Jupyter Notebook
## Intent
Produce an analyis of temperature trends in Oahu, Hawaii. Specifically, summary statistics of temperature data were requested for the months of June and December, and then determine if an ice-cream shop would be a model that can be sustained around the year. 
## Results Deliverable 1
Determine the Summary Statistics for June
This step creates a query that filters the Measurement table to retrieve the temperatures for the month of June + as a list
![image](https://user-images.githubusercontent.com/102266450/172282032-178bcc89-bd03-4507-8d24-19b937f3f407.png)
Next, I creating the dataframe and removed the index to make less confusing. 
![image](https://user-images.githubusercontent.com/102266450/172282193-1fa8fb3e-056b-4b26-9896-93d912344353.png)
Finally, I provided the summary statistics and a plot. 
![image](https://user-images.githubusercontent.com/102266450/172282268-25bca93c-18c9-4991-99c0-5ff9a5b17a20.png)

## Results Deliverable 2
Determine the Summary Statistics for December 
This step creates a query that filters the Measurement table to retrieve the temperatures for the month of December + as a list
![image](https://user-images.githubusercontent.com/102266450/172282360-aea65537-78c1-4824-bc43-de2144d5ecee.png)
Next, I creating the dataframe and removed the index to make less confusing. 
![image](https://user-images.githubusercontent.com/102266450/172282379-6505c9a2-e7ea-42eb-b2e6-73ce430a857e.png)
Finally, I provided the summary statistics and a plot. 
![image](https://user-images.githubusercontent.com/102266450/172282399-f44b8417-8801-4efd-8d12-58d7f4be7c61.png)

## Key Differences and Suggestions
1. The average temperature in June is about 74-75 degrees or about 4 degrees higher than average temperature from December. 
Suggestion: If we see a decrease in temperature by nearly 5% from June to December, we recommend to expand the summary stats to all months of the year to ensure there are no outlier/close shop scenarios. 
2. June temperatures have a normal bell curve, and December seems to have more variability. 
Suggestion: Map out via Matplotlib library for each month, and compare the distribution curves. We ideally want to see a tight curve with a normal distribution, and an emphasis on small stdevs to ensure we can forecast demand according to weather temperatures. 
Broader Suggestion: Review other important variables that are correlated with optimal beach and surfing weather. If we only rely on weather, we may miss other indicators or trends that lead to ice-cream consumption. Currently, our 'hunch' that weather leads to a level of ice-cream consumption is true, but we need to dig further and make sure we have accounted for all external factors/variables---perhaps location or driving distance would be an interesting factor.
