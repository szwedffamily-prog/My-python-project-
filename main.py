import requests

print("Hello from Python!")

# Search for Python repositories
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
response = requests.get(url)

print("GitHub API status:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print(f"Total repositories: {data["total_count"]}")
    
    # Show top 5 repositories
    for repo in data["items"][:5]:
        print(f"- {repo["name"]}: {repo["stargazers_count"]} stars")

