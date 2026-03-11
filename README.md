# 🎬 AI Movie Catalog & Tracker

> Nowoczesna aplikacja webowa do przeglądania bazy filmów, zarządzania prywatną listą "do obejrzenia", oceniania tytułów oraz otrzymywania spersonalizowanych rekomendacji od asystenta AI.

## Opis projektu
Projekt realizowany w ramach przedmiotu **Indywidualny Projekt Programistyczny**. Aplikacja łączy programowanie obiektowe (OOP) w języku Python, analizę danych oraz nowoczesny web development. Dane o filmach są wczytywane z publicznych zbiorów (Kaggle), przetwarzane przy użyciu biblioteki Pandas, a lokalny model sztucznej inteligencji pełni rolę osobistego doradcy filmowego.

## Planowane funkcjonalności
* **Katalog filmów:** Przeglądanie bazy z zaawansowanym filtrowaniem (gatunek, rok wydania, średnia ocen).
* **Szczegóły produkcji:** Wyświetlanie kompleksowych informacji: tytuł, reżyser, opis fabuły oraz plakat.
* **Lista "Do obejrzenia":** Zarządzanie prywatną listą filmów dla zalogowanego użytkownika.
* **System oceniania:** Możliwość oceniania obejrzanych filmów w skali od 1 do 5.
* **Asystent AI (Ollama):** Czat z lokalnym modelem językowym, generującym rekomendacje i odpowiadającym na pytania ze świata kina.
* **Panel statystyczny:** Wizualizacja nawyków użytkownika i trendów (np. ulubione gatunki) za pomocą interaktywnych wykresów.

## Stos technologiczny

**Backend (Logika i Przetwarzanie Danych):**
* **Python** (podejście obiektowe) – główna logika biznesowa
* **Pandas** – wczytywanie, czyszczenie i operacje na danych z plików CSV (Kaggle)
* **Flask / FastAPI** – udostępnianie danych poprzez REST API
* **Ollama** – lokalny model AI odpowiedzialny za system rekomendacji

**Frontend (Interfejs Użytkownika):**
* **React** – budowa dynamicznego interfejsu aplikacji (SPA)
* **Recharts** – renderowanie nowoczesnych wykresów w panelu statystycznym

**Przechowywanie Danych (Faza Prototypu / MVP):**
* **Pliki JSON** – zapis profili użytkowników, ich list oraz ocen (zaimplementowane z użyciem Wzorca Repozytorium dla zachowania czystości architektury obiektowej).

## 📅 Harmonogram prac (Kamienie milowe)

Realizacja projektu została podzielona na etapy (raporty), z których każdy dostarcza konkretne, działające funkcjonalności:

### Raport 1: Fundamenty i Przetwarzanie Danych
* Wybór, pobranie i analiza zbioru danych o filmach z platformy Kaggle.
* Stworzenie logiki wczytywania i filtrowania danych przy użyciu biblioteki **Pandas**.
* Konfiguracja środowiska backendowego (Flask/FastAPI).
* Implementacja Wzorca Repozytorium dla plików JSON (baza użytkowników i ich list).

### Raport 2: Podstawowe API i Interfejs Użytkownika (Frontend)
* Inicjalizacja projektu frontentowego w **React**.
* Stworzenie endpointów REST API do pobierania katalogu filmów i filtrowania wyników.
* Zbudowanie widoku głównego (katalog z kartami filmów) oraz widoku szczegółów.
* Połączenie frontendu z backendem.

### Raport 3: Funkcje Użytkownika i Integracja AI
* Logika dodawania filmów do prywatnej listy "do obejrzenia" i zapisywanie ich w JSON.
* Implementacja systemu wystawiania ocen (1-5).
* Konfiguracja lokalnego środowiska **Ollama** i dobór modelu (np. Llama 3 / Mistral).
* Integracja backendu z AI w celu generowania spersonalizowanych rekomendacji na podstawie ocenionych filmów.

### Raport 4 (Finał): Analityka, Szlify i Prezentacja
* Zbudowanie panelu statystycznego użytkownika z użyciem biblioteki **Recharts** (wykresy ulubionych gatunków, rozkład ocen).
* Obsługa błędów, testowanie i optymalizacja zapytań do Pandas.
* Finalne stylowanie interfejsu (CSS/Tailwind).
* Oddanie i obrona gotowego projektu.
---
*Projekt zrealizowany w ramach przedmiotu: Indywidualny Projekt Programistyczny.*
