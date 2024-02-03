import statsmodels.api as sm
import pandas as pd

data = pd.read_csv(r'C:\Users\francischen\OneDrive - Carleton University\mas thesis\datasets\RawWDI.csv', encoding='iso-8859-1')
value_mapping = {
    "GDP per capita (constant 2015 US$)": "GDP pc",
    "GDP per capita growth (annual %)": "ln_GDPpc",
    "Taxes on income, profits and capital gains (% of revenue)": "tax",
    "Unemployment, total (% of total labor force) (national estimate)": "unemp",
    "Age dependency ratio, old (% of working-age population)": "age_dr",
    "Labor force participation rate, total (% of total population ages 15-64) (modeled ILO estimate)": "labor",
    "GDP deflator (base year varies by country)": "gdp_deflator"
    }
#X = data[['','','','','','','','','','']]

data["Series Name"] = data["Series Name"].map(value_mapping)
data.to_csv("modified_data.csv", index=False)
df = pd.DataFrame(data)

df.head()
