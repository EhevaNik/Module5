from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # имя пользователя, строка
        self.password = self.hash_password(password)  # в хэшированном виде, число
        self.age = age  # возраст, число

    def __str__(self):
        return self.nickname

    def hash_password(self, password):
        return hash(password)

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title # заголовок, строка
        self.duration = duration # продолжительность, секунды
        self.time_now = 0 # секунда остановки (изначально 0)
        self.adult_mode = adult_mode # adult_mode(ограничение по возрасту, bool (False по умолчанию))

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})'

class UrTube:
    def __init__(self):
        self.users = []  # список объектов User
        self.videos = []  # список объектов Video
        self.current_user = None  # текущий пользователь, User

    # Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
    # с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
    # Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == self.hash_password(password):
                self.current_user = user
                return
        print('Неверный логин или пароль')

    # Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
    # если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
    # "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

# Метод log_out для сброса текущего пользователя на None.
    def log_out(self):
        self.current_user = None

# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
# если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
# содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
# (не учитывать регистр).
    def get_videos(self, search_word):
        search_word_lower = search_word.lower()
        return [video.title for video in self.videos if search_word_lower in video.title.lower()]

# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
# то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить
# в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
# Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"
    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        video = next((v for v in self.videos if v.title == title), None)
        if video is None:
            print('Видео не найдено')
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

        for second in range(video.time_now, video.duration):
            print(second + 1)
            sleep(1)

        video.time_now = 0
        print('Конец видео')

    @staticmethod
    def hash_password(password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

# # Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

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

