# Работа с файлами
import os
# Модуль shutil содержит набор функций высокого уровня для обработки файлов, групп файлов, и папок.
# В частности, доступные здесь функции позволяют копировать, перемещать и удалять файлы и папки. 
import shutil
from pathlib import Path
from glob import glob
print(f'Текущая директория {os.getcwd()}')  # # Узнаём текущую рабочую директорию

# os.mkdir('temp_folder')  # Создаём новую директорию в текущей
# Однако, если вы намерены создать новую директорию с несколькими вложенными уровнями
# (имеется в виду наличие одной папки внутри другой), то вам необходимо использовать функцию makedirs()
# os.makedirs(r'tmp_level_1\tmp_level_2')

# Удаление директорий и файлов
# Для удаления файла в модуле os применяется функция remove(), а для удаления папки — функция rmdir().
# Попытка же удалить директорию с помощью remove() вызовет ошибку.
file = open('tmp.txt', 'w')
file.write('hello world\n')
file.close()

print(f"Before deleting file {os.path.isfile('tmp.txt')}")
os.remove('tmp.txt')
print(f"After deleting file {os.path.exists('tmp.txt')}")

# Получение списка файлов
# Зачастую их имена соответствуют определённому шаблону. Допустим, мы хотим найти все файлы .txt в директории.
# Далее рассмотрим, как это можно сделать с помощью метода glob() с объектом Path.
# Обратите внимание, что данный метод создаёт генератор с возможностью итерации.
txt_files = list(Path('.').glob("*.txt"))
print("Txt files:", txt_files)
for file in txt_files:
    print(file.absolute())  # C:\Users\*\PycharmProjects\python-program\Lesson-8\example.txt

# Шаблон поиска glob
# Как вариант, также удобно использовать модуль glob напрямую.
# Он располагает аналогичной функциональностью, создавая списки имён файлов, с которыми впоследствии можно работать.
# заметьте, что Path.glob() создаёт пути.
files = glob('e*')
print("Files starting with e:", files)

# Перемещение и копирование файлов
# Перемещение и копирование — одна из стандартных задач управления файлами, которая довольно легко решается в Python.
# Для перемещения вы просто переименовываете файл, заменяя его старую директорию целевой.
# Предположим, необходимо переместить все файлы .txt в другую папку. В следующем примере кода мы увидим,
# как это можно сделать с помощью модуля pathlib

target_folder = Path("target_folder")
# Имейте в виду, что попытка повторного выполнения вышеприведённого кода может вызвать проблемы — вы не сможете создать
# новую директорию, если такая уже существует. Стоит отметить, что эта проблема решается путём присвоения аргументу
# exist_ok значения True, как показано выше. А вот значение False, установленное для него по умолчанию,
# не позволит повторно создать уже существующую директорию и приведёт к ошибке.
target_folder.mkdir(parents=True, exist_ok=True)
source_folder = Path('.')
txt_files = source_folder.glob('*.txt')
# for txt_file in txt_files:
#     filename = txt_file.name
#     target_path = target_folder.joinpath(filename)
#     print(f"** Moving file {filename}")
#     print("Target File Exists:", target_path.exists())
#     txt_file.rename(target_path)
#     print("Target File Exists:", target_path.exists(), '\n')

# Копирование же можно выполнить при помощи функциональности, доступной в shutil,
# ещё одном полезном модуле из стандартной библиотеки для операций с файлами.
# Здесь за это отвечает функция copy(), в которой исходный и целевой файлы указываются в виде строк.

source_file = "target_folder/hello.txt"
target_file = "hello2.txt"
target_file_path = Path(target_file)
print("* Before copying, file exists:", target_file_path.exists())
shutil.copy(source_file, target_file)
print("* After copying, file exists:", target_file_path.exists())

# Проверка директории/файла
# В них для проверки того, существует ли конкретный путь, применялся метод exists()
# При условии положительного ответа он возвращает True, в противном случае — False.
# Примечательно, что эта функция доступна в обоих модулях, os и pathlib, но с разными сигнатурами.
# exists() в модуле os
print(os.path.exists('target_folder'))
# exists() в модуле pathlib
print(Path('target_folder').exists())
# В модуле pathlib можно также проверить, является ли путь директорией или файлом с готовыми к вызову функциями.
# Проверяем, является ли путь директорией
print(os.path.isdir('target_folder'))
print(Path('target_folder').is_dir())

# Проверяем, является ли путь файлом
print(os.path.isfile('target_folder'))
print(Path('target_folder').is_file())

# Получение информации о файле
# При работе с файлами во многих сценариях возникает необходимость извлечения их имён.
# С объектом Path это просто как дважды два, и вы уже были свидетелями его применения.
# Можно просто извлечь атрибут name файлового объекта Path. Если же вам нужно узнать только имя без расширения,
# то извлекать следует атрибут stem.

for py_file in Path().glob('*.py'):
    print('Name with extension:', py_file.name)
    print('Name only:', py_file.stem)

# В отдельных случаях вам потребуется узнать расширение файла, с которым вы работаете.
# Чаще всего можно воспользоваться атрибутом suffix файлового объекта Path
file_path = Path('1_files.py')
print("File Extension:", file_path.suffix)

# Если необходимо получить больше информации о файле, например, его размер и время изменения,
# то для этого в нашем распоряжении есть метод stat()
# Получаем объект st_stat из пути
current_file_path = Path('2_work_with_files.py')
file_stat = current_file_path.stat()
# Получаем информацию о размере файла:
print("File Size in Bytes:", file_stat.st_size)
# Получаем информацию о времени последнего обращения
# from datetime import datetime
# print("When Most Recent Access:", datetime.fromtimestamp(file_stat.st_atime))
print("When Most Recent Access:", file_stat.st_atime)
# Получаем информацию о времени последнего изменения содержимого
# print("When Most Recent Modification:", datetime.fromtimestamp(file_stat.st_mtime))
print("When Most Recent Modification:", file_stat.st_mtime)

# Архивирование и разархивирование файлов
# При работе с большим числом файлов может потребоваться их архивирование для долгосрочного хранения или
# временной передачи. Соответствующие возможности предоставляются модулем zipfile. Для архивирования файлов функцией
# ZipFile() создаётся файловый объект zip, что напоминает случай с функцией open(),
# поскольку обе эти функции предусматривают создание файлового объекта, управляемого контекстным менеджером
from zipfile import ZipFile
# Создание zip-файла, содержащего все текстовые файлы в директории
with ZipFile('text_files.zip', 'w') as file:
    # for txt_file in Path('target_folder').glob('*.txt'): - из папки target_folder
    for txt_file in Path().glob('*.txt'):
        print(f"*Add file: {txt_file.name} to the zip file")
        file.write(txt_file)

# Вы можете получить zip-файл из внешнего источника, и вам потребуется извлечь из него файлы.
# Чтобы не усложнять, допустим, что мы распаковываем их в текущую директорию. Обратите внимание на то,
# что имена файлов в zip-файле совпадают с содержащимися в директории, вследствие чего последние будут перезаписаны
# без предупреждения. Поэтому вам следует рассмотреть вариант извлечения содержимого zip-файла в отдельную папку,
# где такой проблемы перезаписи не возникнет.
os.mkdir('extract_folder')
with ZipFile('text_files.zip') as zip_file:
    zip_file.printdir()
    zip_file.extractall(path='extract_folder')
