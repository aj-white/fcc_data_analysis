import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df = df.rename(columns=lambda x: x.replace(" ", "_").lower())


    # Create scatter plot
    plt.figure(figsize=(15, 10))
    plt.scatter(df.year, df.csiro_adjusted_sea_level, marker="o", c="lightblue", label="Original data")


    # Create first line of best fit
    first_fit = linregress(df.year,df.csiro_adjusted_sea_level)

    # extend x value to 2050 (stop step not inclusive)
    # https://stackoverflow.com/questions/61205263/how-can-i-extend-a-linear-regression-line-and-predict-the-future
    extend_years_to_2050 = np.arange(1880, 2051, 1)
    first_line_best_fit = [first_fit.slope * year + first_fit.intercept for year in extend_years_to_2050]

    # add first line of best fit
    plt.plot(extend_years_to_2050, first_line_best_fit, c="red", label="Fitted line on all data")
     
       
    # Create second line of best fit using data from 2000 onwards only
    df_from_2000 = df.query("year >= 2000")

    # create second line of fit 2000 - 2050
    second_fit = linregress(df_from_2000.year, df_from_2000.csiro_adjusted_sea_level)

    # create new years list for 2000 onwards
    post_2000_years = np.arange(2000, 2051, 1)
    second_line_best_fit = [second_fit.slope * year + second_fit.intercept for year in post_2000_years]

    # add second line of best fit
    plt.plot(post_2000_years, second_line_best_fit, c="blue", label="Fitted line on data from year 2000")
   
    # Add labels and title
    plt.legend()
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
