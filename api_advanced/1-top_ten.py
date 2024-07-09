#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'

    try:
        response = requests.get(url, headers=user)
        response.raise_for_status()  # Check if the request was successful

        data = response.json()
        for post in data.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Failed to decode JSON response")
    except KeyError:
        print("Unexpected response structure")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: ./script.py <subreddit>")
