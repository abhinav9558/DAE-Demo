# Use Wazuh for Host-Based Intrusion Detection

## Context
In our SOC simulation lab, we needed to monitor and analyze security events on each host (endpoint). We were looking for a lightweight and open-source HIDS solution that works well with other SOC tools and fits within our Parrot OS and Kali VM environment.

## Decision
We chose Wazuh as the HIDS solution for our SOC lab.

## Rationale
- It supports real-time log analysis, file integrity monitoring, and threat detection.
- It integrates natively with ELK Stack, which we’re already using in our lab.
- Wazuh agents are compatible with Linux and provide visibility into the system-level activity.
- It supports alert forwarding, so we can centralize SOC alerts.

### Alternatives Considered
- **OSSEC** – Base project behind Wazuh, but less maintained and lacks new features.
- **Falco** – Geared more toward Kubernetes and containers, which we are not using.
- **Sysmon + Elastic Agent** – Better for Windows environments; complex for our lab VMs.

## Consequences
- Wazuh uses extra system resources and takes time to configure.
- Requires us to maintain both a manager and agent deployment.
- Will need tuning for false positives in alerts.

## References
- https://documentation.wazuh.com
- https://www.elastic.co/what-is/elk-stack
- Our team’s lab architecture diagram: [insert link or attach image]