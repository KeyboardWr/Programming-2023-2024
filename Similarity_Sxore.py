# Author: Herman Li
# Calculating Similarity Score
# Nov 9, 2023

# Calculate similarity scores between two people 
# Create two lists that represent the movies that the like

similarity_score = 0

Ubial_Movie_Favourites = ["the matrix", "avengers: infinity War", "infernal affairs", "rogue one", "the empire strikes back"]
Ben_Fave_Movies = ["thomas and friends", "big world big advanture", "avengres: infinity war", "minions", "paddintong 2", "rogue one"]

# For every movie in the first list
    # If that movie is in the second list
        # Increase the similarity score by 1
for movie in Ubial_Movie_Favourites:
    if movie in Ben_Fave_Movies:
        similarity_score += 1
    

# Display the results
