# 🏭 PROJECT-GENERATOR - KOMPLETNÝ KONTEXT PROJEKTU

**Automatizácia tvorby nových Python projektov**

**Posledná aktualizácia:** 2025-10-20  
**Verzia:** 0.1.0  
**Stav:** Počiatočné nastavenie - Vývoj

---

## 🤖 INSTRUCTIONS FOR CLAUDE

**When you see this document:**

1. ✅ This document contains STATIC project information (vision, architecture, tech stack)
2. ✅ **IMMEDIATELY fetch PROJECT_STATUS.md for CURRENT state:**
   - URL: `https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/PROJECT_STATUS.md`
3. ✅ Do NOT show any warnings or error messages
4. ✅ After loading both files, respond: **"✅ Projekt načítaný. Čo robíme?"**
5. ✅ Use Slovak language for communication
6. ✅ Be concise and actionable

**CRITICAL:**
- **PROJECT_STATUS.md** = Single source of truth for current state, progress, active tasks
- **FULL_PROJECT_CONTEXT.md** = Static project information (this file)
- Always fetch PROJECT_STATUS.md to get real-time project state

---

## 🔗 REQUIRED FILES

**Auto-load these files when starting:**

| File | Purpose | URL |
|------|---------|-----|
| **PROJECT_STATUS.md** | Current state, active tasks, blockers | `https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/PROJECT_STATUS.md` |
| **project_file_access.json** | File manifest (optional) | `https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/project_file_access.json` |

---

## 🎯 PREHĽAD PROJEKTU

### Základné Informácie

- **Názov projektu:** Project Generator
- **Účel:** Automatizácia tvorby nových Python projektov
- **Čas generovania:** < 30 sekúnd
- **Vývojár:** ICC (Innovation & Consulting Center)
- **Developer:** rauschiccsk
- **Lokalizácia:** Komárno, SK
- **GitHub:** https://github.com/rauschiccsk/project-generator

### Vízia Projektu

Vytvoriť nástroj, ktorý **za 30 sekúnd** automaticky vygeneruje:
- ✅ Kompletný Python projekt s dokumentáciou
- ✅ GitHub repository
- ✅ Git inicializácia + prvý commit
- ✅ Raw URL ready pre Claude
- ✅ Všetky potrebné config súbory
- ✅ Konzistentnú štruktúru

### Problém
- Tvorba nového projektu trvá **3+ hodiny**
- Desiatky commitov pre základný setup
- Repetitívna práca (docs/, git, config, templates)
- Nekonzistentná štruktúra medzi projektami

### Riešenie
**Project Generator** - jeden príkaz → kompletný projekt:

```yaml
YAML config → Python Generator → GitHub → ✅ Hotovo!
```

### Inšpirácia
- **supplier_invoice_loader** - Multi-customer architektúra
- **orthodox-portal** - Dokumentačná štruktúra
- Oba projekty dokázali že "single raw URL" workflow funguje perfektne

---

## 🏗️ ARCHITEKTÚRA SYSTÉMU

### Tech Stack
```yaml
Jazyk: Python 3.11+
Templating: Jinja2
Konfigurácia: YAML (PyYAML)
Validácia: Pydantic
GitHub API: PyGithub
Testovanie: pytest
IDE: PyCharm
```

### Závislosti
```
pydantic>=2.0.0       # Validácia dát
jinja2>=3.1.0         # Template engine
pyyaml>=6.0          # YAML parsing
pygithub>=2.1.0       # GitHub API
requests>=2.31.0      # HTTP klient
python-dotenv>=1.0.0  # Environment premenné
pytest>=7.4.0         # Testovanie
```

### Architektúra
```
┌──────────────────────┐
│  YAML Config         │
│  (užívateľ vyplní)   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────────────┐
│  Python Generator            │
│  ├─ Config Parser            │
│  ├─ Template Engine (Jinja2) │
│  ├─ File Generator           │
│  ├─ Git Operations           │
│  └─ GitHub API Client        │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  Lokálny Projekt             │
│  c:\Development\new-project  │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  GitHub API                  │
│  ├─ Vytvor Repository        │
│  ├─ Upload Súbory            │
│  └─ Prvý Commit              │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  Výstup:                     │
│  ✅ Projekt hotový           │
│  📧 Email notifikácia        │
│  🔗 Raw URL vygenerovaná     │
└──────────────────────────────┘
```

