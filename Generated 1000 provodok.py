import pandas as pd
import numpy as np
from datetime import datetime, timedelta
start_date = datetime(2025, 8, 1)
end_date = datetime(2025, 8, 31)

dates = []
current = start_date
while current <= end_date:
    if current.weekday() != 6:  
        dates.append(current.strftime('%Y-%m-%d'))
    current += timedelta(days=1)
np.random.seed(42)  

n = 1000

random_dates = np.random.choice(dates, n)
debit_accounts = np.random.choice([45501, 45502, 45503], n)
credit_accounts = np.random.choice([20201, 20202, 20203], n)
amounts = np.random.randint(100, 501, n)
df = pd.DataFrame({
    'date': random_dates,
    'debit_account': debit_accounts,
    'credit_account': credit_accounts,
    'amount_thousands': amounts
})

df.to_csv('credit_postings_august_2025.csv', index=False)