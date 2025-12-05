import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv(r"C:\Users\Muthuvalli\Downloads\customer_shopping_behavior.csv")
print(df.info())

print(df.describe(include='all'))

print(df.isnull().sum())
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))
print(df['Review Rating'])
print(df.isnull().sum())
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
print(df.columns)
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
labels =['young adult','Adult','Middle-aged','Senior']
df['age-group']=pd.qcut(df['age'],q=4,labels = labels)
print(df[['age','age-group']])
frequency_mapping ={
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months' : 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days','frequency_of_purchases']])
print(df[['discount_applied','promo_code_used']].head(10))
print((df['discount_applied'] == df['promo_code_used']).all())
df = df.drop('promo_code_used',axis=1)
print(df.columns)
# MySQL connection details
username = "root"
password = "root123"
host = "localhost"
port = "3306"
database = "customer"

# Create MySQL engine
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Load DataFrame into MySQL
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data loaded into MySQL table '{table_name}' successfully!")

print(df.to_csv('updated_customer_trends.csv',index=False))