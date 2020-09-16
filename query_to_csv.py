import csv
import requests
import sys

TOKEN = sys.argv[3]

if len(sys.argv) != 4:
    print('Usage: {0} http://prometheus:9090 $query $TOKEN')
    sys.exit(1)

response = requests.get('{0}/api/v1/query'.format(sys.argv[1]),
        headers={'Authorization': 'Bearer ' + TOKEN},
        params={'query': sys.argv[2]})
results = response.json()['data']['result']

# Build a list of all labelnames used.
labelnames = set()
for result in results:
      labelnames.update(result['metric'].keys())

# Canonicalize
labelnames.discard('__name__')
labelnames = sorted(labelnames)

writer = csv.writer(sys.stdout)
# Write the header,
writer.writerow(['name', 'timestamp', 'value'] + labelnames)

# Write the samples.
for result in results:
    l = [result['metric'].get('__name__', '')] + result['value']
    for label in labelnames:
        l.append(result['metric'].get(label, ''))
    writer.writerow(l)
