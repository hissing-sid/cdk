#!/usr/bin/env python3
import os

import aws_cdk as cdk

from vpc.vpc_stack import VpcStack


app = cdk.App()
VpcStack(app, "VpcStack")

app.synth()
