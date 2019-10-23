---
date: 2008-09-19 03:24:15
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/99271/c-com-office-automation-rpc-e-sys-call-failed
tags:
- c#
- com
- ms-office
- questions
- stackoverflow
- software development
title: C# COM Office Automation - RPC_E_SYS_CALL_FAILED
---

I'm writing a C# program that acts as a PowerPoint 2007 plugin. On some machines, some calls to the PowerPoint object model throw a `COMException` with the message `RPC_E_SYS_CALL_FAILED`. I couldn't find any specific advice on what to do regarding this error, or how to avoid it. From Googling it looks like something to do with the message queue or Single-Threaded Apartments. Or am I way off?

Example of the error message is:
>System call failed. (Exception from HRESULT: 0x80010100 (RPC_E_SYS_CALL_FAILED))  
>at Microsoft.Office.Interop.PowerPoint._Presentation.get_FullName()

Unfortunately, the problem is occurring on a client's machine, so I have no easy way to debug it! Should I just retry the calls whenever I get this error?

Any advice to help me resolve this problem would be greatly appreciated!