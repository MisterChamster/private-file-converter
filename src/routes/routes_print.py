import src.utils as utils
import src.askers.askers_printing as asker_prt
from pathlib import Path



def list_images_route(dir_main: Path) -> None:
    while True:
        action = asker_prt.ask_print_convable_images()

        if action == "list_all":
            utils.list_images_in_dir(dir_main, "all")
        elif action == "list_heic":
            utils.list_images_in_dir(dir_main, "heic")
        elif action == "list_png":
            utils.list_images_in_dir(dir_main, "png")
        elif action == "list_jpg":
            utils.list_images_in_dir(dir_main, "jpg")
        elif action == "return":
            return


# def list_audios_route(dir_main: Path):
#     utils.list_images_in_dir(dir_main, "all")
#     print()
