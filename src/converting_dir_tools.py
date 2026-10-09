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
                match target_ext:
                    case "ogg":
                        pass
                    case "wav":
                        pass
                    case "mp3":
                        pass
            case "ogg":
                match target_ext:
                    case "flac":
                        pass
                    case "wav":
                        pass
                    case "mp3":
                        pass
            case "wav":
                match target_ext:
                    case "flac":
                        pass
                    case "ogg":
                        pass
                    case "mp3":
                        pass
            case "mp3":
                match target_ext:
                    case "flac":
                        pass
                    case "ogg":
                        pass
                    case "wav":
                        pass

    files_list = utils.get_files_list(audios_dir, f".{og_ext}")
    convert_funtion = choose_convert_function(og_ext, target_ext)

    for file_path in files_list:
        convert_funtion(file_path)

        if not del_flag:
            continue
        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)
