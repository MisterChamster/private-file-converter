from pathlib import Path
from typing import Literal
from PIL import Image
from mutagen.id3 import (ID3, APIC, ID3NoHeaderError, TIT2, TPE1, TALB, TCON, TDRC, TRCK, TPOS, TCOM, TPE2, TXXX)
from mutagen.flac import FLAC, Picture
from mutagen.oggvorbis import OggVorbis
from mutagen.wave import WAVE
import pillow_heif
import subprocess
import base64

pillow_heif.register_heif_opener()



def convertHEIC(
        image_path: Path,
        target_ext: Literal["png", "jpg"]) -> None:
    try:
        heic_image = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    new_filename = image_path.stem + f".{target_ext}"
    new_filepath = image_path.parent / new_filename

    print("Converting:", image_path.name)
    if target_ext == "jpg":
        heic_image.save(new_filepath, format="JPEG")
    elif target_ext == "png":
        heic_image.save(new_filepath, format="png")


def convertPNG(
        image_path: Path,
        target_ext: Literal["jpg", "heic"]) -> None:
    try:
        png_image = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    new_filename = image_path.stem + f".{target_ext}"
    new_filepath = image_path.parent / new_filename

    print("Converting:", image_path.name)
    rgb_image = png_image.convert("RGB")
    if target_ext == "jpg":
        rgb_image.save(new_filepath, "JPEG")
    elif target_ext == "heic":
        rgb_image.save(new_filepath, "heif")


def convertJPG(
        image_path: Path,
        target_ext: Literal["png", "heic"]) -> None:
    try:
        jpg_image = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    new_filename = image_path.stem + f".{target_ext}"
    new_filepath = image_path.parent / new_filename

    print("Converting:", image_path.name)
    if target_ext == "png":
        jpg_image.save(new_filepath, "PNG")
    elif target_ext == "heic":
        rgb_image = jpg_image.convert("RGB")
        rgb_image.save(new_filepath, "heif")


def is_quality_valid(quality: int, extension: Literal["flac", "ogg", "wav", "mp3"]) -> bool:
    if extension in ["flac", "wav"]:
        return True
    if quality < 0:
        return False
    if extension == "ogg" and quality > 10:
        return False
    if extension == "mp3" and quality > 9:
        return False
    return True


def convertFLAC(audio_path: Path,
                target_ext: Literal["ogg", "wav", "mp3"],
                quality: int| None = None) -> None:
    if not is_quality_valid(quality, target_ext):
        raise ValueError("Invalid quality")

    new_filepath = audio_path.with_suffix(f".{target_ext}")
    print("Converting:", audio_path.name)

    if target_ext == "ogg":
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
    elif target_ext == "wav":
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
    elif target_ext == "mp3":
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


def convertOGG(audio_path: Path,
               target_ext: Literal["flac", "wav", "mp3"],
               quality: int| None = None) -> None:
    if not is_quality_valid(quality, target_ext):
        raise ValueError("Invalid quality")

    new_filepath = audio_path.with_suffix(f".{target_ext}")
    print("Converting:", audio_path.name)

    if target_ext == "flac":
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
    elif target_ext == "wav":
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
                target.tags.delall(frame_class.__name__)
                target.tags.add(
                    frame_class(encoding=3, text=values))
            else:
                target.tags.add(
                    TXXX(encoding=3, desc=key, text=values))

        target.save()
    elif target_ext == "mp3":
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
                tags.add(
                    TXXX(
                        encoding=3,
                        desc=key,
                        text=values))

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


def convertWAV(audio_path: Path,
               target_ext: Literal["flac", "ogg", "mp3"],
               quality: int| None = None) -> None:
    if not is_quality_valid(quality, target_ext):
        raise ValueError("Invalid quality")

    new_filepath = audio_path.with_suffix(f".{target_ext}")
    print("Converting:", audio_path.name)

    if target_ext == "flac":
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
    elif target_ext == "ogg":
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
    elif target_ext == "mp3":
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
    if not is_quality_valid(quality, "ogg"):
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