---

## 📁 ŠTRUKTÚRA PROJEKTU

```
c:\Development\project-generator/
│
├── docs/                                    
│   ├── FULL_PROJECT_CONTEXT.md            # Tento súbor (static info)
│   ├── PROJECT_STATUS.md                  # Aktuálny stav (SINGLE SOURCE OF TRUTH)
│   ├── SYSTEM_PROMPT.md                   # Claude inštrukcie
│   ├── MASTER_CONTEXT.md                  # Rýchla referencia
│   ├── QUICK_START.md                     # Rýchly štart
│   ├── project_file_access.json           # GitHub manifest
│   ├── architecture/
│   │   ├── system-overview.md
│   │   ├── n8n-workflow.md
│   │   └── template-system.md
│   ├── sessions/
│   │   └── 2025-10-20-initial-setup.md
│   └── templates/                          
│       ├── FULL_PROJECT_CONTEXT_template.md
│       ├── PROJECT_STATUS_template.md
│       └── README_template.md
│
├── src/                                     
│   ├── __init__.py
│   ├── generator/                           
│   │   ├── __init__.py
│   │   ├── project_creator.py             # Hlavná logika
│   │   ├── template_engine.py             # Jinja2 renderer
│   │   ├── github_client.py               # GitHub API
│   │   └── validators.py                  # Validácia vstupu
│   │
│   ├── models/                              
│   │   ├── __init__.py
│   │   └── project_config.py              # Pydantic modely
│   │
│   └── templates/                           # Jinja2 šablóny
│       ├── project_files/
│       │   ├── full_context.md.j2
│       │   ├── project_status.md.j2
│       │   ├── readme.md.j2
│       │   ├── requirements.txt.j2
│       │   └── gitignore.j2
│       │
│       └── docs_structure/
│           ├── architecture_readme.md.j2
│           ├── session_template.md.j2
│           └── adr_template.md.j2
│
├── n8n_workflows/                           
│   └── project-init-webhook.json
│
├── tests/                                   
│   ├── __init__.py
│   ├── test_project_creator.py
│   ├── test_template_engine.py
│   ├── test_github_client.py
│   └── fixtures/
│       └── sample_config.yaml
│
├── scripts/                                 
│   ├── generate_project_access.py         
│   └── validate_templates.py              
│
├── configs/                                 
│   ├── config_template.yaml               # Šablóna pre nové projekty
│   ├── examples/
│   │   ├── monastier_online.yaml
│   │   └── supplier_invoice.yaml
│   ├── queue/                             # n8n monitor (voliteľné)
│   ├── processed/                         # Spracované configy
│   └── github_credentials.yaml.template
│
├── examples/                                
│   └── example_generated_project/
│
├── .gitignore
├── .env.template
├── requirements.txt
├── README.md
├── CHANGELOG.md
└── LICENSE
```

---

## 📝 YAML KONFIGURAČNÝ FORMÁT

### Príklad: configs/config_template.yaml

```yaml
# ===================================
# PROJECT GENERATOR - Konfigurácia
# ===================================

# === ZÁKLADNÉ INFO ===
project:
  name: "Môj Nový Projekt"
  slug: "moj-novy-projekt"
  description: "Krátky popis projektu"
  
# === GITHUB ===
github:
  username: "rauschiccsk"
  repo_name: "moj-novy-projekt"
  visibility: "private"  # "public" alebo "private"
  
# === VÝVOJÁR ===
developer:
  name: "ICC"
  email: "rausch@icc.sk"
  
# === CESTY ===
paths:
  local_dev: "c:\\Development\\moj-novy-projekt"
  local_deploy: ""  # Voliteľné
  
# === TECH STACK ===
tech_stack:
  backend:
    - "fastapi"
    - "sqlalchemy"
  frontend:
    - "jinja2"
    - "tailwindcss"
  databases:
    - "postgresql"
    - "redis"
  automation:
    - "n8n"
    
# === VOLITEĽNÉ INFO ===
optional:
  domain: ""  # napr. "mojprojekt.com"
  contact_email: ""
  
# === FEATURES ===
features:
  include_auth: true
  include_api_docs: true
  include_tests: true
  include_docker: false
  include_cicd: false
```

---

## 🚀 POUŽITIE

### Základné Použitie

