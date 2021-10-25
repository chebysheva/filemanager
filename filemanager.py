from directory import main_directory
import shutil, os
os.getcwd()
os.chdir(main_directory)

def new_folder(name):
    '''Создание папки'''
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка уже есть')

def new_file(name, text = None):
    '''Создание файла'''
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

def delete_f(name):
    '''Удаление папки или файла'''
    if os.path.isdir(name):
        os.rmdir(name)  
    else:
        os.remove(name)

def file_copy(name1, name2):
    '''Копирование файлов'''     # name1 - путь копируемого файла, name2 - путь назначения нового файла
    if os.path.isdir(name1):
        try:
            shutil.copytree(name1, name2) 
        except FileExistsError:
            print('Такой файл уже существует')
    else:
        shutil.copy(name1, name2) 

def change_folder(name): 
    '''Перемещение между папками'''       
    if os.path.isdir(name):
        os.chdir(name) 

def text_in_file(name, text):   
    '''Запись текста в файл'''  
    x = open(name,'w')  
    x.write(text)
    x.close()

def read_file(name):
    '''Просмотр содержимого файла'''      
    with open(name) as f:
        for line in f.readlines():
            print(line)

def replace_file(name1, name2):
    '''Перемещние файла'''
    os.replace(name1, name2)

def rename_file(name1, name2):
    '''Переименование файла'''
    os.rename(name1, name2)

def help():
    '''Выыод списка команд'''
    print('new_folder - создание новой папки\nnew_file - создание нового файла\ndelete_f - удаление папки или файла\nfile_copy - копирование файлов\nchange_folder - изменение папки\ntext_in_file - запись текста в файл\nread_file - просмотр содержимого файла\nreplace_file - переместить файл\nrename_file - переименовать файл')

while True:
    com=input('Введите команду: ')
    
    if com == 'excit':
        break

    elif com == 'new_folder':
        name = input('Введите имя папки: ')
        new_folder(name)

    elif com == 'new_file':
        name = input('Введите имя файла: ')
        text = input('Введите текст: ')
        new_file(name, text)

    elif com == 'delete_f':
        name = input('Введите имя файла или папки, которые хотите удалить: ')
        delete_f(name)

    elif com == 'file_copy':
        name1 = input('Введите путь файлов или папки, которые хотите копировать: ')
        name2 = input('Введите путь назначения нового файла или папки: ')
        file_copy(name1, name2)

    elif com == 'change_folder':
        name = input('Введите имя папки, в которую хотите переместиться; чтобы подняться на уровень выше, введите "..": ')
        change_folder(name)
        print('Текущая папка:', os.getcwd())

    elif com == 'text_in_file':
        name = input('Введите имя файла: ')
        text = input('Введите текст: ')
        text_in_file(name, text)

    elif com == 'read_file':
        name = input('Введите имя файла: ')
        read_file(name)

    elif com == 'replace_file':
        name1 = input('Введите имя файла: ')
        name2 = input('Введите имя папки: ')
        replace_file(name1, name2)

    elif com == 'rename_file':
        name1 = input('Введите имя файла: ')
        name2 = input('Введите новое имя файла: ')
        rename_file(name1, name2)

    else:
        help()




    
    

 