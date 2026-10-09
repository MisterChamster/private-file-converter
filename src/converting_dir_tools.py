import os
from pathlib import Path
from typing import Literal
from collections.abc import Callable

import src.converting_file_tools as conv_file
import src.utils as utils



def conv_images_dir(
        images_dir: Path,
        og_ext: Literal["jpg", "png", "heic"],
        target_ext: Literal["jpg", "png", "heic"],
        del_flag: bool = False) -> None:
    if og_ext == target_ext:
        raise ValueError("Cannot convert file type to itself.")

    def choose_convert_function(
            og_ext: Literal["jpg", "png", "heic"],
            target_ext: Literal["jpg", "png", "heic"]) -> Callable[[Path], None]:
        match og_ext:
            case "heic":
                match target_ext:
                    case "png":
                        return conv_file.HEICtoPNG
                    case "jpg":
                        return conv_file.HEICtoJPG
            case "png":
                match target_ext:
                    case "heic":
                        return conv_file.PNGtoHEIC
                    case "jpg":
                        return conv_file.PNGtoJPG
            case "jpg":
                match target_ext:
                    case "png":
                        return conv_file.JPGtoPNG
                    case "heic":
                        return conv_file.JPGtoHEIC

    files_list = utils.get_files_list(images_dir, f".{og_ext}")
    convert_funtion = choose_convert_function(og_ext, target_ext)

    for file_path in files_list:
        convert_funtion(file_path)

        if not del_flag:
            continue
        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)


def conv_FLACs_dir(
        images_dir: Path,
        target_ext: Literal["ogg", "wav", "mp3"],
        del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".flac")
    pass


def conv_OGGs_dir(
        images_dir: Path,
        target_ext: Literal["flac", "wav", "mp3"],
        del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".ogg")
    pass


def conv_WAVs_dir(
        images_dir: Path,
        target_ext: Literal["flac", "ogg", "mp3"],
        del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".wav")
    pass


def conv_MP3s_dir(
        images_dir: Path,
        target_ext: Literal["flac", "ogg", "wav"],
        del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".mp3")
    pass
