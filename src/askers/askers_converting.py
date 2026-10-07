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
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_htp_action() -> Literal[
    "list_heic",
    "heic_to_png_no_del",
    "heic_to_png_del",
    "return",
    "exit"]:
    returns_dict = {
        "lh": "list_heic",
        "hn": "heic_to_png_no_del",
        "hd": "heic_to_png_del",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose heic to png action:\n"
              "lh - List all .heic files in folder\n"
              "hn - Convert .heic files to .png files (leave heic files)\n"
              "hd - Convert .heic files to .png files (delete heic files)\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_htj_action() -> Literal[
    "list_heic",
    "heic_to_jpg_no_del",
    "heic_to_jpg_del",
    "return",
    "exit"]:
    returns_dict = {
        "lh": "list_heic",
        "hn": "heic_to_jpg_no_del",
        "hd": "heic_to_jpg_del",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose heic to jpg action:\n"
              "lh - List all .heic files in folder\n"
              "hn - Convert .heic files to .jpg files (leave heic files)\n"
              "hd - Convert .heic files to .jpg files (delete heic files)\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_ptj_action() -> Literal[
    "list_png",
    "png_to_jpg_no_del",
    "png_to_jpg_del",
    "return",
    "exit"]:
    returns_dict = {
        "lp": "list_png",
        "pn": "png_to_jpg_no_del",
        "pd": "png_to_jpg_del",
        "r":  "return",
        "x":  "exit"}

    while True:
        print("Choose png to jpg action:\n"
              "lp - List all .png files in folder\n"
              "pn - Convert .png files to .jpg files (leave png files)\n"
              "pd - Convert .png files to .jpg files (delete png files)\n"
              "r  - Return\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")
