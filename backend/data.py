import pandas as pd

# read the csv.
df = pd.read_csv("vendas_ultimos_12_meses.csv")

# transforming data into manipulable dates (datetime).
def preprocess_data():
    df["Data"] = pd.to_datetime(df["Data"])
    df["year"] = df["Data"].dt.year
    df["month"] = df["Data"].dt.month

    return df

# the date the user was selected
def selected_date(df, years=None, months=None):

    # transform the selected years and months into an array.
    # if it is already an array, do nothing.
    if years is not None and not isinstance(years, list):
        years = [years]

    if months is not None and not isinstance(months, list):
        months = [months]
    
    if months and 13 in months:
        months = list(range(1, 13))


    # makes pandas read all selected years and months.
    if years:
        df = df[df["year"].isin(years)]

    if months:
        df = df[df["month"].isin(months)]

    return df


# sales by year and selected months.
def sales_per_month(years=None, months=None):
    df = preprocess_data()
    df = selected_date(df, years, months)

    # add up how much was sold each month
    result = df.groupby("month")["Valor (R$)"].sum()

    # return the result as a dict for JSON.
    return result.to_dict()


# sales by sellers by year and months.
def sales_per_seller(years=None, months=None):
    df = preprocess_data()
    df = selected_date(df, years, months)

    # add up how much the sellers was sold each month.
    result = df.groupby("Vendedor")["Valor (R$)"].sum()

    # return result as a fict for JSON.
    return result.to_dict()


# products sales by year and months.
def best_selling_products(years=None, months=None):
    df = preprocess_data()
    df = selected_date(df, years, months)

    # count how many times the product was sold.
    result = df.groupby("Produto")["Valor (R$)"].count()

    # return result as a dict for JSON.
    return result.to_dict()
