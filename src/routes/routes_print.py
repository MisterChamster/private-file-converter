import src.utils as utils
import src.askers.askers_printing as asker_prt
from pathlib import Path



def list_images_route(dir_main: Path) -> None:
    while True:
        action = asker_prt.ask_print_convable_images()
        print()

        if action == "list_all":
            utils.list_convable_images_in_dir(dir_main, "all")
            print()
        elif action == "list_heic":
            utils.list_convable_images_in_dir(dir_main, "heic")
            print()
        elif action == "list_png":
            utils.list_convable_images_in_dir(dir_main, "png")
            print()
        elif action == "list_jpg":
            utils.list_convable_images_in_dir(dir_main, "jpg")
            print()
        elif action == "return":
            return


def list_audios_route(dir_main: Path) -> None:
    while True:
        action = asker_prt.ask_print_convable_audios()
        print()

        if action == "list_all":
            utils.list_convable_audios_in_dir(dir_main, "all")
            print()
        elif action == "list_flac":
            utils.list_convable_audios_in_dir(dir_main, "flac")
            print()
        elif action == "list_ogg":
            utils.list_convable_audios_in_dir(dir_main, "ogg")
            print()
        elif action == "list_wav":
            utils.list_convable_audios_in_dir(dir_main, "wav")
            print()
        elif action == "list_mp3":
            utils.list_convable_audios_in_dir(dir_main, "mp3")
            print()
        elif action == "return":
            return
