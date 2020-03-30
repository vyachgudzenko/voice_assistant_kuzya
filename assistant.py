import speech_recognition as sr
import sys
from  internet import Google, YouTube

class Assistant(object):
    """Основной класс голосового помощника"""
    def listen(self):
        """Функция listen записывает аудио с микрофона и передает его
        на распознование в Google Speech Recognition.
        Возвращает command = тип str"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Скажи команду: ")
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='ru')
            print(command)
            return command
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def choice(self):
        """Функция choice постоянно прослушивает микрофон с помощью listen"""
        while True:
            try:
                command = self.listen().lower()
                if 'кузя' in command:
                    if 'открой' in command:
                        if 'google' in command or 'гугл' in command:
                            print('Ассистент: запускаем Google',command)
                            google = GoogleAssistant()
                            google.choice()
                        elif 'youtube' in command or 'ютуб' in command:
                            print('Ассистент: запускаем YouTube',command)
                            youtube = YouTubeAssistant()
                            youtube.choice()
                    elif 'выход' in command:
                        sys.exit()
                    else:
                        print('Ассистент: я пока не знаю этой команды ',command)
                else:
                    print('Инициализируйте Ассистента с помощью заданных команд ')
            except AttributeError:
                pass

class GoogleAssistant(Assistant):
    """Субкласс голосового помощника, отвечающего за поиск Google"""
    def __init__(self):
        self.google = Google()

    def choice(self):
        while True:
            try:
                command = self.listen().lower()
                print('GoogleAssistant: ',command)
                if 'кузя' in command:
                    if 'найди' in command:
                        query = command.split('найди ')[1]
                        self.google.search(query)
                    elif 'ссылка' in command:
                        link = command.split('ссылка ')[1]
                        self.google.open_link(link)
                    elif 'вниз' in command:
                        self.google.flipping_down()
                    elif 'вверх' in command:
                        self.google.flipping_up()
                    elif 'назад' in command:
                        self.google.back()
                    elif 'закрой' in command:
                        self.google.quit()
                        a = Assistant()
                        a.choice()
                    else:
                        print('Ассистент не знает такой команды - ', command)
            except AttributeError:
                pass
            except IndexError:
                print('Озвучте запрос правильно')

class YouTubeAssistant(Assistant):
    """Субкласс голосового помощника, отвечающего за работу YouTube"""
    def __init__(self):
        self.youtube = YouTube()

    def choice(self):
        """Функция choice постоянно прослушивает микрофон с помощью listen"""
        while True:
            try:
                command = self.listen().lower()
                print('YouTubeAssistant: ',command)
                if 'кузя' in command:
                    if 'найди' in command:
                        query = command.split('найди ')[1]
                        self.youtube.search(query)
                    elif 'открой' in command:
                        if 'ссылка' in command:
                            link = command.split('ссылка ')[1]
                            self.youtube.open_link(link)
                        elif 'канал' in command:
                            self.youtube.open_channel()
                        elif 'видео' in command:
                            link = command.split('видео ')[1]
                            self.youtube.open_video(link)
                        elif 'плейлист' in command:
                            self.youtube.playlist()
                        elif 'список' in command:
                            link = command.split('список')[1]
                            self.youtube.open_playlist(link)
                    elif 'стоп' in command:
                        self.youtube.play_stop()
                    elif 'вниз' in command:
                        self.youtube.flipping_down()
                    elif 'вверх' in command:
                        self.youtube.flipping_up()
                    elif 'назад' in command:
                        self.youtube.back()
                    elif 'закрой' in command:
                        self.youtube.quit()
                        a = Assistant()
                        a.choice()
            except AttributeError:
                pass
            except IndexError:
                print('Озвучте запрос правильно')

if __name__ == '__main__':
    assistant = Assistant()
    assistant.choice()
