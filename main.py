# with open("iris.data", 'r') as file:
#     dataset = []
#     for line in file:
#         lista = line.split(',')
#         lista[-1] = lista[-1].replace('\n', '')
#         # print(lista)
#         # break
#         dataset.append(lista)
#
# def ciecie_listy(lista, znacznik1 = None, znacznik2 = None):
#     print(lista[znacznik1:znacznik2])
#
# # print(dataset)
# # [print(i) for i in dataset]
#
# print(dataset[1][1].upper())

import os
def menu_load_dataset():
    print('''WCZYTANIE DANYCH
    1 - Pliki z folderu /bazy do wczytania
    2 - Ścieżka do pliku
    3 - Link
    9 - Powrót do menu
    0 - Zakończenie programu''')



def main(filepath):
    """ główna funkcja modułu"""
    while True:
        print('*'*40)
        print('''MENU GŁÓWNE
        1 - Wczytanie data setu
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
                load_dataset()
            case 0:
                exit('Do zobaczenia!', )

def load_dataset():
    os.system('cls')
    menu_load_dataset()
    try:
        choice_2 = int(input('Wybierz opcję: '))
    except:
        print('Wprowadzono niepoprawną wartość!')

    match choice_2:
        case 1:
            print(os.listdir())

        case 2:
            pass
        case 3:
            pass
        case 9:
            next
        case 0:
            exit('Do zobaczenia')

if __name__ == "__main__":
    filepath = ''
    main(filepath)