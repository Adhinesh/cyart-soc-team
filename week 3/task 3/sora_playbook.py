# Simulated Splunk Phantom Playbook Logic
def auto_escalation_playbook(alert):
    print(f"--- Processing Alert: {alert['name']} ---")
    
    # Logic: If Severity is High, auto-assign and isolate
    if alert['severity'] == "High":
        print("[ACTION] Severity is HIGH. Triggering Auto-Escalation...")
        print("[ACTION] Assigning case to: Tier 2 Analyst Group.")
        print(f"[ACTION] Running Network Isolation on host: {alert['host']}")
        print("[ACTION] Notifying Incident Lead via Slack/Email.")
    else:
        print("[ACTION] Severity is Low/Medium. Routing to Tier 1 queue.")

# Mock Alert from Server-Y
mock_alert = {
    "name": "Unauthorized Access",
    "host": "Server-Y",
    "severity": "High",
    "source_ip": "192.168.1.200"
}

auto_escalation_playbook(mock_alert)
