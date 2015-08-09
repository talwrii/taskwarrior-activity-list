#!/usr/bin/python

import argparse
import csv
import datetime
import json
import subprocess
import sys

PARSER = argparse.ArgumentParser(description='Display a summary of activities recorded using the taskwarrior"activity list hook')
PARSER.add_argument('--format', help='How to format the output must be csv at present', choices=('csv',))
PARSER.add_argument('filter', nargs='*', type=str)

def pair_intervals(annotations):
    starts = [a for a in annotations if a['description'] == u'taskwarrior.activity.start']
    ends = [a for a in annotations if a['description'] == u'taskwarrior.activity.stop']
    starts.sort(key=lambda x: x['entry'])
    ends.sort(key=lambda x: x['entry'])
    if len(starts) - len(ends) not in (0, 1):
        raise Exception('starts and stops do not match')

    return zip(starts, ends)

def parse_date(string):
    return datetime.datetime.strptime(string, '%Y%m%dT%H%M%SZ')

def main():
    args = PARSER.parse_args()

    if args.format != 'csv':
        raise Exception('Must use --format csv (preparation for backwards compatability)')

    json_lines = subprocess.check_output(['task', 'export'] + args.filter).splitlines()
    writer = csv.writer(sys.stdout)

    writer.writerow(['task', 'start', 'stop', 'duration_seconds'])
    for line in json_lines:
        activity = json.loads(line)
        for pair in pair_intervals(activity.get('annotations', ())):
            start_ann, stop_ann = pair
            start = parse_date(start_ann['entry'])
            stop = parse_date(stop_ann['entry'])

            duration = int((stop - start).total_seconds())

            writer.writerow([activity['description'], start.isoformat(), stop.isoformat(), duration])

if __name__ == '__main__':
	main()
