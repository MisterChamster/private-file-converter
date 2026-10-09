from pathlib import Path

import src.utils as utils
import src.askers.askers_converting as ask_cnv
import src.converting_dir_tools as cnv

exit_flags = {
    "return": False,
    "exit": True}


def convert_images_loop(dir_path: Path) -> bool:
    while True:
        action = ask_cnv.ask_imgs_conv_action()
        print()

        if action == "convert_heic":
            print()
            exit_flag = conv_heic_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "convert_png":
            print()
            exit_flag = conv_png_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "convert_jpg":
            print()
            exit_flag = conv_jpg_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action in exit_flags:
            return exit_flags[action]


def conv_heic_loop(dir_path: Path) -> bool:
    while True:
        action = ask_cnv.ask_conv_heic_action()
        print()

        if action == "list_heic":
            utils.list_convable_images_in_dir(dir_path, "heic")
            print()

        elif action == "heic_to_png":
            del_og = ask_cnv.ask_del_og_files("heic")
            print()
            cnv.conv_images_dir(dir_path, "heic", "png", del_og)
            print()

        elif action == "heic_to_jpg":
            del_og = ask_cnv.ask_del_og_files("heic")
            print()
            cnv.conv_images_dir(dir_path, "heic", "jpg", del_og)
            print()

        elif action in exit_flags:
            return exit_flags[action]


def conv_png_loop(dir_path: Path) -> bool:
    while True:
        action = ask_cnv.ask_conv_png_action()
        print()

        if action == "list_png":
            utils.list_convable_images_in_dir(dir_path, "png")
            print()

        elif action == "png_to_jpg":
            del_og = ask_cnv.ask_del_og_files("png")
            print()
            cnv.conv_images_dir(dir_path, "png", "jpg", del_og)
            print()

        elif action == "png_to_heic":
            del_og = ask_cnv.ask_del_og_files("png")
            print()
            cnv.conv_images_dir(dir_path, "png", "heic", del_og)
            print()

        elif action in exit_flags:
            return exit_flags[action]


def conv_jpg_loop(dir_path: Path) -> bool:
    while True:
        action = ask_cnv.ask_conv_jpg_action()
        print()

        if action == "list_jpg":
            utils.list_convable_images_in_dir(dir_path, "jpg")
            print()

        elif action == "jpg_to_png":
            del_og = ask_cnv.ask_del_og_files("jpg")
            print()
            cnv.conv_images_dir(dir_path, "jpg", "png", del_og)
            print()

        elif action == "jpg_to_heic":
            del_og = ask_cnv.ask_del_og_files("jpg")
            print()
            cnv.conv_images_dir(dir_path, "jpg", "heic", del_og)
            print()

        elif action in exit_flags:
            return exit_flags[action]


def convert_audios_loop(dir_path: Path) -> bool:
    while True:
        action = ask_cnv.ask_aud_conv_action()
        print()

        if action == "convert_flac":
            print()
            exit_flag = conv_flac_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "convert_ogg":
            print()
            exit_flag = conv_ogg_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "convert_wav":
            print()
            exit_flag = conv_wav_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "convert_mp3":
            print()
            exit_flag = conv_mp3_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action in exit_flags:
            return exit_flags[action]


def conv_flac_loop(dir_path: Path) -> bool:
    while True:
        action = ask_cnv.ask_conv_flac_action()
        print()

        if action == "list_flac":
            utils.list_convable_audios_in_dir(dir_path, "flac")
            print()
        elif action == "flac_to_ogg":
            del_og = ask_cnv.ask_del_og_files("flac")
            print()
            cnv.conv_FLACs_dir(dir_path, "ogg", del_og)
            print()
        elif action == "flac_to_wav":
            del_og = ask_cnv.ask_del_og_files("flac")
            print()
            cnv.conv_FLACs_dir(dir_path, "wav", del_og)
            print()
        elif action == "flac_to_mp3":
            del_og = ask_cnv.ask_del_og_files("flac")
            print()
            cnv.conv_FLACs_dir(dir_path, "mp3", del_og)
            print()
        elif action in exit_flags:
            return exit_flags[action]


def conv_ogg_loop(dir_path: Path) -> bool:
    while True:
        action = ask_cnv.ask_conv_ogg_action()
        print()

        if action == "list_ogg":
            utils.list_convable_audios_in_dir(dir_path, "ogg")
            print()
        elif action == "ogg_to_flac":
            del_og = ask_cnv.ask_del_og_files("ogg")
            print()
            cnv.conv_OGGs_dir(dir_path, "flac", del_og)
            print()
        elif action == "ogg_to_wav":
            del_og = ask_cnv.ask_del_og_files("ogg")
            print()
            cnv.conv_OGGs_dir(dir_path, "wav", del_og)
            print()
        elif action == "ogg_to_mp3":
            del_og = ask_cnv.ask_del_og_files("ogg")
            print()
            cnv.conv_OGGs_dir(dir_path, "mp3", del_og)
            print()
        elif action in exit_flags:
            return exit_flags[action]


def conv_wav_loop(dir_path: Path) -> bool:
    while True:
        action = ask_cnv.ask_conv_wav_action()
        print()

        if action == "list_wav":
            utils.list_convable_audios_in_dir(dir_path, "wav")
            print()
        elif action == "wav_to_flac":
            del_og = ask_cnv.ask_del_og_files("wav")
            print()
            cnv.conv_WAVs_dir(dir_path, "flac", del_og)
            print()
        elif action == "wav_to_ogg":
            del_og = ask_cnv.ask_del_og_files("wav")
            print()
            cnv.conv_WAVs_dir(dir_path, "ogg", del_og)
            print()
        elif action == "wav_to_mp3":
            del_og = ask_cnv.ask_del_og_files("wav")
            print()
            cnv.conv_WAVs_dir(dir_path, "mp3", del_og)
            print()
        elif action in exit_flags:
            return exit_flags[action]


def conv_mp3_loop(dir_path: Path) -> bool:
    while True:
        action = ask_cnv.ask_conv_mp3_action()
        print()

        if action == "list_mp3":
            utils.list_convable_audios_in_dir(dir_path, "mp3")
            print()
        elif action == "mp3_to_flac":
            del_og = ask_cnv.ask_del_og_files("mp3")
            print()
            cnv.conv_MP3s_dir(dir_path, "flac", del_og)
            print()
        elif action == "mp3_to_ogg":
            del_og = ask_cnv.ask_del_og_files("mp3")
            print()
            cnv.conv_MP3s_dir(dir_path, "ogg", del_og)
            print()
        elif action == "mp3_to_wav":
            del_og = ask_cnv.ask_del_og_files("mp3")
            print()
            cnv.conv_MP3s_dir(dir_path, "wav", del_og)
            print()
        elif action in exit_flags:
            return exit_flags[action]
