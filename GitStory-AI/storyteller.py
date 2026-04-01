from git import Repo
from datetime import datetime

def extract_story(repo_path):
    repo = Repo(repo_path)
    commits = list(repo.iter_commits())

    story = []

    for commit in reversed(commits):
        files = commit.stats.files

        added = []
        modified = []
        deleted = []

        for file, data in files.items():
            if data["insertions"] > 0 and data["deletions"] == 0:
                added.append(file)
            elif data["insertions"] > 0 and data["deletions"] > 0:
                modified.append(file)
            elif data["deletions"] > 0 and data["insertions"] == 0:
                deleted.append(file)

        event = {
            "time": datetime.fromtimestamp(commit.committed_date),
            "author": commit.author.name,
            "message": commit.message.strip(),
            "files_added": added,
            "files_modified": modified,
            "files_deleted": deleted,
            "insertions": commit.stats.total["insertions"],
            "deletions": commit.stats.total["deletions"],
            "type": classify_event(commit, added)
        }

        story.append(event)

    return story


# 🧠 CLASSIFICATION
def classify_event(commit, added_files):
    msg = commit.message.lower()

    for file in added_files:
        if "readme" in file.lower():
            return "readme"

    if "fix" in msg:
        return "fix"

    if "add" in msg or "feature" in msg:
        return "feature"

    if "remove" in msg:
        return "remove"

    return "normal"


# 🎬 STORY GENERATOR
def make_story(event):
    t = event["type"]

    if t == "readme":
        line = "📘 Documentation evolved and shaped the project"

    elif t == "feature":
        line = "🚀 New functionality expanded the system"

    elif t == "fix":
        line = "⚔️ Issues were resolved to stabilize the project"

    elif t == "remove":
        line = "🧹 Old components were removed"

    else:
        line = "📜 Development continues steadily"

    return {
        "time": event["time"],
        "author": event["author"],
        "text": line,
        "added": event["files_added"],
        "modified": event["files_modified"],
        "deleted": event["files_deleted"],
        "impact": event["insertions"]
    }