import requests
print("Hello from Python!")
response = requests.get("https://api.github.com")
print("GitHub API status:", response.status_code)
