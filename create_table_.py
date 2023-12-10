import psycopg2

# Tentukan parameter koneksi
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=ipah1251")
cur = conn.cursor()

# Membuat Tsbel
cur.execute("""
            CREATE TABLE IF NOT EXISTS latihan_user(
                id serial primary key
                ,email text
                ,name text
                ,phone text
                ,postal_code text
            )
            """)

conn.commit()