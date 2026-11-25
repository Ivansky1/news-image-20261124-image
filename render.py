"""Render the editorial labels over the supplied illustration."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source-art.png"
DESTINATION = ROOT / "entry.png"


def font(size: int, *, bold: bool = False, serif: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = []
    if serif:
        candidates.append("C:/Windows/Fonts/georgiab.ttf" if bold else "C:/Windows/Fonts/georgia.ttf")
    else:
        candidates.append("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf")
    candidates.append("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"The source illustration is missing: {SOURCE.name}")

    image = Image.open(SOURCE).convert("RGB")
    draw = ImageDraw.Draw(image)
    navy = (18, 40, 58)
    cream = (247, 235, 207)
    red = (191, 65, 48)
    teal = (31, 106, 111)
    white = (255, 249, 232)

    # Replace decorative ticker numbers with the reported market moves.
    draw.rounded_rectangle((980, 695, 1238, 904), radius=14, fill=navy, outline=cream, width=4)
    draw.text((1004, 721), "NASDAQ", font=font(27, bold=True), fill=cream)
    draw.text((1000, 757), "−1.5%", font=font(58, bold=True, serif=True), fill=white)
    draw.line((1005, 838, 1055, 834, 1103, 845, 1155, 850, 1214, 858), fill=red, width=8)
    draw.polygon(((1214, 858), (1187, 842), (1183, 868)), fill=red)
    draw.text((1003, 867), "TUESDAY CLOSE", font=font(17, bold=True), fill=cream)

    draw.rounded_rectangle((468, 780, 604, 919), radius=10, fill=navy, outline=cream, width=3)
    draw.text((484, 800), "DOW", font=font(22, bold=True), fill=cream)
    draw.text((484, 837), "+0.9%", font=font(33, bold=True), fill=white)
    draw.text((484, 883), "TUESDAY", font=font(16, bold=True), fill=cream)

    draw.text((62, 22), "WORLD DESK  /  TUESDAY, 24 NOVEMBER 2026", font=font(22, bold=True), fill=teal)
    draw.text((60, 58), "THREE SHOCKS, ONE DAY", font=font(48, bold=True, serif=True), fill=navy)
    draw.line((62, 127, 1192, 127), fill=red, width=4)

    stories = (
        (62, "ZAPORIZHZHIA", "2 killed · 48 wounded", red),
        (455, "VATICAN", "Francis’ private diary released", teal),
        (846, "MARKETS", "Nasdaq −1.5% · Dow +0.9%", red),
    )
    for left, heading, detail, accent in stories:
        draw.rounded_rectangle((left, 1090, left + 12, 1214), radius=5, fill=accent)
        draw.text((left + 25, 1092), heading, font=font(21, bold=True), fill=accent)
        draw.text((left + 25, 1125), detail, font=font(20), fill=navy)
        draw.text((left + 25, 1163), "WORLD NEWS  •  24 NOV", font=font(15, bold=True), fill=teal)

    image = image.resize((1024, 1024), Image.Resampling.LANCZOS)
    image.save(DESTINATION, "JPEG", quality=86, optimize=True, progressive=True, subsampling=0)
    print(f"Wrote {DESTINATION.name}: {image.width}×{image.height}, {DESTINATION.stat().st_size} bytes")


if __name__ == "__main__":
    main()
