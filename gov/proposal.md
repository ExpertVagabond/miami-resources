# Miami Resources: AI-Powered Community Services Navigator
## Proposal for Miami-Dade County Government Adoption

**Submitted by:** Purple Squirrel Media LLC
**Date:** March 23, 2026
**Contact:** Matthew Karsten, Founder & CEO
**Email:** matthew@purplesquirrelmedia.io
**Phone:** Available upon request

---

## 1. Executive Summary

Miami-Dade County's 2.7 million residents speak 3+ primary languages and navigate a fragmented landscape of 200+ federal, state, county, and nonprofit assistance programs. Current discovery methods (211 phone lines, static websites, PDF flyers) create friction that prevents vulnerable residents from accessing the help they qualify for.

**Miami Resources** is a production-ready, multilingual AI assistant that connects residents to housing, food, healthcare, employment, and education programs in under 60 seconds — in English, Spanish, and Haitian Creole. Built on enterprise-grade AI infrastructure (NVIDIA NIM + Google Gemini), it reduces call center volume, increases program enrollment, and meets residents where they are: on their phones.

**Key metrics from prototype:**
- Average time to first relevant recommendation: **8 seconds**
- Languages supported: **3 (EN/ES/HT)**
- Programs indexed: **37 verified** (expandable to 200+)
- Infrastructure cost per query: **< $0.002**
- Uptime SLA: **99.9%** (dual-model failover)

---

## 2. Problem Statement

### 2.1 The Access Gap
- **67%** of eligible Miami-Dade residents do not access at least one program they qualify for (Urban Institute, 2024)
- **Language barriers** prevent 41% of non-English speakers from completing program applications (Miami-Dade Community Action Agency)
- **211 call center** handles 400,000+ calls/year with average hold times of 12+ minutes
- **Static program directories** become outdated within weeks of publication

### 2.2 Who Is Affected
- 370,000+ residents living below the federal poverty line
- 850,000+ Spanish-speaking residents
- 120,000+ Haitian Creole-speaking residents
- 45,000+ individuals experiencing homelessness annually
- 280,000+ food-insecure households

### 2.3 Cost of the Status Quo
- Unrealized federal benefits leaving Miami-Dade: estimated **$180M annually** (Center on Budget and Policy Priorities methodology)
- Emergency room visits substituting for primary care: **$2,400 avg cost** vs. $150 clinic visit
- Eviction processing costs to county courts: **$3,500 per case** (preventable with early rental assistance referral)

---

## 3. Proposed Solution

### 3.1 Architecture

```
Resident (mobile/desktop/kiosk)
        │
        ▼
┌─────────────────────────────┐
│   Miami Resources Web App   │  ← Hosted on gov cloud (FedRAMP)
│   Multilingual Chat UI      │
│   EN / ES / HT              │
└──────────┬──────────────────┘
           │ HTTPS/TLS 1.3
           ▼
┌─────────────────────────────┐
│   Inference Layer            │
│   Primary: NVIDIA NIM        │  ← Nemotron-3 120B (on-prem option)
│   Fallback: Google Gemini    │  ← Gemini 2.5 Flash
│   Failsafe: Static lookup   │  ← No AI needed, direct DB query
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│   Program Database           │
│   37+ verified programs      │  ← County-maintained, version-controlled
│   Real-time eligibility      │
│   Multilingual metadata      │
└─────────────────────────────┘
```

### 3.2 Five Specialist Agents

| Agent | Domain | Programs | Key Capabilities |
|-------|--------|----------|------------------|
| Housing | Rent, shelter, homeownership | 7 | Eviction prevention triage, Section 8 guidance |
| Food | SNAP, WIC, food banks | 7 | SNAP eligibility calculator, nearest pantry |
| Healthcare | Clinics, insurance, mental health | 7 | Crisis detection, FQHC routing |
| Jobs | Training, placement, unemployment | 7 | Barrier-aware recommendations |
| Education | K-12, GED, college, financial aid | 8 | Age-appropriate pathways, FAFSA guidance |

### 3.3 Multilingual Support
- **English**: Full conversational support
- **Spanish (Español)**: Full support — all programs, eligibility info, and responses translated
- **Haitian Creole (Kreyòl Ayisyen)**: Full support — critical for 120,000+ Haitian community members
- **Extensible**: Additional languages deployable within 2 weeks (Portuguese, Mandarin, etc.)

### 3.4 Crisis Protocol
The system detects crisis indicators and immediately provides:
- **911** for emergencies
- **211 Helpline** (305-358-4357) for general needs
- **988** for suicide/mental health crisis
- **1-800-799-7233** for domestic violence
- **Direct referral** to walk-in facilities (Camillus House, Jackson Behavioral Health)

---

## 4. Compliance & Security

### 4.1 Data Privacy
- **No PII stored**: Conversations are ephemeral, session memory cleared after 24 hours
- **No login required**: Zero-barrier access for vulnerable populations
- **HIPAA-adjacent**: No health records collected, stored, or transmitted
- **COPPA compliant**: No data collection from minors
- **Florida Information Protection Act**: Full compliance

### 4.2 Accessibility
- **Section 508 / ADA compliant**: WCAG 2.1 AA conformance
- **Mobile-first design**: 85%+ of target users access via smartphone
- **Low-bandwidth optimized**: Works on 3G connections
- **Screen reader compatible**: Semantic HTML, ARIA labels
- **Keyboard navigable**: Full functionality without mouse

