import analysis

def main():
    co2_df = analysis.load_data()
    
    if co2_df is None:
        return

    while True:
        print("\n" + "="*40)
        print("   🌎 Global CO2 Emissions Explorer 🌎")
        print("="*40)
        print("1. Show Top 10 Total CO2 Emitters")
        print("2. Show Top 10 Per Capita CO2 Emitters")
        print("3. Analyze Emissions for a Specific Country")
        print("4. Compare Emissions Between Two Countries")
        print("5. Show Global Statistics")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            analysis.show_top_emitters(co2_df)
        
        elif choice == '2':
            analysis.show_top_per_capita(co2_df)
        
        elif choice == '3':
            analysis.analyze_country(co2_df)
        
        elif choice == '4':
            analysis.compare_countries(co2_df)
        
        elif choice == '5':
            analysis.show_global_stats(co2_df)
        
        elif choice == '6':
            print("Exiting... Thank you for using the explorer!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

input("\nPress Enter to exit...")
