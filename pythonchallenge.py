#!/usr/bin/env python3

def no_of_handshakes(no_people):

    # Check no. of people is positive int
    if type(no_people) is not int or no_people <= 0:
        raise ValueError("Number of people must be a positive integer.")

    # Calculate no. of handshakes using formula n * (n - 1) / 2
    handshakes = (no_people * (no_people - 1)) // 2
    return handshakes

# Calling the function with 20 people to check it is 190 handshakes 
num_people = 20
result = no_of_handshakes(num_people)
print(f"Number of handshakes with {num_people} people: {result}")