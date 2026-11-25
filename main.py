"""Write the finished news image to the directory used by the make.fun runner."""

import os
import shutil
from pathlib import Path


def main() -> None:
    repository = Path(__file__).resolve().parent
    configured_output = os.environ.get("MAKEFUN_OUTPUT_DIR")
    output_dir = Path(configured_output) if configured_output else Path("/output")
    image_path = repository / "entry.png"

    if not image_path.is_file():
        raise FileNotFoundError(f"The entry image is missing: {image_path.name}")

    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(image_path, destination)


if __name__ == "__main__":
    main()
