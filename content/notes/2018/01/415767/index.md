---
date: 2018-01-09 09:23:53
source: stackexchange
syndicated:
- type: stackexchange
  url: https://unix.stackexchange.com/questions/415767/centos-amazon-ec2-instance-wont-boot-after-upgrading-to-centos-6-9-via-yum
tags:
- centos
- amazon-ec2
- aws
- questions
- unix
- tech life
title: CentOS Amazon EC2 instance won't boot after upgrading to CentOS 6.9 via yum
---

A client updated their EC2 CentOS 6.4 instance to 6.9 using yum update. After the update and a reboot, the instance wouldn't start up anymore (became unreachable)

The system log (recovered from the AWS console) goes something like this:

    Xen Minimal OS!
    
      start_info: 0x10d3000(VA)
    
        nr_pages: 0xe4f53
    
      shared_inf: 0xeea31000(MA)
    
         pt_base: 0x10d6000(VA)
    
    nr_pt_frames: 0xd
    
        mfn_list: 0x9ab000(VA)
    
       mod_start: 0x0(VA)
    
         mod_len: 0
    
           flags: 0x300
    
        cmd_line: root=/dev/sda1 ro console=hvc0 4
    
      stack:      0x96a100-0x98a100
    
    MM: Init
    
          _text: 0x0(VA)
    
         _etext: 0x7b824(VA)
    
       _erodata: 0x97000(VA)
    
         _edata: 0x9cce0(VA)
    
    stack start: 0x96a100(VA)
    
           _end: 0x9aa700(VA)
    
      start_pfn: 10e6
    
        max_pfn: e4f53
    
    Mapping memory range 0x1400000 - 0xe4f53000
    
    setting 0x0-0x97000 readonly
    
    skipped 0x1000
    
    MM: Initialise page allocator for 1807000(1807000)-e4f53000(e4f53000)
    
    MM: done
    
    Demand map pfns at e4f54000-20e4f54000.
    
    Heap resides at 20e4f55000-40e4f55000.
    
    Initialising timer interface
    
    Initialising console ... done.
    
    gnttab_table mapped at 0xe4f54000.
    
    Initialising scheduler
    
    Thread "Idle": pointer: 0x20e4f55050, stack: 0xe4810000
    
    Thread "xenstore": pointer: 0x20e4f55800, stack: 0xe4820000
    
    xenbus initialised on irq 3 mfn 0xfeffc
    
    Thread "shutdown": pointer: 0x20e4f55fb0, stack: 0xe4830000
    
    Dummy main: start_info=0x98a200
    
    Thread "main": pointer: 0x20e4f56760, stack: 0xe4840000
    
    "main" "root=/dev/sda1" "ro" "console=hvc0" "4" 
    
    vbd 2048 is hd0
    
    ******************* BLKFRONT for device/vbd/2048 **********
    
    
    
    
    
    backend at /local/domain/0/backend/vbd/2334/2048
    
    629145600 sectors of 512 bytes
    
    **************************
    
    vbd 2128 is hd1
    
    ******************* BLKFRONT for device/vbd/2128 **********
    
    
    
    
    
    backend at /local/domain/0/backend/vbd/2334/2128
    
    314572800 sectors of 512 bytes
    
    **************************
    
    [H[J
    
    
        GNU GRUB  version 0.97  (3751244K lower / 0K upper memory)
    
    
    
    
    
    [m[4;2H+-------------------------------------------------------------------------+[5;2H|[5;76H|[6;2H|[6;76H|[7;2H|[7;76H|[8;2H|[8;76H|[9;2H|[9;76H|[10;2H|[10;76H|[11;2H|[11;76H|[12;2H|[12;76H|[13;2H|[13;76H|[14;2H|[14;76H|[15;2H|[15;76H|[16;2H|[16;76H|[17;2H+-------------------------------------------------------------------------+[m
    
    
        Use the ^ and v keys to select which entry is highlighted.
    
    
        Press enter to boot the selected OS, 'e' to edit the
    
    
        commands before booting, or 'c' for a command-line.[5;78H [m[7m[5;3H CentOS (2.6.32-696.18.7.el6.x86_64)                                     [5;75H[m[m[6;3H CentOS (2.6.32-573.el6.x86_64)                                          [6;75H[m[m[7;3H CentOS (2.6.32-358.18.1.el6.x86_64)                                     [7;75H[m[m[8;3H CentOS-6.4-x86_64-GA-03 2.6.32-358.el6.x86_64                           [8;75H[m[m[9;3H                                                                         [9;75H[m[m[10;3H                                                                         [10;75H[m[m[11;3H                                                                         [11;75H[m[m[12;3H                                                                         [12;75H[m[m[13;3H                                                                         [13;75H[m[m[14;3H                                                                         [14;75H[m[m[15;3H                                                                         [15;75H[m[m[16;3H                                                                         [16;75H[m[16;78H [5;75H[23;4H The highlighted entry will be booted automatically in 1 seconds.   [5;75H[H[J  Booting 'CentOS (2.6.32-696.18.7.el6.x86_64)'
    
    
    
    
    
    root (hd0)
    
    
     Filesystem type is ext2fs, using whole disk
    
    
    kernel /boot/vmlinuz-2.6.32-696.18.7.el6.x86_64 root=/dev/xvde ro crashkernel=a
    
    
    uto LANG=en_US.UTF-8 KEYTABLE=us
    
    
    initrd /boot/initramfs-2.6.32-696.18.7.el6.x86_64.img
    
    
    
    
    
    ============= Init TPM Front ================
    
    Tpmfront:Error Unable to read device/vtpm/0/backend-id during tpmfront initialization! error = ENOENT
    
    Tpmfront:Info Shutting down tpmfront
    
    close blk: backend=/local/domain/0/backend/vbd/2334/2048 node=device/vbd/2048
    
    close blk: backend=/local/domain/0/backend/vbd/2334/2128 node=device/vbd/2128

We're all not too experienced with AWS so we don't have much clue what to do. Any idea what we should be looking at or anything to point us in the right direction? The instance was actually a clone of production that we tested the upgrade on before doing it on actual production, so we have a chance to try it again and adjust any settings or whatever before or after the update.