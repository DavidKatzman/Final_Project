# Hockey Player Classification Project

## Dataset
- The dataset is compiled from four separate datasets from hockey-reference.com for the 2018-19 NHL season: 
	1) Basic Stats
	2) Advanced Stats
	3) Time on Ice Stats
	4) Miscellaneous Stats
	
## Goal
- The Goal of the project was to group hockey players based on skill-level and playstyle to help GM's and coaches determine the attributes of a given player
- Initially, the goal was to classify only based on playstyle, but leaving out skill left out important features

## Final Variables
- The compiled dataset was then altered to create new variables that were irrespective of total time on ice (although time on ice percentage was left in) and that helped better account for skill and playstyle
- A final subset of the initial and created features was then chosen for modeling
- Only players in the top 3/4 of both time on ice per game and games played were selected
- The Final Variables belong to the following categories:
	1) Shooting
	2) Face-offs
	3) Time on Ice Percentage
	4) Penalties and Hits
	5) Power-Play, Even-Strength, and Short-handed Stats
	6) Giveaways and Takeways
	7) Scoring
	8) Defensive Stats
	9) Advanced Stats
	
	
## Imputing NA values
- NA values were coded to 0, as this made the most sense in most of these cases
- For example, if a player has neither scored nor assisted a goal this year, then it makes sense to set their proportion of goals/points and assists/points both to 0

## Models
- Models were ran on the dataset both including and excluding skill variables
- Both K-Means and Agglomerative Clustering models were ran
- The models were evaluated based on their silhouette score

## Final Models
- There were three final models used
- Two of them were created using the dataset with skill features removed:
	1) 8 cluster K-Means model
	2) 10 cluster K-Means model
- The final model was created using the dataset with skill features included:
	3) 20 cluster K-Means model
- The 20 cluster K-Means model was chosen based on having the lowest silhouette score of any K-Means or Agglomerative Clustering model with at least 15 clusters, since running a model on fewer clusters would have defeated the purpose of the exercise