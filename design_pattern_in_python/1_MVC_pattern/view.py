"""
This interface will be used to display data
"""


def show_all_users(list):
    print(f"we have {len(list)} users !!!")
    for item in list:
        print(item.name())


def start_view():
    print("view started!!")


def end_view():
    print("good bye!!1")