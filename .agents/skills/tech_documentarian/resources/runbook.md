# Runbook Template

**When to use this template**: operational guides for service on-call response, troubleshooting, and system recovery. Typical triggers: "write an on-call runbook," "what to do when service X goes down," "document recovery steps for database failover."

Follow the parent skill's rules: ground error conditions and exact commands in real scripts/configs (§1); provide concrete step-by-step mitigation commands, not vague instructions (§7).

---

## Template

# [Service/System Name] — Runbook

## Overview
One paragraph: what service this runbook covers, its critical SLAs/SLOs, and who is the primary owner or on-call team.

## System Architecture & Quick Links
- **Dashboard / Metrics**: [Grafana/Datadog URL]
- **Logs**: [Kibana/CloudWatch URL]
- **Deployment Repo / Pipeline**: [CI/CD Pipeline URL]

---

## Common Incident Scenarios

### 1. High CPU / Memory Exhaustion

**Symptoms**
- Alert: `ServiceMemoryHigh` or `ServiceCPUHigh`
- P99 latency spikes above target threshold.

**Diagnosis**
Run the following commands to check current node utilization and processes:
```bash
top -b -n 1 | head -n 20
```

**Mitigation Steps**
1. Scale up replicas or restart worker pods:
   ```bash
   kubectl rollout restart deployment/service-name -n production
   ```
2. Verify recovery by monitoring active memory graph on Dashboard.

---

### 2. Database Connection Failure

**Symptoms**
- Error logs displaying `ConnectionRefused` or `DatabaseTimeout`.

**Diagnosis**
Check connectivity from application instance to DB host:
```bash
nc -zv db-host.internal 5432
```

**Mitigation Steps**
1. Check if DB primary failover is in progress.
2. Verify environment secrets for connection strings are valid.

---

## Rollback Procedure
If a recent deployment caused instability:
```bash
kubectl rollout undo deployment/service-name -n production
```

## Escalation Path
If steps above fail to resolve the incident within 15 minutes:
1. Ping on-call lead in `#incident-response` channel.
2. Page secondary on-call engineer.
