# Tech Report
This is where you can type out your tech report.

### Where is the data from?

We obtained our first dataset on Grammy Awards winners from Kaggle (https://www.kaggle.com/unanimad/grammy-awards). This file contains all nominations and winners of Grammy Awards from 1958-2019. Information include year, award title, song/album/artist names. We would need to perform data cleaning since we're only interested in the songs winning the award.

We also need data about features of those award winning songs and we utilized Spotify API to collect those information. We collected numeric features related to the song (details stated in data_spec) and the numeric values made it easier for future comparison and analysis.

Since one of our hypothesis is about how fame of the singer and popularity of the song could affect the chance of award-winning, we also need data that represent the popularity. We utilized Billboard API to get popularity data on the songs and singers that previously won the Grammy. Specificly, we looked at Billboard ranking of singer, the number of weeks on Billboard of the song, the highest rank on the chart etc. 


### How did you collect your data?

We downloaded one dataset from Kaggle, and used API data collection for the two other datasets.

### Is the source reputable?

The Kaggle dataset is put together by Raphael Fontes, a data scientist from Federal Institute of Sergipe in Brazil. Though he's not an official source, he is a "Datasets Master" endorsed by Kaggle and have experience in research, lecturing at Universidade Federal de Sergipe, and working in the industry.
The other sources are from Spotify and Billboard official API, which is reputable and reliable. 

### How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?



### Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)


### How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently, but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)


### How many data points are there total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? Do you think this is enough data to perform your analysis later on?


### Are there missing values? Do these occur in fields that are important for your project's goals?


### Are there duplicates? Do these occur in fields that are important for your project's goals?


### How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)

### Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them?


### Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?


### Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)
