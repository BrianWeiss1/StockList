import requests
import pandas as pd

from datetime import datetime, timedelta


def get_data(timeFrame="5"):
    api_key = 'your_api_key'
    url = 'https://www.alphavantage.co/query'
    full_data = pd.DataFrame()

    start_date = datetime(2015, 1, 1)
    end_date = datetime(2024, 5, 1)

    current_date = start_date
    while current_date < end_date:
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': 'SPY',
            'interval': f'{timeFrame}min',
            'outputsize': 'full', 
            'datatype': 'json',
            'apikey': api_key,
            'month': datetime.strptime(str(current_date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m')
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()  
            print(data)
            if f'Time Series ({timeFrame}min)' in data:
                time_series = data[f'Time Series ({timeFrame}min)']
                df = pd.DataFrame.from_dict(time_series, orient='index')
                df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
                df.index = pd.to_datetime(df.index)
                full_data = pd.concat([full_data, df])
                current_date += timedelta(days=30)  
            
            else:
                print("Time series data not found in response.")
                input("Did you change your VPN?")
        else:
            print(f"Error: {response.status_code}")

        print(datetime.strptime(str(current_date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m'))

    # Sort the data by date
    full_data = full_data.sort_index()
    full_data.to_csv(f'{timeFrame}min_data_SPY_2019_to_2024.csv')

    print(f"Data saved to {timeFrame}min_data_SPY_2019_to_2024.csv")
    print(full_data)