import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# calcualte bmi
bmi = df.weight / (df.height / 100) ** 2
# Add 'overweight' column
df['overweight'] = np.where(bmi > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
normalised_df = (
    df
    .assign(cholesterol=np.where(df.cholesterol > 1, 1, 0))
    .assign(gluc=np.where(df.gluc > 1, 1, 0))
)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(
        normalised_df,
        id_vars=['cardio'],
        value_vars=[
            'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # https://theprogrammingexpert.com/pandas-groupby-size/
    df_cat = (
    df_cat
    .groupby(['cardio', 'variable', 'value'])
    .size()
    .to_frame()
    .rename({0: "total"}, axis="columns")
    # flattens multi-index
    .reset_index()
)

    # Draw the catplot with 'sns.catplot()'
    catplot = sns.catplot(x='variable', y='total', hue="value", data=df_cat, col='cardio', kind='bar')
    fig = catplot.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    # Store quantile values from dataframe before filtering takes place otherwise we will get incorrect results
    height_025_quantile = normalised_df.height.quantile(0.025) # noqa
    height_975_quantile = normalised_df.height.quantile(0.975) # noqa
    weight_025_quantile = normalised_df.weight.quantile(0.025) # noqa
    weight_975_quantile = normalised_df.weight.quantile(0.975) # noqa

    df_heat = (
        normalised_df
        .query('ap_lo <= ap_hi')
        .query('@height_025_quantile <= height <= @height_975_quantile')
        .query('@weight_025_quantile <= weight <= @weight_975_quantile')
    )

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    # from https://www.geeksforgeeks.org/how-to-create-a-triangle-correlation-heatmap-in-seaborn-python/
    mask = np.triu(np.ones_like(corr))


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, mask=mask, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
