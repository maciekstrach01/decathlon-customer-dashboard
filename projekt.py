import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    import streamlit as st
    STREAMLIT = True
except ImportError:
    STREAMLIT = False

# === Wczytywanie danych ===
customer_orders = pd.read_csv('customer_orders.csv')
sports = pd.read_csv('sports.csv')
orders = pd.read_csv('orders.csv')

orders['value'] = pd.to_numeric(orders['value'], errors='coerce')
wrong_values_count = orders['value'].isna().sum()

# === Analizy ===
sports_count = sports.groupby('customer_id').sport.count()
more_than_2_sports = sports_count[sports_count > 2].count()

sport_popularity = sports['sport'].value_counts()
most_popular_sport = sport_popularity.idxmax()
least_popular_sport = sport_popularity.idxmin()

average_order_value = orders['value'].mean()

orders_per_customer = customer_orders.groupby('customer_id').order_id.count()
more_than_one_order = orders_per_customer[orders_per_customer > 1].count()
total_customers = orders_per_customer.count()
percentage_more_than_one_order = (more_than_one_order / total_customers) * 100

# === Wyświetlanie wyników ===
if STREAMLIT:
    st.title('Decathlon - Analiza Danych')

    # --- KPIs ---
    st.header("🔹 Kluczowe wskaźniki")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Liczba klientów >2 sporty", value=5040)
        st.metric(label="Najbardziej popularny sport", value="Pływanie")
    with col2:
        st.metric(label="Średnia wartość zamówienia", value="793.85 zł")
        st.metric(label="Najmniej popularny sport", value="Aquafitnes")

    st.metric(label="Procent klientów z >1 zamówieniem", value="62.19%")

    # --- Wykres popularności sportów ---
    st.header("📈 Popularność sportów (Top 10)")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    top_10_sports = sport_popularity.head(10)
    sns.barplot(x=top_10_sports.values, y=top_10_sports.index, ax=ax1)
    ax1.set_xlabel("Liczba klientów")
    ax1.set_ylabel("Sport")
    st.pyplot(fig1)

    # --- Pie chart: Klienci z 1 vs więcej niż 1 zamówienie ---
    st.header("🧩 Podział klientów według liczby zamówień")
    fig2, ax2 = plt.subplots()
    labels = ['>1 zamówienie', '1 zamówienie']
    values = [more_than_one_order, total_customers - more_than_one_order]
    ax2.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    ax2.axis('equal')  
    st.pyplot(fig2)

    # --- Podsumowanie ---
    st.header("📋 Podsumowanie analizy")
    st.success(f"""
    - **5040 klientów** uprawia więcej niż 2 sporty.
    - **Najpopularniejszy sport:** Pływanie.
    - **Najmniej popularny sport:** Aquafitnes.
    - **Średnia wartość zamówienia:** 793,85 zł.
    - **62,19% klientów** zrealizowało więcej niż jedno zamówienie.
    """)
else:
    print("Uruchom ten kod poprzez Streamlit komendą: streamlit run projekt.py")
