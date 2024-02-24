import random
import os
import csv

def clear_terminal():
    os.system('clear')

def menu_naglowki():
    print(40*'*')
    print('''Dostępne akcje dla pliku:
    1: Wydrukuj zestaw danych
    2: Podział zbioru danych na zbiory testowe i treningowe
    3: Wydrukowanie nagłówków 
    4: Klasy decyzyjne
    5: 
    0: Powrót
    ''')
    print(40*'*')

def kontunuacja():
    input('Kliknij enter aby kontynuować...')


def wartosci_podzialu(dataset):
    print('''
    1. Cały plik
    2. Liczbę wierszy
    3. Zakres wierszy
    0: Powrót''')
    try:
        choice = int(input('Wybierz opcję: '))
    except:
        print('Wprowadzono nieprawidłową wartość')
    match choice:
        case 1:
            return (1, 'all')
        case 2:
            try:
                while True:
                    liczba_wierszy = int(input('Podaj liczbę wierszy: '))
                    if liczba_wierszy > len(dataset):
                        print(f'Maksymalna liczba wierszy to: {len(dataset)}')
                        continue
                    else:
                        return (2, liczba_wierszy)
            except:
                print('Wprowadzono nieprawidłową wartość')
        case 3:
            while True:
                try:
                    poczatek = int(input('Podaj początek zakresu: '))
                except:
                    print('Wprowadzono nieprawidłową wartość')
                try:
                    while True:
                        koniec = int(input(f'Podaj koniec zakresu (maksymalna wartość to {len(dataset)}): '))
                        if koniec > len(dataset):
                            print(f'Koniec zakresu poza długością datasetu! Maksymalna długość: {len(dataset)}')
                            continue
                        else:
                            break
                except:
                    print('Wprowadzono nieprawidłową wartość')
                try:
                    krok = input('Podaj krok (domyślnie 1): ')
                    if len(krok) == 0:
                        krok = 1
                    else:
                        krok = int(krok)
                except:
                    print('Wprowadzono nieprawidłową wartość')
                if koniec < poczatek:
                    print('Wprowadzono błędne zakresy! punkt końcowy nie może być mniejszy od punktu początkowego')
                    continue
                elif koniec < 0 or poczatek < 0:
                    print('Wartości nie mogą być minusowe')
                    continue
                else:
                    break
            return (3, poczatek, koniec, krok)
        case 0:
            return 0
                
                
def podzial_zbioru(dataset, naglowki, naglowki_dane):
    while True:
        try:
            wartosc_1 = int(input('Podaj procent zbioru treningowego: '))
            wartosc_2 = int(input('Podaj procent zbioru testowego: '))
            wartosc_3 = int(input('Podaj procent zbioru walidacyjnego: '))
        except:
            print('Podane wartości nie są liczbami')
        if wartosc_1+wartosc_2+wartosc_3 == 100:
            break
        else:
            print('Nie mogę podzielić więcej niż 100%!')
    dane_treningowe_liczba = int(round((len(dataset)*wartosc_1/100), 0))
    dane_testowe_liczba = int(round((len(dataset)*wartosc_2/100), 0))
    dane_walidayjne_liczba = int(round((len(dataset)*wartosc_3/100),0))
    # print(f'dane treningwe = {dane_treningowe_liczba}\ndane testowe = {dane_testowe_liczba}\ndane walidacyjne = {dane_walidayjne_liczba}')
    # print(f'Suma wartości = {dane_walidayjne_liczba + dane_testowe_liczba + dane_treningowe_liczba}')
    rand_list = random.sample(range(0, len(dataset)), len(dataset))
    # print(f'type dane = {type(dane_treningowe_liczba)}')
    # kontunuacja()
    rand_list_treningowe = rand_list[0:dane_treningowe_liczba]
    # kontunuacja()
    rand_list = rand_list[dane_treningowe_liczba:]
    rand_list_testowe = rand_list[0:dane_testowe_liczba]
    rand_list = rand_list[dane_testowe_liczba:]
    rand_list_walidacyjne = rand_list[0:]
    dane_treningowe = [dataset[i] for i in rand_list_treningowe]
    dane_testowe = [dataset[i] for i in rand_list_testowe]
    dane_walidacyjne = [dataset[i] for i in rand_list_walidacyjne]
    while True:
        print('''
        Który zbiór chcesz wyświetlić?
        1. Treningowy
        2. Testowy
        3. Walidacyjny
        4. Wszystkie
        0. Powrót''')
        try:
            choice = int(input(': '))
        except:
            print('Wprowadzono błędną wartość.')
        match choice:
            case 1:
                [print(el) for el in dane_treningowe]
                save_csv_menu(dane_treningowe, naglowki, naglowki_dane)
                kontunuacja()
                clear_terminal()
            case 2:
                [print(el) for el in dane_testowe]
                save_csv_menu(dane_testowe, naglowki, naglowki_dane)
                kontunuacja()
                clear_terminal()
            case 3:
                [print(el) for el in dane_walidacyjne]
                save_csv_menu(dane_walidacyjne, naglowki, naglowki_dane)
                kontunuacja()
                clear_terminal()
            case 4:
                print('Dane treningowe')
                [print(el) for el in dane_treningowe]
                print('Dane testowe')
                [print(el) for el in dane_testowe]
                print('Dane Walidacyjne')
                [print(el) for el in dane_walidacyjne]
                save_csv_menu(dataset, naglowki, naglowki_dane)
                kontunuacja()
                clear_terminal()
            case 0:
                return 0


