import psycopg2

# Tentukan parameter koneksi
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=ipah1251")
cur = conn.cursor()

# Buat tabel 
cur.execute("""
            CREATE TABLE IF NOT EXISTS users_using_copy(
                id serial primary key
                ,email text
                ,name text
                ,phone text
                ,postal_code text
            )
            """)

# Buka file CSV
with open("C:\\Users\\maalg\\OneDrive\\Documents\\Project 3\\source\\users_w_postal_code.csv", "r") as f:
    # Lewati baris header
    next(f)
    # Gunakan fungsi copy_from untuk mengimpor data ke tabel
    cur.copy_from(f, "users_using_copy", sep=",", columns=("email", "name", "phone", "postal_code"))

# Commit perubahan ke database
conn.commit()