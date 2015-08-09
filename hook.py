#!/usr/bin/python
import logging
import sys
import json
import datetime

logger = logging.getLogger(__name__)

def main(stdin):
    lines = stdin.split('\n')
    original = json.loads(lines[0])
    modified = json.loads(lines[1])
    timestamp = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    timestamp = unicode(timestamp)

    annotations = modified.get('annotations', [])

    if 'start' in original and 'start' not in modified:
        modified['annotations'] = annotations + [{u'entry': timestamp, u'description': u'taskwarrior.activity.stop'}]
    elif 'start' in modified and 'start' not in original:
        modified['annotations'] = annotations + [{u'entry': timestamp, u'description': u'taskwarrior.activity.start'}]

    return json.dumps(modified, separators=(',', ':'))


def cmdline():
    sys.stdout.write(main(sys.stdin.read()))


if __name__ == '__main__':
    cmdline()
