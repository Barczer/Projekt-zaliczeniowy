import random
import os

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
                liczba_wierszy = int(input('Podaj liczbę wierszy: '))
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
                    koniec = int(input(f'Podaj koniec zakresu (maksymalna wartość to {len(dataset)}): '))
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
                
                
def podzial_zbioru(dataset):
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
                kontunuacja()
                clear_terminal()
            case 2:
                [print(el) for el in dane_testowe]
                kontunuacja()
                clear_terminal()
            case 3:
                [print(el) for el in dane_walidacyjne]
                kontunuacja()
                clear_terminal()
            case 4:
                print('Dane treningowe')
                [print(el) for el in dane_treningowe]
                print('Dane testowe')
                [print(el) for el in dane_testowe]
                print('Dane Walidacyjne')
                [print(el) for el in dane_walidacyjne]
                kontunuacja()
                clear_terminal()
            case 0:
                return 0


def klasy_decyzyjne(dataset):
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
    [print(f'Klasa: {class_key}, liczebność: {value}') for class_key, value in wartosci.items()]
    kontunuacja()