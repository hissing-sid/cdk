import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
            
class VpcStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self, "TheVPC", 
            cidr="10.0.0.0/16",
            enable_dns_hostnames=True,
            enable_dns_support=True
        )

        security_group = ec2.SecurityGroup(
            self, "CDKSecurityGroup",
            vpc=vpc,
            allow_all_outbound=None,
            description= "Allow SSM Access to instances",
            security_group_name= "CDKSecurityGroup"
        )

        security_group.add_ingress_rule(security_group, ec2.Port.tcp(22) )