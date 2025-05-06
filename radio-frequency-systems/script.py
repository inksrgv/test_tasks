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