from moviepy.editor import ImageSequenceClip, CompositeVideoClip, ImageClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_watermark(text):
    # Create transparent image
    img = Image.new("RGBA", (800, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 28)
    except:
        font = ImageFont.load_default()

    draw.text((10, 10), text, font=font, fill=(255, 255, 255, 150))

    return np.array(img)


def create_video(frames, story, output_file):
    durations = []

    # 🧠 Smart timing
    for i in range(len(frames)):
        if i == 0:
            durations.append(4)
        else:
            text_len = len(story[i-1]["text"])
            durations.append(min(6, 2 + text_len / 80))

    # 🎬 Base video
    clip = ImageSequenceClip(frames, durations=durations)

    # 🏷️ WATERMARK IMAGE (SAFE)
    watermark_img = create_watermark("GitStory AI • Krishnamohan Yagneswaran")

    watermark = (
        ImageClip(watermark_img)
        .set_duration(clip.duration)
        .set_position(("right", "bottom"))
        .set_opacity(0.6)
    )

    # 🎥 Combine
    final = CompositeVideoClip([clip, watermark])

    # 🎬 Export
    final.write_videofile(
        output_file,
        codec="libx264",
        fps=24,
        audio=False
    )