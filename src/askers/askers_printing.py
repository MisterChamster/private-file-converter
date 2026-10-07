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
        print("Choose printing action:\n"
              "a - Print all images\n"
              "h - Print .heic images\n"
              "p - Print .png images\n"
              "j - Print .jpg images\n"
              "r  - Return\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


# def ask_print_convable_audios() -> str:
#     pass