def klasy_decyzyjne(dataset, naglowki, naglowki_dane):
    print(f'Wskaż, które element listy to kasa decyzyjna: ')
    i = 1
    for el in dataset[0]:
        print(f'{i}: {el}')
        i += 1
    try:
        choice_class = int(input(': '))
    except:
        print('Błędna wartość!')
    choice_class -= 1

    wartosci = {}
    for list in dataset:
        class_name = list[choice_class]
        if class_name not in wartosci.keys():
            wartosci[class_name] = 1
        else:
            wartosci[class_name] += 1
    # [print(f'Klasa: {class_key}, liczebność: {value}') for class_key, value in wartosci.items()]
    i = 1
    for class_key, value in wartosci.items():
        print(f'{i}: {class_key}, liczebność zbioru: {value}')
        i += 1
    while True:
        choice_class = input('Czy chcesz wyświelić któryś z elementów? T/n: ').lower()
        if choice_class not in ['t', 'n']:
            print('Nieprawidłowa wartość!')
        elif choice_class == 't':
            keys = [keys for keys, value in wartosci.items()]
            break
        else:
            return 0

    while True:
        try:
            i = 1
            for class_key, value in wartosci.items():
                print(f'{i}: {class_key}')
                i += 1
            choice_class = int(input('Którą klasę chcesz wyświetlić?: '))
            if choice_class > len(keys) or choice_class < 0:
                print('Wartość z poza listy!')
                continue
            elif choice_class == 0:
                return 0
        except:
            print('Nieprawidłowa wartość!')
        temp_set = []
        for set in dataset:
            if keys[choice_class-1] in set:
                print(set)
                temp_set.append(set)
        save_csv_menu(temp_set, naglowki, naglowki_dane)
        while True:
            choice_class_2 = input('Czy chcesz wydrukować jeszcze jakąś klase?: T/n').lower()
            if choice_class_2 not in ['t', 'n']:
                print('Nieprawidłowa wartość!')
            else:
                break
        if choice_class_2 == 't':
            continue
        else:
            break

def save_csv_file(data, file_name):
    with open (f'{file_name}.csv', 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerows(data)
def save_csv_menu(date, naglowki, naglowki_dane):
    date = date
    while True:
        choice_csv = input('Czy chcesz zapisać dane? T/n: ').lower()
        if choice_csv not in ['t', 'n']:
            print('Nieprawidłowa wartość!')
            continue
        else:
            break
    if choice_csv == 't':
        if naglowki == 't':
            temp_date = date[:]
            temp_date.insert(0, naglowki_dane)
        else:
            temp_date = date
        file_name = input('Podaj nazwę pliku: ')
        save_csv_file(temp_date, file_name)
        print('Plik został pomyślnie zapisany.')
        return 0
    else:
        return 0