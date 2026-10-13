import os
from pathlib import Path
from typing import Literal
from collections.abc import Callable

import src.converting_file_tools as conv_file
import src.utils as utils
import src.askers.askers_converting as ask_conv



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
                return conv_file.convertHEIC
            case "png":
                return conv_file.convertPNG
            case "jpg":
                return conv_file.convertJPG

    files_list = utils.get_files_list(images_dir, f".{og_ext}")
    convert_funtion = choose_convert_function(og_ext, target_ext)

    for file_path in files_list:
        convert_funtion(file_path, target_ext)

        if not del_flag:
            continue
        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)


def conv_audios_dir(
        audios_dir: Path,
        og_ext: Literal["flac", "ogg", "wav", "mp3"],
        target_ext: Literal["flac", "ogg", "wav", "mp3"],
        del_flag: bool = False) -> None:
    if og_ext == target_ext:
        raise ValueError("Cannot convert file type to itself.")

    def choose_convert_function(
        og_ext: Literal["flac", "ogg", "wav", "mp3"],
        target_ext: Literal["flac", "ogg", "wav", "mp3"]) -> Callable[[Path], None]:
        match og_ext:
            case "flac":
                return conv_file.convertFLAC
            case "ogg":
                return conv_file.convertOGG
            case "wav":
                return conv_file.convertWAV
            case "mp3":
                match target_ext:
                    case "flac":
                        return conv_file.MP3toFLAC
                    case "ogg":
                        return conv_file.MP3toOGG
                    case "wav":
                        return conv_file.MP3toWAV

    if target_ext in ["mp3", "ogg"]:
        quality = ask_conv.ask_lossy_quality(target_ext)
        print()
    else:
        quality = None
    files_list = utils.get_files_list(audios_dir, f".{og_ext}")
    convert_funtion = choose_convert_function(og_ext, target_ext)

    for file_path in files_list:
        convert_funtion(file_path, target_ext, quality)

        if not del_flag:
            continue
        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)
