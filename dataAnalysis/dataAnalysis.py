import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_path = 'dataAnalysis/data.csv'  # Path to the dataset
data = pd.read_csv(data_path, delimiter=';')  # Read the CSV file with semicolon delimiter

# Define a function to calculate graduation rates
def calculate_graduation_rates(data, parent_column):
    """
    Calculate normalized graduation rates based on the specified parent's qualification column.
    
    Args:
        data (pd.DataFrame): The dataset.
        parent_column (str): The column indicating parent's qualification.
    
    Returns:
        pd.Series: Graduation rates.
    """
    # Group data by parent's qualification and target (graduation status), normalize counts
    graduation_counts = data.groupby(parent_column)['Target'].value_counts(normalize=True).unstack().fillna(0)
    # Extract graduation rates for the 'Graduate' category
    graduation_rates = graduation_counts.get('Graduate', 0)
    return graduation_rates

# Calculate graduation rates based on mother's and father's education levels
mother_education_graduation_rates = calculate_graduation_rates(data, "Mother's qualification")
father_education_graduation_rates = calculate_graduation_rates(data, "Father's qualification")

# Display the menu
def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\nMenu:")
    print("1. Plot Marital status")
    print("2. Plot Application mode")
    print("3. Plot Course")
    print("4. Plot Admission grade")
    print("5. Plot Age at enrollment")
    print("6. Plot Curricular units 1st sem (grade)")
    print("7. Plot Curricular units 2nd sem (grade)")
    print("8. Plot Graduation Rates by Mother's Qualification Level")
    print("9. Plot Graduation Rates by Father's Qualification Level")
    print("10. Exit")

# Plot sorted data for a given column
def plot_sorted_data(data, column):
    """
    Plot the sorted data for a specified column.
    
    Args:
        data (pd.DataFrame): The dataset.
        column (str): The column to be plotted.
    """
    # Count the occurrences of each value in the column, normalize to get proportions, and sort by index
    sorted_data = data[column].value_counts(normalize=True).sort_index()
    # Create a bar plot of the sorted data
    ax = sorted_data.plot(kind='bar', alpha=0.7)
    # Set the x-axis label, y-axis label, and title of the plot
    plt.xlabel(column.replace('_', ' ').title())
    plt.ylabel("Proportion")
    plt.title(f"Proportion of {column.replace('_', ' ').title()}")
    # Add grid lines to the y-axis
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    # Add data labels to the bars
    for container in ax.containers:
        ax.bar_label(container, label_type='edge')
    # Display the plot
    plt.show()

# Plot graduation rates
def plot_graduation_rates(graduation_rates, title, color):
    """
    Plot the graduation rates.
    
    Args:
        graduation_rates (pd.Series): The graduation rates to be plotted.
        title (str): The title of the plot.
        color (str): The color of the bars.
    """
    # Create a bar plot of the graduation rates
    ax = graduation_rates.plot(kind='bar', color=color, alpha=0.7)
    # Set the x-axis label, y-axis label, and title of the plot
    plt.xlabel("Qualification Level")
    plt.ylabel("Graduation Rate")
    plt.title(title)
    # Add grid lines to the y-axis
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    # Add data labels to the bars
    for container in ax.containers:
        ax.bar_label(container, label_type='edge')
    # Display the plot
    plt.show()

# Sort data based on the menu option
def sort_data(option):
    """
    Sort and plot data based on the user's menu choice.
    
    Args:
        option (int): The menu option selected by the user.
    """
    # Mapping of menu options to dataset columns
    column_mapping = {
        1: 'Marital status',
        2: 'Application mode',
        3: 'Course',
        4: 'Admission grade',
        5: 'Age at enrollment',
        6: 'Curricular units 1st sem (grade)',
        7: 'Curricular units 2nd sem (grade)',
    }
    # Get the corresponding column for the chosen option
    column = column_mapping.get(option)
    if column:
        # Plot the data for the chosen column
        plot_sorted_data(data, column)
    elif option == 8:
        # Plot graduation rates by mother's qualification level
        plot_graduation_rates(mother_education_graduation_rates, "Graduation Rates by Mother's Qualification Level", 'blue')
    elif option == 9:
        # Plot graduation rates by father's qualification level
        plot_graduation_rates(father_education_graduation_rates, "Graduation Rates by Father's Qualification Level", 'green')
    else:
        print("Invalid option.")  # Handle invalid options

# Main function to display the menu and handle user input
def main():
    """
    Main function to display the menu and process user input.
    """
    while True:
        display_menu()  # Display the menu options
        try:
            choice = int(input("Enter your choice (1-10): "))  # Get user input
            if choice == 10:
                print("Exiting the program.")  # Exit the program if choice is 10
                break
            sort_data(choice)  # Sort and plot data based on the user's choice
        except ValueError:
            print("Please enter a valid integer between 1 and 10.")  # Handle invalid input

if __name__ == "__main__":
    main()  # Run the main function
