from pathlib import Path
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()



def HEICtoPNG(image_path: Path) -> None:
    try:
        heic_image = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path}")

    print("Converting:", image_path.name)
    new_filename = image_path.stem + ".png"
    new_filepath = image_path.parent / new_filename
    heic_image.save(new_filepath, format = "png")


def HEICtoJPG(image_path: Path) -> None:
    try:
        img = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    print("Converting:", image_path.name)
    new_filename = image_path.stem + ".jpg"
    new_filepath = image_path.parent / new_filename
    img.save(new_filepath, format="JPEG")


def PNGtoJPG(image_path: Path) -> None:
    try:
        png_image = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    print("Converting:", image_path.name)
    rgb_image = png_image.convert("RGB")
    new_filename = image_path.stem + ".jpg"
    new_filepath = image_path.parent / new_filename
    rgb_image.save(new_filepath, "JPEG")


def PNGtoHEIC(image_path: Path) -> None:
    try:
        png_image = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    print("Converting:", image_path.name)
    rgb_image = png_image.convert("RGB")
    new_filename = image_path.stem + ".heic"
    new_filepath = image_path.parent / new_filename
    rgb_image.save(new_filepath, "heif")


def JPGtoPNG(image_path: Path) -> None:
    try:
        jpg_image = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    print("Converting:", image_path.name)
    new_filename = image_path.stem + ".png"
    new_filepath = image_path.parent / new_filename
    jpg_image.save(new_filepath, "PNG")


def JPGtoHEIC(image_path: Path) -> None:
    try:
        jpg_image = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    print("Converting:", image_path.name)
    rgb_image = jpg_image.convert("RGB")
    new_filename = image_path.stem + ".heic"
    new_filepath = image_path.parent / new_filename
    rgb_image.save(new_filepath, "heif")
