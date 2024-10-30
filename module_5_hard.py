import hashlib
import time
from time import sleep


class User():

    Users = {}
    current_user = None

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

class Video():

    Videos = {}

    def __init__(self, title, duration, adult_mode = False):
        self.title = str(title)
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube():

    Users = {}
    current_user = None
    Videos = {}

    def register(self, nickname, password, age):
        if nickname in self.Users:
            print(f'Пользователя {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.Users[nickname] = [new_user.password, age]
            self.current_user = new_user.nickname
            print(f'Пользователя {nickname} успешно зарегистрирован, добро пожаловать')

    def log_in(self):
        for nickname, password in self.Users.items():
            login = input('Пожалуйста введите сой Login: ')
            pas = hashlib.sha256(input('Пожалуйста введите свой Password: ').encode()).hexdigest()
            if login in nickname and pas in password:
                print(f'Авторизация прошла успешно, добро пожаловать {login}')
                self.current_user = login
            else:
                print(f'Неверный логин или пароль. Попробуйте снова(')
        return self.current_user

    def log_out(self):
        self.current_user = None
        pass

    def add(self, *other):
        for i in other:
            if bool(self.Videos) == False:
                self.Videos[i.title] = [i.duration, i.time_now, i.adult_mode]
                print(f'Видео "{i.title}" успешно загруженно!')
            else:
                for vid in self.Videos:
                    if i.title.lower() in vid.lower():
                        print(f'Видео с ткаеим именем - "{i.title}", уже существует')
                        return
                    else:
                        self.Videos[i.title] = [i.duration, i.time_now, i.adult_mode]
                        print(f'Видео "{i.title}" успешно загруженно!')
                        return

    def get_videos(self,poisk):
        list_ = []
        for i in self.Videos:
            if poisk.lower() in i.lower():
                list_.append(i)
        return list_

    def watch_video(self, vidik):
        vid = {}
        us = {}

        if self.current_user == None:
            print(f'Войдите в профиль чтобы смотреть видео')
            return
        else:
            for a, b in self.Users.items():
                if self.current_user == a:
                    us[a] = b

        for i, j in self.Videos.items():
            if vidik == i:
                vid[i] = j
                for l, p in us.items():
                    for v, am in vid.items():
                        if p[1] < am[2]:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
                            return
                        else:
                            for second in range(am[1], am[0]):
                                print(f"Секунда: {second + 1}")
                                sleep(1)
                            print('Конец')
                            return
                else:
                    print('Видео не найдено')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 4)
v2 = Video('Для чего девушкам парень программист?', 2, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')