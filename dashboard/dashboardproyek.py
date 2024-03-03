import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_bycity_df(df):
    bycity_df = customers_df.groupby(by="customer_city").customer_id.nunique().reset_index()
    bycity_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
    
    return bycity_df

def create_bystate_df(df):
    bystate_df = customers_df.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
    
    return bystate_df

def create_byscore_df(df):
    byscore_df = orderreviews_df.groupby(by="review_score").order_id.nunique().reset_index()
    byscore_df.rename(columns={
    "order_id": "customer_count"
}, inplace=True)
    
    return byscore_df

def create_byproducts_df(df):
    byproducts_df = most_sold_products_df.groupby(by="product_category_name_english").order_item_id.count().reset_index()
    byproducts_df.rename(columns={
    "order_item_id": "customer_count"
}, inplace=True)
    
    return byproducts_df

def create_byproducts_df(df):
    byproducts_df = most_sold_products_df.groupby(by="product_category_name_english").order_item_id.count().reset_index()
    byproducts_df.rename(columns={
    "order_item_id": "customer_count"
}, inplace=True)
    
    return byproducts_df

customers_df = pd.read_csv("C:/Users/Acer/dashboardproyek/customers.csv")
orderreviews_df = pd.read_csv("C:/Users/Acer/dashboardproyek/orderreviews.csv")
most_sold_products_df = pd.read_csv("C:/Users/Acer/dashboardproyek/most_sold_products.csv")

datetime_columns = ["review_creation_date", "review_answer_timestamp"]
orderreviews_df.sort_values(by="review_creation_date", inplace=True)
orderreviews_df.reset_index(inplace=True)
 
for column in datetime_columns:
    orderreviews_df[column] = pd.to_datetime(orderreviews_df[column])

datetime_columns = ["shipping_limit_date"]
most_sold_products_df.sort_values(by="shipping_limit_date", inplace=True)
most_sold_products_df.reset_index(inplace=True)
 
for column in datetime_columns:
    most_sold_products_df[column] = pd.to_datetime(most_sold_products_df[column])

min_date = most_sold_products_df["shipping_limit_date"].min()
max_date = most_sold_products_df["shipping_limit_date"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/annisacahyaning/logoproyek/assets/160316907/5a535613-6b4d-4647-ae70-e8ab4208c50b")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = most_sold_products_df[(most_sold_products_df["shipping_limit_date"] >= str(start_date)) & 
                (most_sold_products_df["shipping_limit_date"] <= str(end_date))]

bycity_df = create_bycity_df(main_df)
bystate_df = create_bystate_df(main_df)
byscore_df = create_byscore_df(main_df)
byproducts_df = create_byproducts_df(main_df)
byproducts_df = create_byproducts_df(main_df)

st.header('Dashboard E-Commerce :sparkles:')

st.subheader("Data 10 Kota dengan Customer Terbanyak")

fig, ax = plt.subplots(figsize=(40, 30))  

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="customer_count",
    y="customer_city",
    data=bycity_df.sort_values(by="customer_count", ascending=False).head(10),
    hue="customer_city",
    palette=colors,
    legend=False
)
ax.set_ylabel("Kota", fontsize=50)
ax.set_xlabel("Jumlah Customer", fontsize=50)
ax.set_title("Data 10 Kota dengan Customer Terbanyak", loc="center", fontsize=60)
ax.tick_params(axis='y', labelsize=50)
ax.tick_params(axis='x', labelsize=50)

st.pyplot(fig)
st.write("Berdasarkan diagram di atas, dapat disimpulkan jumlah customer terbanyak berada pada kota Sao Paulo.")

st.subheader("Data 10 State dengan Customer Terbanyak")

fig, ax = plt.subplots(figsize=(40, 30))  

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="customer_count",
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False).head(10),
    hue="customer_state",
    palette=colors,
    legend=False
)
ax.set_ylabel("State", fontsize=50)
ax.set_xlabel("Jumlah Customer", fontsize=50)
ax.set_title("Data 10 State dengan Customer Terbanyak", loc="center", fontsize=60)
ax.tick_params(axis='y', labelsize=50)
ax.tick_params(axis='x', labelsize=50)

st.pyplot(fig)
st.write("Berdasarkan diagram di atas, dapat disimpulkan jumlah customer terbanyak berada pada state SP.")

st.subheader("Nilai dari Customer")

fig, ax = plt.subplots(figsize=(40, 30))  

colors = ["#90CAF9", "#90CAF9", "#90CAF9","#90CAF9", "#90CAF9"]

sns.barplot(
    y="customer_count",
    x="review_score",
    data=byscore_df.sort_values(by="customer_count", ascending=False),  # Mengurutkan berdasarkan jumlah pelanggan
    hue="review_score",
    palette=colors,
    order=byscore_df.sort_values(by="customer_count", ascending=False)["review_score"],  # Mengurutkan label sumbu x sesuai dengan urutan jumlah pelanggan
    legend=False
)
ax.set_ylabel("Jumlah Customer", fontsize=50)
ax.set_xlabel("Nilai", fontsize=50)
ax.set_title("Nilai dari Customer", loc="center", fontsize=60)
ax.tick_params(axis='y', labelsize=50)
ax.tick_params(axis='x', labelsize=50)

st.pyplot(fig)
st.write("Berdasarkan diagram di atas, customer sangat puas dengan layanan e-commerce karena data terbanyak berada pada nilai 5.")

st.subheader("Data 10 Kategori Produk Paling Banyak Terjual")

fig, ax = plt.subplots(figsize=(40, 30))  

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="customer_count",
    y="product_category_name_english",
    data=byproducts_df.sort_values(by="customer_count", ascending=False).head(10),
    hue="product_category_name_english",
    palette=colors,
    legend=False
)
ax.set_ylabel("Kategori", fontsize=50)
ax.set_xlabel("Jumlah Customer", fontsize=50)
ax.set_title("10 Kategori Produk Paling Banyak Terjual", loc="center", fontsize=60)
ax.tick_params(axis='y', labelsize=50)
ax.tick_params(axis='x', labelsize=50)

st.pyplot(fig)
st.write("Berdasarkan diagram di atas, kategori produk yang paling banyak terjual adalah bed_bath_table")

st.subheader("Data 10 Kategori Produk Paling Sedikit Terjual")

fig, ax = plt.subplots(figsize=(40, 30))  

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="customer_count",
    y="product_category_name_english",
    data=byproducts_df.sort_values(by="customer_count", ascending=True).head(10),
    hue="product_category_name_english",
    palette=colors,
    legend=False
)
ax.set_ylabel("Kategori", fontsize=50)
ax.set_xlabel("Jumlah Customer", fontsize=50)
ax.set_title("10 Kategori Produk Paling Sedikit Terjual", loc="center", fontsize=60)
ax.tick_params(axis='y', labelsize=50)
ax.tick_params(axis='x', labelsize=50)

st.pyplot(fig)
st.write("Berdasarkan diagram di atas, kategori produk yang paling sedikit terjual adalah security_and_services")