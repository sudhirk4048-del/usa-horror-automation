from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

os.makedirs("output", exist_ok=True)

title = "THE HOUSE THAT WHISPERED"
story = [
    "At 3 AM, Emily heard someone whispering her name.",
    "She lived alone in an abandoned house.",
    "The whisper came from behind a locked door.",
    "She opened it slowly. There was nobody inside.",
    "Then her phone rang. The caller ID showed her own name.",
    "A voice whispered: DO NOT TURN AROUND.",
    "Emily slowly looked behind her...",
    "And saw herself smiling in the darkness."
]

W, H = 1080, 1920

try:
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48
    )
except OSError:
    font = ImageFont.load_default()

for i, line in enumerate(story, start=1):
    img = Image.new("RGB", (W, H), (12, 12, 18))
    draw = ImageDraw.Draw(img)

    draw.text((60, 100), title, fill=(220, 30, 30), font=font)

    wrapped = textwrap.fill(line, width=28)
    draw.multiline_text(
        (80, 800), wrapped,
        fill=(245, 245, 245),
        font=font,
        spacing=25,
        align="center"
    )

    draw.text(
        (80, 1750), f"SCENE {i}/{len(story)}",
        fill=(180, 180, 180),
        font=font
    )

    img.save(f"output/scene_{i:02d}.png")

print("Horror story scenes created successfully!")
