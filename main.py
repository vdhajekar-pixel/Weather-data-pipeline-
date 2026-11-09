import sqlite3
from fetch import fetch_all
from database import create_table,save_rows
from analysis import avg_max_by_city,hot_cities,extremes_by_city,save_outputs


def main():
    conn = sqlite3.connect("weather.db")
    print(conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
    print(conn.execute("SELECT * FROM readings LIMIT 5").fetchall())
    print(conn.execute)

    # 1. fetch
    rows = fetch_all()
    print(f"Fetched {len(rows)} rows")

    # 2. store
    create_table(conn)
    save_rows(conn,rows)

    # 3. analyze
    print(avg_max_by_city(conn))
    print(hot_cities(conn,30))
    print(extremes_by_city(conn))

    # 4. chart and save
    save_outputs(conn)

    conn.close()

if __name__ == "__main__":
    main()