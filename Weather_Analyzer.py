import pandas as pd

# Load the data
data = pd.read_csv('weather_data.csv')

print("Welcome to the Weather Analyzer!")

# Placeholder for user choice
choice = ""

# Main Menu Loop
while(choice != '4'):
    choice = input("\nEnter '1' to analyze a city, '2' to display however many rows of the data you would like, '3' to display the analysis of the data as a whole, or '4' to exit: \n")
    # Analyze a specific city
    if choice == '1':
        print("Here are the cities in the data: ")
        print(data['Location'].unique())
        end = False
        city = input("\nEnter the city you would like to analyze: ")
        while end == False:
            # Check if the city is in the data
            if city not in data['Location'].unique():
                print(f"City '{city}' not found in the data.")
                print("Here are the cities in the data: ")
                print(data['Location'].unique())
                end = False
                city = input("\nEnter the city you would like to analyze: ")
            else:
                end = True
                # Display the analysis of the city
                temp = input("\nThe data originally has only a temperature column of Celsius.\nWould you like to add a column that tells the temerature in Fahrenheit?\nEnter 'C' for only Celsius or 'F' to add Fahrenheit: ")
                while (temp != 'C' or temp != 'F'):
                    if temp == 'F':
                        # Convert Celsius to Fahrenheit and add a new column
                        data['Temperature_F'] = data['Temperature_C'] * 9/5 + 32
                        print(data[data['Location'] == city].describe())
                        break
                    elif temp == 'C':
                        # Display the analysis of the city with only Celsius
                        print(data[data['Location'] == city].describe())
                        break
                    else:
                        temp = input("\nInvalid input. Please enter 'C' or 'F': ")
    # Display however many rows of the data the user wants
    elif choice == '2':
        num = int(input("Enter the number of rows you would like to display: "))
        while num < 0 or num > len(data) or num == 0:
            if num > len(data):
                    print("\nInvalid input. The number of rows you want to display is greater than the number of rows in the data.")
                    num = int(input("Enter the number of rows you would like to display: "))
            elif num < 0:
                print("\nInvalid input. The number of rows you want to display is less than 0.")
                num = int(input("Enter the number of rows you would like to display: "))
            elif num == 0:
                print("\nInvalid input. The number of rows you want to display is 0.")
                num = int(input("Enter the number of rows you would like to display: "))
        # Display the number of rows the user wants
        print(data.head(n=num))
    # Display analysis of all the data
    elif choice == '3':
        analysis = data.describe()
        print(analysis)
    # Exit the program
    elif choice == '4':
        print("Goodbye!")
    # Handle Invalid input
    else:
        choice = input("\nInvalid input. Please enter '1', '2', '3', or '4'.\n")
