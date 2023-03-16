import boto3


def get_regions(regionname):
    ec2 = boto3.client('ec2',
                       aws_access_key_id='xxxxxxxxxxxx4',
                       aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                       region_name=regionname

                       )
    vm = ec2.describe_instances().get('Reservations','thsi is not there')
    print(vm)


get_regions('ap-northeast-1')
print('=============================================================')
get_regions('us-east-1')
