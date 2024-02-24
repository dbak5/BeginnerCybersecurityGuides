# **_Work in Progress_**

# Beginner Windows Registry Analysis

Analysis of registry files using a Windows disk image.

It is recommended to carry out this process on a virtual machine.

During your analysis, you should be mindful of [anti-forensic techniques](https://github.com/dbak5/BeginnerCybersecurityGuides/blob/main/AntiForensicTechniques.md) that may be used by a threat actor to cover up their tracks.

## Process

From registry files contained in: \
%SystemRoot%\System32\Config\

Registry files:

- Sam – HKEY_LOCAL_MACHINE\SAM
- Security – HKEY_LOCAL_MACHINE\SECURITY
- Software – HKEY_LOCAL_MACHINE\SOFTWARE
- System – HKEY_LOCAL_MACHINE\SYSTEM

## Other files to look at: Registry Keys

- Customised Event Log

  `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog`

  This provides default and customized event log settings. Analyse to determine custom location of event logs, DLLs and executables.

- Additional Logging Details

  `HKLM\SYSTEM\CurrentControlSet\Services\EventLog`

## Network data

System Registry File -> Root -> Services -> Tcpip -> Parameters

## Computer name

System Registry File -> Root -> ControlSet001 -> Control -> ComputerName -> ComputerName

## Default size for the Windows EventLogs

System Registry File -> Root -> ControlSet001 -> Services -> EventLog -> Application -> MaxSize

Value is in bytes, need to convert to MB or GB

## Windows OS

Software Registry File -> Root -> Microsoft -> Windows NT -> CurrentVersion -> ProductName

## Timeline and evidence

Create a timeline of the events you have uncovered and record all evidence found, including screenshots.

Crowdstrike have an Incident Response Tracker Template which you can download [here](https://www.crowdstrike.com/blog/crowdstrike-releases-digital-forensics-and-incident-response-tracker/).

It is also good to align events with the MITRE ATT&CK framework. [Here](https://www.socinvestigation.com/mapping-mitre-attck-with-window-event-log-ids/) is an example.
