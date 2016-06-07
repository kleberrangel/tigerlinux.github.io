# OPENSTACK AWS EC2 COMPATIBILITY

**By Reinaldo Martínez P.**

**Caracas, Venezuela:**

**TigerLinux AT gmail DOT com**


## Introduction:

Up to recent OpenStack releases (being kilo the last version oficially supported for EC2), NOVA (the compute component of OpenStack) had very limited EC2 compatibility. On Liberty, this compatibility layer entered in the "deprecation" cycle, and from Mitaka is no longer available from inside Nova.

Lucky us, a group from the OpenStack community decided to re-include EC2 support, and created a "more robust and complete" AWS-EC2 compatibility layer, even with VPC Support:

* [AWS-EC2 OpenStack Project Site at Github.](https://github.com/openstack/ec2-api)

While is not considered part of the OpenStack core modules, it still offer more than old EC2 compatibility on Nova up to Kilo. The EC2 support can be installed in the last 3 more recents OpenStack versions: Kilo, Liberty and Mitaka.

We'll explore in our recipes how to properlly install it on an already-working cloud, and how to use it for EC2 instance creation, both EC2-Classic and EC2-VPC.


## What recipes you'll find here ?:

For the moment, we are including only the recipe for Centos 7. As soon as we finish the translation, the recipe for Ubuntu 14.04lts will be included too.

* [RECIPE: OpenStack AWS-EC2 Compatibility and LAB - Centos 7, in markdown format.](https://github.com/tigerlinux/tigerlinux.github.io/blob/master/recipes/openstack/openstack-aws-ec2-compatibility/RECIPE-aws-ec2-openstack-compat-lab.md "OpenStack AWS-EC2 Compat - Centos 7")
