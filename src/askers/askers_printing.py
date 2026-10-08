from typing import Literal



def ask_print_convable_images() -> Literal[
    "list_all",
    "list_heic",
    "list_png",
    "list_jpg",
    "return"]:
    returns_dict = {
        "a": "list_all",
        "h": "list_heic",
        "p": "list_png",
        "j": "list_jpg",
        "r": "return"}

    while True:
        print("Choose image printing action:\n"
              "a - Print all convertable images\n"
              "h - Print .heic images\n"
              "p - Print .png images\n"
              "j - Print .jpg images\n"
              "r  - Return\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_print_convable_audios() -> Literal[
    "list_all",
    "list_flac",
    "list_ogg",
    "list_wav",
    "list_mp3",
    "return"]:
    returns_dict = {
        "a": "list_all",
        "f": "list_flac",
        "o": "list_ogg",
        "w": "list_wav",
        "m": "list_mp3",
        "r": "return"}

    while True:
        print("Choose audio printing action:\n"
              "a - Print all convertable audios\n"
              "f - Print .flac audios\n"
              "o - Print .ogg audios\n"
              "w - Print .wav audios\n"
              "m - Print .mp3 audios\n"
              "r  - Return\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")
