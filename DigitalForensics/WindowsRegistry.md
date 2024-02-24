# **_Work in Progress_**

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

This may depend on the version of Windows that is on the disk image.

- Windows XP, 2000 and 2003 files are located at: `Windows\System32\Config folder`
- Windows 10 files are located at: `%SystemRoot%\System32\Config\`

You may want to google your particular OS if not listed above.

Also note that the `HKEY_CURRENT_USER` hive is stored separately to the others, and is located at: `%SystemRoot%\Profiles\Username`

The registry files we will examine are located in the `HKEY_LOCAL_MACHINE` hive. These are:

- SAM
- SECURITY
- SOFTWARE
- SYSTEM

There are also other files which we will not look at in this exercise, but may be worth checking, and these are:

- Customised Event Log: `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog`. This provides default and customized event log settings. Analyse to determine custom location of event logs, DLLs and executables.
- Additional Logging Details: `HKLM\SYSTEM\CurrentControlSet\Services\EventLog`

## Process

## Some Registry Key Locations

- Network data - System Registry File -> Root -> Services -> Tcpip -> Parameters
- Computer name - System Registry File -> Root -> ControlSet001 -> Control -> ComputerName -> ComputerName
- Default size for the Windows EventLogs - System Registry File -> Root -> ControlSet001 -> Services -> EventLog -> Application -> MaxSize
  Value is in bytes, need to convert to MB or GB
- Windows OS - Software Registry File -> Root -> Microsoft -> Windows NT -> CurrentVersion -> ProductName

## Timeline and evidence

Create a timeline of the events you have uncovered and record all evidence found, including screenshots.

Crowdstrike have an Incident Response Tracker Template which you can download [here](https://www.crowdstrike.com/blog/crowdstrike-releases-digital-forensics-and-incident-response-tracker/).

It is also good to align events with the MITRE ATT&CK framework. [Here](https://www.socinvestigation.com/mapping-mitre-attck-with-window-event-log-ids/) is an example.
