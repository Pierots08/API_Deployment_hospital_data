def convertTime(t):
t = int(t)
return datetime.fromtimestamp(t)
df_final = df_final.dropna(subset=["Last_Update"])
df_final["Province_State"].fillna(value="", inplace=True)
df_final["Last_Update"]= df_final["Last_Update"]/1000
df_final["Last_Update"] =
df_final["Last_Update"].apply(convertTime)
df_total = df_final.groupby("Country_Region",
as_index=False).agg(
{
"Confirmed" : "sum",
"Deaths" : "sum",
"Recovered" : "sum"
}
)
total_confirmed = df_final["Confirmed"].sum()
total_recovered = df_final["Recovered"].sum()
total_deaths = df_final["Deaths"].sum()
df_top10 = df_total.nlargest(10, "Confirmed")
top10_countries_1 = df_top10["Country_Region"].tolist()
top10_confirmed = df_top10["Confirmed"].tolist()
df_top10 = df_total.nlargest(10, "Recovered")
top10_countries_2 = df_top10["Country_Region"].tolist()
top10_recovered = df_top10["Recovered"].tolist()
df_top10 = df_total.nlargest(10, "Deaths")
top10_countries_3 = df_top10["Country_Region"].tolist()
top10_deaths = df_top10["Deaths"].tolist()