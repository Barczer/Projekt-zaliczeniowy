import random
import os
import csv


def head_menu():
    print(40*'*')
    print('''Dostępne akcje dla pliku:
    1: Wydrukuj zestaw danych
    2: Podział zbioru danych na zbiory testowe i treningowe
    3: Wydrukowanie nagłówków 
    4: Klasy decyzyjne
    0: Powrót
    ''')
    print(40*'*')

def continuation():
    input('Kliknij enter aby kontynuować...')


def print_menu(dataset):
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
                    row_count = int(input('Podaj liczbę wierszy: '))
                    if row_count > len(dataset):
                        print(f'Maksymalna liczba wierszy to: {len(dataset)}')
                        continue
                    else:
                        return (2, row_count)
            except:
                print('Wprowadzono nieprawidłową wartość')
        case 3:
            while True:
                try:
                    start = int(input('Podaj początek zakresu: '))
                except:
                    print('Wprowadzono nieprawidłową wartość')
                try:
                    while True:
                        end = int(input(f'Podaj koniec zakresu (maksymalna wartość to {len(dataset)}): '))
                        if end > len(dataset):
                            print(f'Koniec zakresu poza długością datasetu! Maksymalna długość: {len(dataset)}')
                            continue
                        else:
                            break
                except:
                    print('Wprowadzono nieprawidłową wartość')
                try:
                    step = input('Podaj step (domyślnie 1): ')
                    if len(step) == 0:
                        step = 1
                    else:
                        step = int(step)
                except:
                    print('Wprowadzono nieprawidłową wartość')
                if end < start:
                    print('Wprowadzono błędne zakresy! punkt końcowy nie może być mniejszy od punktu początkowego')
                    continue
                elif end < 0 or start < 0:
                    print('Wartości nie mogą być minusowe')
                    continue
                else:
                    break
            return (3, start, end, step)
        case 0:
            return 0
                
                
def dataset_split(dataset, header, header_list):
    while True:
        try:
            value_1 = int(input('Podaj procent zbioru treningowego: '))
            value_2 = int(input('Podaj procent zbioru testowego: '))
            value_3 = int(input('Podaj procent zbioru walidacyjnego: '))
        except:
            print('Podane wartości nie są liczbami')
        if value_1+value_2+value_3 == 100:
            break
        else:
            print('Nie mogę podzielić więcej niż 100%!')
    training_data_number = int(round((len(dataset)*value_1/100), 0))
    test_data_number = int(round((len(dataset)*value_2/100), 0))
    validation_data_number = int(round((len(dataset)*value_3/100),0))
    rand_list = random.sample(range(0, len(dataset)), len(dataset))
    rand_list_training = rand_list[0:training_data_number]
    rand_list = rand_list[training_data_number:]
    rand_list_test = rand_list[0:test_data_number]
    rand_list = rand_list[test_data_number:]
    rand_list_validation = rand_list[0:]
    training_data = [dataset[i] for i in rand_list_training]
    test_data = [dataset[i] for i in rand_list_test]
    validation_data = [dataset[i] for i in rand_list_validation]
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
                [print(el) for el in training_data]
                save_csv_menu(training_data, header, header_list)
            case 2:
                [print(el) for el in test_data]
                save_csv_menu(test_data, header, header_list)
            case 3:
                [print(el) for el in validation_data]
                save_csv_menu(validation_data, header, header_list)
            case 4:
                print('Dane treningowe')
                [print(el) for el in training_data]
                print('Dane testowe')
                [print(el) for el in test_data]
                print('Dane Walidacyjne')
                [print(el) for el in validation_data]
                save_csv_menu(dataset, header, header_list)
            case 0:
                return 0

def choice_class(dataset, header, header_list):
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

    values = {}
    for list in dataset:
        class_name = list[choice_class]
        if class_name not in values.keys():
            values[class_name] = 1
        else:
            values[class_name] += 1
    # [print(f'Klasa: {class_key}, liczebność: {value}') for class_key, value in values.items()]
    i = 1
    for class_key, value in values.items():
        print(f'{i}: {class_key}, liczebność zbioru: {value}')
        i += 1
    while True:
        choice_class = input('Czy chcesz wyświelić któryś z elementów? T/n: ').lower()
        if choice_class not in ['t', 'n']:
            print('Nieprawidłowa wartość!')
        elif choice_class == 't':
            keys = [keys for keys, value in values.items()]
            break
        else:
            return 0

    while True:
        try:
            i = 1
            for class_key, value in values.items():
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
        save_csv_menu(temp_set, header, header_list)
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