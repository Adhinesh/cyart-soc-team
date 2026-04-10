# cyart-soc-team — Week 2: SOC Alert Management & Incident Response

## Student Details
- **Name:** Dhinesh
- **Team:** cyart-soc-team
- **Week:** 2
- **Submission Date:** Friday, April 10, 2026 — 4:30 PM

---

## Overview
This repository documents Week 2 practical tasks covering SOC alert 
management, incident classification, basic incident response, alert 
triage, evidence preservation, and a full capstone attack-to-response 
simulation. All tasks follow the SANS PICERL framework and MITRE 
ATT&CK methodology.

---

---

## Task Summary

### Theoretical Knowledge
| Topic | Status |
|---|---|
| Alert Priority Levels (CVSS Scoring) | Done |
| Incident Classification (MITRE ATT&CK) | Done |
| Basic Incident Response (NIST SP 800-61) | Done |

### Practical 1 — Alert Management
| Task | Tool | Status |
|---|---|---|
| Alert Classification Table | Google Sheets | Done |
| CVSS Priority Scoring | Google Sheets | Done |
| Wazuh Alert Dashboard | Wazuh | Done |
| TheHive Incident Ticket | TheHive / Mock | Done |
| Escalation Email | Google Docs | Done |

### Practical 2 — Response Documentation
| Task | Tool | Status |
|---|---|---|
| SANS IR Report Template | Google Docs | Done |
| Investigation Steps Log | Google Docs | Done |
| Phishing Response Checklist | Google Docs | Done |
| Post-Mortem Summary | Google Docs | Done |
| IR Workflow Diagram | Draw.io | Done |

### Practical 3 — Alert Triage
| Task | Tool | Status |
|---|---|---|
| Triage Simulation (SSH Brute-force) | Wazuh | Done |
| Threat Intel Validation | AlienVault OTX | Done |

### Practical 4 — Evidence Preservation
| Task | Tool | Status |
|---|---|---|
| Volatile Data Collection (netstat) | Velociraptor | Done |
| Memory Dump + SHA256 Hash | Velociraptor | Done |
| Chain of Custody Documentation | Google Docs | Done |

### Capstone — Full Alert-to-Response Cycle
| Task | Tool | Status |
|---|---|---|
| Attack Simulation (vsftpd backdoor) | Metasploit | Done |
| Detection & Alert Triage | Wazuh | Done |
| IP Block & Verification | CrowdSec | Done |
| 200-word SANS Incident Report | Google Docs | Done |
| 100-word Manager Briefing | Google Docs | Done |

---

## Key Tools Used
- **Wazuh** — SIEM, alert detection and dashboard
- **TheHive** — Incident case management
- **Metasploit** — Attack simulation (Metasploitable2)
- **CrowdSec** — IP blocking and verification
- **Velociraptor** — Volatile data and memory collection
- **VirusTotal** — IOC validation
- **AlienVault OTX** — Threat intelligence
- **Draw.io** — IR workflow diagram
- **Google Docs/Sheets** — Documentation

---

## MITRE ATT&CK Techniques Covered
| Technique ID | Name | Tactic |
|---|---|---|
| T1566.002 | Spear Phishing Link | Initial Access |
| T1190 | Exploit Public-Facing Application | Initial Access |
| T1110.003 | Password Spraying | Credential Access |
| T1486 | Data Encrypted for Impact | Impact |
| T1046 | Network Service Discovery | Discovery |

---

## References
- NIST SP 800-61 — Incident Handling Guide
- SANS Incident Handler's Handbook
- MITRE ATT&CK Framework — https://attack.mitre.org
- FIRST CVSS Guide — https://www.first.org/cvss
- Metasploit Unleashed — https://www.offensive-security.com/metasploit-unleashed
