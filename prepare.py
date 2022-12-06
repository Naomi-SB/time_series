import pandas as pd


# function turns date column into datetime object and then sets that as the index
def date_to_dt_index(df, dt_feature):
    '''This function takes in a df with a date column
    and converts date to a datetime object
    then sets that as the index'''
    df[dt_feature] = pd.to_datetime(df[dt_feature])
    df = df.set_index(dt_feature).sort_index()
    return df

def add_time_labels(df):
    '''This function creates columns for name of the month
    and name of the day'''
    df['day_of_the_week']=df.index.day_name()
    df['month']=df.index.month_name()
    return df

def sales_tot(df):
    '''This function adds a column called sales total
    that is the number of items sold times the price of the item'''
    df['sales_total']=df.sale_amount * df.item_price
    return df

def rename(df):
    df=  df.rename(columns={'sale_id' : 'upc_per_store'})
    return df