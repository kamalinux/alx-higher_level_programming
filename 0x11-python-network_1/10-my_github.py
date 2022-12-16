#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id

- You must use Basic Authentication with a personal access token as
password to access to your information (only read:user permission is needed)
- The first argument will be your username
- The second argument will be your password (in your case, a personal
access token as password)
- You must use the package requests and sys
- You are not allowed to import packages other than requests and sys

Usage: ./10-my_github.py [github_username] [github_pw]
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
