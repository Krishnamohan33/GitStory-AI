# 🎬 GitStory AI

Turn any GitHub repository into a cinematic story video.

GitStory AI transforms raw commit history into a visual, story-driven timeline — showing how a project evolved over time with commits, file changes, and milestones. It bridges development and storytelling, making code history engaging, understandable, and shareable.

---

## 🚀 Features

* 📜 Converts commits into cinematic story narration
* 📦 Shows files added, modified, and removed
* 📘 Detects README/documentation evolution
* 📊 Tracks project growth (lines of code over time)
* 🎬 Generates a complete MP4 video timeline
* ⚡ Works directly with GitHub repository URLs
* 🏷️ Permanent watermark branding (author credit)
* 🧠 Smart timing so text is readable in video

---

## 🎥 What It Visualizes

* Project journey from first commit → latest
* Feature additions and bug fixes
* File-level evolution (added / modified / removed)
* Major development breakthroughs
* Documentation changes and growth

---

## ⚡ Installation

```bash
git clone https://github.com/YOUR_USERNAME/gitstory-ai
cd gitstory-ai

pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py --repo https://github.com/user/repo
```

Optional output file:

```bash
python main.py --repo https://github.com/user/repo --output myvideo.mp4
```

---

## 🎬 Output

```
gitstory.mp4
```

A cinematic timeline video showing your repository evolution.

---

## 🧠 Example Story Output

```
🚀 New functionality expanded the system  
📦 Added: auth.py, api.py  

⚔️ Issues were resolved to stabilize the project  
🛠️ Modified: main.py  

📘 Documentation evolved and shaped the project  
```

---

## 💡 Use Cases

* 🎥 YouTube developer content
* 📊 Project demos and presentations
* 🧠 Learning Git visually
* 🚀 Portfolio storytelling
* 📢 Open-source project promotion

---

## 🛠 Tech Stack

* Python
* GitPython
* MoviePy
* Matplotlib
* Pillow

---

## 🧩 How It Works

```
GitHub Repo
   ↓
Commit History Extraction
   ↓
Event Classification (feature / fix / readme / etc.)
   ↓
Story Conversion
   ↓
Frame Generation
   ↓
Video Rendering (MP4)
```

---

## ❤️ Support This Project

If you have got even 1 dollar to support, please do:
https://www.krishnamohanproductions.com/donate

Donate me : https://buymeacoffee.com/krishnamohanz

---

## 👨‍💻 Author

**Krishnamohan Yagneswaran**

---

## ⭐ Star This Repo

If you like this project, please consider giving it a star ⭐
It helps the project grow and reach more developers.

---

## 📌 Future Improvements

* 🎙️ AI voice narration
* 🎵 Background music
* 🎬 Smooth animations and transitions
* 🌐 Web-based version (paste repo → download video)
* 📊 Advanced analytics (commit heatmaps, graphs)

---
