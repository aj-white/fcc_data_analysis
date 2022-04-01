import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'adult.data.csv')

    df.columns = [x.replace('-', '_') for x in df.columns]

    # data cleaning to reduce memory
    df = (
        df
        .assign(
            workclass=df.workclass.replace('?', 'Unknown').astype('category'),
            education=df.education.astype('category'),
            marital_status=df.marital_status.astype('category'),
            occupation=df.occupation.replace('?', 'Unknown').astype('category'),
            relationship=df.relationship.astype('category'),
            race=df.race.astype('category'),
            sex=df.sex.astype('category'),
            native_country=df.native_country.replace('?', 'Unknown'),
            salary=df.salary.astype('category')
        )
        .astype({'age': 'int8', 'education_num': 'int8', 'capital_loss': 'int16', 'hours_per_week': 'int8'})
    )

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.query('sex == "Male"')['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df['education'].value_counts(normalize=True)['Bachelors'] * 100, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.query('education.isin(["Bachelors", "Masters", "Doctorate"])')
    lower_education = df.query('~education.isin(["Bachelors", "Masters", "Doctorate"])')

    # percentage with salary >50K
    higher_education_rich = round((higher_education.query('salary == ">50K"').shape[0] / higher_education.shape[0]) * 100, 1)
    lower_education_rich = round((lower_education.query('salary == ">50K"').shape[0] / lower_education.shape[0]) * 100, 1)
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours_per_week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.query('hours_per_week == @min_work_hours')

    rich_percentage = round((num_min_workers.query('salary == ">50K"').shape[0] / num_min_workers.shape[0]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    # https://theprogrammingexpert.com/pandas-groupby-size/
    country_earners = (
                    df
                    .groupby(['native_country', 'salary'])
                    .size()
                    .unstack()
                    .assign(total=lambda x: x['<=50K'] + x['>50K'])
                    .assign(rich_pct=lambda x: (x['>50K'] / x['total']) * 100)
                )
    highest_earning_country = country_earners['rich_pct'].idxmax()
    highest_earning_country_percentage = round(country_earners['rich_pct'].max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (
                        df
                        .query(
                            '(native_country == "India") & (salary == ">50K")'
                        )
                        ['occupation']
                        .value_counts()
                        .idxmax()
                    )

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
