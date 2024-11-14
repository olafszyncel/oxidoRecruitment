# oxidoRecruitment
Rekrutacja do Oxido na stanowisko JR AI Developer

## Opis projektu
Aplikacja w Pythonie łączy się z API OpenAI w celu przetworzenia tekstowego artykułu (tresc_artykulu.txt) do sekcji <body> formatu HTML (artykul.html), API oznacza miejsca, gdzie powinny znaleźć się grafiki, korzystając z tagu <img>. Sekcja body jest strukturalnie przygotowana do wstawienia w szablon pliku HTML (szablon.html). Dodatkowo, aplikacja wkleja przygotowaną sekcje <body> przez API do przygotowanego wcześniej szablonu (podglad.html).

### Projekt zawiera pliki: 
* main.py - plik główny, który zawiera kod aplikacji do odczytu artykułu, wysyłania zapytań do API OpenAI oraz zapisywania wynikowego HTML.
* tresc_artykulu.txt - przykładowy plik tekstowy zawierający treść artykułu do przetworzenia
* api_key.txt - plik zawierający klucz API OpenAI
* artykul.html - plik wynikowy z sekcją <body> kodu HTML artykułu, gotowy do osadzenia w strukturze strony
* szablon.html - szablon HTML do podglądu artykułu. Sekcja <body> jest pusta, gotowa na wklejenie zawartości z artykul.html
* podglad.html - plik z pełnym podglądem artykułu, zawierający szablon i wygenerowany kod HTML w jednym pliku

### Instalacja i uruchomienie
* Wymagane posiadanie biblioteki openai (można zainstalować poprzez pip install openai)
* klonowanie repozytorium (w bashu można to zrobić za pomocą komend)
```
git clone https://github.com/olafszyncel/oxidoRecruitment/
cd oxidoRecruitment
```
* należy wpisać swój klucz API OpenAI w pliku api_key.txt (w bashu to można zrobić za pomocą poniższych komend)
```
echo "twój klucz api" > api_key.txt
```
* uruchomienie aplikacji
```
python main.py
```
