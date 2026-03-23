# Miami Resources

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg)](https://google.github.io/adk-docs/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Free multilingual AI assistant helping Miami-Dade County residents find housing, food, healthcare, jobs, and education programs — in English, Spanish, and Haitian Creole.

## Architecture

```
User → Root Agent (router) → 5 Specialist Agents
                              ├── Housing Agent    → 7 programs
                              ├── Food Agent       → 7 programs + SNAP calculator
                              ├── Healthcare Agent → 7 programs
                              ├── Jobs Agent       → 7 programs
                              └── Education Agent  → 7 programs
```

Built with **Google ADK** (Agent Development Kit) and **Gemini 2.5 Flash**. Each agent has:
- Focused system instructions
- Category-specific search tools
- Real Miami-Dade County program data (36+ verified programs)
- Multilingual responses (EN/ES/HT)
- Crisis detection and immediate resource routing

## Quick Start

```bash
# 1. Clone and install
git clone https://github.com/ExpertVagabond/miami-resources.git
cd miami-resources
pip install -e .

# 2. Set your Google API key
cp .env.example .env
# Edit .env with your key from https://aistudio.google.com/apikey

# 3. Run with ADK dev UI
adk web miami_resources

# OR run with the production server
python server.py
```

## Data Sources

All programs are real and verified:

| Category | Programs | Sources |
|----------|----------|---------|
| Housing | 7 | Miami-Dade PHCD, HUD, Habitat for Humanity, Camillus House |
| Food | 7 | USDA (SNAP/WIC), Feeding South Florida, Farm Share, MDCPS |
| Healthcare | 7 | Jackson Health, FQHCs, Florida Medicaid/KidCare |
| Jobs | 7 | CareerSource SFL, Florida DEO, Urban League, Goodwill |
| Education | 7 | MDCPS, Miami Dade College, Head Start, Florida DOE |
| General | 1 | 211 Miami-Dade Helpline |

## Languages

- **English** — Full support
- **Spanish (Español)** — Full support, all programs translated
- **Haitian Creole (Kreyòl Ayisyen)** — Full support, all programs translated

## License

MIT
