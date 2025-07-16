import pandas as pd

def read_csv(path, prediction_horizon = 30):
    df = pd.read_csv(path, parse_dates=['date'])
    
    df['future_close'] = df['close'].shift(-prediction_horizon)
    df['label'] = (df['future_close']> df['close']).astype(int)

    features = pd.DataFrame()

    features['label'] = df['label']
    features['rsi'] = df['rsi_14'].round(2)
    features['macd'] = df['macd'].round(2)
    features['cci'] = df['cci_14'].round(2)
    features['is_above_sma50'] = (df['close'] > df['sma_50']).astype(int)
    features['is_above_ema50'] = (df['close'] > df['ema_50']).astype(int)
    features['is_above_sma100'] = (df['close'] > df['sma_100']).astype(int)
    features['is_above_ema100'] = (df['close'] > df['ema_100']).astype(int)
    features['volume'] = df['volume'].round(2)
    features['volatility'] = (df['atr_14']/df['close']).round(2)
    features['momentum'] = (df['close']-df['open'])
    features['oversold'] = (df['rsi_14'] < 30).astype(int)
    features['overbought'] = (df['rsi_14']> 70).astype(int)
    features['rsi_macd'] = (df['rsi_14']*df['macd']).round(2)

    window = prediction_horizon * 2 + 1  

    features['close_mean_window'] = df['close'].rolling(window=window, center=True).mean().round(2)
    features['close_std_window'] = df['close'].rolling(window=window, center=True).std().round(2)
    features['rsi_mean_window'] = df['rsi_14'].rolling(window=window, center=True).mean().round(2)
    features['rsi_std_window'] = df['rsi_14'].rolling(window=window, center=True).std().round(2)



    features.dropna(inplace=True)

    features.to_csv("processed_data.csv", index=False)


read_csv('./btc_2015_2024.csv')
 


