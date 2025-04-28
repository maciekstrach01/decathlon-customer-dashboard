
## Podgląd dashboardu

Dashboard dostępny jest pod adresem:  
👉 [Kliknij tutaj, aby zobaczyć aplikację](https://TUTAJ-TWÓJ-LINK.streamlit.app/)
## Opis projektu

Celem projektu było:
- Analiza danych klientów Decathlon,
- Wyciągnięcie kluczowych wniosków z danych,
- Przygotowanie interaktywnego dashboardu prezentującego wyniki.

Aplikacja została zbudowana w technologii **Python + Streamlit** i umożliwia wizualizację profilu klienta na podstawie danych o zamówieniach i uprawianych sportach.
## Widok z aplikacji

![Image](https://github.com/user-attachments/assets/320438b7-c756-4850-8e16-5cfcb695a79c)

![Image](https://github.com/user-attachments/assets/488be333-7816-401d-8f30-ec02af618b7d)

![Image](https://github.com/user-attachments/assets/9e124a89-adba-482f-bb64-8b52d7029c23)

![Image](https://github.com/user-attachments/assets/4672e2a6-19a6-4f54-a809-b46fbd859176)
## Zrealizowane zadania

- **Ilu klientów uprawia więcej niż 2 sporty** – liczba klientów aktywnych w wielu dyscyplinach.
- **Najbardziej i najmniej popularny sport** – analiza popularności poszczególnych sportów.
- **Średnia wartość zamówienia** – średnia wartość zakupów klientów.
- **Odsetek klientów z więcej niż jednym zamówieniem** – analiza lojalności zakupowej klientów.
- **Przygotowanie dashboardu** – prezentacja wyników analizy w formie graficznej i liczbowej.
## Użyte technologie

- Python 3.11
- Streamlit
- Pandas
- Matplotlib
- Seaborn
## Struktura projektu

Pliki użyte w projekcie:
- `projekt.py` – główny plik aplikacji Streamlit,
- `customer_orders.csv` – zamówienia klientów,
- `orders.csv` – wartość i liczba produktów w zamówieniu,
- `sports.csv` – sporty uprawiane przez klientów.
## Uruchomienie aplikacji 

1. Zainstaluj wymagane biblioteki:
   ```bash
   pip install streamlit pandas matplotlib seaborn

2. Uruchomienie aplikacji
    ```bash
    streamlit run projekt.py
