## TF-IDF

To skrót od Term Frequency-Inverse Document Frequency (częstotliwość występowania słowa - odwrotna częstotliwość w dokumencie). Jest to
technika używana w przetwarzaniu języka naturalnego, czyli w analizowaniu tekstu.


Pomyśl o tekście jako o wielkim kawałku tortu. TF-IDF pomaga nam dowiedzieć się, które składniki są najważniejsze w danym kawałku tortu.

Termin Frequency (częstotliwość występowania słowa) oznacza, jak często dane słowo występuje w dokumencie. Jeśli pewne słowo pojawia się wiele razy, to jest ono ważniejsze dla tego dokumentu. Można to porównać do sytuacji, gdy pewien składnik, na przykład truskawki, występuje wielokrotnie w naszym kawałku tortu.

Inverse Document Frequency (odwrotna częstotliwość w dokumencie) mówi nam, jak unikalne jest dane słowo w całej kolekcji dokumentów. Jeśli słowo występuje rzadko we wszystkich dokumentach, to jest ono bardziej wartościowe. To tak, jakbyśmy mieli rzadki składnik, na przykład czekoladę, którym dekorujemy nasz tort.

Wykorzystując TF-IDF, możemy obliczyć wartość każdego słowa w dokumencie. Im wyższa wartość TF-IDF dla słowa, tym ważniejsze jest dla danego dokumentu.

Na przykład, jeśli mamy dokument o sporcie, to słowa takie jak "piłka nożna" i "bramka" będą miały wysoką wartość TF-IDF, ponieważ występują często w tym dokumencie, ale rzadko w innych. Natomiast słowa takie jak "kot" lub "telewizor" będą miały niską wartość TF-IDF, ponieważ nie są związane z tematem sportu.

Dzięki TF-IDF możemy więc identyfikować ważne słowa w tekście, klasyfikować dokumenty na podstawie ich zawartości i wiele innych zastosowań związanych z analizą tekstu.


## Wektoryzacja


Wektoryzacja w uczeniu maszynowym odnosi się do procesu przekształcania danych tekstowych lub ciągów znaków na liczbowe wektory, które mogą być używane jako dane wejściowe do modeli uczenia maszynowego.

Wektoryzacja jest konieczna, ponieważ większość algorytmów uczenia maszynowego nie jest w stanie bezpośrednio operować na danych tekstowych. Dlatego konieczne jest przekształcenie tych danych na liczbowe reprezentacje, które modele mogą zrozumieć i wykorzystać do predykcji


### liczbowe wektory


Wyobraź sobie, że liczbowe wektory to jak magiczne pudełka, które przechowują różne liczby. Każde pudełko reprezentuje różne informacje lub cechy.

Na przykład, możemy mieć pudełko oznaczone jako "wiek", w którym przechowujemy liczby reprezentujące wiek różnych osób. Innym pudełkiem może być "wzrost", w którym przechowujemy liczby reprezentujące wzrost różnych osób.

Teraz, zamiast trzymać informacje jako osobne pudełka, możemy je połączyć i utworzyć jeden duży wektor. Ten wektor będzie miał różne elementy, z których każdy reprezentuje inną cechę. Może to być wektor, w którym pierwszy element to wiek, drugi element to wzrost, a tak dalej.

Na przykład, jeśli mamy osobę o wieku 10 lat i wzroście 150 cm, możemy utworzyć wektor [10, 150], gdzie pierwszy element (10) reprezentuje wiek, a drugi element (150) reprezentuje wzrost tej osoby.
