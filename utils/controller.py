def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}! z miejscowosci {user['location']} opublikował {user['posts']} postów")


def add_user(users_data: list) -> None:
    user_name = input('podaj imię nowego urzytkownika: ')
    user_location = input('podaj lokalizację nowego znajomego: ')
    user_posts = int(input('podaj liczbę postów: '))
    users_data.append({"name": user_name, "location": user_location, "posts": user_posts})


def remove_user(users_data: list) -> None:
    user_name = input('podaj imie urzytkownika do usunięcia: ')
    for user in users_data:
        if user["name"] == user_name:
            users_data.remove(user)


def update_user(users_data: list) -> None:
    user_name = input('podaj imie użytkownika którego dane chcez zaktualizować: ')
    for user in users_data:
        if user["name"] == user_name:
            user["name"] = input('podaj nowe imię użytkownika: ')
            user["location"] = input('podaj nową lokację użytkownika: ')
            user["posts"] = int(input('podaj nową liczbę postów użytkownika: '))
