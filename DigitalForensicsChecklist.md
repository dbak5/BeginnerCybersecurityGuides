# **_Work in Progress_**

# Checklist for Carrying Out Digital Forensics

<em>**Disclaimer:** This list is not exhaustive but is a simple guide for beginners and probably more appropriate for use in CTFs.</em>

This is a list of things that you can look for when carrying our forensics on a potentially compromised image.

1. Set up VM (if applicable). Guide can be found [here](https://github.com/dbak5/BeginnerCybersecurityGuides/blob/main/VirtualMachineSetUp.md).
2. Check and set up timezones appropriately. More information[here](https://github.com/dbak5/BeginnerCybersecurityGuides/blob/main/TimeZones.md).

**To add?**

- Event logs (for Windows)
  - look for potential data exflitration
  - look for potential malicious scripts - common scripts used by threat actors
  - unusual log in accounts
  - unusual log in times
- Windows Registry
  - Tools:
    - FTK Imager or Autopsy
    - RegRipper
    - Get-ZimmermanTools
- Anti-forensics
  - Tools:
    - FTK Imager or Autopsy
    - Get-ZimmermanTools
  - Review NTFS/MFT - timestomping
- Document evidence and findings in tracker
- Construct timeline
- Verify evidence

## References

- [Digital Forensics Checklist](https://hackforlab.com/digital-forensic-checklist/)
- [SANS Log Management Cheatsheet](https://www.sans.org/brochure/course/log-management-in-depth/6?msc=Cheat+Sheet+Blog)
- [SANS Cheatsheet for Server Administrators](https://zeltser.com/media/docs/security-incident-survey-cheat-sheet.pdf?msc=Cheat+Sheet+Blog)
