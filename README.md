# Продвинутый криптер
Господа! сегодня знаминательный день!

в эти выходные мне стало скучно!

и... результат этого вы наверное видели в нашем тг.

некоторые восприняли это с интересом.

некоторые с агрессией 

![image](https://user-images.githubusercontent.com/103320407/222927039-3ec5597a-a363-40f6-8ae1-effdcb912d8e.png)

но все были схожи в одном -> НИКТО не понял как именно это работает (за редким исключением)

и вот сейчас мы раскажем как работает продвинутый криптер!

но сначала давайте узнаем что такое криптер

https://ru.wikipedia.org/wiki/Криптор

Ну что узнали?

Ну пойдёмте дальше

Если вы пробовали написать свой криптер заметили
что у любой буковы есть свой код в любой из кодировок (ну да код кодировки)

и вот с этим кодом мы и будем работать.

представим что у нас есть буква А
и есть слово в котором эта буква употребляется несколько раз.
Пусть будет А-Н-А-Н-А-С
и код маленько (ЭТО ВАЖНО) буквы а это [1072]

в закодированом виде это выглядит так - [1072, 1085, 1072, 1085, 1072, 1089]
зная кодировку и то какой код что означает мы можем перевести всё обратно.
[а, 1085, а, 1085, а, 1089] - и если есть таблица с кодами где код "а" 1072 мы подбираем остальные

[а, н, а, н, а, с]

но представим что у нас есть зашифрованное слово.

и что с ним делать шифра ( под шифром подразумевается сдвиг )

[1124, 1137, 1124, 1137, 1124, 1141]

если мы знаем что имменно за слово у нас то мы отнимаем от изменённого значения

изначальное - 1124 - 1072 = <52>

вот наш сдвиг. теперь отняв от изменённых наш сдвиг мы получим изначальные значения по кодировке

и наше слово - ананас

но что если нам не известно изначальное слово?

а это тема уже для отдельной стать... строк на 1000 ( и писать я её конечно же не буду )
