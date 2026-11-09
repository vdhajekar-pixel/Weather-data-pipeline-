def create_table(conn):
    conn.execute("""CREATE TABLE IF NOT EXISTS readings(
    city TEXT,
    date TEXT,
    max_temp REAL,
    min_temp REAL,
    UNIQUE (city,date)
    )  
    """)

def save_rows(conn,rows):
    values = [(r["city"],r["date"],r["max_temp"],r["min_temp"]) for r in rows]
    conn.executemany("INSERT OR IGNORE INTO readings VALUES (?,?,?,?)",values)
    conn.commit()
