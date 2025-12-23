## ETAP 1: Inicjalizacja projektu i środowiska
**CEL:** Stworzenie izolowanego środowiska pracy, aby uniknąć konfliktów bibliotek i zachować porządek zgodny z dobrymi praktykami inżynierii danych.

**Kroki:**

1. **Stworzyłem strukturę katalogów:**
    * `data/raw` - na surowe pliki CSV (odseparowanie danych od kodu).
    * `notebooks/` - na eksperymenty i analizę.
    * `src/` - na finalne skrypty Python.
2. **Skonfigurowałem środowisko wirtualne (`venv`):**
    * Zainstalowałem niezbędne biblioteki: `pandas`, `sqlalchemy`, `psycopg2-binary`.
    * Wygenerowałem plik `requirements.txt` dla zapewnienia powtarzalności środowiska.
3. **Zainicjowałem Git i skonfigurowałem `.gitignore`:**
    * Uruchomiłem śledzenie zmian w projekcie.
    * **Problem:** Plik `.gitignore` początkowo blokował widoczność wszystkich plików (przez wildcard `*`).
    * **Rozwiązanie:** Wyczyściłem `.gitignore` i dodałem precyzyjne reguły (ignorowanie tylko `venv/`, `.DS_Store`, `data/`).
4. **Zintegrowałem projekt z GitHubem:**
    * Utworzyłem puste repozytorium publiczne.
    * Podpiąłem zdalny serwer (`git remote add`).
    * Wypchnąłem pierwszą wersję projektu (`git push`).

## ETAP 2: Ekstrakcja i transformacja wstępna (Jupyter)
**CEL:** Zrozumienie struktury danych, naprawa typów oraz przygotowanie datasetu do załadowania do SQL.

**Kroki:**

1. **Wczytałem dane:**
    * Użyłem kodowania `encoding='latin1'`, aby rozwiązać problem z błędami znaków przy imporcie pliku CSV.
2. **Przeprowadziłem audyt danych (`df.info()`):**
    * **Zidentyfikowane problemy:**
        * Kolumny `Order Date` i `Ship Date` były typu `object` (tekst) zamiast `datetime`.
        * Nazwy kolumn zawierały spacje i myślniki (np. `Row Id`, `Sub-Category`), co jest niezgodne ze standardem SQL.
    * **Czyszczenie i transformacja:**
        * Zestandaryzowałem nazwy kolumn na format `snake_case`, by ułatwić późniejsze zapytania SQL.
        * Przekonwertowałem kolumny dat na format `datetime64[ns]` używając metody `.astype()`.
3. **Zaimplementowałem logikę biznesową i walidację:**
    * Dodałem nową kolumnę `delivery_days`, żeby wyciągnąć z dat informację o czasie dostawy.
    * Sprawdziłem spójność danych pod kątem błędów logicznych (np. ujemne dni dostawy).
    * **Wynik:** Dane są czyste, wszystkie wysyłki mieszczą się w poprawnym przedziale (0-7 dni).
4. **Wyeksportowałem przetworzone dane:**
    * Profilaktycznie usunąłem duplikaty.
    * Zapisałem gotowy plik jako `cleaned_superstore.csv` w folderze `processed_data` (z parametrem `index=False`), przygotowując wsad do bazy SQL.