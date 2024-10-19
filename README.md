Stock List in stocks.txt
SPY (S&P500) Data from 2015 to 2024 (5 minute data)
SPY (S&P500) Data from 2019 to 2024 (15 minute data)
Data grabber to make this work you either need 
1. A VPN
OR
2. A AlphaVantage Subscription (not free)

Set the start data and end date of the data you want:
```python
start_date = datetime(2015, 1, 1)
end_date = datetime(2024, 5, 1)
```

Change the timeframe to whatever minute interval you want
```python
def get_data(timeFrame="5"):
```

Change the stock symbol if you don't want S&P500 data:
```python
params = {
    ...
    'symbol': 'SPY',
    ...
}
```

When you reach the message (if doing #1):
```
{'Note': 'Thank you for using Alpha Vantage! Our standard API rate limit is 25 requests per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency.'}
Time series data not found in response.
Did you change your VPN?
```
Change your VPN location to a new location and hit enter.

If you are doing #2 you shouldn't have a problem with API requests

Then do that until all data is collected and moved to:
```python
full_data.to_csv(f'{timeFrame}min_data_SPY_2019_to_2024.csv')
```
