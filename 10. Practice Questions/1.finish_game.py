"""
In order to finish a game, a player has to complete N missions. The missions are numbered
0 to N-1. The Kth mission has an integer D[K] assigned, representing the difficulty level. 

During a day, you can perform any number of missions given the following 2 rules: 

1. Missions should be performed in the specified order, in other words, a mission can be 
undertaken if all the missions preceding it have already been completed. 

2. The difference between the difficulty levels of any two missions performed on the same level
should not be greater than the integer X. # DIFFICULTY LEVEL OF ANY 2 MISSIONS 

Write a function 

def solution(D, x):

That given the array D of N integers and an integer X, returns the minimum number of days 
required to complete all the missions in the game
"""


def solution(D, x) -> int:
    # Check the edge case: when D is empty
    if len(D) == 0:
        return 0  # TAKES 0 DAYS

    # If not empty, then we'll always have atleast 1 day,
    # and set the min and max difficulty to the first number in the D array
    days_to_complete = 1
    min_difficulty = D[0]
    max_difficulty = D[0]

    for d in D[1:]:  # any challenge from D at index one onwards, - exclude the first number
        # set the max and min to be compared to x
        new_min_difficulty = min(min_difficulty, d) # returns 1 number
        new_max_difficulty = max(max_difficulty, d) # will return 1 number

        # then check for the constraint:
        if new_max_difficulty - new_min_difficulty <= x:
            # We are still on teh same day
            # dont increment the days 
            # juct the new min and max changes 
            min_difficulty = new_min_difficulty
            max_difficulty = new_max_difficulty

        else:
            days_to_complete += 1
            min_difficulty = d
            max_difficulty = d

    return days_to_complete
