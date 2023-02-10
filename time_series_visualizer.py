import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("D:\\Dataset\\fcc-forum-pageviews.csv", index_col="date")

# Clean data
df = df = df[
    (df['value'] >= (df['value'].quantile(0.025))) & 
    (df['value'] <= (df['value'].quantile(0.975)))   
    ]
df.index = pd.to_datetime(df.index)


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots()
    ax.plot(df.index, df.value)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('images/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month
    cbar = df_bar.groupby(
        ['year', 'month'])['value'].agg(['mean']).rename_axis(['year', 'month']).reset_index()
    df_pivtab = pd.pivot_table(cbar, values='mean', index='year', columns='month')
    # Draw bar plot
    ax = df_pivtab.plot(kind='bar')
    fig = ax.get_figure()
    fig.set_size_inches(10,8)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title = 'Months')



    # Save image and return fig (don't change this part)
    fig.savefig('images/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axis = plt.subplots(1,2)
    fig.set_size_inches(12, 6)
    sns.boxplot(x=df_box['year'], y=df_box['value'], ax=axis[0]).set(xlabel='Year', ylabel='Page Views')
    sns.boxplot(x=df_box['month'], y=df_box['value'], ax=axis[1],
        order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']).set(xlabel='Month', ylabel='Page Views')
    axis[0].set_title('Year-wise Box Plot (Trend)')
    axis[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('images/box_plot.png')
    return fig
