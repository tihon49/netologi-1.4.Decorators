import datetime


def my_decorator(old_function):
    output_file = 'log.txt'
    path = 'output_dir/' + output_file
    
    def new_foonction(*args, **kwargs):
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f'{datetime.datetime.now()}\n')
            print(datetime.datetime.now())

            file.write(f'Имя функции: {old_function.__name__}\n')
            print(f'Имя функции: {old_function.__name__}')

            file.write(f'Аргументы: {args}\n')
            print(f'Аргументы: {args}')

            file.write(f'Результат: {old_function(*args, **kwargs)}\n\n')

        return old_function(*args, **kwargs)
    return new_foonction


#############################################################################################
#Каталог документов хранится в следующем виде:
documents = [
        {"type": "passport",
         "number": "2207 876234",
         "name": "Василий Гупкин"
         },

        {"type": "invoice",
         "number": "11-2",
         "name": "Геннадий Покемонов"
         },

        {"type": "insurance",
         "number": "10006",
         "name": "Аристарх Павлов"
         },

         {"type": "insurance",
         "number": "10"
         }
      ]


# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': ['10']
      }


# функция p
@my_decorator
def people():
    out = input('Введите номер документа: ')

    try:
      for doc in documents:
          for item in doc:
              if out == doc[item]:
                  return doc['name']

      return 'Такого документа нет'
    except KeyError:
      return 'У данного документа нет поля "name"'
    except Exception as e:
      return f'[ОШИБКА] {e}'



# функция l
@my_decorator
def lst():
    for items in documents:
      try:
        print(f"{items['type']} \"{items['number']}\" \"{items['name']}\"")
      except KeyError:
        print(f'[ОШИБКА] у документа № {items["number"]} отсутствует поле "name"')



# функция s
@my_decorator
def shelf():
    out = input('Введите номер документа чтобы узнать на какой он полке: ')

    for key, value in directories.items():
        if out in value:
            return f'Документ на полке № {key}'

    return 'Такого документа нет'



# функция a
@my_decorator
def add():
    doc_type = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    doc_holder_name = input('Введите имя владельца документа: ')
    directories_number = input('Введите номер полки для данного документа: ')

    if directories_number not in directories.keys():
        return 'Такой полки нет'
    else:
        # добавление нового документа в каталог документов
        documents.append({
                'type': doc_type,
                'number': doc_number,
                'name': doc_holder_name
            })

        # добавление номера документа на полку
        directories[directories_number].append(doc_number)
        return f'Документ добавлен на полку {directories_number}'



# функция d
@my_decorator
def delete():
    doc_number = input('Введиет номер документа, который следует удалить: ')


    # удаление из списка документов
    for item in documents:
        if item['number'] == doc_number:
            documents.remove(item)


    # удаление из директорий с полоками
    for value in directories.values():
        for item in value:
            if item == doc_number:
                value.remove(item)
                return 'deleted from documents\ndeleted from directories'

    return 'Такого документа нет.'



# функция m
@my_decorator
def move():
    doc_number = input('Введите номер документа который следует перенести на другую полку: ')
    directories_number = input('Введите номер полки на которую следует перенести выбранный документ: ')

    if directories_number not in directories.keys():
        return 'Не верно указан номер полки'
    else:
        for item in documents:
            if item['number'] == doc_number:
                for value in directories.values():
                    if doc_number in value:
                        value.remove(doc_number)

                directories[directories_number].append(doc_number)
                return f'Документ перенесен на полку {directories_number}'
        return 'Такого номера документа нет.'


# функция as
@my_decorator
def add_shelf():
    new_shelf = input('Введите номер новой полки: ')

    # проверка на существование полки с таким номером
    if new_shelf in directories.keys():
        return f'Полка № {new_shelf} уже существует.'
    else:
        directories[new_shelf] = []
        return f'Полка с номером {new_shelf} создана.'



# функция cn
@my_decorator
def check_name():
    out = input ('Введите номер документа: ')

    try:
        for doc in documents:
            for item in doc:
                if out == doc[item]:
                    return f'доукумент №{out} имеет поле "name": {doc["name"]}'
        return 'Такого документа нет'
    except KeyError:
        return 'У данного документа нет поля "name"'
    except Exception as e:
        return f'[ОШИБКА] {e}'




def main(out):
    if out == 'p':
        print(people())
    elif out == 'l':
        lst()
    elif out == 's':
        print(shelf())
    elif out == 'a':
        print(add())
    elif out == 'd':
        print(delete())
    elif out == 'm':
        print(move())
    elif out == 'as':
        print(add_shelf())
    elif out == 'cn':
        print(check_name())
    else:
        print('Введена не верная команда.')



if __name__ == '__main__':
    print('''
p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
cn - проверить есть ли у документа поле "name".
''')


    while True:
        out = input ('\nВведите команду: ').lower()

        if out == 'q':
            break
        else:
            main(out)