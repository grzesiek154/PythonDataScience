## Pickle

Moduł `pickle` w języku Python jest używany do serializacji obiektów, czyli przekształcania ich w postać, która może być łatwo zapisana do pliku lub przesłana przez sieć, a następnie deserializowana,  czyli odtworzona w pierwotny obiekt. Moduł `pickle` umożliwia przechowywanie obiektów Pythona w trwałej formie i odzyskiwanie ich w późniejszym czasie.


Zapis i odczyt danych:

```python
import pickle

# Zapisanie obiektu do pliku
data = [1, 2, 3, 4, 5]
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Odczytanie obiektu z pliku
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
```


Przesyłanie obiektów między aplikacjami:

```python
import pickle
import socket

# Wysłanie obiektu przez sieć
data = {'name': 'John', 'age': 30}
serialized_data = pickle.dumps(data)
# Wysłanie serialized_data przez socket

# Odbiór obiektu
# Odbierz serialized_data przez socket
received_data = pickle.loads(serialized_data)
```


Caching:

```python
import pickle
import os.path

def get_data():
    # Funkcja, która pobiera dane
    # ...

def get_data_with_cache():
    cache_file = 'cache.pkl'

    if os.path.isfile(cache_file):
        with open(cache_file, 'rb') as file:
            data = pickle.load(file)
    else:
        data = get_data()
        with open(cache_file, 'wb') as file:
            pickle.dump(data, file)

    return data
```


Moduł pickle jest przydatny, gdy chcemy zapisywać i odczytywać struktury danych lub obiekty Pythona w trwałej formie, przekazywać je między aplikacjami lub wykorzystywać w mechanizmach pamięci podręcznej. Należy jednak pamiętać, że deserializacja danych z niezaufanego źródła może stanowić zagrożenie bezpieczeństwa, ponieważ kod pickle może być złośliwie spreparowany. Dlatego należy zachować ostrożność przy deserializacji danych pickle z nieznanych lub niezaufanych źródeł.


### load()


Przykład użycia metody `pickle.load()`:


```python
import pickle

# Odczytanie obiektu z pliku
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
```


W powyższym przykładzie, po wywołaniu `pickle.load(file)`, metoda `load()` odczytuje zawartość pliku w formacie pickle i odtwarza oryginalny obiekt, który został wcześniej zapisany. Odtworzony obiekt jest przypisywany do zmiennej `loaded_data` i może być dalej używany w programie.

Warto zauważyć, że metoda `pickle.load()` jest bezpieczna, jeśli dane pickle są pochodzenia zaufanego i nie zostały zmodyfikowane przez niezaufane źródło. Dlatego należy zachować ostrożność podczas deserializacji danych z nieznanych lub niezaufanych źródeł, ponieważ może to prowadzić do wykonania złośliwego kodu.
