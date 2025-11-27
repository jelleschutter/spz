from datetime import datetime
import pandas as pd

pd.set_option("mode.copy_on_write", True)

def get_sentinella_data(url):
    df = pd.read_csv(url, low_memory=False)
    df = df[df['georegion'] == 'CH']
    df = df[df['agegroup'] == 'all']
    df = df[df['sex'] == 'all']
    df = df[df['valueCategory'] == 'consultations']

    df['date'] = pd.to_datetime(df['temporal'] + '-3', format='%G-W%V-%w')

    df = df.drop(columns=['georegion', 'georegion_type', 'agegroup', 'sex', 'agegroup_type', 'temporal_type', 'temporal'])
    df = df.sort_values(by='date', ascending=True)
    return df


df_influenza = get_sentinella_data('https://idd.bag.admin.ch/api/v1/export/latest/INFLUENZA_sentinella/csv')

df_influenza.set_index('date')[['incValue']].to_csv('data/influenza_cases_ch_newest.csv', index=True)