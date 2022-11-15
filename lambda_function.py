import pandas as pd


def lambda_handler(event, context):
    d = {'col1':[1,2,3],'col2':[4,5,6]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.5')