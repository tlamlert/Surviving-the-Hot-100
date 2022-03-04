# Data Spec
This is where you will be describing your data spec comprehensively. Please refer to the handout for a couple of examples of good data specs.

You will also need to provide a sample of your data in this directory. Please delete the example `sample.db` and replace it with your own data sample. ***Your sample does not necessarily have to be in the `.db` format; feel free to use `.json`, `.csv`, or any other data format that you are most comfortable with***.


Type of data that will be used for the representation.
Default value
Range of value.
Simplified analysis of the distribution of values
Is this an identifier?
Are these values unique?
Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?
Is this a required value?
Do you plan to use this attribute/feature in the analysis? If so, how?
Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?

artist_name:
  type - strings
  The name of the artist for a given song.
  
  default - there is no default value for an artist's name
  A song needs an artist name.
  
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
  
  distribution - the names of songs should be normally distributed
  
  identifier - no, not an identifier.
  
  unique - no, multiple unique songs may have the same name
  
  duplicate - no. There can be multiple songs with the same name
  
  required - yes this is required, should have a name
  
  analysis - no, the name of a song should not impact in our model
  
  sensitive - 
  
release_date:

genre:

lyrics:

danceability:

loudness:

acousticness:

instrumentalness:

valence:

energy:

topic:
