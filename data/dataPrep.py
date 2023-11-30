import pandas as pd
from datetime import datetime

# Load the data
data = pd.read_csv("C:\\Users\\nouro\\Desktop\\Workload-prediction\\data\\anon_jobs.csv")

# Select important features
feature_to_keep = ["SubmitTime", "NProc"]
data = data[feature_to_keep]

# Convert the SubmitTime column to datetime
def conv_date(row):
    dt_object = datetime.utcfromtimestamp(row["SubmitTime"])
    date_string = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    return date_string

data["date"] = data.apply(conv_date, axis=1)

# Aggregate the data by 15 min intervals
data['date'] = pd.to_datetime(data['date'])
# Set 'date' as the index
data.set_index('date', inplace=True)
# Resample the data in 15-minute intervals and sum the 'NProc' values
data_new = data.resample('15T').sum()
data_new = data_new.drop(columns=['SubmitTime'])


# Save the data
data_new.to_csv('C:\\Users\\nouro\\Desktop\\Workload-prediction\\data\\anon_jobs_new.csv')