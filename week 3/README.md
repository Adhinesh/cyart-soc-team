
# week 3 Task

## 📂 Project Modules

### 1. Advanced Log Analysis
**Objective:** Correlate disparate log sources to identify malicious patterns and automate anomaly detection.
*   **Log Correlation:** Ingested Boss of the SOC (BOTS) datasets into Elastic. Correlated Event ID 4625 (Failed Logins) with outbound DNS requests.
*   **Anomaly Detection:** Developed a threshold rule to alert on data exfiltration (bytes_out > 1MB/min).
*   **Enrichment:** Integrated GeoIP plugins to map attacker origins.

| Timestamp            | Event ID | Source IP      | Destination IP | Notes                     |
|----------------------|----------|----------------|----------------|---------------------------|
| 2025-08-18 12:00:00  | 4625     | 192.168.1.100  | 8.8.8.8        | Suspicious DNS request    |

---

### 2. Threat Intelligence Integration
**Objective:** Operationalize threat feeds to reduce "Mean Time to Detect" (MTTD).
*   **Feed Integration:** Imported AlienVault OTX pulses into Wazuh.
*   **Threat Hunting:** Conducted hunts for MITRE Technique **T1078 (Valid Accounts)** to identify potential credential compromise.

| Alert ID | IP            | Reputation        | Notes                     |
|----------|---------------|-------------------|---------------------------|
| 003      | 192.168.1.100 | Malicious (OTX)   | Linked to known C2 infra  |

---

### 3. Incident Escalation & SITREP
**Objective:** Standardize communication between Tier 1 and Tier 2 analysts.
*   **Case Management:** Created high-priority cases in **TheHive**.
*   **SITREP:** Drafted formal Situation Reports for "Unauthorized Access on Server-Y."
*   **SOAR Automation:** Developed a Splunk Phantom playbook to auto-assign alerts based on severity.

---

### 4. Alert Triage Simulation
**Objective:** Validate Indicators of Compromise (IOCs) using multi-source intelligence.
*   **Analysis:** Investigated "Suspicious PowerShell Execution" alerts.
*   **Validation:** Cross-referenced hashes and IPs against VirusTotal and OTX to confirm malicious intent.

| Alert ID | Description            | Source IP      | Priority | Status |
|----------|------------------------|----------------|----------|--------|
| 004      | PowerShell Execution   | 192.168.1.101  | High     | Open   |

---

### 5. Evidence Preservation (Forensics)
**Objective:** Collect volatile and non-volatile data while maintaining forensic integrity.
*   **Volatile Data:** Used **Velociraptor** to capture `netstat` connections and process trees.
*   **Disk Imaging:** Created a logical image of triage directories using **FTK Imager** (stored as `.ad1`).
*   **Integrity:** Verified all evidence using MD5, SHA1, and SHA256 hashing.

| Item           | Description       | Collected By | Date       | Hash Value (SHA256) |
|----------------|-------------------|--------------|------------|---------------------|
| Forensic Image | Server-Y Triage   | SOC Analyst  | 2026-04-16 | [YOUR_HASH_HERE]    |

---

### 6. Capstone: Full SOC Workflow Simulation
**Objective:** A "Live Fire" exercise covering the entire kill chain.
*   **Attack:** Exploited Samba vulnerabilities via Metasploit.
*   **Detection:** Configured Wazuh rules to trigger on `multi/samba/usermap_script` exploit patterns.
*   **Containment:** Automated IP blocking via **CrowdSec** and isolated the infected VM.
*   **Reporting:** Produced a SANS-standard 200-word technical report and a 100-word non-technical briefing for management.

---


