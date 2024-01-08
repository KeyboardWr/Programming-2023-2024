# Herman Li
# Winder Holidays
# Jan 8, 2024

# Requirement's:
# - create a function called winter_holiday()
# - Take on parameter
    # - string
# - return a summary of an event from your holidays

import random

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
    
    params:
        good_or_bad - indicate what kind of event to summarize
        
    Returns:
        An event that happened during the holidays"""
    
    bad_evennts = ["Went skiing but snow conditions were horrible due to early season", "Had to study ARCT music history over winter break","Often got bored at home because of the lack of things to do"]
    good_events = ["Went out with friends and went swimming", "Slept a lot","I had a lot of parties and one had a cat to play with"]
    if good_or_bad.lower() == "bad":
        print(random.choice(bad_evennts))
    if good_or_bad.lower() == "good":
        print(random.choice(good_events))



    


def main() -> None:
    response = input("Would you like a good or bad event for my winter holidays?")
    winter_holiday(response)


if __name__ == "__main__":
    main()