"""Create web-sized images from the source portfolio material."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


PROJECT_DIR = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_DIR.parent / "素材"
OUTPUT_DIR = PROJECT_DIR / "assets" / "images"

IMAGE_JOBS = {
    "脑电PCB.png": ("eeg-hardware.webp", 1800),
    "脑电采集实验.png": ("eeg-experiment.webp", 2000),
    "电刺激PCB.png": ("electrical-stimulation-hardware.webp", 1800),
    "电刺激实验.png": ("electrical-stimulation-experiment.webp", 2000),
    "alfa1.png": ("alpha-montage.webp", 1800),
    "alfa2.png": ("alpha-protocol.webp", 2200),
    "alfa3.png": ("alpha-results.webp", 2200),
    "ssvep1.png": ("ssvep-protocol.webp", 2200),
    "ssvep2.png": ("ssvep-results.webp", 2200),
}


def resize_to_width(image: Image.Image, target_width: int) -> Image.Image:
    if image.width <= target_width:
        return image.copy()
    target_height = round(image.height * target_width / image.width)
    return image.resize((target_width, target_height), Image.Resampling.LANCZOS)


def redact_badge(image: Image.Image) -> Image.Image:
    """Blur the ID badge visible on the left side of the experiment photo."""
    image = image.copy()
    left = round(image.width * 0.095)
    top = round(image.height * 0.405)
    right = round(image.width * 0.168)
    bottom = round(image.height * 0.475)
    blurred = image.filter(ImageFilter.GaussianBlur(42))
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        (left, top, right, bottom),
        radius=round(image.width * 0.012),
        fill=255,
    )
    mask = mask.filter(ImageFilter.GaussianBlur(20))
    return Image.composite(blurred, image, mask)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for source_name, (output_name, target_width) in IMAGE_JOBS.items():
        source_path = SOURCE_DIR / source_name
        if not source_path.exists():
            raise FileNotFoundError(source_path)
        with Image.open(source_path) as source:
            image = source.convert("RGB")
            if source_name == "脑电采集实验.png":
                image = redact_badge(image)
            image = resize_to_width(image, target_width)
            output_path = OUTPUT_DIR / output_name
            image.save(output_path, "WEBP", quality=84, method=6)
            print(f"{source_name} -> {output_path.name} ({image.width}x{image.height})")


if __name__ == "__main__":
    main()