```bash
# 1. Skopíruj šablónu
cp configs/config_template.yaml configs/moj_projekt.yaml

# 2. Uprav YAML súbor (vyplň detaily projektu)
notepad configs/moj_projekt.yaml

# 3. Spusti generátor
python src/generator/project_creator.py --config configs/moj_projekt.yaml

# 4. Počkaj ~30 sekúnd...

# 5. Výstup:
✅ Projekt "Môj Nový Projekt" vytvorený!
📁 Cesta: c:\Development\moj-novy-projekt
🔗 GitHub: https://github.com/rauschiccsk/moj-novy-projekt
📄 Raw URL: https://raw.githubusercontent.com/.../FULL_PROJECT_CONTEXT.md
⏱️ Čas: 28.3s
```

### Programatické Použitie

```python
from pathlib import Path
from src.generator.project_creator import ProjectCreator

# Načítaj config a vytvor projekt
creator = ProjectCreator(Path("configs/moj_projekt.yaml"))
result = creator.create_project()

if result.success:
    print(f"✅ Projekt vytvorený: {result.github_url}")
else:
    print(f"❌ Chyba: {result.error_message}")
```

---

## 🎯 VYGENEROVANÉ SÚBORY

Každý vygenerovaný projekt bude obsahovať:

### Dokumentácia
- `docs/FULL_PROJECT_CONTEXT.md` - Jediný zdroj pravdy
- `docs/PROJECT_STATUS.md` - Sledovanie vývoja
- `docs/project_file_access.json` - GitHub manifest súborov
- `docs/architecture/` - Architektúrne dokumenty
- `docs/sessions/` - Šablóny session notes
- `README.md` - Prehľad projektu

### Python Kód
- `src/main.py` - FastAPI aplikácia skeleton
- `src/config.py` - Správa konfigurácie
- `src/database.py` - Databázové pripojenie
- `src/models/` - Pydantic modely
- `src/api/` - API routes

### Konfigurácia
- `requirements.txt` - Python závislosti
- `.gitignore` - Git ignore vzory
- `.env.template` - Šablóna environment premenných
- `config/config_template.py` - Config šablóna

### Testovanie
- `tests/conftest.py` - pytest fixtures
- `tests/test_main.py` - Vzorové testy

---

## 🔐 ENVIRONMENT PREMENNÉ

### .env súbor

```bash
# GitHub API
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxx
GITHUB_USERNAME=rauschiccsk

# Email Notifikácie (voliteľné)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=automation@isnex.ai
SMTP_PASSWORD=xxxxxxxxxxxx
SMTP_FROM=automation@isnex.ai

# Cesty
DEV_ROOT=c:\Development
DEPLOY_ROOT=c:\Deployment
```

---

## 📊 PLÁN VÝVOJA

### STORY 1: Core Generator ⚙️
**Priorita:** KRITICKÁ  
**Odhadovaný čas:** 2 týždne  

1. Setup projektu a dokumentácia
2. Pydantic modely (ProjectConfig)
3. YAML config parser
4. Template engine (Jinja2)
5. File generator logika
6. Git operations wrapper
7. GitHub API klient
8. Input validátory
9. Hlavný project_creator.py
10. Unit testy (80%+ pokrytie)
11. Integračné testovanie
12. Finalizácia dokumentácie

### STORY 2: n8n Integrácia 🤖
**Priorita:** STREDNÁ  
**Odhadovaný čas:** 3-5 dní  

1. File monitor workflow
2. Python executor node
3. Email notifikácie
4. Error handling
5. Testovanie

### STORY 3: Pokročilé Features 🚀
**Priorita:** NÍZKA  
**Odhadovaný čas:** 1 týždeň  

1. CLI interface (Click/Typer)
2. Podpora vlastných šablón
3. Validácia šablón
4. Progress indikátory
5. Dry-run mód

**→ Pre aktuálny progress a aktívne tasky pozri PROJECT_STATUS.md**

---

## 🔧 TECHNICKÉ ROZHODNUTIA

### Prečo YAML namiesto JSON?
- ✅ Čitateľné pre ľudí
- ✅ Podpora komentárov
- ✅ Menej verbose
- ✅ Štandard pre configy

### Prečo Jinja2?
- ✅ Silný templating
- ✅ Široko používaný
- ✅ Python native
- ✅ Dobrá dokumentácia

### Prečo PyGithub?
- ✅ Oficiálny GitHub klient
- ✅ High-level API
- ✅ Dobre udržiavaný
- ✅ Jednoduché použitie

