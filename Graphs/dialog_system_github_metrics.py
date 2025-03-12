import os
import requests
import matplotlib.pyplot as plt
import datetime

# Ensure the graphs directory exists
os.makedirs("Graphs", exist_ok=True)

# GitHub Repo Info
OWNER = "JarrettGilp"
REPO = "Dialog_System"
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/stats/commit_activity"

# Get the GitHub token from the environment variable (set in GitHub Actions Secrets)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Headers for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# Fetch commit data from GitHub API
response = requests.get(API_URL, headers=headers)
if response.status_code != 200:
    print("Error fetching commit data")
    exit()

data = response.json()

# Get the current date
current_date = datetime.datetime.now()

# Filter data for the last 7 days
last_7_days_data = []
for week in data:
    # Get each week's date range (start of the week)
    week_start_date = datetime.datetime.utcfromtimestamp(week["week"])

    # Check if the week is within the last 7 days
    if (current_date - week_start_date).days <= 7:
        last_7_days_data.append((week_start_date, week["total"]))

# Extract days and commits
days = [entry[0].strftime('%Y-%m-%d') for entry in last_7_days_data]  # Format dates as YYYY-MM-DD
commits = [entry[1] for entry in last_7_days_data]

# Plot graph
plt.figure(figsize=(10, 5))
plt.bar(days, commits, color='blue', label="Commits in Last 7 Days")
plt.xlabel("Days")
plt.ylabel("Number of Commits")
plt.title(f"Commit Activity for {OWNER}/{REPO} (Last 7 Days)")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.grid(True)

# Save graph in the Graphs folder
plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig("Graphs/commit_graph.png")
