#!/usr/bin/env python3
import os

import aws_cdk as cdk

from vpc.vpc_stack import VpcStack
from application.application_stack import ApplicationStack

app = cdk.App()
vpc_stack=VpcStack(app, "VpcStack" )

# Add tag to all resources in stack
cdk.Tags.of(vpc_stack).add("env", "dev",
    apply_to_launched_instances=True
    )

# application_stack=ApplicationStack(app, "ApplicationStack" )

app.synth()
