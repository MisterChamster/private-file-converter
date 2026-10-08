import os
from pathlib import Path
from typing import Literal

import src.converting_file_tools as conv_file
import src.utils as utils



def conv_HEICs_dir(
        images_dir: Path,
        target_ext: Literal["png", "jpg"],
        del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".heic")

    for file_path in files_list:
        if target_ext == "png":
            conv_file.HEICtoPNG(file_path)
        elif target_ext == "jpg":
            conv_file.HEICtoJPG(file_path)

        if not del_flag:
            return
        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)


def conv_PNGs_dir(
        images_dir: Path,
        target_ext: Literal["jpg", "heic"],
        del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".png")

    for file_path in files_list:
        if target_ext == "jpg":
            conv_file.PNGtoJPG(file_path)
        elif target_ext == "heic":
            conv_file.PNGtoHEIC(file_path)

        if not del_flag:
            return
        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)


def conv_JPGs_dir(
        images_dir: Path,
        target_ext: Literal["png", "heic"],
        del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".jpg")

    for file_path in files_list:
        if target_ext == "png":
            conv_file.JPGtoPNG(file_path)
        elif target_ext == "heic":
            conv_file.JPGtoHEIC(file_path)

        if not del_flag:
            return
        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)
