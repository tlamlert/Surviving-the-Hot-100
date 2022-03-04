# Data Spec
This is where you will be describing your data spec comprehensively. Please refer to the handout for a couple of examples of good data specs.

You will also need to provide a sample of your data in this directory. Please delete the example `sample.db` and replace it with your own data sample. ***Your sample does not necessarily have to be in the `.db` format; feel free to use `.json`, `.csv`, or any other data format that you are most comfortable with***.


## This is for the Mendeley data

artist_name:
  type - strings
  The name of the artist for a given song.
  
  default - there is no default value for an artist's name
  A song needs an artist name.
  
  range - artists have unique names, there is no set range
  
  distribution - based on the string, there shoud be a very normal distribution
  
  identifier - no, not an identifier
  
  unique - no. There can be multiple songs with the same artist
  
  duplicate - no, we will not. There can exists multiple unique songs with the same artists.
  
  required - yes, this is required. A song should have an artist
  
  analysis - yes, an artist who is already big would more likely have another song on the billboard
  
  sensitive - no, not sensitive. Public information
  
track_name:
  type - string
  The name of the song
  
  default - there is no default for the name of a song
  
  range - songs have unique names, there is no set range
  
  distribution - the names of songs should be normally distributed
  
  identifier - no, not an identifier.
  
  unique - no, multiple unique songs may have the same name
  
  duplicate - no. There can be multiple songs with the same name
  
  required - yes this is required, should have a name
  
  analysis - no, the name of a song should not impact in our model
  
  sensitive - not sensitive, very public data
  
release_date:
  type - integer
  Represents the year
  
  default - no default year
  
  range - 1950 to 2016
  
  distribution - uniform. There should be about the same number of songs each year we track
  
  identifier - yes, used to analyze a particular year's model
  
  unique - no, multiple songs can be in made in the same year
  
  duplicate - no, there can be multiple songs with the same date
  
  required - yes this is required, will be used to bin the different years for analysis
  
  analysis - no, we will not use the year it was released to determine if it will be a billboard song
  
  sensitive - not senstivie, very public data

Genre:
  Type: string
  
  Default value: none
  
  Range: blues, country, jazz, pop, reggae, rock
  
  Distribution: 50%  jazz, 20% blues, 20% country, 10% the rest 3 genres
  
  Identifier: Maybe, depends on the specifics of our analysis
  
  Uniqueness: no
  
  Duplicate: No, since this attribute is supposed to be duplicative across data points
  
  Required: Maybe, depends on the specifics of our analysis
  
  Use in analysis: Yes. We can see which genres of music appear on Billboard Hot 100 more/less often
  
  Sensitive information: No, because the genre of music is publicly defined


lyrics:


Danceability:
  Type: Float
  
  Default value: 0
  
  Range: 0.05 to 0.83
  
  Distribution: Uniform 
  
  Identifier: No
  
  Uniqueness: No
  
  Duplicate: Perhaps, songs can have similar danceability traits 
  
  Required Value: Yes
  
  Used in Analysis: Yes, this will be heavily used to analyze trends in similarity that may lead to similar popularity results
  
  Sensitive Information: No, this is not a sensitive data attribute 


Loudness:
  Type: Float
  
  Default value: 0
  
  Range: 0.34 to 0.37
  
  Distribution: Uniform 
  
  Identifier: No
  
  Uniqueness: No
  
  Duplicate: Perhaps, songs can have similar loudness traits 
  
  Required Value: Yes
  
  Used in Analysis: Yes, this will be heavily used to analyze trends in similarity that may lead to similar popularity results
  
  Sensitive Information: No, this is not a sensitive data attribute 


