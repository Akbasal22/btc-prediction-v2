import pandas as pd

def create_arrays():
    df = pd.read_csv('./processed_data.v')
    print(df.shape)

create_arrays()
