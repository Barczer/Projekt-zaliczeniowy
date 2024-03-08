import os
import csv
import time
import sys
from funkcje import *
import random

def local_file():
    extensions = ['.xlsx', '.data', '.csv', '.xls']
    os.system('cls')
    list_file_all = os.listdir()
    data_set_list = [el for el in list_file_all if el[el.find('.'):] in extensions]
    if len(data_set_list) > 0:
        print('LISTA PLIKÓW')
    else:
        print(f'Brak plików lokalnych z rozszerzeniem {extensions}')
        return 0
    i = 1
    while i <= len(data_set_list):
        print(f'{i}: {data_set_list[i - 1]}')
        if i == len(data_set_list):
            print('0: Powrót do poprzedniego menu')
        i += 1
    while True:
        try:
            choice_2 = int(input('Wybierz dateset: '))
            if choice_2 > len(data_set_list):
                print('Nie ma takiego pliku!')
                continue
            break
        except:
            print('Wprowadzono niepoprawną wartość!')
    if choice_2 != 0:
        lp_data_set = choice_2 - 1
    else:
        return 0
    while True:
        is_header = input('Czy zestaw zawiera nagłówki? T/n: ').lower()
        if is_header == 't' or is_header == 'n':
            break
        else:
            print('Wprowadzono niepoprawną wartość.')
    while True:
        separator = input('Podaj separator (domyślnie to ";"): ')
        if len(separator) == 1:
            break
        elif len(separator) == 0:
            separator = ';'
            break
        else:
            print('Wygląda na to, że wprowadziłeś więcej niż jeden separator!')
    load_dataset(data_set_list[lp_data_set], is_header, separator)

def filepath():
    while True:
        file_path = input('Podaj dokładną ścieżkę do pliku: ')
        if os.path.isfile(file_path):
            break
        else:
            print('Podany plik nie istnieje!')
    while True:
        is_header = input('Czy zestaw zawiera nagłówki? T/n: ').lower()
        if is_header == 't' or is_header == 'n':
            break
        else:
            print('Wprowadzono niepoprawną wartość.')
    while True:
        separator = input('Podaj separator (domyślnie to ";"): ')
        if len(separator) == 1:
            break
        elif len(separator) == 0:
            separator = ';'
            break
        else:
            print('Wygląda na to, że wprowadziłeś więcej niż jeden separator!')
    load_dataset(file_path, is_header, separator)

def main():
    """ główna funkcja modułu"""
    while True:
        print('*'*40)
        print('''MENU GŁÓWNE
        1 - Wczytanie data setu z listy plików z folderu projektu
        2 - Wczytanie data setu z wskazanej ścieżki
        0 - Zakończenie programu''')
        print('*'*40)
        while True:
            try:
                choice = int(input('Wybierz opcje: '))
                break
            except:
                print('Wprowadzono niepoprawną wartość!')

        match choice:
            case 1:
                local_file()
            case 2:
                filepath()
            case 0:
                exit('Do zobaczenia!', )

def load_dataset(file_path, is_header, separator):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=separator)
            date = []
            header_list = []
            if is_header == 't':
                i = 1
                for row in reader:
                    if i == 1:
                        header_list = row
                    else:
                        date.append(row)
                    i += 1
            else:
                for row in reader:
                    date.append(row)
        if len(date[len(date)-1]) == 0:
            date = date[:-1]
    except:
        print(f'Błąd przy wczytywaniu danych {sys.exc_info()}. Powrót do menu głównego...')
        time.sleep(3)
        return 0
    while True:
        head_menu()
        try:
            choice_2 = int(input('Jaką czynność wybierasz?: '))
        except:
            print('Podano nieprawidłową wartość')
        match choice_2:
            case 1:
                print_choice = print_menu(date)
                if print_choice == 0:
                    return 0
                elif print_choice[0] == 1:
                    [print(el) for el in date]
                    save_csv_menu(date, is_header, header_list)
                elif print_choice[0] == 2:
                    [print(el) for el in date[:print_choice[1]]]
                    save_csv_menu(date[:print_choice[1]], is_header, header_list)
                elif print_choice[0] == 3:
                    print(date[print_choice[1]-1:print_choice[2]:print_choice[3]])
                    # dopisać zapisywanie pliku do csv
                else:
                    pass
            case 2:
                dataset_split(date, is_header, header_list)
            case 3:
                if is_header == 't':
                    print(header_list)
                else:
                    print('''
                          
                          
                W datasecie brak nagłówków
                          
                          
                          ''')
                    continuation()
            case 4:
                choice_class(date, is_header, header_list)
            case 0:
                return 0


if __name__ == "__main__":
    main()