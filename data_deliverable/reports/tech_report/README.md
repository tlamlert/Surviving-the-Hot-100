# Tech Report
This is where you can type out your tech report.

### Where is the data from?

The data comes from songs on Spotify, songs from the Billboard Hot 100 list, and songs released by year that were recorded in the US.

### How did you collect your data?

We scraped all past weekly Billboard Hot 100 Data from 2015 to 2021.

We also used Spotify API to collect the features of songs from the Billboard Dataset. Features include danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence and tempo. These are numerical values.

We find a dataset from Mendeley Data with songs from 1950 to 2019. This resource includes the name and numeric attributes (extracted from Spotify) of the songs. (https://data.mendeley.com/datasets/3t9vbwxgr5/3)

For the ML part of the project, we also needed a pool of all songs published in the past. We obtained this information through Wikipedia scraped through this page. (https://en.wikipedia.org/w/index.php?title=Category:Songs_by_year&from=2000) 

### Is the source reputable?

Yes, the sources are reputable. Spotify provides API data for developers that contain information about songs in its repertoire. The source we obtain our Billboard Hot 100 data from is from the Billboard website itself, and is therefore highly reputable. The Mendeley data comes from a published dataset used in academic research papers (there is a DOI). Wikipedia has a highly comprehensive list of songs throughout time and is a website that is (now) highly regulated and considered very reputable.

### How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?

The sample of 100 rows is comparably small to our dataset. Since it's only representing about 1% of our data. The sample we submitted is not randomly selected from our entire database, since we have not yet finished scraping all websites. However, from the samples we submitted based on our existing database, we don’t see any sampling bias and the sample is pretty representative.

Pandas random sample or np.random - check distribution of the sample vs whole dataset (how many times we see certain values, mean variance etc.), see how sample compares to whole distribution of dataset
Copy rows from csv files and load those, then take samples from there

### Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)

The data may be skewed in the fact that we only look at songs that are popular enough to be recorded in Wikipedia and our Mendeley dataset. There are many excluded songs that are not popular enough to have sold many albums or played on radios (such as SoundCloud or YouTube songs) that may have attributes to them that hurt its chances of being on the BillBoard Top 100. These attributes would not be accounted for in our learning model.

### How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently, but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)

The data we collected has cleaned individual values that were generically formatted to not include non-relevant white spaces and other string format impurities. We made sure that key song identifiers were uniformly stored to ensure the data collected on songs from different sources could cohesively be combined. 

### How many data points are there total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? Do you think this is enough data to perform your analysis later on?

Though we have not finished scraping all the songs from Wikipedia, we can see there will be at least a couple thousand data points, each representing an individual song between the years 2014 and 2021. There are about 70 songs per page, 15 pages per year and we are looking at years 2014-2021. Hence there will be approximately 8400 data points in total. Since we’re dividing it up by years, there should be about 1050 data points per year. The data we get from Billboard should be a subset of these 8400 data points. We believe that this is a sufficient amount of data for us to do both hypothesis testing and machine learning. 

### Are there missing values? Do these occur in fields that are important for your project's goals?

At the moment, we believe there are no missing values in the sense that for every data point (song) we collected, we have a value for all the attributes we collected. If there were, it would be that a song is not in Spotify so we would not be able to obtain the Spotify attributes.

### Are there duplicates? Do these occur in fields that are important for your project's goals?

Yes. Since we’re collecting weekly data from the Billboard Hot 100, it’s common to have duplicates. The same song could stay on the ranking for a long period of time. We tackled this issue when cleaning our data and put together a distinct list.

### Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them?

Yes, the number of weeks a certain song remained on the Billboard Hot 100 list was initially interpreted as a string while it was parsed from the Billboard web-scraping program we created.
We addressed this and additional concerns by individually selecting to parse these variables as their actual data format to ensure they could be properly used with their comparison operators during future analysis.

### Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?

We removed 10 attributes from meta song data which we found to not be useful for our data analysis. 

### Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)

We had challenges web scraping data from the Billboard website since a captcha was prompted every time tenth time data from the website was requested. We had to mitigate this issue by automating a break between web scraping attempts. Although this will not impact analysis long-term, we did experience a delay in data collection because of the aforementioned issue.


