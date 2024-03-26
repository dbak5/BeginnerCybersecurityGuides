<span style="color:red; font-size:32px">Work in Progress</span>

# Beginner's guide to setting up a Virtual Machine (VM)

## What are VMs?

VMs are essentially a virtual computer (referred to as a <em>guest</em>) that runs on your computer (referred to as a <em>host</em>), They share your computer's resources (such as memory and graphics) and you can access it by opening up a hypervisor or VM viewer.

Although a VM is running on your computer, it is considered 'isolated' from your normal operating system (OS) (although care should still be taken). Furthermore, a VM can run a totally different OS to what you're running. For example, if you are using Windows, you can spin up a VM using Linux.

<em>Note: This is recommended if you are carrying out digital forensics on potentially compromised machines and for this reason, it is good to familiarise yourself with multiple operating environments.</em>

## What are they used for?

There are many use-cases for VMs across various sectors. In terms of cybersecurity, some examples include:

- disaster recovery or backup
- analysing malware
- digital forensics
- incident response

If you are participating in a capture the flag event or competition where you are required to analyse disk images or files, it is recommended that you practice setting up and using a VM to carry out exercises.

### Advantages

- **Security**: They are considered isolated and therefore malicious activity or malware is unlikely to spread to another machine (i.e. your own!)
- **Sandboxing**: You can set up an environment where you can play around with settings, analyse malware and test software
- **Backups**: You can take snapshots of the VM environment and if you make any "unforgivable" errors while messing around, you have a rollback plan
- **Flexibility**: Some companies offer VMs as-a-service, where you can create and deploy machines in the cloud. This allows for flexibility as you can create as many as you need (for a fee, of course)

### Disadvantages

- **Performance**: You may run into resource allocation and performance issues if not configured properly
- **Complexity**: May not be an easy to understand concept for beginners, and set up does require some knowledge of computer hardware and functionality
- **Risks**: Caution is still advised because flaws can exist:

  - [Hypervisor Jackpotting, Part 3: Lack of Antivirus Support Opens the Door to Adversary Attacks](https://www.crowdstrike.com/blog/hypervisor-jackpotting-lack-of-antivirus-support-opens-the-door-to-adversaries/)
  - [A fully compromised ESXi host can force VMware Tools to fail to authenticate host-to-guest operations](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20867)

## What do I need to create a VM?

### Computer prepared for virtualisation

This can be a bit technical and depends on the hardware or OS of your computer. It may be that you need to enable some settings through BIOS. \
To complete this step, it is recommended that you google something like: `virtualisation setup for [OS]` and/or `virtualisation setup for [MOTHERBOARD]`.

If you are on a work computer, you will need Administrator privileges to install a hypervisor.

Finally, you want to ensure that you have the right amount of memory (disk space) on your computer. You can find this information in your Task Manager.
10GB or more is typical for a VM and remember, you still need sufficient memory for your host computer to run properly at the same time.

### Hypervisor

A hypervisor is the application running on your <em>host</em> computer that runs the <em>guest</em> virtual computer (VM).

Some examples include VirtualBox or VMware. Whatever you choose, ensure that you are downloading from a **reliable source** (i.e. official vendor pages). You can follow the vendor instruction pages for setup and install.

Some considerations when choosing a hypervisor:

- **Cost**: Some are offered for free (obviously with limitations in functionality), but many will have a fee if offered as a cloud service.
- **Functionality and ease of use**: Such as copy and paste to/from host and guest, and some may be easier to configure and deploy than others
- **Available support**: If using an obscure hypervisor and you run into issues, resolving them may be an issue if there are no active developer or user communities

There are other ways to set up and access a VM, but I will not go into them here.

Some useful resources:

- [Transferring Files to and from Virtual Machines](https://carleton.ca/scs/tech-support/virtual-machines/transferring-files-to-and-from-virtual-machines/)
- [VirtualBox Virtualization Error](https://carleton.ca/scs/2019/virtualbox-virtualization-error-intel-vt-d-vt-x-or-amd-v/)

### Disk image

The disk image will contain the OS for the VM and will usually come in an `.iso` format and can be quite large so may take a while to download.

Therefore, consider which OS you want/need to use. You can find these by simply googling them (e.g. `kali linux iso` or `windows 10 iso`) but ensure that you are downloading them from a **reliable source** (i.e. official vendor pages).

#### Windows

Obviously there are licensing considerations if using Windows; they do not offer free images. \
They may offer a 30 day trial, but after that, you may have to start another VM.

#### Linux

Many cybersecurity professionals use Linux, and it is open source, which means that it is free to download and use (yay!) \
There are various versions of Linux, which I won't go into, but Kali Purple Linux is already set up with many cybersecurity tools. You do have to install them. Here's a [guide](https://sysadmin102.com/2023/05/installing-kali-linux-purple-tools-and-theme/).

#### MacOS

I haven't yet used MacOS for a VM and I'm not sure of its considerations as yet. \
[Here's a guide](https://developer.apple.com/documentation/virtualization/installing_macos_on_a_virtual_machine).

## What now?

<em>Tip: I haven't installed a single VM without some sort of error, just keep googling errors and codes until you find the solution.</em>

Once you have all the above, proceed with the following:

- Install and set up your VM as per the vendor guides. Make sure you **correctly allocate resources**, google how to do this if necessary.
- Start up VM (There will usually be a **Start** button on the hypervisor) and go through setup and install of the OS
- Go through all the settings on your VM and personalise as if you were using a normal OS
- Install any tools that you need
- For digital forensics, time zones are an important consideration, so always make sure you have this set up properly, as well as administrator privileges.

Finally, it is highly recommended that you take a **snapshot** of your machine before carrying out any other activities (remember, always have a rollback plan). This is usually a feature in a hypervisor.

After you have completed using the VM, it is always recommended that you **shut down** the VM, as if you were shutting down your own computer. This is to ensure that it does not keep running, using your host computer resources. There will usually be an easy-to-find shut down button on the hypervisor.
