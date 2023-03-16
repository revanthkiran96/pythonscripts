import boto3


def get_regions(regionname):
    ec2 = boto3.client('ec2',
                       aws_access_key_id='xxxxxxxxxxxxxxxxxx',
                       aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                       region_name=regionname

                       )
    vms = ec2.describe_instances().get('Reservations', 'thsi is not there')
    my_vms = []
    for vm in vms:
        for v in vm['Instances']:
            # print(v['InstanceType'])
            my_vms.append(v['InstanceId'])
    
    
    return my_vms
a =get_regions('ap-northeast-1')
print(a)
# print('=============================================================')
