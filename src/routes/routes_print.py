import src.utils as utils
from pathlib import Path



def list_images_route(dir_main: Path):
    utils.list_images_in_dir(dir_main, "all")
    print()


def list_audios_route(dir_main: Path):
    utils.list_images_in_dir(dir_main, "all")
    print()
