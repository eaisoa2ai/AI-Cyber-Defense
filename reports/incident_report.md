# Security Incident Report

## Summary

- **High Severity**: 20
- **Medium Severity**: 1
- **Low Severity**: 31

## High Severity Findings

- **Privilege escalation**
  - User: adoyle
  - IP: 23.195.123.128
  - Rule: privilege_escalation

- **Privilege escalation**
  - User: kbrown
  - IP: 52.11.202.71
  - Rule: privilege_escalation

- **Privilege escalation**
  - User: jsmith
  - IP: 44.69.198.117
  - Rule: privilege_escalation

- **Privilege escalation**
  - User: jsmith
  - IP: 66.75.33.33
  - Rule: privilege_escalation

- **Privilege escalation**
  - User: adoyle
  - IP: 23.195.123.128
  - Rule: privilege_escalation

- **Privilege escalation**
  - User: kbrown
  - IP: 52.11.202.71
  - Rule: privilege_escalation

- **Privilege escalation**
  - User: jsmith
  - IP: 44.69.198.117
  - Rule: privilege_escalation

- **Privilege escalation**
  - User: jsmith
  - IP: 66.75.33.33
  - Rule: privilege_escalation

- **Brute Force Login**
  - User: jsmith
  - IP: 185.231.112.45
  - Rule: brute_force

- **privilege_escalation**
  - User: adoyle
  - IP: 23.195.123.128
  - Rule: privilege_escalation

- **privilege_escalation**
  - User: kbrown
  - IP: 52.11.202.71
  - Rule: privilege_escalation

- **privilege_escalation**
  - User: jsmith
  - IP: 44.69.198.117
  - Rule: privilege_escalation

- **privilege_escalation**
  - User: jsmith
  - IP: 66.75.33.33
  - Rule: privilege_escalation

- **Brute Force Login**
  - User: jsmith
  - IP: 185.231.112.45
  - Rule: foreign_login

- **Brute Force Login**
  - User: jsmith
  - IP: 185.231.112.45
  - Rule: brute_force_burst

- **Brute Force Login**
  - User: jsmith
  - IP: 185.231.112.45
  - Rule: suspicious_geo_success

- **privilege_escalation**
  - User: adoyle
  - IP: 23.195.123.128
  - Rule: privilege_escalation

- **privilege_escalation**
  - User: kbrown
  - IP: 52.11.202.71
  - Rule: privilege_escalation

- **privilege_escalation**
  - User: jsmith
  - IP: 44.69.198.117
  - Rule: privilege_escalation

- **privilege_escalation**
  - User: jsmith
  - IP: 66.75.33.33
  - Rule: privilege_escalation

## Medium Severity Findings

- **Credential stuffing**
  - User: jsmith
  - IP: 185.231.112.45
  - Rule: brute_force_burst

## Low Severity Findings

- **brute_force**
  - User: jsmith
  - IP: 185.231.112.45
  - Rule: brute_force

- **foreign_login**
  - User: jsmith
  - IP: 185.231.112.45
  - Rule: foreign_login

- **foreign_login**
  - User: svc_backup
  - IP: 201.214.112.115
  - Rule: foreign_login

- **foreign_login**
  - User: fhaant
  - IP: 52.79.110.246
  - Rule: foreign_login

- **foreign_login**
  - User: kbrown
  - IP: 201.125.83.119
  - Rule: foreign_login

- **foreign_login**
  - User: sliu
  - IP: 72.32.197.98
  - Rule: foreign_login

- **foreign_login**
  - User: jsmith
  - IP: 91.80.29.246
  - Rule: foreign_login

- **foreign_login**
  - User: adoyle
  - IP: 185.161.133.53
  - Rule: foreign_login

- **foreign_login**
  - User: sliu
  - IP: 102.51.37.138
  - Rule: foreign_login

- **foreign_login**
  - User: mgarcia
  - IP: 13.180.152.193
  - Rule: foreign_login

- **foreign_login**
  - User: kbrown
  - IP: 201.131.188.43
  - Rule: foreign_login

- **foreign_login**
  - User: fhaant
  - IP: 91.219.189.18
  - Rule: foreign_login

- **foreign_login**
  - User: fhaant
  - IP: 72.115.194.116
  - Rule: foreign_login

- **foreign_login**
  - User: jsmith
  - IP: 13.137.20.196
  - Rule: foreign_login

- **foreign_login**
  - User: sliu
  - IP: 91.187.46.203
  - Rule: foreign_login

- **foreign_login**
  - User: kbrown
  - IP: 23.237.154.167
  - Rule: foreign_login

- **suspicious_geo_success**
  - User: jsmith
  - IP: 185.231.112.45
  - Rule: suspicious_geo_success

- **foreign_login**
  - User: svc_backup
  - IP: 201.214.112.115
  - Rule: foreign_login

- **foreign_login**
  - User: fhaant
  - IP: 52.79.110.246
  - Rule: foreign_login

- **foreign_login**
  - User: kbrown
  - IP: 201.125.83.119
  - Rule: foreign_login

- **foreign_login**
  - User: sliu
  - IP: 72.32.197.98
  - Rule: foreign_login

- **foreign_login**
  - User: jsmith
  - IP: 91.80.29.246
  - Rule: foreign_login

- **foreign_login**
  - User: adoyle
  - IP: 185.161.133.53
  - Rule: foreign_login

- **foreign_login**
  - User: sliu
  - IP: 102.51.37.138
  - Rule: foreign_login

- **foreign_login**
  - User: mgarcia
  - IP: 13.180.152.193
  - Rule: foreign_login

- **foreign_login**
  - User: kbrown
  - IP: 201.131.188.43
  - Rule: foreign_login

- **foreign_login**
  - User: fhaant
  - IP: 91.219.189.18
  - Rule: foreign_login

- **foreign_login**
  - User: fhaant
  - IP: 72.115.194.116
  - Rule: foreign_login

- **foreign_login**
  - User: jsmith
  - IP: 13.137.20.196
  - Rule: foreign_login

- **foreign_login**
  - User: sliu
  - IP: 91.187.46.203
  - Rule: foreign_login

- **foreign_login**
  - User: kbrown
  - IP: 23.237.154.167
  - Rule: foreign_login


## Recommended Actions
- 🚨 IMMEDIATE ACTIONS:
- - Isolate affected systems
- - Reset compromised account passwords
- - Block malicious IP addresses at firewall
- - Initiate incident response procedures
- 
⚠️ URGENT ACTIONS:
- - Review and update access controls
- - Enable multi-factor authentication
- - Monitor affected accounts for suspicious activity
- 
📋 GENERAL RECOMMENDATIONS:
- - Conduct security awareness training
- - Review and update security policies
- - Implement additional monitoring
- - Schedule security assessment
