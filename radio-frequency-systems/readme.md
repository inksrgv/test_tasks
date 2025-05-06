# Тестовое задание для команды "Радиочастотные системы"
## Linux команды
### Задание 1
<details>
<summary> Текст задания </summary>
  Написать команду, которая будет:
  
  1. Печатать строку "Hello, Devops!"
     
  2. Записывать ее в файл домашней директории
  
  3. Выводить содержимое файла на экран
</details>

Для реализации каждого пункта используется отдельная команда:

  0. touch hello.txt - нет в задании, нужна чтоб создать пустой файл
  1. echo "Hello DevOps!" - вывод строки в консоль
  2. tee hello.txt - принимает поток ввода (из echo), перенаправляет вывод в файл `hello.txt` и выводит текст в консоль
  3. cat hello.txt - выводит содержимое файла `hello.txt`

Итоговая команда:
    
    touch hello.txt && echo "Hello, DevOps!" | tee output.txt && cat output.txt

Вывод команды: 

    Hello, DevOps!
    Hello, DevOps!

Если вывод в консоль должен происходить единожды, то можно немного видоизменить команду:

    echo "Hello, DevOps!" > hello.txt && cat hello.txt

В данной команде поток ввода сразу перенаправляется в файл и выводится содержимое только файла

Вывод команды:

    Hello, DevOps!

*команды выполняются в домашней директории `/home/nika`. Чтобы выполнить ее из любой директории, нужен абсолютный путь к файлу, например `/home/nika/hello.txt` :)

### Задание 2
<details>
<summary> Текст задания </summary>
  Написать команду, которая будет:
  
  1. Читать лог-файл /var/log/syslog
     
  2. Искать строки с "error" или любым другим словом
  
  3. Выводить 5 первых совпавших с шаблоном строк 
</details>

Если файл нужно читать полностью, то будет такая последовательность команд:

1. cat /var/log/syslog - прочитает полностью файл и передаст его в след.команду
2. grep -i "error" - будет искать все совпадения по error в файле без учета регистра
3. head -n 5 - выведет 5 первых попавшихся строк

Итоговая команда: 

    cat /var/log/syslog | grep -i "error" | head -n 5

Можно сделать чуть быстрее, не пробегаясь по всему файлу, например, используя команду:

    grep -im 5 "error" /var/log/syslog

Команда в целом сделает то же самое, но остановится после 5 совпадений(не пойдет дальше по файлу).

## Bash/Python

<details>
<summary> Текст задания </summary>
  Написать скрипт на bash/python, который будет искать в файле конкретные слова и выводить строки, содержащие эти слова. 

  Формат входного файла `file.txt`:
      
    name: test_server
    path: /home/user/data
    file : data.txt
    port: 8080
    log path: /var/log/app
  
</details>

