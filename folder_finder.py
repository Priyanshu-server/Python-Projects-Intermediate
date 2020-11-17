from plyer import notification
import os
import time


def folder_finder(folder_name):
    not_found = True
    while not_found:
        directory_list = os.listdir()
        time.sleep(5)
        for name in directory_list:
            print(name)
            if name == folder_name:
                notification.notify(title="Folder Found", message=f"{folder_name} is found on current {os.getcwd()}",
                                    app_icon=None, timeout=10)
                not_found = False
                break
            else:
                continue


folder_finder("don")
