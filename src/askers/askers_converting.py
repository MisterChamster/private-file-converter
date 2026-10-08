from typing import Literal



def ask_convert_action() -> Literal[
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
    "heic_to_png_no_del",
    "heic_to_png_del",
    "heic_to_jpg_no_del",
    "heic_to_jpg_del",
    "return",
    "exit"]:
    returns_dict = {
        "l":  "list_heic",
        "p":  "heic_to_png_no_del",
        "pd": "heic_to_png_del",
        "j":  "heic_to_jpg_no_del",
        "jd": "heic_to_jpg_del",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose heic files conversion action:\n"
              "l  - List all .heic files in folder\n"
              "p  - Convert to .png files (leave heic files)\n"
              "pd - Convert to .png files (delete heic files)\n"
              "j  - Convert to .jpg files (leave heic files)\n"
              "jd - Convert to .jpg files (delete heic files)\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_conv_png_action() -> Literal[
    "list_png",
    "png_to_jpg_no_del",
    "png_to_jpg_del",
    "png_to_heic_no_del",
    "png_to_heic_del",
    "return",
    "exit"]:
    returns_dict = {
        "l":  "list_png",
        "j":  "png_to_jpg_no_del",
        "jd": "png_to_jpg_del",
        "h":  "png_to_heic_no_del",
        "hd": "png_to_heic_del",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose png files conversion action:\n"
              "l  - List all .png files in folder\n"
              "j  - Convert to .jpg files (leave png files)\n"
              "jd - Convert to .jpg files (delete png files)\n"
              "h  - Convert to .heic files (leave png files)\n"
              "hd - Convert to .heic files (delete png files)\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_conv_jpg_action() -> Literal[
    "list_jpg",
    "jpg_to_png_no_del",
    "jpg_to_png_del",
    "jpg_to_heic_no_del",
    "jpg_to_heic_del",
    "return",
    "exit"]:
    returns_dict = {
        "l":  "list_jpg",
        "p":  "jpg_to_png_no_del",
        "pd": "jpg_to_png_del",
        "h":  "jpg_to_heic_no_del",
        "hd": "jpg_to_heic_del",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose jpg files conversion action:\n"
              "l  - List all .jpg files in folder\n"
              "p  - Convert to .png files (leave jpg files)\n"
              "pd - Convert to .png files (delete jpg files)\n"
              "h  - Convert to .heic files (leave jpg files)\n"
              "hd - Convert to .heic files (delete jpg files)\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")
