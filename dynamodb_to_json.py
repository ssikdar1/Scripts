from __future__ import print_function # Python 2/3 compatibility
import boto3
from dynamodb_json import json_util


dynamodb = boto3.client('dynamodb', region_name='us-east-1')


def get_tables_meta():
    tables = dynamodb.list_tables()
    for table in tables['TableNames']:
        print(table)
        table_info = dynamodb.describe_table(TableName=table)['Table']
        pprint.pprint(table_info['AttributeDefinitions'])   
      

print(get_tables_meta()) 

response = dynamodb.scan(TableName='RawFootfall')

# from dynamodb format to normal sane json
dynamodb_json = json_util.loads(response['Items'])

# load into pandas
import pandas
df = pandas.read_json(json.dumps(dynamodb_json) 

# dump to file
import json
with open('footfall.json', 'w') as outfile:
    json.dump(dynamodb_json, outfile)

