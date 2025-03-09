#######################
###   Format Data   ###
#######################

import pandas as pd
from json import loads


########################
### Helper Functions ###
########################
def open_csv(csv):
    """
    parameters:
        csv: string that contains the path to the csv file
                example: "./data/COVID_US_cases.csv"
    """
    return pd.read_csv(csv, encoding="latin-1", low_memory=False)


def divide_population(df, population):
    df["average_value_Scientific and technical journal articles"] /= df["Population"]

    return df

############################
### Clean Population CSV ###
############################
# population = open_csv("./data/population-raw.csv")
# population = population.melt(
#     id_vars=['ï»¿"Country Name"', "Country Code"],
#     var_name="Year",
#     value_name="Population"
# )
# population.dropna(subset=["Population"], inplace=True)
# population.to_csv("./data/population.csv", index=False)


###################
### Format Data ###
###################
"""
Gini
"""
df = open_csv("./data/poverty.csv")
df.dropna(subset=["average_value_Gini index (World Bank estimate)"], inplace=True)

df = df.sort_values(
    by=["Year", "average_value_Gini index (World Bank estimate)", "Country Name"]
)

df = df[
    [
        "Country Name",
        "Country Code",
        "Year",
        "average_value_Gini index (World Bank estimate)",
    ]
]

df.to_csv("./data/gini-data.csv", index=False)


"""
Poverty headcount
"""
df = open_csv("./data/poverty.csv")
df.dropna(
    subset=[
        "average_value_Multidimensional poverty headcount ratio (% of total population)"
    ],
    inplace=True,
)

df = df.sort_values(
    by=[
        "Year",
        "average_value_Multidimensional poverty headcount ratio (% of total population)",
        "Country Name",
    ]
)

df = df[
    [
        "Country Name",
        "Country Code",
        "Year",
        "average_value_Multidimensional poverty headcount ratio (% of total population)",
    ]
]

df.to_csv("./data/poverty-headcount-data.csv", index=False)

"""
Living in slums
"""
df = open_csv("./data/poverty.csv")
df.dropna(
    subset=["average_value_Population living in slums (% of urban population)"],
    inplace=True,
)

df = df.sort_values(
    by=[
        "Year",
        "average_value_Population living in slums (% of urban population)",
        "Country Name",
    ]
)

df = df[
    [
        "Country Name",
        "Country Code",
        "Year",
        "average_value_Population living in slums (% of urban population)",
    ]
]

df.to_csv("./data/living-slums-data.csv", index=False)

"""
Highest 10% income
"""
df = open_csv("./data/poverty.csv")
df.dropna(subset=["average_value_Income share held by highest 10%"], inplace=True)

df = df.sort_values(
    by=["Year", "average_value_Income share held by highest 10%", "Country Name"]
)

df = df[
    [
        "Country Name",
        "Country Code",
        "Year",
        "average_value_Income share held by highest 10%",
    ]
]

df.to_csv("./data/high-10-percent.csv", index=False)

"""
average_value_Poverty gap at $5.50 a day (2011 PPP) (%)
"""
df = open_csv("./data/poverty.csv")
df.dropna(subset=["average_value_Poverty gap at $5.50 a day (2011 PPP) (%)"], inplace=True)

df = df.sort_values(
    by=["Year", "average_value_Poverty gap at $5.50 a day (2011 PPP) (%)", "Country Name"]
)

df = df[
    [
        "Country Name",
        "Country Code",
        "Year",
        "average_value_Poverty gap at $5.50 a day (2011 PPP) (%)",
    ]
]

df.to_csv("./data/gap-550-day.csv", index=False)

# population = open_csv("./data/population.csv")
# result = population.to_json(orient="records")
# parsed = loads(result)

# column = "average_value_Income share held by highest 10%"
# for index, row in df.iterrows():
#     row[column] /= parsed[]
#     print(row)

# print(parsed)




for i in df.columns.tolist():
    print(i, "\n")
