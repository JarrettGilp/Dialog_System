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

##############################

# Get today's date in UTC and format it for the GitHub API
today = datetime.datetime.utcnow().strftime('%Y-%m-%dT00:00:00Z')
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/commits?since={today}"

# Fetch commit data from GitHub API
response = requests.get(API_URL)
if response.status_code != 200:
    print(f"Error fetching commit data: {response.status_code}, {response.text}")
    exit()

commits = response.json()

# Check if there are any commits today
if not commits:
    print("No commits found for today.")
    exit()

# Group commits by hour
commit_hours = [0] * 24  # Initialize array for 24 hours (midnight to 11 PM)
for commit in commits:
    commit_time = commit["commit"]["author"]["date"]  # ISO format timestamp
    commit_hour = datetime.datetime.fromisoformat(commit_time[:-1]).hour  # Extract hour
    commit_hours[commit_hour] += 1  # Increment commit count for the hour

# Generate x-axis labels (0-23 hours)
hours = list(range(24))

# Plot graph
plt.figure(figsize=(10, 5))
plt.bar(hours, commit_hours, color='blue', label="Commits per Hour")
plt.xlabel("Hour of the Day (UTC)")
plt.ylabel("Number of Commits")
plt.title(f"Commit Activity for {OWNER}/{REPO} (Today)")
plt.xticks(hours)  # Show every hour on x-axis
plt.legend()
plt.grid(True)

# Save graph
plt.tight_layout()
plt.savefig("Graphs/todays_commit_graph.png")
print("Graph saved to 'Graphs/todays_commit_graph.png'.")

# Confirm if the image is saved
if os.path.exists("Graphs/todays_commit_graph.png"):
    print("Graph saved successfully.")
else:
    print("Failed to save graph.")


####################################
"""
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
"""