Текст bash скрипта с комментариями:

    #!/bin/bash
    #поверка на количество аргументов: по умолчанию их должно быть три: имя скрипта, имя файла и слово
    if [ $# -lt 2 ]; then
        echo "Нужно ввести три аргумента! Пример использования: python3 script.py имя_файла слово_которое_найти"
        #если ввод аргументов неверный, завершаем выполнение скрипта, выводим сообщение
        exit 1
    fi

    #определяю, что подано в скрипт. он принимает два аргумента: первый - файл, второй - слово
    file="$1"
    word="$2"
    #если файла не сущетствует в текущей директории, завершаем скрипт
    if [ ! -f "$file" ]; then
        echo "Ошибка! Файл '$file' не найден в текущей директории"
        exit 1
    fi
    #цикл для поиска слова. если слово передано в качестве аргумента скрипту, выполняем
    for word in "$word"; do
        #ищу слово в файле, но не вывожу его в консоль, если слово есть, то идем дальше
        if grep -qi "$word" "$file"; then
            echo "Найдены строки с совпадениями по слову '$word':"
            #выводим совпадения с номерами строк для удобства
            grep -ni "$word" "$file"
        #если совпадений в файле нет, выводим сообщение об этом
        else
            echo "Строки, содержащие слово '$word' не найдены"
        fi
    done

Основная логика скрипта сделана в цикле for. Ищу совпадения с помощью `grep`. Если слово найдено, вывожу строку с номером в консоль, а если нет, вывожу сообщения, что такого слова нет.

Запуск скрипта: 

    sudo ./script.sh file.txt path
    
Результаты выполнения:
1. Все передали правильно, файл сущетсвует, количество аргументов=3, слово в файле есть

       nika@nika-vb:~/yadro-test-task$ sudo ./script.sh file.txt path
       Найдены строки с совпадениями по слову 'path':
       2:path: /home/user/data
       5:log path: /var/log/app

2. Файла не существует

       nika@nika-vb:~/yadro-test-task$ sudo ./script.sh file1.txt path
       Ошибка! Файл 'file1.txt' не найден в текущей директории

3. Аргументов меньше, чем ожидается

       nika@nika-vb:~/yadro-test-task$ sudo ./script.sh file1.txt 
       Нужно ввести три аргумента! Пример использования: python3 script.py имя_файла слово_которое_найти

4. Слова в файле нет

       nika@nika-vb:~/yadro-test-task$ sudo ./script.sh file.txt fdkf
       Строки, содержащие слово 'fdkf' не найдены

Аналогичный по работе скрипт на Python:

    #!/usr/bin/env python3
    import sys
    import re

    def main():
      if len(sys.argv) != 3:
          print("Нужно ввести три аргумента! Пример использования: python3 script.py имя_файла слово_которое_найти")
          sys.exit(1)

    filename = sys.argv[1]
    search_word = sys.argv[2]  
    found = False 
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip()
                if re.search(re.escape(search_word), line, re.IGNORECASE):
                    print(f"Найдены строки с совпадениями по слову '{search_word}:'")
                    print(line)
                    found = True
        if not found:
            print(f"Строки, содержащие слово '{search_word}' не найдены")
            sys.exit(1)

    except FileNotFoundError:
        print(f"Ошибка! Файл '{filename}' не найден в текущей директории", file=sys.stderr)
        sys.exit(1)

    if __name__ == "__main__":
        main()
        
## Docker
<details>
<summary> Текст задания </summary>
  Оптимизировать Dockerfile, который запускает скрипт из предыдущего задания. 

  Исходный Dockerfile:
  
    FROM ubuntu:22.04
    RUN apt-update
    RUN apt-get install -y wget
    RUN apt-get install -y python3
    RUN apt-get install -y python3-pip
    COPY search_path.sh /tmp/search_path.sh
    COPY extract_path_value.py /tmp/extract_path_value.py
    COPY config.txt /tmp/config.txt
    RUN chmod +x /tmp/search_path.sh
    RUN chmod +x /tmp/extract_path_value.py
  
</details>

**Вариант без смены образа**

       FROM ubuntu:22.04
       WORKDIR /tmp
       RUN apt-get update && apt-get install -y python3 
       COPY file.txt script.py ./
       RUN chmod +x script.py
       ENTRYPOINT ["python3", "script.py", "file.txt"]

Что изменилось:
1. Тег образа `latest`->`22.04`. Указание тега latest может привести к непредсказуемому поведению сборки и работы контейнера в целом. В обычном контейнере это конечно не очень страшно, но в компоузе могут быть проблемы с несовместимостью образов. 22.04, потому что достаточно стабильная версия
2. Добавлена рабочая директория. Просто хорошая практика :)
3. Инстуркция `RUN` записана в одну команду (это уменьшает количество слоев), убраны зависимости, которые не используются в скрипте
4. Инструкция `COPY` также записана в одну команду, что также уменьшает кол-во слоев, из исходного файла удалено копирование второго скрипта, тк я его не использую
5. В следующей инструкции `RUN` права на исполнение даю только одному скрипту, так как второго нет) Но если необходим второй, то имена файлов записываются также через пробел
6. Добавлена инстуркция `ENTRYPOINT`, в нее переданы в качестве аргументов инструкция по исполнению

Для того, чтобы собрать образ:

    docker build -t script .

Чтобы запустить контейнер:

    docker run --name script script path

В результате получим:

    nika@nika-vb:~/yadro-test-task$ docker run --name script script path
    path: /home/user/data
    log path: /var/log/app

**Вариант со сменой образа**

    FROM python:3.9-slim
    WORKDIR /yadro-test-task
    COPY file.txt script.py ./
    RUN chmod +x script.py
    ENTRYPOINT ["python3", "script.py", "file.txt"]

1. Изменился исходный образ. Данная версия `python` более легковесна, чем `ubuntu`.
2. Также смена образа избавила нас от дополнительной инструкции `RUN` для установки зависимостей, так как образ их уже содержит
3. В остальном вроде без изменений

По командам сборка и запуск аналогичны, как и результат, однако сборка была быстрее так как образ легче, слоев меньше. Результат:

    nika@nika-vb:~/yadro-test-task$ docker run --name script1 script-task log
    log path: /var/log/app


*в `ENTRYPOINT` можно сразу передать искомое слово, тогда параметры не нужны

*вместо `ENTRYPOINT` тут можно также использовать `CMD`

