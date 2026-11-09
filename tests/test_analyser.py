import csv
import tempfile
import unittest
from pathlib import Path
from analyser import detect_suspicious_ips


class AnalyserTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.path = Path(self.directory.name) / 'events.csv'

    def tearDown(self):
        self.directory.cleanup()

    def write_events(self, events):
        with self.path.open('w', newline='', encoding='utf-8') as handle:
            writer = csv.writer(handle)
            writer.writerow(['timestamp', 'ip', 'status'])
            writer.writerows(events)

    def test_repeated_failures_trigger_alert(self):
        self.write_events([['2026-11-01T10:00:00', '192.0.2.1', 'failed']] * 3)
        self.assertEqual(detect_suspicious_ips(self.path), [('192.0.2.1', 3)])

    def test_successes_do_not_count(self):
        self.write_events([['2026-11-01T10:00:00', '192.0.2.1', 'success']] * 5)
        self.assertEqual(detect_suspicious_ips(self.path), [])

    def test_below_threshold_does_not_trigger(self):
        self.write_events([['2026-11-01T10:00:00', '192.0.2.1', 'failed']] * 2)
        self.assertEqual(detect_suspicious_ips(self.path), [])

    def test_invalid_threshold(self):
        with self.assertRaises(ValueError):
            detect_suspicious_ips(self.path, 0)


if __name__ == '__main__':
    unittest.main()
