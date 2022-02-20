import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
            
class VpcStack(Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "TheVPC", cidr="10.0.0.0/16" )
