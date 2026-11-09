import requests

def fetch_daily(name,lat,lon):
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast",
                                params={
                                    "latitude":lat,
                                    "longitude":lon,
                                    "daily":["temperature_2m_max","temperature_2m_min"],
                                    "forecast_days":7,
                                    "timezone":"auto"
                                })
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        return []

    

    daily = data["daily"]
    rows=[]
    for i in range(len(daily["time"])):
        rows.append({
            "city":name,
            "date":daily["time"][i],
            "max_temp":daily["temperature_2m_max"][i],
            "min_temp":daily["temperature_2m_min"][i]
        })
    return rows

CITIES = [
    ("Pune",18.52,73.85),
    ("Mumbai",19.08,72.88),
    ("Delhi",28.61,77.21),
    ("Banglore",12.97,77.59),
    ("Chennai",13.08,80.27)
]

def fetch_all():
    all_rows=[]
    for name,lat,lon in CITIES:
        all_rows.extend(fetch_daily(name,lat,lon))
    return all_rows

rows =fetch_all()
print(len(rows))

