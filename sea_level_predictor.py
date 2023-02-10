import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("D:\\Dataset\\epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(1880, 2051), name="year")
    ax.plot(years, (result.intercept + result.slope*years))

    # Create second line of best fit
    recent = df[df["Year"] >= 2000]
    result_recent = linregress(recent["Year"], recent["CSIRO Adjusted Sea Level"])

    ax.plot(years[-51:], 
    years[-51:] * result_recent.slope + result_recent.intercept, color="red")

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('images/sea_level_plot.png')
    return plt.gca()