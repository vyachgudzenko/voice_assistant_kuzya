# voice_assistant_kuzya
Голосовой помощник Кузя. В память о босоногом детстве и мульфильме о домовенке Кузе - таком же неуклюжем и немного бесполезном.

Не судите строго, это всего лишь учебное приложение, 
которое реализовано с помощью Selenium и Speech Recognition

Кузя распознает два модуля - Google и YouTube

Для работы с ним у вас должен быть установлен SeleniumDriver под Ваш любимый браузер. 
Здесь идет размещен драйвер под Google Chrome.

Кузя слушает постоянно микрофон, так что для его включение надо произнести команду "Кузя..." и дальше по списку команд

Стартовые команды

Кузя, открой... 
    Google - само собой, открывает поисковик Google
    YouTube - открывает YouTube
    
Кузя, выход - закрывает основное приложение

После того, как вы открыли Google или YouTube, запускаются соответствующие модули, который распознают свои команды.
Но для этих модулей есть общие команды. 

Кузя,
     назад - возврат на предыдущую страницу
     вниз - пролистать страницу вниз, аналогично нажатию кнопки PageDown
     вверх - пролистать страницу вверх, аналогично нажатию кнопки PageUp
     закрой - закрытие браузера и передача прослушиванию команд основному модулю
     

Google

Кузя, 
     найди <запрос> - открывает страницу Google с результатами данного запроса
     
     открой ссылка <один, два, десять> - открывает указанную ссылку. Нужно помнить, что первая ссылка в Google - это обычно 
                                         видео по запросу, реклама, или виджеты. Так что если надо открыть первую ссылку в 
                                         выдаче поиска - смело добавляйте плюс один
                                         
YouTube

Кузя, 
     найди <запрос> - открывает страницу YouTube с результатами данного запроса
     
    открой ссылка <один, два, десять> - открывает видео в результатах поиска
    
    открой канал - открывает первый канал, который есть в результатах поиска и сразу переходит на страницу с видео
    
    открой видео <один,два,десять> - открывает указанное видео на странице канала
    
    открой плейлист - переходит на страницу канала с плейлистами
    
    открой список <один, два, десять> - открывает указанный плейлист. Пока может не работать со всеми каналами, 
                                        так как адекватно реагирует только на те, где плейлисты вынесенны вместе, а не по группам.
                                        
    стоп - приостанавливает/запускает текущее видео
    
Так как при включении видео ассистент начинает слушать и звук видео, то есть проблема, что во время проигрывания 
видео он не не корректно распознает команды. 
    
    
    
    





