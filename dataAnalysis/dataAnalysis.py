import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_path = 'dataAnalysis/data.csv'
data = pd.read_csv(data_path, delimiter=';')

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
    graduation_counts = data.groupby(parent_column)['Target'].value_counts(normalize=True).unstack().fillna(0)
    graduation_rates = graduation_counts.get('Graduate', 0)
    return graduation_rates

# Calculate graduation rates based on mother's and father's education levels
mother_education_graduation_rates = calculate_graduation_rates(data, "Mother's qualification")
father_education_graduation_rates = calculate_graduation_rates(data, "Father's qualification")

# Display the menu
def display_menu():
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
    sorted_data = data[column].value_counts(normalize=True).sort_index()
    ax = sorted_data.plot(kind='bar', alpha=0.7)
    plt.xlabel(column.replace('_', ' ').title())
    plt.ylabel("Proportion")
    plt.title(f"Proportion of {column.replace('_', ' ').title()} to Drop Outs")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    for container in ax.containers:
        ax.bar_label(container, label_type='edge')
    plt.show()

# Plot graduation rates
def plot_graduation_rates(graduation_rates, title, color):
    ax = graduation_rates.plot(kind='bar', color=color, alpha=0.7)
    plt.xlabel("Qualification Level")
    plt.ylabel("Graduation Rate")
    plt.title(title)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    for container in ax.containers:
        ax.bar_label(container, label_type='edge')
    plt.show()

# Sort data based on the menu option
def sort_data(option):
    column_mapping = {
        1: 'Marital status',
        2: 'Application mode',
        3: 'Course',
        4: 'Admission grade',
        5: 'Age at enrollment',
        6: 'Curricular units 1st sem (grade)',
        7: 'Curricular units 2nd sem (grade)',
    }
    column = column_mapping.get(option)
    if column:
        plot_sorted_data(data, column)
    elif option == 8:
        plot_graduation_rates(mother_education_graduation_rates, "Graduation Rates by Mother's Qualification Level", 'blue')
    elif option == 9:
        plot_graduation_rates(father_education_graduation_rates, "Graduation Rates by Father's Qualification Level", 'green')
    else:
        print("Invalid option.")

# Main function to display the menu and handle user input
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-10): "))
            if choice == 10:
                print("Exiting the program.")
                break
            sort_data(choice)
        except ValueError:
            print("Please enter a valid integer between 1 and 10.")

if __name__ == "__main__":
    main()
