import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException,ElementNotInteractableException
import time

class Internet(object):
    """ Класс Internet - базовый класс,
    который имеет только один атрибут browser - необходимый для запуска основного окна"""
    def __init__(self):
        self.browser = webdriver.Chrome("chromedriver.exe")
        self.browser.maximize_window()
    def back(self):
        """Функция инициирующего 'Назад'"""
        self.browser.back()
    def quit(self):
        "Закрыть браузер"
        self.browser.close()
    def flipping_down(self):
        "Пролистать вниз"
        self.browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    def flipping_up(self):
        "Пролистать вверх"
        self.browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)

class Google(Internet):
    """Класс Google - отвечает за поиск информации в Google"""
    def __init__(self):
        Internet.__init__(self)
        self.browser.get("https://www.google.com/")

    def search(self,query):
        """Функция search проводит поиск по заданным параметрам
           query: аргумент, переменая str"""
        self.browser.get("https://www.google.com/")
        self.browser.find_element_by_xpath(
        """//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input""").send_keys(query)
        self.browser.find_element_by_xpath(
        """//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input""").send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

    def open_link(self,link):
        """Функция open_link открывает нужную ссылку.
        Принимает на вход переменную link,тип str"""
        try:
            self.browser.find_element_by_xpath(
            """/html/body/div[8]/div[3]/div[8]/div[1]/div[2]/div/div[2]
            /div[2]/div/div/div[""" + link + """]/div/div[1]/a""").click()
        except NoSuchElementException:
            print('Не удается найти, повторите запрос')
        except ElementClickInterceptedException:
            print('Элемент не кликабелен')

class YouTube(Internet):
    """Класс YouTube - отвечает за поиск информации YouTube"""
    def __init__(self):
        Internet.__init__(self)
        self.browser.get("https://www.youtube.com/")

    def search(self,query):
        """Функция search проводит поиск по заданным параметрам
           query: аргумент, переменая str
           """
        format_query = query.replace('','+')
        self.browser.get("https://www.youtube.com/results?search_query="+query)
        time.sleep(1)

    def open_link(self,query):
        """Функция open_link открывает нужную ссылку.
        Принимает на вход переменную link,тип str"""
        try:
            self.browser.find_element_by_xpath("""/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[""" + query + """]""").click()
        except NoSuchElementException:
            print('Что то пошло не так, попробуйте еще')

    def play_stop(self):
        "Функция запускаюющая/останавливающая видео YouTube"
        try:
            self.browser.find_element_by_xpath(
            """//*[@id="movie_player"]/div[1]/video""").click()
        except Exception:
            print('Что то пошло не так')

    def open_channel(self):
        """
        Открыть канал YouTube, который находится первым в
        поиске после выполнения метода search.
        Сразу переходит на страницу с видео.
        """
        self.browser.find_element_by_xpath(
        """/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/
        ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/
        div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer/div""").click()
        channel_path = self.browser.current_url + '/videos'
        self.browser.get(channel_path)

    def open_video(self,query):
        """
        Открыть видео на канале, в списке всех видео
        """
        try:
            self.browser.find_element_by_xpath(
            """/html/body/ytd-app/div/ytd-page-manager/ytd-browse/
            ytd-two-column-browse-results-renderer/div[1]/
            ytd-section-list-renderer/div[2]/ytd-item-section-renderer/
            div[3]/ytd-grid-renderer/div[1]/
            ytd-grid-video-renderer[""" + query + """]/div[1]""").click()
        except NoSuchElementException:
            print('Что то пошло не так, попробуйте еще')

    def playlist(self):
        """
        Открыть список плейлистов канала. Корректно сработает, если вызывается
        с главной страницы канала или с раздела видео
        """
        channel_path = self.browser.current_url
        try:
            if '/videos' in channel_path:
                channel_path = channel_path.replace('/videos','/playlists')
                self.browser.get(channel_path)
            else:
                self.browser.get(channel_path + '/playlists')
        except Exception:
            print('Что то пошло не так')

    def open_playlist(self,query):
        """
        Открыть и запустить плейлист на канале.
        Корректно работает если есть общий список плейлистов, не разбит по
        группам
        """
        try:
            self.browser.find_element_by_xpath(
            """/html/body/ytd-app/div/ytd-page-manager/
            ytd-browse/ytd-two-column-browse-results-renderer/div[1]/
            ytd-section-list-renderer/div[2]/ytd-item-section-renderer/
            div[3]/ytd-grid-renderer/div[1]/
            ytd-grid-playlist-renderer[""" + query + """]/
            yt-formatted-string/a""").click()
            time.sleep(1)
            self.browser.find_element_by_xpath(
            """/html/body/ytd-app/div/ytd-page-manager/
            ytd-browse[2]/ytd-playlist-sidebar-renderer/
            div/ytd-playlist-sidebar-primary-info-renderer/
            h1/yt-formatted-string/a""").click()
        except NoSuchElementException:
            print('Неполучается открыть плейлист')
