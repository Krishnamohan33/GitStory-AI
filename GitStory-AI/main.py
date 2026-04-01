import argparse
from git_handler import get_repo_path
from storyteller import extract_story, make_story
from visualizer import create_frames
from video import create_video

def main():
    parser = argparse.ArgumentParser(description="🎬 GitStory AI")
    parser.add_argument("--repo", required=True, help="GitHub repo URL")
    parser.add_argument("--output", default="gitstory.mp4", help="Output video file")

    args = parser.parse_args()

    print("📥 Cloning repo...")
    repo_path = get_repo_path(args.repo)

    print("📜 Extracting commits...")
    raw_story = extract_story(repo_path)

    print("✨ Converting to cinematic story...")
    story = [make_story(event) for event in raw_story]

    print("🎨 Generating frames...")
    frames = create_frames(story, args.repo)

    print("🎬 Creating video...")
    create_video(frames, story, args.output)

    print(f"✅ Done! Video saved as {args.output}")

if __name__ == "__main__":
    main()