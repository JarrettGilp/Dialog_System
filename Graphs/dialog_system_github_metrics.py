import os
import requests
import matplotlib.pyplot as plt

# Ensure the graphs directory exists
os.makedirs("graphs", exist_ok=True)

# GitHub Repo Info
OWNER = "JarrettGilp"
REPO = "Dialog_System"
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/stats/commit_activity"

# Fetch commit data from GitHub API
response = requests.get(API_URL)
if response.status_code != 200:
    print("Error fetching commit data")
    exit()

data = response.json()

# Extract weekly commit counts
weeks = [week["week"] for week in data]
commits = [week["total"] for week in data]

# Plot graph
plt.figure(figsize=(10, 5))
plt.plot(weeks, commits, marker='o', linestyle='-', color='b', label="Commits per Week")
plt.xlabel("Weeks (Unix Timestamp)")
plt.ylabel("Number of Commits")
plt.title(f"Commit Activity for {OWNER}/{REPO}")
plt.legend()
plt.grid(True)

# Save graph in the graphs folder
plt.savefig("Graphs/commit_graph.png")
