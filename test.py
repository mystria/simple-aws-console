import boto3
iam = boto3.resource('iam')
user = iam.User('min0.son')
groups = user.groups
for group in groups.all()
    print(group.name)
