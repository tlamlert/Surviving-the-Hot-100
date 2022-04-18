# Tech Report
This is where you can type out your tech report.

### A defined hypothesis or prediction task, with clearly stated metrics for success.

1. 
H_0: There is no significant correlation between a song’s Danceability score and whether they are on the billboard for multiple weeks/a long time. (more than 10 weeks?)
H_a: There is a significant correlation between a song’s Danceability score and whether they are on the billboard for multiple weeks/a long time. (more than 10 weeks?)

2. 
H_0: The average Valence score for songs with 10 weeks (subject to change) or more on the Billboard is not significantly different than the overall average Valence score for songs that have ever been on the Billboard.
H_a: The average Valence score for songs with 10 weeks (subject to change) or more on the Billboard is significantly different than the overall average Valence score for songs that have ever been on the Billboard. 

3. 
H_0: The average Energy score for songs in the 80s is not significantly different from the average Energy score for songs in the 2010s.
H_a: The average Energy score for songs in the 80s is significantly different from the average Energy score for songs in the 2010s. 

4. 
H_0: The lasso estimate (coefficient) of Danceability for determining the number of weeks a song is on the billboard will not be among the top __insert number__ characteristics.
H_a: The lasso estimate (coefficient) of Danceability for determining the number of weeks a song is on the billboard will be among the top __insert number__ characteristics. (machine learning hypothesis)


### Why did you use this statistical test or ML algorithm? 

For the 1st hypothesis, we’re using the chi-square independence test to check if danceability is related to a song being on the Billboard chart for an extended period of time (10 weeks?). Intuitively, there should be a relationship between these two variables and songs with higher danceability value should stay on the chart longer. Danceable songs are more desirable for  social events and they tend to be played more often, resulting in longer weeks staying on the chart. Using a chi-square independence test is best here because we are dealing with 

For the second hypothesis, we’re using a one-sample t-test to check if the valence (positivity) of songs that are on the Billboard for a long time are statistically different from the songs that are only on the Billboard for a relatively short amount of time. The intuition behind this question is that songs with more positivity may have a different impact on people’s willingness to keep playing the song. If a song is more positive in mood, it may be true that it is more palatable to listen to over time, hence raising its resilience to stay on the Billboard for longer.

For the third hypothesis, we’re using a two-sample t-test to check if the energy in the songs from the 1980s decade is significantly different from the energy in the songs from the 2010s. The intuition behind this question is that as music production has evolved to use more electronic components, there seems to be a dramatic increase in the overall energy a song can produce. Using a two-sample t-test is best here because we want to compare whether the means of the Energy score from two different samples are different from each other.

For the ML part, we decided to use a feedforward neural network with 4 layers. Our initial thought was to use linear regression, but it did not fit our dataset well. Our goal is to predict how many weeks a song can stay on Billboard Hot 100 given its attributes, and our dataset contains information about songs that have made it to Billboard Hot 100 since 1970s, their attributes and the number of weeks they have been on the chart. It makes sense for us to use FFNN to train our model using our dataset and then use it to predict.


### Which other tests did you consider or evaluate? 

For the hypothesis testing part, we mainly looked at the tests that were covered in the stats homework and it addressed the need for our hypothesis. For ML part, we also considered linear regression, but as mentioned above and also in the upcoming questions, our dataset did not fit it well and the output wasn’t desirable. 

### How did you measure success or failure? Why that metric/value? What challenges did you face evaluating the model? Did you have to clean or restructure your data?

Hypothesis testing-

ML Lasso- We define success by seeing how well lasso regression eliminates irrelevant attributes. We compare the weights produced from lasso regression to results from the hypothesis testing part (heat map and chi-squared tests for instance) and see how well they match. 

ML FFNN- We define success by seeing how close our predictions are to the actual number of weeks a song stays on Billboard. This can be validated by the loss function, which should converge to zero if our model is successful. However, unlike the lasso regression where there exists a hard threshold for determining success (weight = 0 means the song attribute is irrelevant), we do not have as clear a threshold for FFNN. The final loss value we get is a bit high for us to consider our model as good enough (about 40)

We cleaned our data by eliminating songs that we cannot get attributes from Spotify. If there’s not an exact match (for instance, the song on Billboard has a feat singer but it does not on Spotify), we use the alternative version with Spotify (the version without the feat singer). When the song just does not exist on Spotify, we take that song out of the dataset. We did normalize the data so that the accuracy of our model could improve.


### What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

Hypothesis testing-

ML Lasso - The results did not fit the dataset as much as we expected. We think that it’s because the features we used as inputs do not have a strong enough correlation. Initially, we thought that even though outside features such as artists’ fame and social trend would impact the number of weeks a song remains on Billboard, it would not have that big of an impact. However, it seems like from the results, song features by themselves are not sufficient to make accurate predictions. 

ML FFNN- Unfortunately, FFNN results also did not fit the dataset as much as we expected. Our model architecture might not be complicated enough to produce accurate predictions. Instead of thoroughly learning through input data and making predictions, it’s just predicting average values, which indeed minimizes the loss function.

We first implemented lasso regression and noticed that a lot of attributes converged to zero. Noticing that this method did not work as well as we expected, we did some research and switched to FFNN, which should be able to fit into any dataset. However, the results are still unsatisfactory despite that we tried to add more layers and more trainable parameters.



### For your visualization, why did you pick this graph? What alternative ways might you communicate the result? Were there any challenges visualizing the results, if so, what where they? Will your visualization require text to provide context or is it standalone (either is fine, but it's recognize which type your visualization is)?

Our two visualizations are heat map and bar chart. The heat map shows correlations between song features and the bar graph gives us the distribution of song features across decades in the dataset. We considered doing a histogram as an alternative to the bar chart. The issue with histogram is that it only shows frequencies but we desire averages of a certain attribute in a certain decade. 

Need to add challenges and context



### Full results + graphs (at least 1 stats/ml test and at least 1 visualization). You should push your visualizations to the /analysis_deliverable/visualizations folder in your repo. Depending on your model/test/project we would ideally like you to show us your full process so we can evaluate how you conducted the test!

See visualization folder under analysis_deliverable in the repository


### If you did a statistics test, are there any confounding trends or variables you might be observing?

??


### If you did a machine learning model, why did you choose this machine learning technique? Does your data have any sensitive/protected attributes that could affect your machine learning model?

Initially, we were thinking about regression analysis as our ML model. We wanted to see which attributes of the songs matter the most in determining the number of weeks a song stays on the Billboard Hot 100. We discovered lasso regression, which we believed was better than linear regression since it avoids overfitting. However, we later realized that maybe our dataset does not fit linear regression, since the output wasn’t really desirable, and we explored FFNN. FFNN is a deep learning model and ideally, it should be able to fit into any dataset given the right model architecture. This addresses the issue with lasso regression.  

Our data come from weekly Billboard Hot 100 rankings and Spotify API song features. Hence, there are no sensitive or protected attributes.
