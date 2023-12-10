import pandas as pd
from sqlalchemy import create_engine

# Baca data dari file CSV
df = pd.read_csv(r"C:\Users\maalg\OneDrive\Documents\Project 3\source\users_w_postal_code.csv", sep=",")

# Tentukan parameter koneksi PostgreSQL
postgres_conn_str = "postgresql://postgres:ipah1251@127.0.0.1:5432/postgres"
engine = create_engine(postgres_conn_str)

# Nama tabel yang akan dibuat di PostgreSQL
table_name = "from_file_table"

# Buat tabel di PostgreSQL
df.head(0).to_sql(table_name, engine, if_exists='replace', index=False)  # Gunakan if_exists='replace' untuk membuat tabel baru

# Insert data ke tabel PostgreSQL
df.to_sql(table_name, engine, if_exists='append', index=False)

print(f"Tabel {table_name} berhasil dibuat dan data berhasil diimpor ke PostgreSQL.")
