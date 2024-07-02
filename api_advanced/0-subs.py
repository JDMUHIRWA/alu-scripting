#!/usr/bin/python3
"""Module"""

import requests

def number_of_subscribers(subreddit):
    """Function that return the number of subscribers from REDDIT API"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the status code is not 200, return 0
            return 0
    except requests.RequestException:
        # If any request exception occurs, return 0
        return 0

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    print(f"The number of subscribers in r/{subreddit} is: {number_of_subscribers(subreddit)}")
