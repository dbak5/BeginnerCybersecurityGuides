# **_Work in Progress_**

# Windows Registry Analysis

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
