# Name: Adam Klingler
# Section: AB
# Description: This file contains various data manipulations, including pandas
#   dataframe manipulation, datavisualization with seaborn and matplotlib, and
#   machine learning algorithm via sklearn and a decision tree regressor model,
#   then runs all those programs in a main function.

# Imports here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Functions here
# Part 0


def completions_between_years(df, begin, end, sex):
    '''
    Takes in a pandas dataframe, an inclusive beginning year, an exclusive
    ending year, and a sex, and returns a new dataframe for all data
    between those years. If no data exists for these year boundaries and
    sex combination, returns None.
    '''
    is_beginning_atleast = df['Year'] >= begin
    is_end_atmost = df['Year'] < end
    is_sex = df['Sex'] == sex

    result = df[is_beginning_atleast & is_end_atmost & is_sex]

    if len(result) == 0:
        # Empty dataframe
        return None
    else:
        return result


def compare_bachelors_1980(df):
    '''
    Takes in a pandas dataframe, and returning a pandas dataframe that
    is a breakdown by sex of how many earned a bachelors in 1980.
    '''
    is_year = df['Year'] == 1980
    is_bachelor = df['Min degree'] == 'bachelor\'s'
    is_seperated_sex = (df['Sex'] == 'M') | (df['Sex'] == 'F')

    filtered_df = df[is_year & is_bachelor & is_seperated_sex]

    result = filtered_df.loc[:, ['Sex', 'Total']]

    return result


def top_2_2000s(df):
    '''
    Takes in a pandas dataframe, and returns a pandas series with the
    indices being a min degree and the values being the two highest
    mean percents for graduates of the 2000's
    '''
    is_2000s = (df['Year'] >= 2000) & (df['Year'] <= 2010)

    filtered_df = df[is_2000s]

    percents = filtered_df.groupby('Min degree')['Total'].mean()

    return percents.nlargest(2)


def percent_change_bachelors_2000s(df, sex='A'):
    '''
    Takes in a pandas dataframe and an optional sex string and returns a
    float that is the percent difference in bachelor's degrees received
    in 2000 versus 2010.
    '''
    is_sex = df['Sex'] == sex
    is_bachelors = df['Min degree'] == 'bachelor\'s'
    is_ends_of_years = (df['Year'] == 2000) | (df['Year'] == 2010)

    filtered_df = df[is_sex & is_bachelors & is_ends_of_years]
    totals = list(filtered_df['Total'])

    return totals[1] - totals[0]
# Part 1


def line_plot_bachelors(df):
    '''
    Takes in a pandas dataframe, and creates a line plot of the perecentage
    of people with a bachelor's degree. The plot is saved as
    "line_plot_bachelors.png"
    '''
    is_all_sexs = df['Sex'] == 'A'
    is_bachelors = df['Min degree'] == 'bachelor\'s'

    filtered_df = df[is_all_sexs & is_bachelors]
    graph_data = filtered_df.loc[:, ['Year', 'Total']]

    sns.relplot(x='Year', y='Total', data=graph_data, kind='line')
    plt.title('Percentage Earning Bachelor\'s over Time')
    plt.xlabel('Year')
    plt.ylabel('Percentage')

    plt.savefig('line_plot_bachelors.png')


def bar_chart_high_school(df):
    '''
    Takes in a pandas dataframe, and creates a bar chart that is the percentage
    of people who recieved a high school degree in the year 2009. The plot is
    saved as "bar_chart_high_school.png"
    '''
    is_2009 = df['Year'] == 2009
    is_hs = df['Min degree'] == 'high school'

    filtered_df = df[is_2009 & is_hs]

    sns.catplot(x='Sex', y='Total', data=filtered_df, kind='bar')
    plt.title('Percentage Completed High School by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.savefig('bar_chart_high_school.png')


def plot_hispanic_min_degree(df):
    '''
    Takes in a pandas dataframe, and creates a line plot that shows the trend
    in Hispanic people with degrees for high school and bachelor's degrees
    from 1990 to 2010 inclusive. The plot is saved as
    "plot_hispanic_min_degree.png"
    '''
    is_within_time = (df['Year'] >= 1990) & (df['Year'] <= 2010)
    is_correct_degrees = (df['Min degree'] == 'high school') | \
                         (df['Min degree'] == 'bachelor\'s')

    filtered_df = df[is_within_time & is_correct_degrees]

    sns.relplot(x='Year', y='Hispanic', hue='Min degree',
                data=filtered_df, kind='line')

    plt.title('Percentage of Hispanic people with degrees from 1990 to 2010')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.savefig('plot_hispanic_min_degree.png')
# part 2


def fit_and_predict_degrees(df):
    '''
    Takes in a pandas dataframe, and returns the test mean squared error of
    the randomized test set. The model that is developed is a decision tree
    regressor that takes in year, degree type, and sex to predict the percent
    of people of individuals of the specified sex to achieve that degree type
    in the specified year.
    '''
    filtered_df = df.loc[:, ['Year', 'Min degree', 'Sex', 'Total']]

    model_data = filtered_df.dropna()

    X = model_data.loc[:, ['Year', 'Min degree', 'Sex']]
    X = pd.get_dummies(X)
    y = model_data.loc[:, 'Total']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)

    y_test_pred = model.predict(X_test)
    err = mean_squared_error(y_test, y_test_pred)

    return err


def main():
    '''
    '''
    df = pd.read_csv('hw3-nces-ed-attainment.csv', na_values='---')

    # Part 0
    completions_between_years(df, 2007, 2008, 'F')
    compare_bachelors_1980(df)
    top_2_2000s(df)
    percent_change_bachelors_2000s(df)

    # Part 1
    sns.set()

    line_plot_bachelors(df)
    bar_chart_high_school(df)
    plot_hispanic_min_degree(df)

    # Part 2
    fit_and_predict_degrees(df)


if __name__ == '__main__':
    main()
