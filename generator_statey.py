# подключаем библиотеку
import markovify

# отправляем в переменные содержимое файлов
file_zag = open('zag.txt', encoding='utf8').read()
file_text = open('text.txt', encoding='utf8').read()

# сразу обрабатываем весь текст для заголовков одной командой
text_model_zag = markovify.Text(file_zag)
# то же самое делаем с текстом статей
text_model_text = markovify.Text(file_text)

# выводим пустую строку, чтобы отделить результаты от служебного вывода
print()

# выводим новый заголовок
print(text_model_zag.make_sentence(tries=100))

# выводим пустую строку, чтобы отделить заголовок от текста
print()

# выводим статью из 30 предожений
for i in range(30):
    # чтобы предложение точно получилось, даём алгоритму на это 100 попыток
    print(text_model_text.make_sentence(tries=100))
