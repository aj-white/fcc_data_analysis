import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", header=0, names=["date", "page_views"], parse_dates=["date"], index_col="date")

# Clean data
page_views_top_025 = df['page_views'].quantile(0.975)
page_views_bot_025 = df['page_views'].quantile(0.025)
df = df.query('@page_views_bot_025 <= page_views <= @page_views_top_025') 


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(df.index, df['page_views'], color='red')
    ax.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # unstack method from https://scentellegher.github.io/programming/2017/07/15/pandas-groupby-multiple-columns-plot.html
    df_bar.groupby([df_bar.index.year, df_bar.index.month]).mean().unstack().plot(kind='bar', ax=ax)

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    
    # For use as legend labels
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    ax.legend(months, title="Months", loc=0)      

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # order months correctly
    # From Matt Harrison https://www.linkedin.com/posts/panela_this-one-pops-up-quite-a-bit-have-you-ever-activity-6907712476167708673-iDjw?utm_source=linkedin_share&utm_medium=member_desktop_web
    df_box['month'] = df_box['month'].astype('category').cat.reorder_categories(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(figsize=(15, 6), ncols=2)
    plt.tight_layout()
    (
        sns
        .boxplot(
            ax=ax[0],
            x='year',
            y='page_views',
            data=df_box
        )
        .set(
            xlabel="Year",
            ylabel="Page Views",
            title="Year-wise Box Plot (Trend)"
        )
    )

    (
        sns.
        boxplot(
            ax=ax[1],
            x="month",
            y="page_views",
            data=df_box
        )
        .set(
            xlabel="Month",
            ylabel="Page Views",
            title="Month-wise Box Plot (Seasonality)"
        )
    )

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
