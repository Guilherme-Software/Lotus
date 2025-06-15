import pandas as pd

# read the csv.
df = pd.read_csv("vendas_ultimos_12_meses.csv")

# transforming data into manipulable dates
df["Data"] = pd.to_datetime(df["Data"])
df["year"] = df["Data"].dt.year
df["month"] = df["Data"].dt.month

# sales by year and selected months.
def sales_per_month(year, months=None):

    df_year = df[df["year"] == year]
    
    # if any month was selected, return only the selected months.
    if months:
        df_year = df_year[df_year["month"].isin(months)]

    # add up how much was sold each month
    result = df_year.groupby("month")["Valor (R$)"].sum()

    # return the result as a dict
    return result.to_dict()


def sales_per_seller(year):

    df_year = df[df["year"] == year]

    result = df_year.groupby("Vendedor")["Valor (R$)"].sum()

    return result.to_dict()


def best_selling_products(year):

   df_year = df[df["year"] == year]

   result = df_year.groupby("Produto")["Valor (R$)"].count()

   return result.to_dict()
