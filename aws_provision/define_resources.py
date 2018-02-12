from troposphere import ec2, Ref, Base64, Join
from troposphere.ec2 import SecurityGroup


def generate_template(template=None):

    ingress = {"ToPort": "80", "IpProtocol": "tcp", "CidrIp": "0.0.0.0/0", "FromPort": "80"}
    ingress_two = {"ToPort": "443", "IpProtocol": "tcp", "CidrIp": "0.0.0.0/0", "FromPort": "443"}
    security_groups = template.add_resource(SecurityGroup("TestSC",
                                                          SecurityGroupIngress=[ingress, ingress_two],
                                                          GroupDescription="Test Secutity group"))
    template.add_resource(ec2.Instance("nginxtest",
                                       ImageId="ami-79873901",
                                       InstanceType="t1.micro",
                                       SecurityGroups=[Ref(security_groups)],
                                       UserData=Base64(Join('',[
                                           '#!/bin/bash\n',
                                           'sudo apt-get update \n',
                                           'curl -L https:/bootstrap.saltstack.com -o '
                                            '/tmp/bootstrap_salt.sh\n',
                                            'sh /tmp/bootstrap_salt.sh\n'
                                            'sudo apt-get install -y python-pip\n',
                                            'sudo apt-get install -y\n']))))


    return template.to_json()


def write_template(payload=None):

    with open('dev_template.template', 'w') as dev_template:
        print("Generating template...")
        dev_template.write(payload)




