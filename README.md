🔎 KQL Queries for Microsoft 365 Defender

This repository is a curated collection of Kusto Query Language (KQL) queries for use in Microsoft 365 Defender Advanced Hunting.
They are designed to help with threat hunting, detection, and reporting across Defender data tables.
----------------------------------------------------------------------------------------------------------------------------
📂 Repository Structure

ASR/                               # Attack Surface Reduction queries
ExploitGuard-NetworkProtection/    # Network Protection / Exploit Guard
Auth-Logons-Identity/              # NTLM, logons, AD group mods, identity signals
Defender-Health-Reports/           # AV engine/signatures, agent health
Persistence-Registry/              # Registry-based persistence and autoruns
TVM-KEV-Vulns/                     # Threat & Vulnerability Mgmt and CISA KEV
SCCM-Integration/                  # MECM/SCCM + Defender correlations
Utilities/                         # Helpers (e.g., filename search)
_Unsorted/                         # Staging area for uncategorized queries
----------------------------------------------------------------------------------
📑 Query Index

ASR/
  ASR_BlockedEvents_Detail_7d.kql
  ASR_BlockedEvents_Summary_7d.kql
ExploitGuard-NetworkProtection/
  Network_Protection_Exploit_Guard.kql
Auth-Logons-Identity/
  AD_Sensitive_Group_Modifications.kql
  NTLM_Successful_Network_Logons.kql
Defender-Health-Reports/
  Defender_AV_Signature_Engine_Report.kql
  Endpoint_Agent_Health_Status.kql
Persistence-Registry/
  Registry_New_Changed_Keywords.kql
TVM-KEV-Vulns/
  CISA_Top_Vulns_2019_2023.kql
SCCM-Integration/
  SCCM_Process_Execution_and_Security_Alert_Join.kql
  SCCM_Process_AlertTimeAligned_15m_30d.kql
Utilities/
  Filename_Search.kql
_Unsorted/ (any queries that don’t yet fit into a category)
------------------------------------------------------------------------------
🚀 Usage

Open the Microsoft 365 Defender Advanced Hunting portal.
Copy a query from this repo into the query editor.
Adjust:
  Time ranges (ago(7d), ago(30d), etc.)
  Filters (device groups, accounts, file paths)
  Output (summaries vs. raw events)
  Run the query and analyze results.
-----------------------------------------------------------------------------------------
🧩 Query Categories

ASR (Attack Surface Reduction) → Visibility into blocked or audited ASR activity.
Exploit Guard & Network Protection → Exploit Guard triggers and network protection events.
Authentication & Identity → NTLM logons and Active Directory group changes.
Defender Health & AV Reporting → Agent status, AV engine versions, signature health.
Persistence & Registry → Registry key creation/modification tied to persistence.
Vulnerabilities & KEV → Threat & Vulnerability Mgmt queries with CISA KEV mapping.
SCCM Integration → Correlating SCCM activity with Defender signals.
Utilities → General-purpose helper queries.
-----------------------------------------------------------------------------------------
⚠️ Notes

Written for Microsoft 365 Defender Advanced Hunting.
Some queries may require changes to run in Microsoft Sentinel.
Queries are starting points and may need tuning for noise reduction.
Each file includes a standard header with:
  Title
  Purpose
  Scope
  Tables used
  Tunables (time ranges, filters, etc.)
-----------------------------------------------------------------------------------------
🤝 Contributions

This repo is primarily a personal hunting library, but contributions are welcome:
  Fork the repo
  Add or improve queries (using the standard header format)
  Submit a pull request
----------------------------------------------------------------------------------------
📜 License

MIT License 
