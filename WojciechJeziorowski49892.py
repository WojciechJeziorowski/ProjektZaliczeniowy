#Lista Zakupów
import os.path
import time


def wypisz_menu():
    print()
    print('1. Dodaj produkt do kupienia')
    print('2. Oznacz produkt jako kupiony')
    print('3. Pokaż produkty do kupienia i kupione')
    print('4. Usuń produkt z listy')
    print('5. Ustaw dany produkt na początek listy')
    print('6. Ocznacz kupiony produkt jako niekupiony')
    print('7. Pokaz rachunek')
    print('8. Wyjdź z programu')

def pobierz_wybor():
    while True:
        i = input('Co chcesz zrobić? (1-8): ')
        try:
            liczba = int(i)
        except ValueError:
            print('To musi być liczba')
            continue
        if 1 <= liczba <= 8:
            return liczba
        print('To musi być liczba od 1 do 8')

class ListaZakupow:
    def __init__(self):
        self.lista_produktow_do_kupienia = []
        self.lista_produktow_kupionych = []
        self.rachunek = []
    def dodaj_produkt_do_listy(self):
        self.lista_produktow_do_kupienia.append(input('Podaj nazwę produktu do kupienia: '))
    def oznacz_produkt_jako_kupiony(self):
        indeks_kupionego_produktu = self._pobierz_indeks()
        self.lista_produktow_kupionych.append(self.lista_produktow_do_kupienia[indeks_kupionego_produktu])
        del self.lista_produktow_do_kupienia[indeks_kupionego_produktu]
        cena = self._podaj_cene()
        self.rachunek.append(cena)
    def pokaz_produkty_do_kupienia_i_kupione(self):
        print()
        print('Do kupienia jest: ')
        for indeks, produkty_do_kupienia in enumerate(self.lista_produktow_do_kupienia):
            print(f'\t\t{indeks} [ ] {produkty_do_kupienia}')
        print()
        print('Kupiono: ')
        for indeks, produkty_kupione in enumerate(self.lista_produktow_kupionych):
            print(f'\t\t{indeks} [x] {produkty_kupione}')
    def usun_produkt_do_kupienia(self):
        indeks_produktu_do_usuniecia = self._pobierz_indeks()
        del self.lista_produktow_do_kupienia[indeks_produktu_do_usuniecia]
    def ustaw_produkt_na_poczatek_listy(self):
        indeks_produktu_do_kupienia = self._pobierz_indeks()
        element_na_poczatek = self.lista_produktow_do_kupienia[indeks_produktu_do_kupienia]
        del self.lista_produktow_do_kupienia[indeks_produktu_do_kupienia]
        self.lista_produktow_do_kupienia.insert(0, element_na_poczatek)
    def oznacz_produkt_kupiony_jako_niekupiony(self):
        indeks_produktu_kupionego = self._pobierz_indeks(self.lista_produktow_kupionych)
        self.lista_produktow_do_kupienia.append(self.lista_produktow_kupionych[indeks_produktu_kupionego])
        del self.lista_produktow_kupionych[indeks_produktu_kupionego]
        del self.rachunek[indeks_produktu_kupionego]
    def pokaz_rachunek(self):
        print()
        suma = 0
        print('Twój rachunek to: ')
        for indeks, cena in enumerate(self.rachunek):
            print(f'\t\t{indeks} -> {round(cena, 2)} PLN')
            suma += cena
            suma = round(suma, 2)
        print('Łącznie:', suma, 'PLN')
        print()
        while True:
            wybor = input('Czy chcesz zapisać rachunek do pliku? t/n')
            if wybor =='t' or wybor == 'T':
                while not os.path.exists('rachunek.txt'):
                    print('Plik nie istnieje, utworz plik rachunek.txt')
                    time.sleep(5)
                rachunek_string = str(self.rachunek)
                with open('rachunek.txt', 'w') as fp:
                    fp.writelines(rachunek_string)
                return
            elif wybor == 'n' or wybor == 'N':
                return
            else:
                print('Wpisz "t" lub "n" ')

    def _pobierz_indeks(self, lista=None):
        if lista is None:
            lista = self.lista_produktow_do_kupienia
        if len(lista) == 0:
            print('Najpierw dodaj produkt do listy zakupów')
            petla_glowna_programu()
        while True:
            print()
            for indeks, produkt_do_kupienia in enumerate(lista):
                print(f'\t\t{indeks} [ ] {produkt_do_kupienia}')
            print()
            try:
                indeks_produktu = int(input('Który indeks: '))
            except ValueError:
                print('To musi być liczba')
                continue
            if indeks_produktu >= 0 and indeks_produktu < len(lista):
                return indeks_produktu
            else:
                print('Podana liczba jest spoza przedzialu')
    def _podaj_cene(self):
        while True:
            try:
                cena = float(input('Podaj cene zakupionego produktu [PLN]:'))
            except ValueError:
                print('To musi być liczba')
                continue
            if cena >= 0:
                return cena
            else:
                print('Cena musi być liczbą nieujemną')

def petla_glowna_programu():
    instancje_produktow_do_kupienia = ListaZakupow()
    while True:
        wypisz_menu()
        wybor = pobierz_wybor()
        if wybor == 1:
            instancje_produktow_do_kupienia.dodaj_produkt_do_listy()
        elif wybor == 2:
            instancje_produktow_do_kupienia.oznacz_produkt_jako_kupiony()
        elif wybor == 3:
            instancje_produktow_do_kupienia.pokaz_produkty_do_kupienia_i_kupione()
        elif wybor == 4:
            instancje_produktow_do_kupienia.usun_produkt_do_kupienia()
        elif wybor == 5:
            instancje_produktow_do_kupienia.ustaw_produkt_na_poczatek_listy()
        elif wybor == 6:
            instancje_produktow_do_kupienia.oznacz_produkt_kupiony_jako_niekupiony()
        elif wybor == 7:
            instancje_produktow_do_kupienia.pokaz_rachunek()
        elif wybor == 8:
            return
petla_glowna_programu()
