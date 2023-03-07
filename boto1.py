import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-09ba48996007c8b50",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="youtube-key"
    
    
    )