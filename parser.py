# подключаем urlopen из модуля urllib
from urllib.request import urlopen

# подключаем библиотеку BeautifulSout
from bs4 import BeautifulSoup

# общая часть URL-адреса
url = "https://www.kommersant.ru/doc/"
# стартовый номер, с которого начинаем парсинг
start_id = 4804129

# открываем  файл, куда будем добавлять заголовки
file_zag = open("komm_zag.txt", "a")
# открываем  файл, куда будем добавлять текст
file_text = open('komm_text.txt','a')

# перебираем предыдущие 500 адресов
for x in range(0,500):

    # формируем новый адрес из общей части и номера материала
    # на каждом шаге номер уменьшается на единицу, чтобы обратиться к более старым материалам
    work_url = url + str(start_id - x)

    # включаем обработчик исключений для запроса содержимого страницы
    try:
        # получаем исходный код страницы в виде байт-строки
        html_code = urlopen(work_url).read()
    # если случилась любая ошибка
    except Exception as e:
        print('Страница не найдена')
        # прерываем этот шаг цикла и переходим к следующему
        continue

    # отправляем исходный код страницы на обработку в библиотеку
    soup = BeautifulSoup(html_code, "html.parser")

    # включаем обработчик исключений для команды поиска
    try:
        # находим название страницы с помощью метода find()
        s = soup.find('h1').text
    # если случилась любая ошибка
    except Exception as e:
        print("Заголовок не найден")
        # прерываем этот шаг цикла и переходим к следующему
        continue
    # выводим его на экран
    print(s)

    # сохраняем заголовок в файле и переносим курсор на новую строку
    file_zag.write(s + '. ')

    # находим все абзацы с текстом новости
    content = soup.find_all('p', class_ = "b-article__text")
    # перебираем все найденные абзацы
    for item in content:
        # сохраняем каждый абзац в другой файл
        file_text.write(item.text + ' ')
        print(item.text)

# закрываем файл
file.close()