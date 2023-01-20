#zadanie 4
import datetime
import unittest

class Person:
    __libcza_instancji = 0

    def __init__(self, pesel, imie, nazwisko, waga = 0.0, wzrost = 0.0):
        Person.__libcza_instancji += 1
        self.__pesel = pesel
        self.__imie = imie
        self.__nazwisko = nazwisko
        if(pesel[2] == '0'):
            self.__rok_urodzenia = 1900 + int(pesel[0:2])
        else:
            self.__rok_urodzenia = 2000 + int(pesel[0:2])   
        self.__wzrost = wzrost
        self.__waga = waga

    def __del__(self):
        Person.__libcza_instancji -= 1

    @property
    def wzrost(self):
    	return self.__wzrost
    @wzrost.setter
    def wzrost(self, value):
    	if(value < 0):
    		self.__wzrost = 0
    	else:
    		self.__wzrost = value

    @property
    def waga(self):
    	return self.__waga
    @waga.setter
    def waga(self, value):
    	if(value < 0):
    		self.__waga = 0
    	else:
    		self.__waga = value

    @property
    def pesel(self):
    	return self.__pesel

    @property
    def rok_urodzenia(self):
    	return self.__rok_urodzenia

    @property
    def wiek(self):
    	now = datetime.datetime.now()
    	return now.year - self.__rok_urodzenia

    @staticmethod
    def getInstances():
        return Person.__libcza_instancji

    @classmethod
    def createPerson_WzrostCM(cls, pesel, imie, nazwisko, wzrost, waga = 0.0):
        return cls(pesel, imie, nazwisko, waga, wzrost / 100)

    def __str__(self):
        return self.__pesel + ', ' + self.__imie + ' ' + self.__nazwisko 

    def __repr__(self):
        return self.__pesel + ', ' + self.__imie + ' ' + self.__nazwisko 

    def __hash__(self):
        return int(self.__pesel) 

class Employe(Person):
    def __init__(self, pesel, imie, nazwisko, praca, waga = 0.0, wzrost = 0.0, pensja = 0.0):
        super().__init__(pesel, imie, nazwisko, waga, wzrost)
        self.__praca = praca
        self.__pensja = pensja

    @property
    def praca(self):
    	return self.__praca
    @praca.setter
    def praca(self, value):
    	self.__praca = value

    @property
    def pensja(self):
    	return self.__pensja
    @pensja.setter
    def pensja(self, value):
    	if(value < 0):
    		self.__pensja = 0
    	else:
    		self.__pensja = value

    def __str__(self):
        return super().__str__()  + ', ' + self.__praca

    def __repr__(self):
        return super().__repr__()  + ', ' + self.__praca

class TestPersonMethods(unittest.TestCase):

    def test_rok1(self):
        osoba = Person("05211111111", "Adrian", 'Nowak')
        self.assertEqual(osoba.rok_urodzenia, 2005)

    def test_rok2(self):
        osoba = Person("85011111111", "Adrian", 'Nowak')
        self.assertEqual(osoba.rok_urodzenia, 1985)

    def test_rok3(self):
        osoba = Employe("85011111111", "Adrian", 'Nowak', 'ZUT')
        self.assertEqual(osoba.rok_urodzenia, 1985)

    def test_wiek(self):
        osoba = Person("85011111111", "Adrian", 'Nowak')
        now = datetime.datetime.now()
        self.assertEqual(osoba.wiek, now.year - 1985)

    def test_waga1(self):
        osoba = Person("85011111111", "Adrian", 'Nowak')
        osoba.waga = -10
        self.assertGreaterEqual(osoba.waga, 0)

    def test_waga2(self):
        osoba = Person("85011111111", "Adrian", 'Nowak', waga = -10)
        self.assertGreaterEqual(osoba.waga, 0)

    def test_wzrost1(self):
        osoba = Person("85011111111", "Adrian", 'Nowak')
        osoba.wzrost = -10
        self.assertGreaterEqual(osoba.wzrost, 0)

    def test_wzrost2(self):
        osoba = Person("85011111111", "Adrian", 'Nowak', wzrost = -10)
        self.assertGreaterEqual(osoba.wzrost, 0)

    def test_pensja1(self):
        osoba = Employe("85011111111", "Adrian", 'Nowak', 'ZUT')
        osoba.pensja = -10
        self.assertGreaterEqual(osoba.pensja, 0)

    def test_pensja2(self):
        osoba = Employe("85011111111", "Adrian", 'Nowak', 'ZUT', pensja = -10)
        self.assertGreaterEqual(osoba.pensja, 0)

if __name__ == '__main__':
    unittest.main(verbosity = 2)

