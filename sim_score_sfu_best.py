# Author: Herman Li
# SFU's Best-Similarity Score
# Date: Nov 10, 2023

# Load data from a file
# "Read" it in a meaningful way
# Link our Sim Score algp to the data 

# Open the file 
with open("./data.csv") as f:
    # Get the first line of data
    print(f.readline())
    # Get the second line of data
    print(f.readline())

# Create a "profile" of likes of places in SFU

profile = ["Bubble World", 
           "Chef Huang", 
           "Uncle Fatih's", 
           "Guadalupe (MBC)",
           "Steve's Poke Bar"]


# Initialize the top score and their name
most_similar_score = 0
most_similar_name = ""
least_similar_name = ""
least_similar_score = 1_000_000


with open("./data.csv") as f:
    # Throw away trhe header
    header = f.readline()

    for line in f: 
        # Convert the string to a list
        current_likes = line.split(",")

        # Store the person's name
        current_name = current_likes[1]
        # Initialize the current sim score
        current_sim_score = 0
        for item in profile:
             if item in current_likes:
                 current_sim_score += 1

        # Print the results from this line of data
        print(f"{current_name} - Score: {current_sim_score}")

        # Update the most similar person
        if current_sim_score > most_similar_score:
            most_similar_score = current_sim_score
            most_similar_name = current_name

        # Update least similar person
        if current_sim_score < least_similar_score:
            least_similar_score = current_sim_score
            least_similar_name = current_name
 



            





print("Least similar score:")
print(f"{current_name} - score {least_similar_score}")


print("Most similar score:")
print(f"{most_similar_name} - score {most_similar_score}")

