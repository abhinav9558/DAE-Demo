# 🧩 ADR Categories by Track: Cybersecurity, Backend, Web Development

This reference provides ADR topic ideas grouped by track. Each ADR documents a real technical decision made during a project, and helps teams remember what was decided, why, and what trade-offs were involved.

---

## 🛡️ Cybersecurity ADR Categories & Examples

### 1. Intrusion Detection & Logging
- `ADR-use-wazuh.md` – Use Wazuh for HIDS in SOC lab  
- `ADR-network-monitoring.md` – Use Zeek to capture and log network activity  
- `ADR-log-retention.md` – Keep logs for 30 days with daily rotation  

### 2. Authentication & Access Control
- `ADR-auth-method.md` – Use email+OTP over username/password  
- `ADR-access-segmentation.md` – Separate analyst and admin roles via RBAC  

### 3. Threat Simulation & Defense
- `ADR-red-team-framework.md` – Use Caldera instead of Metasploit  
- `ADR-alert-thresholds.md` – Tune Wazuh rules to reduce false positives  

### 4. Incident Response Setup
- `ADR-incident-playbook.md` – Standardize IR workflow in markdown  
- `ADR-alert-forwarding.md` – Forward Wazuh alerts to Slack via webhook  

---

## 🗄️ Backend Development ADR Categories & Examples

### 1. Database & Storage
- `ADR-database-choice.md` – Use PostgreSQL over MongoDB  
- `ADR-file-storage.md` – Use AWS S3 for storing uploads  

### 2. API Design
- `ADR-api-style.md` – Use REST over GraphQL  
- `ADR-versioning.md` – Prefix APIs with `/v1/` for versioning  

### 3. Architecture & Tooling
- `ADR-service-structure.md` – Use Domain-Driven Design structure  
- `ADR-background-tasks.md` – Use Celery with Redis  

### 4. CI/CD & Deployment
- `ADR-ci-cd-tool.md` – Use GitHub Actions for auto-deploy  
- `ADR-docker-setup.md` – Use Docker Compose to containerize services  

---

## 🎨 Web Development ADR Categories & Examples

### 1. Framework & Libraries
- `ADR-frontend-framework.md` – Use React over Vue  
- `ADR-component-library.md` – Use Tailwind CSS instead of Bootstrap  

### 2. Routing & State Management
- `ADR-routing.md` – Use React Router for SPA routing  
- `ADR-state-management.md` – Use Context API instead of Redux  

### 3. Performance & Optimization
- `ADR-bundler-choice.md` – Use Vite over Webpack  
- `ADR-code-splitting.md` – Enable lazy loading for large components  

### 4. Auth & Client-Side Security
- `ADR-session-strategy.md` – Store JWT in HTTP-only cookies  
- `ADR-csrf-protection.md` – Add CSRF token to all forms  