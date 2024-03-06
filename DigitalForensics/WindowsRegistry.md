<span style="color:red; font-size:32px">Work in Progress</span>

# Beginner Windows Registry Analysis

This is a guide for parsing and analysing **registry files** using a Windows disk image.

From registry files, we may see evidence of activities carried out by a threat actor (as long as they have not been deleted) which may include [timestomping](https://attack.mitre.org/techniques/T1070/006/). The registry files also include important information about the image itself such as settings and configuration for the OS, network, event logs and more.

During your analysis, you should be mindful of [anti-forensic techniques](https://github.com/dbak5/BeginnerCybersecurityGuides/blob/main/DigitalForensics/AntiForensicTechniques.md) that may be used by a threat actor to cover up their tracks. Some of these may be found in the registry files!

In addition, make sure to verify all evidence and do not trust outputs immediately; data may have been altered or corrupted so it is always good to get validation from another source.

It is recommended to carry out this process on a virtual machine.

## Registry Files

### Structure

Registry files are organised in a tree structure. There are five main folders, which are called a **hive**:

- `HKEY_CLASSES_ROOT` (HKCR)
- `HKEY_USERS` (HKU)
- `HKEY_CURRENT_USER` (HKCU)
- `HKEY_LOCAL_MACHINE` (HKLM)
- `HKEY_CURRENT_CONFIG` (HKCC)

Hives will also contain a number of sub folders, and these are called **keys**. These keys contain sub keys which contain configuration information.

### Location of Hives

This may depend on the version of Windows that is on the disk image. You may want to google your particular OS to check, but many Windows OS files are located at: `Windows\System32\Config`.

The registry files we will examine from the `HKEY_LOCAL_MACHINE` hive:

- SAM
- SECURITY
- SOFTWARE
- SYSTEM

We will also look at the following `HKEY_CURRENT_USER` files, which are located separately to the other registry files:

- Ntuser.dat located in `Users\[USERNAME]`
- Usrclass.dat located in `Users\[USERNAME]\AppData\Local\Microsoft\Windows`

This key reflects changes that happen while Windows is running and the user is logged in. Important information it contains includes user activity such as installs / executed applications, files / folders accessed and much more.

There are also other files which we will not look at in this exercise, but may be worth checking, and these are:

- Customised Event Log: `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog`. This provides default and customized event log settings. Analyse to determine custom location of event logs, DLLs and executables.
- Additional Logging Details: `HKLM\SYSTEM\CurrentControlSet\Services\EventLog`

## Tools

- FTK Imager

## Access Data using FTK Imager

### FTK Imager

1. Open FTK Imager and add evidence item
2. In the left hand side panel, browse the tree to get to the registry files:

- `Users\[USERNAME]`
  - Ntuser.dat
- `Users\[USERNAME]\AppData\Local\Microsoft\Windows`
  - Usrclass.dat
- `Windows\System32\Config`
  - SAM
  - SECURITY
  - SOFTWARE
  - SYSTEM

3. Right click on the files and click to export and save

### Powershell, RegRipper

## Registry Key Locations

Some registry keys and locations:

- Network data - System Registry File -> Root -> Services -> Tcpip -> Parameters
- Computer name - System Registry File -> Root -> ControlSet001 -> Control -> ComputerName -> ComputerName
- Default size for the Windows EventLogs - System Registry File -> Root -> ControlSet001 -> Services -> EventLog -> Application -> MaxSize
  Value is in bytes, need to convert to MB or GB
- Windows OS - Software Registry File -> Root -> Microsoft -> Windows NT -> CurrentVersion -> ProductName

## Things to look for

- User search history
- Recent activity such as applications and the locations
-

## Timeline and evidence

Create a timeline of the events you have uncovered and record all evidence found, including screenshots.

Crowdstrike have an Incident Response Tracker Template which you can download [here](https://www.crowdstrike.com/blog/crowdstrike-releases-digital-forensics-and-incident-response-tracker/).

It is also good to align events with the MITRE ATT&CK framework. [Here](https://www.socinvestigation.com/mapping-mitre-attck-with-window-event-log-ids/) is an example.

<!--reources
https://www.hackers-arise.com/post/2016/10/21/digital-forensics-part-5-analyzing-the-windows-registry-for-evidence
https://www.linkedin.com/pulse/windows-registry-its-forensic-significance-part-3-akshay-tiwari
https://www.mandiant.com/resources/blog/the-missing-lnk-correlating-user-search-lnk-files

-->
