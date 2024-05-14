from tkinter import *

import tkintermapview

users=[]



class User:
    def __init__(self, imie, nazwisko, posty, miejscowosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.posty = posty
        self.miejscowosc = miejscowosc
def dodaj_uzytkownika():
    imie=entry_imie.get()
    nazwisko=entry_nazwisko.get()
    posty=entry_posty.get()
    miejscowosc=entry_miejscowosc.get()
    user=User(imie, nazwisko, posty, miejscowosc)
    users.append(user)
    print(user.imie)
    lista_uzytkowników()
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_imie.focus()

def lista_uzytkowników():
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f'{user.imie} {user.nazwisko}')


def pokaz_szczegoly_uzytkownika():
    i= listbox_lista_obiektow.index(ACTIVE)
    print(i)
    imie=users[i].imie
    nazwisko=users[i].nazwisko
    posty=users[i].posty
    miejscowosc=users[i].miejscowosc

    label_imie_szczegoly_wartosc.config(text=imie)
    label_miejscowosc_szczegoly_wartosc.config(text=nazwisko)
    label_posty_szcegoly_wartosc.config(text=posty)
    label_miejscowosc_szczegoly_wartosc.config(text=miejscowosc)


def usun_uzytkownika():
    i = listbox_lista_obiektow.index(ACTIVE)
    users.pop(i)
    lista_uzytkowników()



def edytuj_uzytkownika():
    i= listbox_lista_obiektow.index(ACTIVE)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)
    lista_uzytkowników()

    entry_imie.insert(0, users[i].imie)
    entry_nazwisko.insert(0, users[i].nazwisko)
    entry_posty.insert(0, users[i].posty)
    entry_miejscowosc.insert(0, users[i].miejscowosc)
    button_dodaj_uzytkownika.config(text="zapisz zmiany", command=lambda:aktualizuj_uzytkownika(i))

def aktualizuj_uzytkownika(i):
    users[i].imie=entry_imie.get()
    users[i].nazwisko=entry_nazwisko.get()
    users[i].posty=entry_posty.get()
    users[i].miejscowosc=entry_miejscowosc.get()
    lista_uzytkowników()

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)

    button_dodaj_uzytkownika.config(text="Dodaj uzytkownika", command=dodaj_uzytkownika)



root = Tk()
root.geometry('800x700')
root.title('Map Book')


ramka_lista_uzytkownikow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektu=Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2, padx=50, pady=20)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_uzytkownikow, text='Lista znajomych:')
listbox_lista_obiektow=Listbox(ramka_lista_uzytkownikow, width=30)
button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow, text='Pokaz szczegoly', command=pokaz_szczegoly_uzytkownika)
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow, text='Usuń', command=usun_uzytkownika)
button_edytuj_uzytkownika=Button(ramka_lista_uzytkownikow, text= 'Edytuj', command=edytuj_uzytkownika)

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_uzytkownika.grid(row=2, column=1)
button_edytuj_uzytkownika.grid(row=2, column=2)

#ramka_formularz
label_formularz=Label(ramka_formularz, text='Formularz edycji dodawamnia')
label_imie=Label(ramka_formularz, text='Imie:')
label_nazwisko=Label(ramka_formularz, text='Nazwisko:')
label_posty=Label(ramka_formularz, text='Posty:')
label_miejscowosc=Label(ramka_formularz, text='Miejscowość:')
entry_imie=Entry(ramka_formularz)
entry_nazwisko=Entry(ramka_formularz, width=30)
entry_posty=Entry(ramka_formularz)
entry_miejscowosc=Entry(ramka_formularz)


label_formularz.grid(row=0, column=0, columnspan=3)
label_imie.grid(row=1, column=0,sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_posty.grid(row=3, column=0, sticky=W)
label_miejscowosc.grid(row=4, column=0)
entry_imie.grid(row=1, column=1, sticky=W)
entry_nazwisko.grid(row=2, column=1, sticky=W)
entry_posty.grid(row=3, column=1, sticky=W)
entry_miejscowosc.grid(row=4, column=1, sticky=W)

button_dodaj_uzytkownika=Button(ramka_formularz, text='Dodaj użytkownika', command= dodaj_uzytkownika)
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)


# ramka szczegóły obiektu
label_opis_obiektu=Label(ramka_szczegoly_obiektu, text='Szczegóły obiektu:')
label_imie_szczegoly=Label(ramka_szczegoly_obiektu, text='Imie:')
label_imie_szczegoly_wartosc=Label(ramka_szczegoly_obiektu, text='...:', width=10)
label_nazwisko_szczegoly=Label(ramka_szczegoly_obiektu, text='Nazwisko:')
label_nazwisko_szczegoly_wartosc=Label(ramka_szczegoly_obiektu, text='...:', width=10)
label_posty_szcegoly=Label(ramka_szczegoly_obiektu, text='Posty:')
label_posty_szcegoly_wartosc=Label(ramka_szczegoly_obiektu, text='...:', width=10)
label_miejscowosc_szczegoly=Label(ramka_szczegoly_obiektu, text="Miejscowość")
label_miejscowosc_szczegoly_wartosc=Label(ramka_szczegoly_obiektu,text='...:', width=10)



label_opis_obiektu.grid(row=0, column=0, sticky=W)
label_imie_szczegoly.grid(row=1, column=0)
label_imie_szczegoly_wartosc.grid(row=1, column=1)
label_nazwisko_szczegoly.grid(row=1, column=2)
label_nazwisko_szczegoly_wartosc.grid(row=1, column=3)
label_posty_szcegoly.grid(row=1, column=4)
label_posty_szcegoly_wartosc.grid(row=1, column=5)
label_miejscowosc_szczegoly.grid(row=1, column=6)
label_miejscowosc_szczegoly_wartosc.grid(row=1, column=7)


map_widget=tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=700, height=300)
map_widget.grid(row=2, column=0, columnspan=8)



root.mainloop()