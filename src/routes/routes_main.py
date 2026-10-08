import src.askers.askers_main as ask_main
import src.routes.routes_convert as cnv_routes
import src.routes.routes_print as prt_routes



def main_loop() -> None:
    print()
    dir_main = ask_main.ask_path_filedialog("dir", "Choose images directory")
    if not dir_main:
        return

    while True:
        print()
        action = ask_main.ask_mainloop_action()
        print()
        if action == "list_images":
            prt_routes.list_images_route(dir_main)

        if action == "list_audios":
            prt_routes.list_audios_route(dir_main)

        elif action =="convert_images":
            print()
            exit_flag = cnv_routes.convert_images_loop(dir_main)
            if exit_flag:
                return

        elif action =="convert_audios":
            print()
            exit_flag = cnv_routes.convert_audios_loop(dir_main)
            if exit_flag:
                return

        elif action == "change_dir":
            dir_main = ask_main.ask_path_filedialog("dir", "Choose images directory")
            if not dir_main:
                return

        elif action == "exit":
            return
