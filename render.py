from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

root = Path(__file__).parent
im = Image.open(root / 'source-art.png').convert('RGB')
draw = ImageDraw.Draw(im)
navy = (18, 40, 58)
cream = (247, 235, 207)
red = (191, 65, 48)
teal = (31, 106, 111)
white = (255, 249, 232)
font_regular = r'C:\Windows\Fonts\georgia.ttf'
font_bold = r'C:\Windows\Fonts\georgiab.ttf'
sans = r'C:\Windows\Fonts\arial.ttf'
sans_bold = r'C:\Windows\Fonts\arialbd.ttf'
def f(path, size): return ImageFont.truetype(path, size)

# Cover generated, non-factual ticker digits with a single accurate market callout.
draw.rounded_rectangle((980, 695, 1238, 904), radius=14, fill=navy, outline=cream, width=4)
draw.text((1004, 721), 'NASDAQ', font=f(sans_bold, 27), fill=cream)
draw.text((1000, 757), '−1.5%', font=f(font_bold, 58), fill=white)
draw.line((1005, 812, 1055, 798, 1103, 822, 1155, 833, 1214, 860), fill=red, width=8)
draw.polygon([(1214, 860), (1187, 842), (1183, 869)], fill=red)
draw.text((1003, 867), 'TUESDAY CLOSE', font=f(sans_bold, 17), fill=cream)

# Replace the generated, decorative ticker digits with a truthful Dow callout.
draw.rounded_rectangle((380, 626, 473, 751), radius=10, fill=navy, outline=cream, width=3)
draw.text((388, 648), 'DOW', font=f(sans_bold, 18), fill=cream)
draw.text((388, 680), '+0.9%', font=f(sans_bold, 25), fill=white)
draw.text((388, 716), 'TUE', font=f(sans_bold, 15), fill=cream)

# Date and headline in the reserved paper band.
draw.text((62, 22), 'WORLD DESK  /  TUESDAY, 24 NOVEMBER 2026', font=f(sans_bold, 22), fill=teal)
draw.text((60, 58), 'THREE SHOCKS, ONE DAY', font=f(font_bold, 48), fill=navy)
draw.line((62, 127, 1192, 127), fill=red, width=4)

# Three terse, factual captions in the bottom paper band.
cols = [62, 455, 846]
labels = [
    ('ZAPORIZHZHIA', '2 killed · 48 wounded', red),
    ('VATICAN', 'Francis’ private diary released', teal),
    ('MARKETS', 'Nasdaq −1.5% · Dow +0.9%', red),
]
for x, (head, sub, accent) in zip(cols, labels):
    draw.rounded_rectangle((x, 1090, x+12, 1214), radius=5, fill=accent)
    draw.text((x+25, 1092), head, font=f(sans_bold, 21), fill=accent)
    draw.text((x+25, 1125), sub, font=f(sans, 20), fill=navy)
    draw.text((x+25, 1163), 'WORLD NEWS  •  24 NOV', font=f(sans_bold, 15), fill=teal)

im = im.resize((1024, 1024), Image.Resampling.LANCZOS)
im.save(root / 'entry.png', 'JPEG', quality=86, optimize=True, progressive=True, subsampling=0)
print('wrote', im.size, (root / 'entry.png').stat().st_size, 'bytes')

