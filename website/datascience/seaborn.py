import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Available plotting functions in seaborn
available_plotting_functions = {
    'barplot': sns.barplot,
    'histplot': sns.histplot,
    'catplot': sns.catplot,
    'pairplot': sns.pairplot,
    'boxplot': sns.boxplot,
    'lineplot': sns.lineplot,
    'scatterplot': sns.scatterplot
}

# Function to determine variable type automatically
def determine_variable_type(data, variable_name):
    if pd.api.types.is_numeric_dtype(data[variable_name]):
        return 'numeric'
    else:
        return 'categorical'

# Main function to handle dataset plotting
def plot_dataset(data=None, plot_type=None, plot_title=None, x_var=None, y_var=None, figsize=(10, 6)):
    if data is None:
        print("No dataset provided.")
        return
    if plot_type not in available_plotting_functions:
        print("Invalid plot type.")
        return
    if x_var and determine_variable_type(data, x_var) == 'categorical' and 'scatterplot' in plot_type:
        print("Scatterplot does not support categorical x-variable.")
        return
    if y_var and determine_variable_type(data, y_var) == 'categorical' and 'scatterplot' in plot_type:
        print("Scatterplot does not support categorical y-variable.")
        return

    # Create the plot
    sns.set(style="whitegrid")
    plt.figure(figsize=figsize)
    plotting_function = available_plotting_functions[plot_type]

    if plot_type == 'pairplot':  # For pairplot, call the function directly
        plot = plotting_function(data)
    else:  # For other plots, call the function with x and y variables
        plot = plotting_function(x=x_var, y=y_var, data=data)

    if hasattr(plot, 'set_title') and plot_title:
        plot.set_title(plot_title)
    plt.xlabel(x_var.capitalize() if x_var else '')
    plt.ylabel(y_var.capitalize() if y_var else '')

    # Adjust spacing to prevent collisions between data points or labels
    plt.tight_layout()

    # Show the plot
    plt.show()