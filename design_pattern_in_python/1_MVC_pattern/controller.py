"""
This file will be used to pull data from model.py and use views.py to print those

"""
from model import Person
from view import show_all_users, start_view, end_view


def show_all():
    data_in_db = Person.get_all()

    return show_all_users(data_in_db)


def start():
    start_view()
    user_input = input("Do you want to show all users [y/n]")

    if user_input == 'y':
        return show_all()
    else:
        return end_view()


if __name__ == "__main__":
    start()
