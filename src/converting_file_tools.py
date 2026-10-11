from pathlib import Path
from PIL import Image
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
import pillow_heif
import subprocess
import base64

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


def FLACtoOGG(audio_path: Path, quality: int) -> None:
    if quality < 0 or quality > 10:
        raise ValueError("Invalid quality")

    new_filepath = audio_path.with_suffix(".ogg")
    print("Converting:", audio_path.name)
    try:
        subprocess.run([
            "ffmpeg",
            "-i", str(audio_path),
            "-map", "0:a:0",
            "-map_metadata", "0",
            "-c:a", "libvorbis",
            "-q:a", str(quality),
            "-y", str(new_filepath)],
            check=True,
            capture_output=True,
            text=True)
    except Exception as e:
        raise Exception(e)

    source = FLAC(audio_path)
    target = OggVorbis(new_filepath)

    pictures = [
        base64.b64encode(picture.write()).decode("ascii")
        for picture in source.pictures]
    if pictures:
        target["metadata_block_picture"] = pictures
    target.save()


def FLACtoWAV(audio_path: Path, ignore_arg) -> None:
    new_filepath = audio_path.with_suffix(".wav")
    print("Converting:", audio_path.name)
    try:
        subprocess.run([
            "ffmpeg",
            "-i", str(audio_path),
            "-map", "0:a:0",
            "-map_metadata", "0",
            "-c:a", "libvorbis",
            "-y", str(new_filepath)],
            check=True,
            capture_output=True,
            text=True)
    except Exception as e:
        raise Exception(e)


def FLACtoMP3(audio_path: Path, quality: int) -> None:
    if quality < 0 or quality > 9:
        raise ValueError("Invalid quality")

    new_filepath = audio_path.with_suffix(".mp3")
    print("Converting:", audio_path.name)
    try:
        subprocess.run([
            "ffmpeg",
            "-i", str(audio_path),
            "-map", "0:a:0",
            "-map", "0:v?",
            "-map_metadata", "0",
            "-c:a", "libmp3lame",
            "-q:a", str(quality),
            "-c:v", "mjpeg",
            "-id3v2_version", "3",
            "-y", str(new_filepath)],
            check=True,
            capture_output=True,
            text=True)
    except Exception as e:
        raise Exception(e)


def OGGtoFLAC(audio_path: Path) -> None:
    return


def OGGtoWAV(audio_path: Path) -> None:
    return


def OGGtoMP3(audio_path: Path) -> None:
    return


def WAVtoFLAC(audio_path: Path, ignore_arg) -> None:
    new_filepath = audio_path.with_suffix(".flac")
    print("Converting:", audio_path.name)
    try:
        subprocess.run([
            "ffmpeg",
            "-i", str(audio_path),
            "-map", "0:a:0",
            "-map_metadata", "0",
            "-c:a", "flac",
            "-y", str(new_filepath)],
        check=True,
        capture_output=True,
        text=True)
    except Exception as e:
        raise Exception(e)


def WAVtoOGG(audio_path: Path, quality: int) -> None:
    if quality < 0 or quality > 10:
        raise ValueError("Invalid quality")

    new_filepath = audio_path.with_suffix(".ogg")
    print("Converting:", audio_path.name)
    try:
        subprocess.run([
            "ffmpeg",
            "-i", str(audio_path),
            "-map", "0:a:0",
            "-map_metadata", "0",
            "-c:a", "libvorbis",
            "-q:a", str(quality),
            "-y", str(new_filepath)],
        check=True,
        capture_output=True,
        text=True)
    except Exception as e:
        raise Exception(e)


def WAVtoMP3(audio_path: Path, quality: int) -> None:
    if quality < 0 or quality > 9:
        raise ValueError("Invalid quality")

    new_filepath = audio_path.with_suffix(".mp3")
    print("Converting:", audio_path.name)
    try:
        subprocess.run([
            "ffmpeg",
            "-i", str(audio_path),
            "-map", "0:a:0",
            "-map_metadata", "0",
            "-c:a", "libmp3lame",
            "-q:a", str(quality),
            "-y", str(new_filepath)],
        check=True,
        capture_output=True,
        text=True)
    except Exception as e:
        raise Exception(e)


def MP3toFLAC(audio_path: Path) -> None:
    return


def MP3toOGG(audio_path: Path) -> None:
    return


def MP3toWAV(audio_path: Path) -> None:
    return
