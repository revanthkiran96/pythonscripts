import boto3
client = boto3.client('ec2')
all_ec2 = client.describe_instances().get('Reservations', [])
instance_types = []
for ec2 in all_ec2:
    for ec in ec2['Instances']:
        instance_types.append(ec['InstanceType'])
user_input = str(input("please enter the instance type:"))
if user_input in instance_types:
    print(f'machine with type {user_input} exist')
else:
    print(f'machine with type {user_input}  not exist')
