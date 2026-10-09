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
                        return conv_file.FLACtoOGG
                    case "wav":
                        return conv_file.FLACtoWAV
                    case "mp3":
                        return conv_file.FLACtoMP3
            case "ogg":
                match target_ext:
                    case "flac":
                        return conv_file.OGGtoFLAC
                    case "wav":
                        return conv_file.OGGtoWAV
                    case "mp3":
                        return conv_file.OGGtoMP3
            case "wav":
                match target_ext:
                    case "flac":
                        return conv_file.WAVtoFLAC
                    case "ogg":
                        return conv_file.WAVtoOGG
                    case "mp3":
                        return conv_file.WAVtoMP3
            case "mp3":
                match target_ext:
                    case "flac":
                        return conv_file.MP3toFLAC
                    case "ogg":
                        return conv_file.MP3toOGG
                    case "wav":
                        return conv_file.MP3toWAV

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
