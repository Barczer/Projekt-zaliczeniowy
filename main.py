import os
import csv
import time
import sys
from funkcje import *
import random

def local_file():
    rozszerzenia = ['.xlsx', '.data', '.csv', '.xls']
    os.system('cls')
    lista_plikow_all = os.listdir()
    lista_datasetow = [el for el in lista_plikow_all if el[el.find('.'):] in rozszerzenia]
    if len(lista_datasetow) > 0:
        print('LISTA PLIKÓW')
    else:
        print(f'Brak plików lokalnych z rozszerzeniem {rozszerzenia}')
        return 0
    i = 1
    while i <= len(lista_datasetow):
        print(f'{i}: {lista_datasetow[i - 1]}')
        if i == len(lista_datasetow):
            print('0: Powrót do poprzedniego menu')
        i += 1
    while True:
        try:
            choice_2 = int(input('Wybierz dateset: '))
            break
        except:
            print('Wprowadzono niepoprawną wartość!')
    if choice_2 != 0:
        lp_data_set = choice_2 - 1
    else:
        return 0
    while True:
        czy_naglowki = input('Czy zestaw zawiera nagłówki? T/n: ').lower()
        if czy_naglowki == 't' or czy_naglowki == 'n':
            break
        else:
            print('Wprowadzono niepoprawną wartość.')
    while True:
        separator = input('Podaj separator (domyślnie to ";"): ')
        # print(f'sep = {separator}\nlen sep = {len(separator)}')
        if len(separator) == 1:
            break
        elif len(separator) == 0:
            separator = ';'
            break
        else:
            print('Wygląda na to, że wprowadziłeś więcej niż jeden separator!')
    load_dataset(lista_datasetow[lp_data_set], czy_naglowki, separator)


def main(filepath):
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
                pass
            case 0:
                exit('Do zobaczenia!', )

def load_dataset(sciezka, naglowki, separator):
    try:
        with open(sciezka, 'r') as file:
            reader = csv.reader(file, delimiter=separator)
            dane = []
            if naglowki == 't':
                for row in reader:
                    lista_naglowki = row
                    break
                for row in reader:
                    dane.append(row)
            else:
                for row in reader:
                    dane.append(row)
        if len(dane[len(dane)-1]) == 0:
            dane = dane[:-1]
    except:
        print(f'Błąd przy wczytywaniu danych {sys.exc_info()}. Powrót do menu głównego...')
        time.sleep(3)
        return 0
    while True:
        if naglowki == 't':
            menu_naglowki()
        else:
            menu_bez_naglowkow()
        try:
            choice_2 = int(input('Jaką czynność wybierasz?: '))
        except:
            print('Podano nieprawidłową wartość')
        match choice_2:
            case 1:
                podzielnik = wartosci_podzialu(dane)
                if podzielnik[0] == 1:
                    [print(el) for el in dane]
                elif podzielnik[0] == 2:
                    print(dane[:podzielnik[1]])
                elif podzielnik[0] == 3:
                    print(dane[podzielnik[1]-1:podzielnik[2]:podzielnik[3]])
                else:
                    pass
                kontunuacja()
            case 2:
                podzial_zbioru(dane)
            case 0:
                return 0


if __name__ == "__main__":
    filepath = ''
    main(filepath)