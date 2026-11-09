import pandas as pd
import matplotlib.pyplot as plt

def avg_max_by_city(conn):
    df = pd.read_sql("""
        SELECT city, ROUND(AVG(max_temp),1) AS avg_max
        FROM readings
        GROUP BY city
        ORDER BY avg_max DESC
        """,conn)
    return (df)

def hot_cities(conn,threshold):
    df = pd.read_sql("""
         SELECT city, ROUND(AVG(max_temp),1) as avg_max
         FROM readings
         GROUP BY city
         HAVING AVG(max_temp) > ?
         ORDER BY avg_max DESC
    """,conn,params=(threshold,))
    return df

def extremes_by_city(conn):
    df = pd.read_sql("""
         SELECT city, ROUND(MAX(max_temp),1) as hottest, ROUND(MIN(min_temp),1) as coldest
         FROM readings
         GROUP BY city  
         ORDER BY city
         """,conn)
    return df

def save_outputs(conn):
    df = avg_max_by_city(conn)
    df.plot(kind="bar",x="city",y="avg_max")
    plt.xlabel("City")
    plt.ylabel("Average Max Tempeature")
    plt.xticks(rotation=45,ha="right")
    plt.legend().remove()
    plt.tight_layout()
    plt.savefig("average_temp.png")
    plt.show()

    df.to_csv("summary.csv",index=False)
    