# 🔎 KQL Queries for Microsoft 365 Defender

This repository is a curated collection of **Kusto Query Language (KQL)** queries for use in **Microsoft 365 Defender Advanced Hunting**.  
They are designed to help with **threat hunting**, **detection**, and **reporting** across Defender data tables.

---

## 📂 Repository Structure

```
KQL/
├─ ASR/                                   # Attack Surface Reduction queries
├─ ExploitGuard-NetworkProtection/        # Network Protection / Exploit Guard
├─ Auth-Logons-Identity/                  # NTLM, logons, AD group mods, identity signals
├─ Defender-Health-Reports/               # AV engine/signatures, agent health
├─ Persistence-Registry/                  # Registry-based persistence and autoruns
├─ TVM-KEV-Vulns/                         # Threat & Vulnerability Mgmt and CISA KEV
├─ SCCM-Integration/                      # MECM/SCCM + Defender correlations
├─ Utilities/                             # Helpers (e.g., filename search)
└─ _Unsorted/                             # Staging area for uncategorized queries
```

---

## 📑 Query Index

### ASR/
- [ASR_BlockedEvents_Detail_7d.kql](KQL/ASR/ASR_BlockedEvents_Detail_7d.kql) — Detailed list of ASR block events in the last 7 days.
- [ASR_BlockedEvents_Summary_7d.kql](KQL/ASR/ASR_BlockedEvents_Summary_7d.kql) — Summarized count of ASR events by category.
- [ASR_Filename_Search_7d.kql](KQL/ASR/ASR_Filename_Search_7d.kql) — Search ASR events for specific file names.

### ExploitGuard-NetworkProtection/
- [Network_Protection_Exploit_Guard.kql](KQL/ExploitGuard-NetworkProtection/Network_Protection_Exploit_Guard.kql) — List of Exploit Guard / Network Protection events.

### Auth-Logons-Identity/
- [AD_Sensitive_Group_Modifications.kql](KQL/Auth-Logons-Identity/AD_Sensitive_Group_Modifications.kql) — Detect modifications to sensitive AD groups.
- [NTLM_Successful_Network_Logons.kql](KQL/Auth-Logons-Identity/NTLM_Successful_Network_Logons.kql) — Successful NTLM network logon attempts.

### Defender-Health-Reports/
- [Defender_AV_Health_Status_6h.kql](KQL/Defender-Health-Reports/Defender_AV_Health_Status_6h.kql) — Unified Defender AV health report (mode, signatures, engine, platform).
- [Endpoint_Agent_Health_Status.kql](KQL/Defender-Health-Reports/Endpoint_Agent_Health_Status.kql) — Status and health of Defender agents across endpoints.
- [Defender_SecureConfig_BestPracticeReport.kql](Defender-Health-Reports/Defender_SecureConfig_BestPracticeReport.kql) — Report on Defender secure configuration compliance vs. best practices (sensor, tamper protection, PUA, AV, cloud).

### Persistence-Registry/
- [Registry_New_Changed_Keywords.kql](KQL/Persistence-Registry/Registry_New_Changed_Keywords.kql) — Detect new or modified suspicious registry keys.
- [Registry_AttachmentManager_ScanWithAntiVirus_30d.kql](KQL/Persistence-Registry/Registry_AttachmentManager_ScanWithAntiVirus_30d.kql) — Monitor changes to the ScanWithAntiVirus flag under Attachment Manager.
- [Registry_Service_Modifications.kql](KQL/Persistence-Registry/Registry_Service_Modifications.kql) — Detect registry modifications within the Services hive.

### Persistence-Services/
- [Process_ServiceCreation_sc_powershell.kql](KQL/Persistence-Services/Process_ServiceCreation_sc_powershell.kql) — Detect service creation via sc.exe or PowerShell.
- [Process_ServiceName_CommandLine.kql](KQL/Persistence-Services/Process_ServiceName_CommandLine.kql) — Detect processes that include ServiceName in their command line.
- [Process_ServicesExe_Children.kql](KQL/Persistence-Services/Process_ServicesExe_Children.kql) — Detect child processes spawned by services.exe.

### TVM-KEV-Vulns/
- [CISA_Top_Vulns_2019_2023.kql](KQL/TVM-KEV-Vulns/CISA_Top_Vulns_2019_2023.kql) — Identify devices exposed to top CISA KEV vulnerabilities.

### SCCM-Integration/
- [SCCM_Process_Execution_and_Security_Alert_Join.kql](KQL/SCCM-Integration/SCCM_Process_Execution_and_Security_Alert_Join.kql) — Join SCCM process execution data with Defender security alerts.
- [SCCM_Process_AlertTimeAligned_15m_30d.kql](KQL/SCCM-Integration/SCCM_Process_AlertTimeAligned_15m_30d.kql) — Time-align SCCM process and alert data within 15m windows over 30 days.

### Utilities/
- [Filename_Search.kql](KQL/Utilities/Filename_Search.kql) — Search events for specific filenames.
- [Process_SuspiciousExe_UserPaths.kql](KQL/Utilities/Process_SuspiciousExe_UserPaths.kql) — Detect execution of .exe files from Temp, AppData, or Public directories.

### _Unsorted/
- *(any queries that don’t yet fit into a category)*

---

## 🚀 Usage

1. Open the **Microsoft 365 Defender Advanced Hunting** portal: https://security.microsoft.com/advanced-hunting  
2. Paste a query from this repo into the editor.  
3. Adjust as needed:
   - **Time ranges** (`ago(7d)`, `ago(30d)`, etc.)
   - **Filters** (device groups, accounts, file paths)
   - **Output** (summaries vs. raw events)
4. Run the query and analyze results.

---

## 🧱 Standard Query Header

Use this header block at the top of each `.kql` file to keep things consistent:

```kusto
// Title: <Short descriptive name>
// Purpose: <What this query helps you find or decide>
// Scope: <Windows 11 / Server 2016+ / All Windows / etc.>
// Tables: <DeviceEvents, DeviceRegistryEvents, AlertInfo, DeviceTvm* ...>
// Tunables:
//   - Time range: change `ago(7d)` as needed
//   - Filters: device groups, account names, file paths, etc.
// Author: Lokis-Lab  |  License: MIT
// Last Updated: 2025-09-10
```

---

## ⚠️ Notes

- Written for **Microsoft 365 Defender Advanced Hunting**.  
- Some queries may require changes to run in **Microsoft Sentinel**.  
- Queries are **starting points** and may need tuning for noise reduction.

---

## 🤝 Contributions

This repo is primarily a personal hunting library, but contributions are welcome:

1. Fork the repo  
2. Add or improve queries (using the standard header format)  
3. Submit a pull request

---
## 📜 License

MIT License — see [LICENSE](LICENSE) for details.
