from pathlib import Path
import pillow_heif

import src.askers.askers_renaming as ask_rnm
import src.renaming_tools as rnm_tools
import src.utils as utils

pillow_heif.register_heif_opener()



def rename_images_onebyone_loop(
    dir_path: Path,
    naming_style: str
) -> bool:
    date_types = {
        "date_time_original": "EXIF_DTO",
        "date_time_digitized": "EXIF_DTD",
        "date_time": "EXIF_DT",
        "file_creation": "FILE_CREAT",
        "file_modification": "FILE_MOD"}
    exit_flags = {
        "return": False,
        "exit": True}
    valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.heic')

    print()
    files_list = utils.get_files_list(dir_path)
    for file_path in files_list:
        if file_path.suffix.lower() in valid_extensions:
            action = ""
            print()

            if action in date_types:
                rnm_tools.rename_image_with_style(
                    file_path,
                    date_types[action],
                    naming_style)
                print("\n\n")

            elif action in exit_flags:
                return exit_flags[action]
    print("All files have been considered.\n")


def rename_all_images_loop(
    dir_path: Path,
    date_type: str,
    naming_style: str
) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ""
        print()

        if action == "list_images_new_names":
            rnm_tools.list_images_with_dates(dir_path, date_type, naming_style)
            print("\n")

        elif action == "rename_all_images":
            rnm_tools.rename_images_in_dir(dir_path, date_type, naming_style)
            print("\n")

        elif action in exit_flags:
            return exit_flags[action]


def rename_basis_loop(
        dir_path: Path,
        naming_style: str
        ) -> bool:
    date_types = {
        "date_time_original": "EXIF_DTO",
        "date_time_digitized": "EXIF_DTD",
        "date_time": "EXIF_DT",
        "file_creation": "FILE_CREAT",
        "file_modification": "FILE_MOD"}
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ""
        print("\n")

        if action in date_types:
            exit_flag = rename_all_images_loop(
                dir_path,
                date_types[action],
                naming_style)
            if exit_flag:
                return exit_flags["exit"]

        elif action in exit_flags:
            return exit_flags[action]


def rename_actionloop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}
    styles_dict = {
        "iso": "IMG_[Y][M][D]_[H][M][S]",
        "eu":  "IMG_[D][M][Y]_[H][M][S]",
        "us":  "IMG_[M][D][Y]_[H][M][S]"}
    naming_style = "iso"

    while True:
        action = ""

        if action == "rename_one_by_one":
            exit_flag = rename_images_onebyone_loop(dir_path, naming_style)
            if exit_flag:
                return exit_flags["exit"]

        elif action == "rename_all_images":
            exit_flag = rename_basis_loop(dir_path, naming_style)
            if exit_flag:
                return exit_flags["exit"]
