---
date: 2018-01-04 23:13:32
source: twitter
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/949177027843702784/
tags:
- spectre
- meltdown
repost_source:
  name: gsuberland
  type: twitter
  url: https://twitter.com/gsuberland/status/948907452786933762
title: "gsuberland: Explainer on #Spectre & #Meltdown"
---

Explainer on #Spectre & #Meltdown:



When a processor reaches a conditional branch in code (e.g. an 'if' clause), it tries to predict which branch will be taken before it actually knows the result. It executes that branch ahead of time - a feature called "speculative execution".

---

The idea is that if it gets the prediction right (which modern processors are quite good at) it'll already have executed the next bit of code by the time the actually-selected branch is known. If it gets it wrong, execution unwinds back and the correct branch is executed instead.

---

What makes the processor so good at branch prediction is that it stores details about previous branch operations, in what's called the Branch History Buffer (BHB). If a particular branch instruction took path A before, it'll probably take path A again, rather than path B.

---

What makes this interesting is that code is executed *speculatively*, before the result of a conditional statement has completed. That conditional statement could be security-critical. Thankfully the processor is (mostly) smart enough to roll back any side-effects of execution.

---

There are two important exclusions to the rollback of side-effects: cache and branch prediction history. These generally aren't rolled back because speculative execution is a performance feature, and rolling back cache and BHB contents would generally hurt performance.

---

There are three ways to exploit this behaviour. The Spectre paper describes the first two exploits, with the following results:



1. Kernel memory disclosure from userspace on bare metal.

2. Kernel memory disclosure of the VM host/hypervisor from kernelspace in a VM.

---

The first exploit works by getting the kernel to execute some carefully written attacker-specified code which contains an array bounds check followed by an array read, where the read index is controlled by an attacker. This sounds like a big ask, but it's not thanks to JIT.

---

On Linux, Extended Berkley Packet Filter (eBPF) allows users to write socket filters from usermode which get JIT compiled by the kernel in order to efficiently filter packets on a socket. The details aren't important, but it means an attacker can get the kernel to execute code.

---

The exploit involves writing eBPF code which compiles to the following steps:

1. Allocate two fixed-size arrays

2. Bounds-check the user-provided index

3. If ok, read from the array1 at that index

4. Compute another index from 1 bit of the result

5. Read from array2 at that index

---

There's actually a step before 5, which is "bounds check the read to array2", but we never intend to do an out-of-bounds read here, so it's irrelevant. I omitted it because I ran out of characters.

---

In terms of "real" execution, this code always terminates at step 2 when the user passes an out-of-bounds index for array1. But if the processor's branch predictor assumes that check will succeed, it'll speculatively execute the out-of-bounds read in step 3, and continue to 5.

---

Here's the clever bit. In step 4 we take the value we got from the out-of-bounds read (which we wouldn't normally have access to) and use one bit from it to select a particular memory address (array index) to read. If b=0 it reads index 0x200; if b=1 it reads index 0x300.

---

This ensures that the memory at either index 0x200 or index 0x300 is now cached. The CPU then realises that the bounds check in step 2 failed, so it unwinds back to that branch. However, the data from step 5 is still cached!

---

We can then go in and read the data at 0x200 and 0x300 and see which is cached by measuring how quick the read is. Once we know which index was cached we can directly infer one bit of kernel memory, based on the index selection from step 4.

---

There are some details as to how the cache needs to be primed before this attack, but it is possible to do this whole process in a loop and dump kernel memory from unprivileged userspace.

---

The second attack described in the Spectre paper involves poisoning the branch prediction history to trick the processor into speculatively executing code at an attacker-specified address, leading to further cache attacks as described above.

---

By performing a carefully selected sequence of indirect jumps, an attacker can fill up the branch prediction history in a way that allows the attacker to select which branch will be speculatively executed when performing an indirect jump.

---

This can be very powerful. If I know there's a piece of code in kernel space that exhibits similar behaviour to our eBPF example from before, and I know what the address of that code is, I can indirectly jump to that code and the CPU will speculatively execute it.

---

If you've done exploitation before, you'll probably recognise this as being similar to a ROP gadget. We're looking for a sequence of code in kernel space that happens to have the right sequence of instructions to leak information via cache.

---

Keep in mind that the execution is speculative only - the processor will later realise that I didn't have the privilege to jump to that code and throw an exception. So the target code has to leak kernel data via cache side-channels like before.

---

You'll also notice that we need to know address of the target kernel code. With KASLR this isn't so easy. Project Zero's writeup explains how KASLR can be defeated using branch prediction and caching as side-channels, so I won't go into the details here. https://googleprojectzero.blogspot.co.uk/2018/01/reading-privileged-memory-with-side.html…

---

What makes this extra powerful is that it works across VM boundaries too. Instead of a traditional indirect jump (e.g. jmp eax), we can use the vmcall instruction to speculatively execute code within the VM host's kernel in the same way we would our VM's kernel.

---

Finally, there's the third approach. This involves a flush+reload cache attack against kernel memory, similar to the first variant of the attack but without requiring kernel code execution - it can all be done from usermode.

---

The idea is that we try to read kernelspace memory using a mov instruction, then perform a secondary memory read with an address based on the value that was read. If you're thinking the first mov will fail because we're in usermode and can't read kernel addresses, you're right.

---

The trick is that the microarchitectural implementation of mov contains the memory page privilege level check, which itself is a branch instruction. The processor may speculatively execute that branch like any other.

---

So, if you can outrun the interrupt, you can speculatively execute some other instruction that loads data into cache based on the value read from kernelspace. This then becomes a cache attack like the previous tricks.

---

And that's just about it.



For full details I recommend checking out the two papers, as well as the Project Zero writeup I linked above.



https://spectreattack.com/spectre.pdf



https://meltdownattack.com/meltdown.pdf