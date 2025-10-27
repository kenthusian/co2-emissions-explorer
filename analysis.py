import pandas as pd
import numpy as np

def load_data(file_path="owid-co2-data.csv"):
    try:
        df = pd.read_csv(file_path)
        df.fillna(0, inplace=True)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please download 'owid-co2-data.csv' from Kaggle and put it in the same folder.")
        return None

def get_latest_year_df(df):
    latest_year = df['year'].max() # -> Changed from 'Year'
    
    non_country_list = [
        'World', 'Asia', 'Africa', 'Europe', 'North America', 
        'South America', 'Oceania', 'EU-27', 'International transport'
    ]
    
    latest_df = df[
        (df['year'] == latest_year) &  # -> Changed from 'Year'
        (~df['country'].isin(non_country_list)) # -> Changed from 'Country'
    ]
    return latest_df, latest_year

def show_top_emitters(df):
    latest_df, year = get_latest_year_df(df)
    
    top_10 = latest_df.sort_values(by='co2', ascending=False).head(10)
    
    print(f"\n--- Top 10 Total CO2 Emitters ({year}) ---")
    print(top_10[['country', 'co2']].to_string(index=False)) # -> Changed from 'Country'

def show_top_per_capita(df):
    latest_df, year = get_latest_year_df(df)
    
    top_10 = latest_df.sort_values(by='co2_per_capita', ascending=False).head(10)
    
    print(f"\n--- Top 10 Per Capita CO2 Emitters ({year}) ---")
    print(top_10[['country', 'co2_per_capita']].to_string(index=False)) # -> Changed from 'Country'

def analyze_country(df):
    country = input("Enter the Country name (e.g., 'India'): ").strip().title()
    
    country_df = df[df['country'] == country] # -> Changed from 'Country'
    
    if country_df.empty:
        print(f"No data found for: {country}")
    else:
        print(f"\n--- Emissions Trend for {country} (every 5 years) ---")
        print(country_df[country_df['year'] % 5 == 0][['year', 'co2', 'co2_per_capita']].to_string(index=False)) # -> Changed from 'Year'

def compare_countries(df):
    country1 = input("Enter first country: ").strip().title()
    country2 = input("Enter second country: ").strip().title()
    
    latest_df, year = get_latest_year_df(df)
    
    compare_df = latest_df[latest_df['country'].isin([country1, country2])] # -> Changed from 'Country'
    
    if compare_df.empty:
        print(f"One or both countries not found in {year} data.")
    else:
        print(f"\n--- Comparison for {year} ---")
        print(compare_df[['country', 'co2', 'co2_per_capita']].to_string(index=False)) # -> Changed from 'Country'

def show_global_stats(df):
    latest_year = df['year'].max() # -> Changed from 'Year'
    world_data = df[(df['year'] == latest_year) & (df['country'] == 'World')] # -> Changed from 'Year' and 'Country'
    
    if world_data.empty:
        print("Could not find 'World' data for global stats.")
        return
        
    world_stats = world_data.iloc[0]

    latest_countries_df, _ = get_latest_year_df(df)
    
    valid_emitters = latest_countries_df[latest_countries_df['co2'] > 0]
    
    avg_emission = np.mean(valid_emitters['co2'])
    median_emission = np.median(valid_emitters['co2'])
    
    print(f"\n--- Global Stats for {latest_year} ---")
    print(f"Total Global CO2 Emissions: {world_stats['co2']:.2f} (million tonnes)")
    print(f"Average Global CO2 Per Capita: {world_stats['co2_per_capita']:.2f} (tonnes per person)")
    print(f"--- Per-Country Stats ---")
    print(f"Average Emission per Country: {avg_emission:.2f} (million tonnes)")
    print(f"Median Emission per Country: {median_emission:.2f} (million tonnes)")