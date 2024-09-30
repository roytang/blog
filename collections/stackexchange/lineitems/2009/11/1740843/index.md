---
date: 2009-11-16 08:34:23
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1740843/how-to-enforce-a-site-wide-license
tags:
- .net
- licensing
- questions
- stackoverflow
- software development
title: How to enforce a site-wide license?
---

We have a small .Net program that we sell with individual licenses. The individual licenses are enforced by registering a key file that is generated using information from the machine used to install the program (MAC address, etc.)

Now, we have a customer request for a site-wide license, such that they can deploy to as many machines on their site as possible. From the technical POV I'm not sure what are the usual approaches for this; our old approach won't work since we can't map the license to any machine-specific information.

Any suggestions?

A few more details:

  - the program is a client-side program that includes an Office Add-In
  - the machines to be installed on may or may not have internet access
  - we aren't restricted to .Net-only approaches, I'm just looking for a general idea of how this sort of thing is usually handled