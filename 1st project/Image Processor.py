from pathlib import Path
from PIL import Image, ImageOps


root = Path("../images").resolve()
output = Path("../outputs").resolve()

output.mkdir(parents=True, exist_ok=True)

EXT = {".png", ".jpg", ".jpeg"}
images = sorted(
    path for path in root.rglob("*")
    if path.is_file() and path.suffix.lower() in EXT
)

counter = 0

for path in images:
    with Image.open(path) as image:

        thumb = image.copy()
        thumb.thumbnail((160, 160))

        thumb.save(
            output / f"{path.stem}_thumb.jpg",
            quality=90
        )

        gray = image.convert("L")

        gray.save(
            output / f"{path.stem}_gray.png"
        )

        mirror = ImageOps.mirror(image)

        mirror.save(
            output / f"{path.stem}_mirror.jpg",
            quality=90
        )

        counter += 1

    print(f"Successfully processed: {counter} out of {len(images)} files")




