# Miami Resources — Compliance & Security Framework

## 1. Data Privacy

### What We Collect
- **Nothing.** No personally identifiable information (PII) is collected, stored, or transmitted.
- No login, no account creation, no cookies tracking individuals.
- Conversation sessions are ephemeral — cleared after 24 hours or on browser close.

### Regulatory Compliance

| Regulation | Status | Notes |
|-----------|--------|-------|
| Florida Information Protection Act (FIPA) | Compliant | No personal data stored |
| HIPAA | Not applicable | No health records collected or stored |
| COPPA | Compliant | No data collection from any user, including minors |
| FERPA | Not applicable | No student records accessed |
| Executive Order 13166 (LEP) | Compliant | Full support for Spanish and Haitian Creole |
| ADA / Section 508 | Compliant | WCAG 2.1 AA conformance |
| Florida Sunshine Law | Compatible | No resident records to disclose |
| SOC 2 Type II | Infrastructure certified | NVIDIA, Google Cloud, Cloudflare |

## 2. Accessibility (Section 508 / WCAG 2.1 AA)

- Semantic HTML5 with ARIA landmarks and labels
- Keyboard-navigable — all functions accessible without mouse
- Screen reader compatible (VoiceOver, NVDA, JAWS tested)
- Color contrast ratio ≥ 4.5:1 for all text
- Focus indicators visible on all interactive elements
- Mobile-first responsive design (320px minimum viewport)
- No CAPTCHA or visual verification barriers
- Plain language at 6th-grade reading level (Flesch-Kincaid)

## 3. AI Safety & Responsible Use

### Grounding
- All program recommendations sourced from a verified, version-controlled database
- Phone numbers, addresses, and websites are never AI-generated
- Eligibility information based on published federal/state/county criteria

### Guardrails
- System refuses to provide medical diagnoses or legal advice
- Crisis detection routes to human services (911, 988, 211) immediately
- "I don't know" responses direct users to 211 rather than guessing
- No political content, no opinions on policy, no recommendations beyond program matching

### Bias Mitigation
- Equal treatment across all three languages verified via automated testing
- Program recommendations do not vary by inferred demographics
- Quarterly bias audit comparing response quality across EN/ES/HT
- Community advisory review of Haitian Creole translations

### Transparency
- Users informed they are interacting with an AI assistant
- AI model provider and version logged for every interaction (audit trail)
- No decision-making authority — AI recommends, humans decide

## 4. Security Architecture

### Data in Transit
- TLS 1.3 encryption for all client-server communication
- HSTS headers enforced
- Certificate pinning available for kiosk deployments

### Data at Rest
- **No resident data stored** — eliminates the primary attack surface
- Program database is public information, stored in version-controlled repository
- API keys stored in encrypted environment variables, never in source code

### Infrastructure Security
- **Cloudflare**: DDoS protection, WAF, bot management
- **NVIDIA NIM**: SOC 2 Type II certified, ISO 27001
- **Google Cloud**: SOC 2 Type II, FedRAMP Authorized (Moderate)
- **On-premises option**: Eliminates all third-party data transit

### Incident Response
- 24/7 automated monitoring with alerting
- Incident response plan with 4-hour SLA for critical issues
- Annual penetration testing by third-party security firm
- Vulnerability disclosure program

## 5. On-Premises Deployment Option

For maximum data sovereignty, Miami Resources can be deployed entirely within county infrastructure:

- **NVIDIA NIM** runs on a single GPU server (A100 80GB recommended)
- **No internet required** for inference — air-gapped operation possible
- **Program database** hosted on county PostgreSQL or file system
- **Frontend** served from county web servers
- **Zero data leaves the building**

This option is recommended for agencies with strict data residency requirements or existing NVIDIA GPU infrastructure.

## 6. Audit & Reporting

| Report | Frequency | Contents |
|--------|-----------|----------|
| Usage analytics | Monthly | Query volume, language distribution, category breakdown |
| Accuracy audit | Quarterly | Sample review of 500 interactions across all languages |
| Bias assessment | Quarterly | Response quality comparison across EN/ES/HT |
| Security scan | Annual | Penetration test, vulnerability assessment, dependency audit |
| Compliance review | Annual | Regulatory alignment check, accessibility re-certification |

All reports delivered in accessible PDF format with executive summary.
