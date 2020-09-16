# prometheus-query-csv

## Usage

Provide three arguments to the python script:
1. Prometheus URL
2. $QUERY refers to promql expression, e.g ```process_cpu_seconds_total```
3. $TOKEN refers to login token, e.g ```oc whoami -t```

```
python query_to_csv.py https://prometheus-k8s-openshift-monitoring.apps.cluster-0668.0668.example.opentlc.com $QUERY $TOKEN > output.csv
```
