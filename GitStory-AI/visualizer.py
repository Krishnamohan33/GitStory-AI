import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "frames"

def short_list(files, limit=3):
    return ", ".join(files[:limit]) + ("..." if len(files) > limit else "")

def create_frames(story, repo_url):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    frames = []

    # 🎬 TITLE
    fig, ax = plt.subplots(figsize=(10, 6))
    title_text = f"""
🎬 GitStory AI

The Evolution of:
{repo_url.split('/')[-1]}

By Krishnamohan Yagneswaran
"""
    ax.text(0.5, 0.5, title_text, ha='center', va='center', fontsize=18)
    ax.axis('off')

    title_file = f"{OUTPUT_DIR}/frame_0.png"
    plt.savefig(title_file)
    plt.close()
    frames.append(title_file)

    total_lines = 0

    # 📜 STORY FRAMES
    for i, event in enumerate(story):
        total_lines += event["impact"]

        fig, ax = plt.subplots(figsize=(10, 6))

        added = short_list(event["added"])
        modified = short_list(event["modified"])
        deleted = short_list(event["deleted"])

        change_text = ""

        if added:
            change_text += f"\n📦 Added: {added}"
        if modified:
            change_text += f"\n🛠️ Modified: {modified}"
        if deleted:
            change_text += f"\n🧹 Removed: {deleted}"

        text = f"""
📅 {event['time'].strftime('%Y-%m-%d')}
👤 {event['author']}

{event['text']}
{change_text}

📈 Total Growth: {total_lines} lines
"""

        ax.text(0.5, 0.5, text, ha='center', va='center', fontsize=13)
        ax.set_title("Project Evolution Timeline", fontsize=16)
        ax.axis('off')

        filename = f"{OUTPUT_DIR}/frame_{i+1}.png"
        plt.savefig(filename)
        plt.close()

        frames.append(filename)

    return frames