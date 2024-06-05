#!/usr/bin/env python3
# Import function which is being tested
from pythonchallenge import no_of_handshakes

def test_no_of_handshakes():
    # Positive test cases (valid inputs)
    assert no_of_handshakes(1) == 0
    assert no_of_handshakes(20) == 190

    # Negative test cases (invalid inputs)
    # Inserting a negative int
    try:
        no_of_handshakes(-1)  # Should raise ValueError
    except ValueError:
        pass  # Expected exception

    # Inserting a string
    try:
        no_of_handshakes("hello")  # Should raise ValueError
    except ValueError:
        pass  # Expected exception

    # Inserting a float 
    try: 
        no_of_handshakes(20.5)
    except ValueError: 
        pass  # Expected exception 

    print("All the test cases passed successfully.")


# Call the test function
test_no_of_handshakes()