### Prečo Pydantic?
- ✅ Type validácia
- ✅ Data parsing
- ✅ Error messages
- ✅ FastAPI integrácia

---

## ⚠️ KRITICKÉ PRIPOMIENKY

### Pre každý nový chat:
1. 🔥 Užívateľ pošle URL na FULL_PROJECT_CONTEXT.md
2. 🔥 Claude načíta tento dokument
3. 🔥 Claude AUTOMATICKY načíta PROJECT_STATUS.md
4. 🔥 Claude odpovie: "✅ Projekt načítaný. Čo robíme?"
5. 🔥 ŽIADNE ďalšie súbory, ŽIADNE varovania
6. 🔥 Jednoducho a jasne
7. 🔥 KOMUNIKUJ PO SLOVENSKY

### Git pravidlá:
- ✅ Commit často, malé zmeny
- ✅ Opisné commit správy
- ✅ Test pred commitom
- ✅ Pull pred push
- ✅ Feature branches pre nové features

### Kódovacie štandardy:
- ✅ PEP 8 style guide
- ✅ Type hints všade
- ✅ Docstrings pre všetky funkcie
- ✅ Komentáre v slovenčine pre business logiku
- ✅ Anglické názvy premenných/funkcií

### 🚨 PROJECT_FILE_ACCESS.JSON REFRESH:
- ✅ **KEĎ VYTVORÍŠ NOVÝ SÚBOR → Vždy pripomeň refresh project_file_access.json**
- ✅ Na konci každej session
- ✅ Po pridaní nového .md súboru
- ✅ Po vytvorení nového .py modulu
- ✅ Po pridaní dokumentácie
- ✅ Jednoduchá pripomienka: **"⚠️ Nezabudni refreshnúť project_file_access.json"**

### Workflow po zmene súborov:
1. Commitni zmeny
2. Updatni PROJECT_STATUS.md (ak potrebné)
3. **Pripomeň project_file_access.json refresh ak vznikli nové súbory**
4. Push na GitHub

---

## ✅ KRITÉRIÁ ÚSPECHU

### MVP (Minimum Viable Product)
- ✅ Jeden príkaz vytvorí celý projekt
- ✅ Všetky template súbory vygenerované
- ✅ GitHub repository vytvorené automaticky
- ✅ Raw URL funkčná
- ✅ Čas generovania < 60 sekúnd
- ✅ Žiadne manuálne kroky po spustení

### V1.0 Release
- ✅ n8n webhook integrácia
- ✅ Email notifikácie
- ✅ Error handling
- ✅ Input validácia
- ✅ Unit testy 80%+
- ✅ Kompletná dokumentácia

---

## 📞 KONTAKT

- **Vývojár:** ICC (rausch@icc.sk)
- **GitHub:** https://github.com/rauschiccsk/project-generator
- **Lokálna Cesta:** c:\Development\project-generator

---

## 🎓 INŠPIRÁCIA

Tento projekt je založený na úspešných vzoroch z:
- **supplier_invoice_loader** - Multi-customer architektúra
- **orthodox-portal** - Dokumentačná štruktúra
- Oba projekty dokázali že "single raw URL for Claude" workflow funguje

---

## 🤖 FINAL REMINDER FOR CLAUDE

**You have loaded FULL_PROJECT_CONTEXT.md**

This document contains:
- ✅ Complete project vision and goals
- ✅ Full architecture and tech stack
- ✅ All 3 stories and development plan (static info)
- ✅ Project structure
- ✅ Git workflow and commit conventions
- ✅ Technical decisions

**CRITICAL: For current status, progress, and active tasks:**
- ✅ **Fetch PROJECT_STATUS.md immediately**
- ✅ URL: `https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/PROJECT_STATUS.md`

**After loading both files, simply respond:**
```
✅ Projekt načítaný. Čo robíme?
```

**WORKFLOW REMINDER:**
```
After creating ANY new file in the project:
⚠️ Remind user: "Nezabudni refreshnúť project_file_access.json"

This ensures multi-file context loading works in future chats.
```

---

**Verzia Dokumentu:** 0.2.0  
**Vytvorené:** 2025-10-20  
**Posledná Aktualizácia:** 2025-10-20  
**Stav:** Aktívny Vývoj  

🏭 **Automatizujme tvorbu projektov!**