Acousticness:
  Type: Float
  
  Default value: 0
  
  Range: 0.09 to 0.99
  
  Distribution: Uniform 
  
  Identifier: No
  
  Uniqueness: No
  
  Duplicate: Perhaps, songs can have similar acoustic traits 
  
  Required Value: Yes
  
  Used in Analysis: Yes, this will be heavily used to analyze trends in similarity that may lead to similar popularity results
  
  Sensitive Information: No, this is not a sensitive data attribute 


Instrumentalness
  Type: Float
  
  Default value: 0
  
  Range: 0 to 0.98
  
  Distribution: Uniform 
  
  Identifier: No
  
  Uniqueness: No
  
  Duplicate: Perhaps, songs can have similar instrumental traits 
  
  Required Value: Yes
  
  Used in Analysis: Yes, this will be heavily used to analyze trends in similarity that may lead to similar popularity results
  
  Sensitive Information: No, this is not a sensitive data attribute 


Valence
  Type: Float
  
  Default value: 0
  
  Range: 0.07 to 0.96
  
  Distribution: Uniform 
  
  Identifier: No
  
  Uniqueness: No
  
  Duplicate: Perhaps, songs can have similar “popularity” levels 
  
  Required Value: Yes
  
  Used in Analysis: Yes, this will be heavily used to analyze trends in similarity that may lead to similar popularity results
  
  Sensitive Information: No, this is not a sensitive data attribute 


energy:
  type - float
  
  default - the default value is 0 for energy if no information is given
  
  range - 0.008 to 0.37
  
  distribution - normal, centered around the average
  
  identifier - no, not using this as an identifier
  
  unique - no, songs can have the same energy
  
  duplicate - no, unique songs can have the same energy
  
  required - yes, it is required to have an energy score for analysis
  
  analysis - yes, we will use energy of songs to deterine likelihood of being on the billboard
  
  sensitive - no, this information is very public

topic:
  type - strings
  The theme of the song captured in one to two words

  default - "music" is the default value if a topic of a song is unidentified

  range - feelings, music, night/time, obscene, romantic, sadness, violence, world/life
  
  distribution - uniform, should be about the same for all categories
  
  identifier - no, we will not use this as an identifier
  
  unique - no, songs can be of the same topic
  
  duplicate - no, unique songs can have the same topic
  
  required - no, there is no need for a valid 

  analysis - no, the topic is not important to our analysis
  
  sensitive - not sensitive, these songs' topics are public


# This is for BillBoard data - this can be found in the repository under Team-Name/data_deliverable/data/billboard100/sample

song
  type - string
  The name of the song
  
  default - there is no default for the name of a song
  
  range - songs have unique names, there is no set range
  
  distribution - the names of songs should be normally distributed
  
  identifier - no, not an identifier.
  
  unique - no, multiple unique songs may have the same name
  
  duplicate - no. There can be multiple songs with the same name
  
  required - yes this is required, should have a name
  
  analysis - no, the name of a song should not impact in our model
  
  sensitive - not sensitive, very public data
  
artist:
  type - strings
  The name of the artist for a given song.
  
  default - there is no default value for an artist's name
  A song needs an artist name.
  
  range - artists have unique names, there is no set range
  
  distribution - based on the string, there shoud be a very normal distribution
  
  identifier - no, not an identifier
  
  unique - no. There can be multiple songs with the same artist
  
  duplicate - no, we will not. There can exists multiple unique songs with the same artists.
  
  required - yes, this is required. A song should have an artist
  
  analysis - yes, an artist who is already big would more likely have another song on the billboard
  
  sensitive - no, not sensitive. Public information

Weeks_on_chart
  Type: Integer
  
  Default value: 1
  
  Range: 1 to 45
  
  Distribution: skewed towards 1 
  
  Identifier: No
  
  Uniqueness: No
  
  Duplicate: Yes, many songs in this sample were on the chart for only 1 week 
  
  Required Value: Yes
  
  Used in Analysis: Yes, this will be useful when we perform the ML part of the project
  
  Sensitive Information: No, this is not a sensitive data attribute. It reflects the popularity of the song 
