# Tech Report
This is where you can type out your tech report.

### Where is the data from?

The data comes from songs on Spotify, songs from the Billboard Hot 100 list, and songs released by year that were recorded in the US.

### How did you collect your data?

We scraped all past weekly Billboard Hot 100 Data from 2015 to 2021.

We also used Spotify API to collect the features of songs from the Billboard Dataset. Features include danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence and tempo. These are numerical values.

For the ML part of the project, we also needed a pool of all songs published in the past. We obtained this information through Wikipedia scraped through this page. (https://en.wikipedia.org/w/index.php?title=Category:Songs_by_year&from=2000) 

### Is the source reputable?

Yes, the sources are reputable. Spotify provides API data for developers that contain information about songs in its repertoire. The source we obtain our Billboard Hot 100 data from is from the Billboard website itself, and is therefore highly reputable.

### How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?



### Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)


### How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently, but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)


### How many data points are there total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? Do you think this is enough data to perform your analysis later on?

Though we have not finished scraping all the songs from Wikipedia, we can see there will be at least a couple thousand data points, each representing an individual song between the years 2014 and 2021. There are about 70 songs per page, 15 pages per year and we are looking at years 2014-2021. Hence there will be approximately 8400 data points in total. Since we’re dividing it up by years, there should be about 1050 data points per year. The data we get from Billboard should be a subset of these 8400 data points. We believe that this is a sufficient amount of data for us to do both hypothesis testing and machine learning. 

### Are there missing values? Do these occur in fields that are important for your project's goals?


### Are there duplicates? Do these occur in fields that are important for your project's goals?

Yes. Since we’re collecting weekly data from the Billboard Hot 100, it’s common to have duplicates. The same song could stay on the ranking for a long period of time. We tackled this issue when cleaning our data and put together a distinct list.

### How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)

### Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them?


### Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?


### Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)
