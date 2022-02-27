import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
            
class VpcStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self, "TheVPC", 
            cidr="10.0.0.0/16",
            max_azs=2,
            enable_dns_hostnames=True,
            enable_dns_support=True
        )

        # Send Flow Logs containing REJECTS to CloudWatch Logs
        vpc.add_flow_log("FlowLogCloudWatch",
            traffic_type=ec2.FlowLogTrafficType.REJECT
        )

        security_group = ec2.SecurityGroup(
            self, "CDKSecurityGroup",
            vpc=vpc,
            allow_all_outbound=False,
            description= "Allow SSM Access to instances",
            security_group_name= "CDKSecurityGroup"
        )

        security_group.add_ingress_rule(security_group, ec2.Port.tcp(443) )
        security_group.add_egress_rule(security_group, ec2.Port.tcp(443) )

        # Create vpc interface endpoints for SSM, only assigned to the private subnets
        ssm_endpoint = ec2.InterfaceVpcEndpoint(self, "SSM Endpoint",
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointService("com.amazonaws.eu-west-2.ssm", 443),
            subnets=ec2.SubnetType.PRIVATE_WITH_NAT,
            security_groups=[security_group]
        )

        ssm_messages_endpoint = ec2.InterfaceVpcEndpoint(self, "SSM Messages Endpoint",
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointService("com.amazonaws.eu-west-2.ssmmessages", 443),
            subnets=ec2.SubnetType.PRIVATE_WITH_NAT,
            security_groups=[security_group]
        )