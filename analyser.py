"""Analyse simple sample authentication events for repeated failures."""
import csv
from collections import Counter
from pathlib import Path


def detect_suspicious_ips(path, threshold=3):
    """Return IPs with at least threshold failed logins, sorted by count."""
    if threshold < 1:
        raise ValueError('threshold must be positive')
    failures = Counter()
    with open(path, newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            if row['status'].strip().lower() == 'failed':
                failures[row['ip'].strip()] += 1
    return sorted(((ip, count) for ip, count in failures.items() if count >= threshold), key=lambda item: (-item[1], item[0]))


def main():
    source = Path(__file__).parent / 'sample_data' / 'auth_events.csv'
    results = detect_suspicious_ips(source)
    print('Security log analysis (sample data)')
    if not results:
        print('No IPs reached the failed-login threshold.')
    for ip, count in results:
        print(f'ALERT: {ip} had {count} failed logins')


if __name__ == '__main__':
    main()
