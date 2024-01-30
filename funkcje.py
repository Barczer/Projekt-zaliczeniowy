def menu_naglowki():
    print(40*'*')
    print('''Dostępne akcje dla pliku:
    1: Wydrukuj zestaw danych
    2: Podział zbioru danych na zbiory testowe i treningowe
    3:
    4:
    5:
    0: Powrót
    ''')
    print(40*'*')
def menu_bez_naglowkow():
    print(40*'*')
    print('''Dostępne akcje dla pliku:
    1: Wydrukuj zestaw danych
    2: Podział zbioru danych na zbiory testowe i treningowe
    3:
    4:
    0: Powrót
    ''')
    print(40*'*')

def kontunuacja():
    input('Kliknij enter aby kontynuować...')


def wartosci_podzialu(dataset):
    print('''
    1. Cały plik
    2. Liczbę wierszy
    3. Zakres wierszy''')
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
    dane_treningowe_liczba = len(dataset)*wartosc_1/100
    dane_treningowe = dataset[:dane_treningowe_liczba]
    dane_testowe_liczba = len(dataset)*wartosc_1/100+len(dataset)*wartosc_2/100
    dane_testowe = dataset[dane_treningowe_liczba:dane_testowe_liczba]
    dane_walidayjne_liczba = len(dataset)*wartosc_1/100+len(dataset)*wartosc_2/100+len(dataset)*wartosc_3/100
    dane_walidayjne = dataset[dane_treningowe_liczba:dane_walidayjne_liczba] 