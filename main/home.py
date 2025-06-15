import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas_ultimos_12_meses.csv")

def sales_per_month(year, month):
    df["Data"] = pd.to_datetime(df["Data"])
    df["year"] = df["Data"].dt.year
    df["month"] = df["Data"].dt.month

    df_year = df[df["year"] == year]

    month = df_year.groupby("month").count()

    fig, ax = plt.subplots(figsize=(8,4))

    month.plot(kind="bar", ax=ax, color="blue")

    ax.set_title(f"{year}, Sales per month")
    ax.set_xlabel("Months")
    ax.set_ylabel("Sales")

    plt.show()

