###########################################
###   Analyze data to complete graphs   ###
###########################################

import pandas as pd


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


####################
### Analyze Data ###
####################
df = open_csv("./data/COVID_US_cases.csv")

new_confirmed = df["new_confirmed"].tolist()
seven_day_average = [0 for i in range(6)]
for i in range(len(new_confirmed) - 6):
    average = 0
    for j in range(i, i+7):
        average += new_confirmed[j]
    average /= 7
    seven_day_average.append(average)
df["seven_day_average"] = seven_day_average

df.to_csv("./data/data-with-average.csv", index=False)
