import boto3
client = boto3.client('ec2',
 aws_access_key_id='xxxxxxxxxxxxxxx',
aws_secret_access_key='xxxxxxxxxxxxxxxxx',
region_name="ap-northeast-1")
all_instances = client.describe_instances().get(
    'Reservations', 'this is not there')
instance_type = []
for all_ec2 in all_instances:
    for ec2 in all_ec2['Instances']:
        instance_type.append(ec2['InstanceType'])
a_input =str(input("please enter the instancetype: "))
if a_input in instance_type:
    print(f'machine with type {a_input} is exist')
else:
    print(f'machine with type {a_input} is not exist')
