from pathlib import Path

import src.utils as utils
import src.askers.askers_converting as ask_cnv
import src.converting_dir_tools as cnv



def convert_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_convert_action()
        print()

        if action == "convert_heic":
            print()
            pass
            exit_flag = conv_heic_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "convert_png":
            print()
            pass
            exit_flag = conv_png_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "convert_jpg":
            print()
            pass
            exit_flag = conv_jpg_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action in exit_flags:
            return exit_flags[action]


def conv_heic_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_htp_action()
        print()

        if action == "list_heic":
            utils.list_images_in_dir(dir_path, "heic")
            print("\n")

        elif action == "heic_to_png_no_del":
            cnv.HEICtoPNG_dir(dir_path)
            print("\n")

        elif action == "heic_to_png_del":
            cnv.HEICtoPNG_dir(dir_path, True)
            print("\n")

        elif action in exit_flags:
            return exit_flags[action]


def conv_png_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_htj_action()
        print()

        if action == "list_heic":
            utils.list_images_in_dir(dir_path, "heic")
            print("\n")

        elif action == "heic_to_jpg_no_del":
            cnv.HEICtoJPG_dir(dir_path)
            print("\n")

        elif action == "heic_to_jpg_del":
            cnv.HEICtoJPG_dir(dir_path, True)
            print("\n")

        elif action in exit_flags:
            return exit_flags[action]


def conv_jpg_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_ptj_action()
        print()

        if action == "list_png":
            utils.list_images_in_dir(dir_path, "png")
            print("\n")

        elif action == "png_to_jpg_no_del":
            cnv.PNGtoJPG_dir(dir_path)
            print("\n")

        elif action == "png_to_jpg_del":
            cnv.PNGtoJPG_dir(dir_path, True)
            print("\n")

        elif action in exit_flags:
            return exit_flags[action]
