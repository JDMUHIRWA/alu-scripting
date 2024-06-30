#!/usr/bin/python3
"""
Retrieve the number of subscribers from the external module 0-subs.py
The retrieved subscriber count is then printed to the console.
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        try:
            subscribers = number_of_subscribers(sys.argv[1])
            if isinstance(subscribers, int):
                print("{:d}".format(subscribers))
            else:
                print("Error: The function did not return an integer value.")
        except Exception as e:
            print(f"An error occurred: {e}")
