from typing import Literal



def ask_del_og_files(extension: str) -> bool:
    returns_dict = {
        "y": True,
        "n": False}

    while True:
        print(f"Do You want to have original {extension} files deleted? (y/n)\n>> ", end="")
        answer = input().strip().lower()

        if answer in returns_dict:
            return returns_dict[answer]
        print("Incorrect input.\n")


def ask_imgs_conv_action() -> Literal[
        "convert_heic",
        "convert_png",
        "convert_jpg",
        "return",
        "exit"]:
    returns_dict = {
        "h": "convert_heic",
        "p": "convert_png",
        "j": "convert_jpg",
        "r": "return",
        "x": "exit"}

    while True:
        print("Choose convert action:\n"
              "h - Convert .heic files...\n"
              "p - Convert .png files...\n"
              "j - Convert .jpg files...\n"
              "r - Return\n"
              "x - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_conv_heic_action() -> Literal[
    "list_heic",
    "heic_to_png",
    "heic_to_jpg",
    "return",
    "exit"]:
    returns_dict = {
        "l":  "list_heic",
        "p":  "heic_to_png",
        "j":  "heic_to_jpg",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose heic files conversion action:\n"
              "l  - List all .heic files in folder\n"
              "p  - Convert to .png files\n"
              "j  - Convert to .jpg files\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_conv_png_action() -> Literal[
    "list_png",
    "png_to_jpg",
    "png_to_heic",
    "return",
    "exit"]:
    returns_dict = {
        "l":  "list_png",
        "j":  "png_to_jpg",
        "h":  "png_to_heic",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose png files conversion action:\n"
              "l  - List all .png files in folder\n"
              "j  - Convert to .jpg files\n"
              "h  - Convert to .heic files\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_conv_jpg_action() -> Literal[
    "list_jpg",
    "jpg_to_png",
    "jpg_to_heic",
    "return",
    "exit"]:
    returns_dict = {
        "l":  "list_jpg",
        "p":  "jpg_to_png",
        "h":  "jpg_to_heic",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose jpg files conversion action:\n"
              "l  - List all .jpg files in folder\n"
              "p  - Convert to .png files\n"
              "h  - Convert to .heic files\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_aud_conv_action() -> Literal[
        "convert_flac",
        "convert_ogg",
        "convert_wav",
        "convert_mp3",
        "return",
        "exit"]:
    returns_dict = {
        "f": "convert_flac",
        "o": "convert_ogg",
        "w": "convert_wav",
        "m": "convert_mp3",
        "r": "return",
        "x": "exit"}

    while True:
        print("Choose convert action:\n"
              "f - Convert .flac files...\n"
              "o - Convert .ogg files...\n"
              "w - Convert .wav files...\n"
              "m - Convert .mp3 files...\n"
              "r - Return\n"
              "x - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_conv_flac_action() -> Literal[""]:
    return ""


def ask_conv_ogg_action() -> Literal[""]:
    return ""


def ask_conv_wav_action() -> Literal[""]:
    return ""


def ask_conv_mp3_action() -> Literal[""]:
    return ""
