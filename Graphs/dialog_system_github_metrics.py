import os
import requests
import matplotlib.pyplot as plt
import datetime

print("Starting to generate the commit graph...")

# Ensure the graphs directory exists
os.makedirs("Graphs", exist_ok=True)

# GitHub Repo Info
OWNER = "JarrettGilp"
REPO = "Dialog_System"
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/stats/commit_activity"

# Fetch commit data from GitHub API
response = requests.get(API_URL)
if response.status_code != 200:
    print(f"Error fetching commit data: {response.status_code}, {response.text}")
    exit()

data = response.json()

# Get the current date
current_date = datetime.datetime.now()

# Extract the most recent week of commits (last available week)
if data:
    latest_week = data[-1]  # Last week's commit data
    week_start_date = datetime.datetime.utcfromtimestamp(latest_week["week"])

    # Get daily breakdown of commits
    daily_commits = latest_week["days"]  # List of 7 integers (Sun-Sat)

    # Create date labels for the last 7 days
    days = [(week_start_date + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
    commits = daily_commits  # Commits per day in the last recorded week
else:
    print("No commit data available.")
    exit()

# Plot graph
plt.figure(figsize=(10, 5))
plt.bar(days, commits, color='blue', label="Commits in Last Recorded Week")
plt.xlabel("Days")
plt.ylabel("Number of Commits")
plt.title(f"Commit Activity for {OWNER}/{REPO} (Last Recorded Week)")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.grid(True)

# Save graph in the Graphs folder
plt.tight_layout()  # Adjust layout to prevent overlap

# Print statement for debugging
print("Saving graph to 'Graphs/commit_graph.png'...")

plt.savefig("Graphs/commit_graph.png")

# Confirm if the image is saved
if os.path.exists("Graphs/commit_graph.png"):
    print("Graph saved successfully.")
else:
    print("Failed to save graph.")
