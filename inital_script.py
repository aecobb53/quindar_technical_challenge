import os
import json
import pandas as pd

data_dir = os.path.join(os.path.dirname(__file__), 'challenge_data')

# station_id   date  hour  num_contacts  total_bytes_received  total_bytes_sent
df = pd.read_csv(os.path.join(data_dir, 'example_station_data.csv'))

station_metrics = {}

# This part was for me to get a feel for the data and understand how to approach this
for index, row in df.iterrows():
    station_id = row['station_id']
    # date = row['date']
    # hour = row['hour']
    num_contacts = row['num_contacts']
    total_bytes_received = row['total_bytes_received']
    total_bytes_sent = row['total_bytes_sent']
    if station_id not in station_metrics:
        station_metrics[station_id] = {
            'contact_count': 0,
            'total_bytes_received': 0,
            'total_bytes_sent': 0
        }
    station_metrics[station_id]['contact_count'] += num_contacts
    station_metrics[station_id]['total_bytes_received'] += total_bytes_received
    station_metrics[station_id]['total_bytes_sent'] += total_bytes_sent

for station_id, metrics in station_metrics.items():
    metrics['average_bytes_received'] = metrics['total_bytes_received'] / metrics['contact_count']
    metrics['average_bytes_sent'] = metrics['total_bytes_sent'] / metrics['contact_count']
    metrics['total_missed_bytes'] = metrics['total_bytes_received'] - metrics['total_bytes_sent']
    metrics['average_missed_bytes'] = metrics['total_missed_bytes'] / metrics['contact_count']


print(json.dumps(station_metrics, indent=4))

# This is to understand what is considered normal vs abnormal
total_missed_bytes_list = [m['total_missed_bytes'] for m in station_metrics.values()]
total_contacts_list = [m['contact_count'] for m in station_metrics.values()]
average_missed_bytes = sum(total_missed_bytes_list) / sum(total_contacts_list)

import statistics
standard_deviation_missed_bytes = statistics.stdev(total_missed_bytes_list)

# With the average and the standard deviation, we can now understand what is a candidate for a closer look
for station_id, metrics in station_metrics.items():
    if metrics['total_missed_bytes'] > average_missed_bytes + 2 * standard_deviation_missed_bytes:
        metrics['healthy'] = False
    else:
        metrics['healthy'] = True

print(json.dumps(station_metrics, indent=4))

# THIS IS CRUDE AND IM NOT HAPPY WITH IT BUT ITS A START AND CAN BE IMPROVED LATER BUT WONT HALT PROGRESS ON THE PROJECT
