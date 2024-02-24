# **_Work in Progress_**

# Beginner Windows Event Logs Analysis

Analysis of event logs from Windows disk image.

It is recommended to carry out this process on a virtual machine.

Windows event logs are saved in <em>.evtx</em> format.

## EVTX Structures

- **Application** - information logged by system applications.
- **Security** - security events according to the auditing policy of the Windows operating system - including login activities (success and failure), elevated priviledges.
- **Setup** - installation or upgrading of Windows OS.
- **System** - Windows OS generated messages.
- **Forwarded Events** - events which are forwarded by other computers.

## EVTX Categories/Levels

- Information
- Warning
- Error
- Critical
- Success

## Tools

- FTK Imager or Autopsy
- Get-Zimmerman Tools - EZTools EvtxCmd.exe
- Get-Zimmerman Tools - TimelineExplorer.exe

## Collect and Prepare EVTX using FTK Imager

### FTK Imager

1. Open FTK Imager and add new evidence item (disk image)
2. In the left hand panel, navigate to where the event logs are stored on the image:

   `C:\Windows\System32\Winevt\Logs`

3. In the File List, right click on the event logs you want to parse and export. The main ones to look at are (but not limited to):

   - System.evtx
   - Security.evtx
   - Application.evtx
   - Microsoft-Windows-Windows Defender%4Operational.evtx

### Powershell, EvtxECmd.exe

4. Now open Powershell as administrator
5. Change directory (`cd`) to where the EZTools EvtxECmd.exe has been installed.
6. Run the following command to export the evtx files to csv as follows:

   `.\EvtxECmd.exe -f "[PATH WHERE EVTX WAS SAVED]\[NAME OF EVTX FILE].evtx" --csv "[PATH TO SAVE CSV]" --csvf [NAME].csv`

   Instructions on how to use EvtxECmd.exe can be found [here](https://github.com/EricZimmerman/evtx), but the breakdown of the above is as follows:

   - `.\EvtxECmd.exe` runs the program
   - `-f` is the file to process, which includes the file path and name
   - `--csv` the directory to save CSV file to
   - `--csvf` the file name of the CSV

7. Repeat the process for each EVTX file you want to analyse.

   The files should now be in csv format in your chosen folder. You can review them using TimelineExplorer (optional below) or Excel.

### Optional: TimelineExplorer

8. In File Explorer, navigate to the TimelineExplorer file (where Get-Zimmerman Tools installed to).
9. Open the TimelineExplorer.exe
10. In TimelineExplorer, go to File -> Open, and select the csv file you want to analyse.
11. Repeat the above process to open all the csv files you want to analyse, there should be a different tab for each.

## Collect and Prepare EVTX using Autopsy

### Autopsy

1. Open Autopsy and add new evidence item
2. Go through configuration steps:

   Step 1. Select Host: <em>Specify new host name</em> - provide a name for the file. \
   Step 2. Select Data Source Type: <em>Logical Files</em> \
   Step 3. Select Data Source: Add the disk image file. \
   Step 4. Configure Digest: Scroll down and select ParseEvtx.

   - If parsing **System.evtx, Security.evtx or Application.evtx**, select them.
   - If parsing another type of evtx file do the following: - Enter the name of the evtx file (i.e. `Microsoft-Windows-Windows Defender%4Operational.evtx`) in the text box.
   - <em>Then</em> check the "Other" box just above it

   Step 5. Click Finish

3. There should now be event logs in the Data Artifacts tree in the left hand panel

## Other files to look at: Registry Keys

- Customised Event Log

  `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog`

  This provides default and customized event log settings. Analyse to determine custom location of event logs, DLLs and executables.

- Additional Logging Details

  `HKLM\SYSTEM\CurrentControlSet\Services\EventLog`

## Critical events

- User logon/logoff
- Computer logon/logoff/restart
- Access to objects, files and folders
- System time is modified
- Audit logs are cleared
- Remote access

More information on critical events with event IDs

- [Common events for investigation](https://www.socinvestigation.com/most-common-windows-event-ids-to-hunt-mind-map/)
- [Common and useful events](https://ss64.com/ps/syntax-eventids.html)
- [Top 5 Windows Events for Incident Response](https://www.linkedin.com/pulse/top-5-windows-events-incident-response-invictus-incident-response/)
- [RDP events](https://www.socinvestigation.com/windows-rdp-event-ids-cheatsheet/)
- [Account access and management](https://medium.com/@rajeevranjancom/windows-event-log-analysis-incident-response-guide-739af79b518b)
- [Password changes and privilege escalation](https://alparslanakyildiz.medium.com/windows-event-ids-for-incident-response-cases-f3a069b8309f)
- [Security log event IDs](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx?i=j)
