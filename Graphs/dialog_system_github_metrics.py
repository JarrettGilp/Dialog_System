import os
import subprocess
import matplotlib.pyplot as plt
from datetime import datetime

# Ensure the graphs directory exists
os.makedirs("Graphs", exist_ok=True)

# Fetch commits from the Git history using git log
git_log_command = "git log --since='1 year ago' --pretty=format:'%ad' --date=short"
commit_dates = subprocess.check_output(git_log_command, shell=True).decode().splitlines()

# Convert commit dates to weeks
week_dates = [datetime.strptime(date, "%Y-%m-%d").isocalendar()[1] for date in commit_dates]

# Count commits per week
last_5_days_data = []
for week in data:
    # Get each week's date range (start of the week)
    week_start_date = datetime.datetime.utcfromtimestamp(week["week"])

    # Check if the week is within the last 5 days
    if (current_date - week_start_date).days <= 5:
        last_5_days_data.append((week_start_date, week["total"]))

# Extract days and commits
days = [entry[0].strftime('%Y-%m-%d') for entry in last_5_days_data]  # Format dates as YYYY-MM-DD
commits = [entry[1] for entry in last_5_days_data]

# Plot graph
plt.figure(figsize=(10, 5))
plt.bar(days, commits, color='blue', label="Commits in Last 5 Days")
plt.xlabel("Days")
plt.ylabel("Number of Commits")
plt.title(f"Commit Activity for {OWNER}/{REPO} (Last 5 Days)")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.grid(True)

# Save graph in the Graphs folder
plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig("Graphs/commit_graph.png")
