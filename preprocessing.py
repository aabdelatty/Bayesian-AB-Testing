# -*- coding: utf-8 -*-
import math
import pandas as pd
def train_test_split(df, time_column, experiment_data_size=.8):
    """
    Given A/B test data, split the data into prior_data and experiment_data
    Input:
        df: dataframe to be splitted 
        time_column: column to be used for splitting. prior_data and experiment_data must be ordered: 
            all the data in prior_data must have been taken place before all the data in experiment_data
        experiment_data_size: portion of experiment data
    Output:
        prior_data: data which will be used to calculate prior probabilities 
        experiment_data: data which will be used to conduct the experiment
    """
    # make sure time column is in date time format
    df[time_column] = pd.to_datetime(df[time_column])

    # split data
    # sort data by time_column, to preserve order before splitting the data
    df_copy = df.sort_values(by=time_column)
    split_point = math.floor(len(df) * (1 - experiment_data_size))
    experiment_data = df_copy[split_point:]
    prior_data = df_copy[:split_point]
    
    return prior_data, experiment_data

def rank_by_cols(df, cols):
    """
    Given A/B experiment data, rank rows by cols (similar to SQL's dense_rank)
    Input:
        df: dataframe to be splitted 
        cols: columns to be used for ranking 
    Output:
        rank column
    """
    return df.sort_values(cols).groupby(cols, sort=False).ngroup() + 1

def drop_users_in_control_and_treatment(df, user_id_col, group_col):
    """
    Given A/B experiment data, drop users that have been assigned to botht groups
    Input:
        df: dataframe to be splitted 
        user_id_col: column used to uniquely identify each user in the experiment
        group_col: column identifing the group each user is assigned to (control/treatment)
    Output:
        filtered df, containing only users assigned to a single group
    """
    # get number of groups each user is assigned to
    groups_count_df = df.groupby(user_id_col)[group_col].nunique().reset_index(name='count')

    # single group users
    single_group_users = groups_count_df[groups_count_df['count'] == 1][[user_id_col]]

    return pd.merge(df, single_group_users)

def rank_ab_data(df, time_column):
    """
    Given A/B test data, rank rows according to time (weeks and days). 
    For example, which actions took place in the nth day/ week since the experiment started
    Input:
        df: dataframe to be splitted 
        time_column: column to be used for splitting. prior_data and experiment_data must be ordered: 
            all the data in prior_data must have been taken place before all the data in experiment_data
    Output:
        add two columns to the dataframe:
            rank_year_week: week number since the experiment started
            rank_year_day: day number since the experiment started
    """
    
    # make sure time column is in date time format
    df[time_column] = pd.to_datetime(df[time_column])

    # extract time components 
    df['year'] = df[time_column].dt.year
    df['week'] = df[time_column].dt.isocalendar().week
    df['day'] = df[time_column].dt.day_of_year

    # rank rows according to time (weeks and days)
    df['weeks_since_experiment_started'] = rank_by_cols(df, ['year', 'week'])
    df['days_since_experiment_started'] = rank_by_cols(df, ['year', 'day'])

    return df
