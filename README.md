# Install and run

```bash
virtualenv --python=python3 ./venv/
source ./venv/bin/activate
pip install -r requirements.txt
python eth.py

```

## Access 
`localhost:5000/ws`

## format
`{'validator': '1', 'duty': 'ATTESTER', 'height': 0}`

### possible duties

`'PROPOSER', 'ATTESTER', 'AGGREGATOR', 'SYNC_COMMITTEE'`