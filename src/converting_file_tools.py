from pathlib import Path
from PIL import Image
from mutagen.id3 import (ID3, APIC, ID3NoHeaderError, TIT2, TPE1, TALB, TCON, TDRC, TRCK, TPOS, TCOM, TPE2, TXXX)
from mutagen.flac import FLAC, Picture
from mutagen.oggvorbis import OggVorbis
from mutagen.wave import WAVE
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


def FLACtoWAV(audio_path: Path, ignore_arg = None) -> None:
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


def OGGtoFLAC(audio_path: Path, ignore_arg = None) -> None:
    new_filepath = audio_path.with_suffix(".flac")
    print("Converting:", audio_path.name)
    subprocess.run([
        "ffmpeg",
        "-i", str(audio_path),
        "-map", "0:a:0",
        "-c:a", "flac",
        "-y", str(new_filepath)],
    check=True,
    capture_output=True,
    text=True)

    source = OggVorbis(audio_path)
    encoded_pictures = source.get("METADATA_BLOCK_PICTURE", [])
    target = FLAC(new_filepath)
    for key, values in source.items():
        if key.upper() != "METADATA_BLOCK_PICTURE":
            target[key] = values

    target.clear_pictures()
    for item in encoded_pictures:
        picture = Picture(base64.b64decode(item))
        target.add_picture(picture)

    target.save()


def OGGtoWAV(audio_path: Path, ignore_arg = None) -> None:
    new_filepath = audio_path.with_suffix(".wav")
    print("Converting:", audio_path.name)
    subprocess.run([
            "ffmpeg",
            "-i", str(audio_path),
            "-map", "0:a:0",
            "-c:a", "pcm_s16le",
            "-y", str(new_filepath)],
        check=True,
        capture_output=True,
        text=True)

    source = OggVorbis(audio_path)
    target = WAVE(new_filepath)
    if target.tags is None:
        target.add_tags()

    for key, values in source.items():
        if key.upper() != "METADATA_BLOCK_PICTURE":
            target.tags[key] = values

    target.save()


def OGGtoMP3(audio_path: Path, quality: int) -> None:
    if quality < 0 or quality > 9:
        raise ValueError("Invalid quality")

    new_filepath = audio_path.with_suffix(".mp3")
    print("Converting:", audio_path.name)
    subprocess.run([
        "ffmpeg",
        "-i", str(audio_path),
        "-map", "0:a:0",
        "-c:a", "libmp3lame",
        "-q:a", str(quality),
        "-y", str(new_filepath)],
        check=True,
        capture_output=True,
        text=True)

    source = OggVorbis(audio_path)

    try:
        tags = ID3(new_filepath)
    except ID3NoHeaderError:
        tags = ID3()

    frame_map = {
        "title": TIT2,
        "artist": TPE1,
        "album": TALB,
        "genre": TCON,
        "date": TDRC,
        "year": TDRC,
        "tracknumber": TRCK,
        "discnumber": TPOS,
        "composer": TCOM,
        "albumartist": TPE2}

    for key, values in source.items():
        normalized = key.lower()

        if normalized == "metadata_block_picture":
            continue

        frame_class = frame_map.get(normalized)
        if frame_class:
            tags.delall(frame_class.__name__)

            tags.add(frame_class(encoding=3, text=values))
        else:
            # Preserve unrecognized Vorbis comments as custom ID3 tags.
            tags.add(
                TXXX(
                    encoding=3,
                    desc=key,
                    text=values,
                )
            )

    tags.delall("APIC")
    encoded_pictures = source.get("METADATA_BLOCK_PICTURE", [])

    for item in encoded_pictures:
        picture = Picture(base64.b64decode(item))

        tags.add(APIC(
            encoding=3,
            mime=picture.mime,
            type=picture.type,
            desc=picture.desc,
            data=picture.data))

    tags.save(new_filepath, v2_version=4)


def WAVtoFLAC(audio_path: Path, ignore_arg = None) -> None:
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


def get_mp3_pic_data(source_path: Path) -> list[Picture]:
    tags = ID3(source_path)
    pictures = []

    for frame in tags.getall("APIC"):
        picture = Picture()
        picture.data = frame.data
        picture.mime = frame.mime
        picture.type = frame.type
        picture.desc = frame.desc
        picture.width = 0
        picture.height = 0
        picture.depth = 0
        picture.colors = 0
        pictures.append(picture)

    return pictures


def MP3toFLAC(audio_path: Path, ignore_arg = None) -> None:
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

    pictures = get_mp3_pic_data(audio_path)
    target = FLAC(new_filepath)
    target.clear_pictures()

    for picture in pictures:
        target.add_picture(picture)
    target.save()


def MP3toOGG(audio_path: Path, quality: int) -> None:
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

    pictures = get_mp3_pic_data(audio_path)
    target = OggVorbis(new_filepath)
    key = "METADATA_BLOCK_PICTURE"
    if key in target:
        del target[key]

    target[key] = [
        base64.b64encode(picture.write()).decode("ascii")
        for picture in pictures]
    target.save()


def MP3toWAV(audio_path: Path, ignore_arg = None) -> None:
    new_filepath = audio_path.with_suffix(".wav")
    print("Converting:", audio_path.name)
    try:
        subprocess.run([
            "ffmpeg",
            "-i", str(audio_path),
            "-map", "0:a:0",
            "-map_metadata", "0",
            "-c:a", "pcm_s16le",
            "-y", str(new_filepath)],
        check=True,
        capture_output=True,
        text=True)
    except Exception as e:
        raise Exception(e)