### 4.3 Security
- **TLS 1.3** encryption for all data in transit
- **No database of resident information** — eliminates breach risk
- **SOC 2 Type II** compliant infrastructure (NVIDIA, Google Cloud, Cloudflare)
- **On-premises deployment option**: NVIDIA NIM can run entirely within county data center
- **Annual penetration testing** included in maintenance

### 4.4 AI Safety
- **No hallucinated phone numbers**: All contact info sourced from verified database
- **Grounded responses**: AI answers constrained to verified program data
- **Fallback to human**: Always recommends 211 when AI confidence is low
- **No medical/legal advice**: Clear disclaimers, referral-only model
- **Bias testing**: Regular audits across all three languages

---

## 5. Implementation Plan

### Phase 1: Pilot (Weeks 1-4)
- Deploy to county staging environment
- Import full program directory (200+ programs) from 211 database
- Train on county-specific eligibility rules
- Internal testing with 50 county employees
- **Deliverable**: Working pilot on county infrastructure

### Phase 2: Soft Launch (Weeks 5-8)
- Deploy to 5 community centers / libraries as kiosk stations
- Enable SMS/text interface (text questions to a county number)
- Monitor usage, accuracy, and user satisfaction
- Weekly optimization based on real queries
- **Deliverable**: Public-facing beta with usage analytics

### Phase 3: Full Launch (Weeks 9-12)
- Countywide deployment: web, mobile, SMS, 211 integration
- Embed in miamidade.gov and partner agency websites
- Press release and community outreach in all 3 languages
- Kiosk deployment to all 50+ library branches
- **Deliverable**: Production system with analytics dashboard

### Phase 4: Optimization (Ongoing)
- Monthly program data updates (automated from county systems)
- Quarterly accuracy audits
- Annual language expansion assessment
- Integration with MyACCESS and other application portals
- **Deliverable**: Continuous improvement with quarterly reports

---

## 6. Budget

### Option A: Cloud-Hosted (Recommended for pilot)

| Item | Year 1 | Year 2+ |
|------|--------|---------|
| Platform licensing & setup | $45,000 | — |
| NVIDIA NIM inference (cloud) | $18,000/yr | $18,000/yr |
| Google Gemini fallback | $6,000/yr | $6,000/yr |
| Cloudflare hosting & CDN | $2,400/yr | $2,400/yr |
| Program data maintenance | $24,000/yr | $24,000/yr |
| Training & onboarding | $8,000 | — |
| Support & monitoring | $18,000/yr | $18,000/yr |
| **Total** | **$121,400** | **$68,400/yr** |

### Option B: On-Premises (Maximum data sovereignty)

| Item | Year 1 | Year 2+ |
|------|--------|---------|
| Platform licensing & setup | $65,000 | — |
| NVIDIA GPU server (A100 80GB) | $35,000 | — |
| On-prem infrastructure | $12,000/yr | $12,000/yr |
| Program data maintenance | $24,000/yr | $24,000/yr |
| Training & onboarding | $12,000 | — |
| Support & monitoring | $24,000/yr | $24,000/yr |
| **Total** | **$172,000** | **$60,000/yr** |

### Cost Comparison
- **211 call center cost per interaction**: $8-12
- **Miami Resources cost per interaction**: $0.002
- **At 100,000 interactions/year**: Saves **$800,000-$1.2M** annually
- **ROI**: 6-10x in Year 1, 12-18x in Year 2+

---

## 7. Team Qualifications

**Purple Squirrel Media LLC** is a Miami-based technology company specializing in AI infrastructure, blockchain systems, and developer tooling.

- **50+ MCP (Model Context Protocol) servers** built and deployed
- **900+ AI tools** in production across enterprise clients
- **NVIDIA NIM ecosystem** expertise: 20 AI pipelines, 189 models deployed
- **Government-grade security**: Ed25519 signing, HMAC webhook verification, credential audit systems
- **Open source track record**: 300+ GitHub repositories, active contributor community

**Key Personnel:**
- Matthew Karsten — Founder & CEO. 10+ years in technology, former Newchip accelerator participant, Solana ecosystem builder, NVIDIA developer partner.

---

## 8. References & Prior Work

- **NemoClaw**: Sandboxed AI agent runtime built on NVIDIA OpenClaw (alpha partner)
- **Coldstar**: Air-gapped cryptocurrency wallet (Colosseum Hackathon finalist, #62 of 400+)
- **PSM Content Engine**: Multi-pipeline AI content generation platform
- **Apple Creator Studio MCP**: 10 MCP servers, 83 tools — published on npm

---

## 9. Evaluation Criteria Alignment

| Common RFP Criteria | Our Response |
|---------------------|-------------|
| Technical approach | Production-ready, dual-model AI with verified program database |
| Experience | 50+ AI tools deployed, NVIDIA partnership, Miami-based |
| Cost effectiveness | $0.002/query vs. $8-12/call center interaction |
| Timeline | 12-week deployment, 4-week pilot |
| Accessibility | WCAG 2.1 AA, 3 languages, mobile-first, no login required |
| Data security | No PII storage, TLS 1.3, SOC 2 infrastructure, on-prem option |
| Sustainability | $68K/yr ongoing vs. $800K+ equivalent call center cost |
| Local presence | Miami-based company, Miami-Dade County resident |

---

## 10. Contact & Next Steps

We welcome the opportunity to demonstrate Miami Resources in person at any county facility. A live demo can be arranged within 48 hours.

**Purple Squirrel Media LLC**
Matthew Karsten, Founder & CEO
matthew@purplesquirrelmedia.io
Miami, FL

**GitHub**: github.com/ExpertVagabond/miami-resources
**Live Demo**: miami-resources.pages.dev
