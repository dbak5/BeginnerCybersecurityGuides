# Anti-Forensic Techniques

Definition can be found [here](https://cisomag.com/6-anti-forensic-techniques-that-every-digital-forensic-investigator-dreads/). It can include:

- System time modifications - evtx
- [VPN usage](https://attack.mitre.org/techniques/T1133/)
- [Timestomping](https://attack.mitre.org/techniques/T1070/006/) - NFTS
- [Disk wiping](https://attack.mitre.org/techniques/T1561/002/)
- [Data encryption](https://attack.mitre.org/techniques/T1573/001/)
- [Clear Event Logs](https://attack.mitre.org/techniques/T1070/001/) - evtx
- [File deletion](https://attack.mitre.org/techniques/T1070/004/)
- [Clear network connection history and configurations](https://attack.mitre.org/techniques/T1070/007/)

Some of these may be found in event logs or they may be found in the New Technology File System (NTFS) master file tables.
