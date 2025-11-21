from datetime import datetime
import pandas as pd

pd.set_option("mode.copy_on_write", True)

# df_ari = pd.read_csv('https://idd.bag.admin.ch/api/v1/export/latest/RESPVIRUSES_sentinella/csv', low_memory=False)

# df_ari = df_ari[df_ari['georegion'] == 'CH']
# df_ari = df_ari[df_ari['valueCategory'] == 'detections']

# df_ari_all = df_ari
# # df_ari_all = df_ari_all[df_ari_all['pathogen'] == 'all']
# df_ari_all = df_ari_all.sort_values(by=['temporal'], ascending=True)

# print(df_ari_all.head())

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

def get_wastewater_data(url):
    df = pd.read_csv(url, low_memory=False)

    df['date'] = pd.to_datetime(df['temporal'], format='%Y-%m-%d')

    df = df.sort_values(by='date', ascending=True)
    return df

df_influenza = get_sentinella_data('https://idd.bag.admin.ch/api/v1/export/latest/INFLUENZA_sentinella/csv')

# last 10 years
# df_influenza = df_influenza[df_influenza['date'] >= datetime.now() - pd.DateOffset(years=10)]

df_influenza.set_index('date')[['incValue']].to_csv('data/influenza_cases_ch_newest.csv', index=True)
# df_influenza.set_index('date').to_csv('data/influenza_cases_ch_newest.csv', index=True)

# df_covid_19 = get_sentinella_data('https://idd.bag.admin.ch/api/v1/export/latest/COVID19_sentinella/csv')

# df_covid_19.set_index('date')[['incValue']].to_csv('data/covid_19_cases_ch.csv', index=True)

# df_ww = get_wastewater_data('https://idd.bag.admin.ch/api/v1/export/latest/RESPVIRUSES_wastewater/csv')
# print(df_ww.head())

