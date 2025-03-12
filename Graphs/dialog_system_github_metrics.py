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
commit_counts = {}
for week in week_dates:
    if week not in commit_counts:
        commit_counts[week] = 0
    commit_counts[week] += 1

# Prepare data for plotting
weeks = sorted(commit_counts.keys())
commits = [commit_counts[week] for week in weeks]

# Plot graph
plt.figure(figsize=(10, 5))
plt.plot(weeks, commits, marker='o', linestyle='-', color='b', label="Commits per Week")
plt.xlabel("Weeks")
plt.ylabel("Number of Commits")
plt.title("Commit Activity Over Time")
plt.legend()
plt.grid(True)

# Save graph
plt.savefig("/Graphs/commit_graph.png")
