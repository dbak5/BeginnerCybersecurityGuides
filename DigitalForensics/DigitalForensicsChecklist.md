<span style="color:red; font-size:32px">Work in Progress</span>

# Checklist for Carrying Out Digital Forensics

<em>**Disclaimer:** This list is not exhaustive but is a simple guide for beginners and probably more appropriate for use in CTFs.</em>

This is a list of things that you can look for when carrying our forensics on a potentially compromised image.

1. Set up VM (if applicable). Guide can be found [here](https://github.com/dbak5/BeginnerCybersecurityGuides/blob/main/DigitalForensics/VirtualMachineSetUp.md).
2. Check and set up timezones appropriately. More information[here](https://github.com/dbak5/BeginnerCybersecurityGuides/blob/main/DigitalForensics/TimeZones.md).

- Event logs (for Windows)
  - look for potential data exflitration
  - look for potential malicious scripts - common scripts used by threat actors
  - unusual log in accounts
  - unusual log in times
- Autopsy
  - Web search history
  - Recent activity - run prorgams - Recently Executed according to Background Activity Moderator (BAM)
    Recent documents
  - [Shellbags](https://www.sciencedirect.com/science/article/pii/S1742287609000413#:~:text=Built%20into%20Microsoft%20Windows%20is,in%20the%20Windows%20Operating%20System) - Built into Microsoft Windows is the ability for the operating system to track user window viewing preferences specific to Windows Explorer. This information, which is called “ShellBag” information
- Windows Registry
  - Tools:
    - FTK Imager
    - RegRipper
    - Get-ZimmermanTools **_you will need .NET and Windows to use these tools_**
  - [Boot or logon autostart execution](https://attack.mitre.org/techniques/T1547/001/)
  - UserAssist
- Anti-forensics
  - Tools:
    - FTK Imager or Autopsy
    - Get-ZimmermanTools **_you will need .NET and Windows to use these tools_**
  - Review NTFS/MFT - [timestomping](https://attack.mitre.org/techniques/T1070/006/)
- Document evidence and findings in tracker
- Construct timeline
- Verify evidence

## References

- [Digital Forensics Checklist](https://hackforlab.com/digital-forensic-checklist/)
- [SANS Log Management Cheatsheet](https://www.sans.org/brochure/course/log-management-in-depth/6?msc=Cheat+Sheet+Blog)
- [SANS Cheatsheet for Server Administrators](https://zeltser.com/media/docs/security-incident-survey-cheat-sheet.pdf?msc=Cheat+Sheet+Blog)
