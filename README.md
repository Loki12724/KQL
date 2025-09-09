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
- [ASR_BlockedEvents_Detail_7d.kql](KQL/ASR/ASR_BlockedEvents_Detail_7d.kql)
- [ASR_BlockedEvents_Summary_7d.kql](KQL/ASR/ASR_BlockedEvents_Summary_7d.kql)

### ExploitGuard-NetworkProtection/
- [Network_Protection_Exploit_Guard.kql](KQL/ExploitGuard-NetworkProtection/Network_Protection_Exploit_Guard.kql)

### Auth-Logons-Identity/
- [AD_Sensitive_Group_Modifications.kql](KQL/Auth-Logons-Identity/AD_Sensitive_Group_Modifications.kql)
- [NTLM_Successful_Network_Logons.kql](KQL/Auth-Logons-Identity/NTLM_Successful_Network_Logons.kql)

### Defender-Health-Reports/
- [Defender_AV_Signature_Engine_Report.kql](KQL/Defender-Health-Reports/Defender_AV_Signature_Engine_Report.kql)
- [Endpoint_Agent_Health_Status.kql](KQL/Defender-Health-Reports/Endpoint_Agent_Health_Status.kql)

### Persistence-Registry/
- [Registry_New_Changed_Keywords.kql](KQL/Persistence-Registry/Registry_New_Changed_Keywords.kql)

### TVM-KEV-Vulns/
- [CISA_Top_Vulns_2019_2023.kql](KQL/TVM-KEV-Vulns/CISA_Top_Vulns_2019_2023.kql)

### SCCM-Integration/
- [SCCM_Process_Execution_and_Security_Alert_Join.kql](KQL/SCCM-Integration/SCCM_Process_Execution_and_Security_Alert_Join.kql)
- [SCCM_Process_AlertTimeAligned_15m_30d.kql](KQL/SCCM-Integration/SCCM_Process_AlertTimeAligned_15m_30d.kql)

### Utilities/
- [Filename_Search.kql](KQL/Utilities/Filename_Search.kql)

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
// Author: Kevin Hilt (@Lokis-Lab)  |  License: MIT
// Last Updated: 2025-09-09
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
