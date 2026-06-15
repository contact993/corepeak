"""Draw the PikaXPS mascot app icon (a round pika sitting on a spectral peak) and
emit build_scripts/icon_1024.png, icon.icns (via iconutil) and icon.ico (Pillow)."""
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw

D = Path(__file__).parent
SS = 2                      # supersample for smooth edges
SZ = 1024 * SS

# native pika coords (≈120×130) → logical 1024 canvas
SX, OX, OY = 5.2, 200, 178
def X(x): return (OX + x * SX) * SS
def Y(y): return (OY + y * SX) * SS
def W(r): return r * SX * SS

img = Image.new("RGBA", (SZ, SZ), (0, 0, 0, 0))
dr = ImageDraw.Draw(img)

BODY, BODY_LN, BELLY = (215, 201, 180, 255), (183, 168, 143, 255), (236, 227, 210, 255)
ROSE, EYE = (224, 163, 154, 255), (35, 43, 56, 255)

# rounded-square dark tile
dr.rounded_rectangle([18 * SS, 18 * SS, 1006 * SS, 1006 * SS], radius=232 * SS, fill=(14, 20, 28, 255))
dr.rounded_rectangle([18 * SS, 18 * SS, 1006 * SS, 1006 * SS], radius=232 * SS, outline=(255, 255, 255, 26), width=int(3 * SS))

# spectral peak the pika sits on
curve = [(X(x), Y(120 - 48 * math.exp(-((x - 60) / 15.0) ** 2))) for x in range(6, 115)]
dr.polygon([(X(6), Y(120))] + curve + [(X(114), Y(120))], fill=(40, 74, 140, 255))
dr.line(curve, fill=(79, 140, 255, 255), width=int(W(2.6)), joint="curve")

# ears (rotated, behind the head)
def ear(cx, cy, ang):
    pad = int(W(26))
    w = int(W(13) * 2) + pad
    h = int(W(18) * 2) + pad
    tmp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    td = ImageDraw.Draw(tmp)
    td.ellipse([w / 2 - W(13), h / 2 - W(18), w / 2 + W(13), h / 2 + W(18)], fill=BODY, outline=BODY_LN, width=int(W(1.4)))
    td.ellipse([w / 2 - W(6.5), h / 2 - W(10), w / 2 + W(6.5), h / 2 + W(10)], fill=ROSE)
    tmp = tmp.rotate(ang, resample=Image.BICUBIC, expand=True)
    img.alpha_composite(tmp, (int(X(cx) - tmp.width / 2), int(Y(cy) - tmp.height / 2)))

ear(40, 28, 16)
ear(80, 28, -16)

# body + belly
dr.ellipse([X(21), Y(12), X(99), Y(118)], fill=BODY, outline=BODY_LN, width=int(W(1.6)))
dr.ellipse([X(34), Y(59), X(86), Y(117)], fill=BELLY)

# blush (translucent) on its own layer
blush = Image.new("RGBA", (SZ, SZ), (0, 0, 0, 0))
bd = ImageDraw.Draw(blush)
bd.ellipse([X(26), Y(75), X(42), Y(85)], fill=(224, 163, 154, 120))
bd.ellipse([X(78), Y(75), X(94), Y(85)], fill=(224, 163, 154, 120))
img.alpha_composite(blush)

# front paws
dr.ellipse([X(38), Y(105.5), X(54), Y(118.5)], fill=BODY, outline=BODY_LN, width=int(W(1.3)))
dr.ellipse([X(66), Y(105.5), X(82), Y(118.5)], fill=BODY, outline=BODY_LN, width=int(W(1.3)))

# eyes + highlights
dr.ellipse([X(40), Y(59), X(52), Y(73)], fill=EYE)
dr.ellipse([X(68), Y(59), X(80), Y(73)], fill=EYE)
dr.ellipse([X(46.5), Y(60), X(50.5), Y(64)], fill=(255, 255, 255, 255))
dr.ellipse([X(74.5), Y(60), X(78.5), Y(64)], fill=(255, 255, 255, 255))

# nose + mouth
dr.polygon([(X(55), Y(77)), (X(65), Y(77)), (X(60), Y(85))], fill=(199, 127, 117, 255))
dr.arc([X(51), Y(82), X(60), Y(90)], 20, 110, fill=(154, 138, 108, 255), width=int(W(1.5)))
dr.arc([X(60), Y(82), X(69), Y(90)], 70, 160, fill=(154, 138, 108, 255), width=int(W(1.5)))

# whiskers
for x1, y1, x2, y2 in [(30, 74, 12, 70), (30, 79, 11, 79), (30, 84, 13, 88),
                       (90, 74, 108, 70), (90, 79, 109, 79), (90, 84, 107, 88)]:
    dr.line([X(x1), Y(y1), X(x2), Y(y2)], fill=(183, 168, 143, 200), width=int(W(1)))

icon = img.resize((1024, 1024), Image.LANCZOS)
icon.save(D / "icon_1024.png")
print("icon_1024.png ok")

# .icns via iconutil
iconset = D / "icon.iconset"
iconset.mkdir(exist_ok=True)
for px, names in [(16, ["16x16"]), (32, ["16x16@2x", "32x32"]), (64, ["32x32@2x"]),
                  (128, ["128x128"]), (256, ["128x128@2x", "256x256"]),
                  (512, ["256x256@2x", "512x512"]), (1024, ["512x512@2x"])]:
    r = icon.resize((px, px), Image.LANCZOS)
    for n in names:
        r.save(iconset / f"icon_{n}.png")
subprocess.run(["iconutil", "-c", "icns", str(iconset), "-o", str(D / "icon.icns")], check=True)
print("icon.icns ok")

# .ico (Pillow multi-size)
icon.save(D / "icon.ico", format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
print("icon.ico ok")
