import pandas as pd
import statistics


class AggregateMetricsHandler:
    async def aggregate_metrics(self, file):
        df = pd.read_csv(file.file)

        station_metrics = {}

        for index, row in df.iterrows():
            station_id = row['station_id']
            if station_id not in station_metrics:
                station_metrics[station_id] = {
                    'contact_count': 0,
                    'total_bytes_received': 0,
                    'total_bytes_sent': 0
                }
            station_metrics[station_id]['contact_count'] += row['num_contacts']
            station_metrics[station_id]['total_bytes_received'] += row['total_bytes_received']
            station_metrics[station_id]['total_bytes_sent'] += row['total_bytes_sent']

        for station_id, metrics in station_metrics.items():
            metrics['average_bytes_received'] = metrics['total_bytes_received'] / metrics['contact_count']
            metrics['average_bytes_sent'] = metrics['total_bytes_sent'] / metrics['contact_count']
            metrics['total_missed_bytes'] = metrics['total_bytes_received'] - metrics['total_bytes_sent']
            metrics['average_missed_bytes'] = metrics['total_missed_bytes'] / metrics['contact_count']

        total_missed_bytes_list = [m['total_missed_bytes'] for m in station_metrics.values()]
        total_contacts_list = [m['contact_count'] for m in station_metrics.values()]
        average_missed_bytes = sum(total_missed_bytes_list) / len(total_contacts_list)

        standard_deviation_missed_bytes = statistics.stdev(total_missed_bytes_list)

        for station_id, metrics in station_metrics.items():
            metrics['healthy'] = self.assess_healthiness(
                metrics,
                average_missed_bytes,
                standard_deviation_missed_bytes)

        return station_metrics

    def assess_healthiness(self, station_metric: dict, average_missed_bytes: float, standard_deviation_missed_bytes: float):
        # This makes it easier to implement a better solution in the future
        if station_metric['total_missed_bytes'] > average_missed_bytes + standard_deviation_missed_bytes:
            return False
        return True
