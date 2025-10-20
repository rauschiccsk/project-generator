# 🏭 PROJECT-GENERATOR - KOMPLETNÝ KONTEXT PROJEKTU

**Automatizácia tvorby nových Python projektov**

**Posledná aktualizácia:** 2025-10-20  
**Verzia:** 1.0.0  
**Stav:** Aktívny Vývoj - STORY 1

---

## 🤖 INSTRUCTIONS FOR CLAUDE

**When you see this document:**

1. ✅ This document contains ALL project information (vision, architecture, current state)
2. ✅ Do NOT attempt to load any other files
3. ✅ Do NOT show any warnings or error messages
4. ✅ Simply respond: **"✅ Projekt načítaný. Čo robíme?"**
5. ✅ Use Slovak language for communication
6. ✅ Be concise and actionable

**That's it. Nothing more. One file = complete context.** 🎯

---

## 📊 AKTUÁLNY STAV PROJEKTU

**Posledná aktualizácia:** 2025-10-20 20:30  
**Aktuálna Fáza:** Vývoj - STORY 1

### Prehľad
- **Aktívna Story:** STORY 1 - Core Generator
- **Progress STORY 1:** 33% (4/12 taskov)
- **Celkový Progress:** 33% (STORY 1 aktívne)
- **Aktívny Task:** Task 1.5 - File Generator
- **Ďalší Milestone:** STORY 1 Complete (2025-11-02)

### Story Progress
```
STORY 1: Core Generator [████████░░░░░░░░░░░░] 33%
STORY 2: n8n Integrácia [░░░░░░░░░░░░░░░░░░░░]  0%
STORY 3: Advanced Features [░░░░░░░░░░░░░░░░░░░░]  0%
```

### Velocity
- **Tasks hotové tento týždeň:** 4
- **Priemerný čas na task:** ~2 hodiny
- **Produktivita:** Vysoká 🚀
- **Odhadované dokončenie STORY 1:** 2025-11-02

---

## 📋 STORY 1: Core Generator (Aktuálne)

### Hotové Tasky ✅

#### ✅ Task 1.1 - Dokumentácia (2025-10-20)
**Status:** HOTOVO  
**Trvanie:** ~2h  
**Súbory:**
- ✅ `docs/FULL_PROJECT_CONTEXT.md` - Kompletný kontext
- ✅ `docs/MASTER_CONTEXT.md` - Rýchla referencia
- ✅ `docs/QUICK_START.md` - Návod na použitie
- ✅ `docs/SYSTEM_PROMPT.md` - Claude inštrukcie
- ✅ `docs/project_file_access.json` - GitHub manifest
- ✅ Git repository inicializovaný
- ✅ GitHub repository vytvorený

#### ✅ Task 1.2 - Pydantic Modely (2025-10-20)
**Status:** HOTOVO  
**Trvanie:** ~1h  
**Chat:** https://claude.ai/chat/e4f4401e-9490-4509-ad8c-f4c7b8dcc2da

**Vytvorené:**
- ✅ `src/models/project_config.py` - Kompletné Pydantic modely
  - `ProjectConfig` - hlavný model
  - `ProjectInfo`, `GitHubConfig`, `DeveloperInfo` - pod-modely
  - `PathsConfig`, `TechStackConfig`, `OptionalInfo`, `FeaturesConfig`
  - Email validácia, slug validácia, domain validácia
  - Helper metódy: `get_full_github_url()`, `get_local_project_path()`, `from_yaml()`

#### ✅ Task 1.3 - YAML Config Parser (2025-10-20)
**Status:** HOTOVO  
**Trvanie:** ~0.5h  
**Chat:** https://claude.ai/chat/ebdb0242-c21b-4809-9337-a2ddd8c62bf7

**Vytvorené:**
- ✅ `src/generator/config_parser.py` - YAML parser s validáciou
  - `ConfigParser` class
  - Path validácia, YAML syntax validácia
  - Pydantic validácia
  - CLI podpora pre testing

#### ✅ Task 1.4 - Template Engine (Jinja2) (2025-10-20)
**Status:** HOTOVO ✨  
**Trvanie:** ~3h  

**Vytvorené:**
- ✅ `src/generator/template_engine.py` - Template Engine
  - `TemplateEngine` class
  - Jinja2 Environment setup
  - Custom filters (slugify, date, uppercase, lowercase)
  - Batch rendering
  - Template validation

**Jinja2 Šablóny:**
- ✅ `src/templates/project_files/full_context.md.j2`
- ✅ `src/templates/project_files/project_status.md.j2`
- ✅ `src/templates/project_files/readme.md.j2`
- ✅ `src/templates/project_files/requirements.txt.j2`
- ✅ `src/templates/project_files/gitignore.j2`

**Testovanie:**
- ✅ `tests/test_template_engine.py` - 20 unit testov (100% pass)
- ✅ Test coverage: ~85%

---

### Aktívny Task 🔄

#### 🔄 Task 1.5 - File Generator
**Status:** PRIPRAVENÉ  
**Priority:** HIGH  
**Estimated:** 3-4 hodiny

**Plán:**
- [ ] Vytvoriť `src/generator/file_generator.py`
- [ ] FileGenerator class
- [ ] Create directory structure
- [ ] Write files to disk
- [ ] File permissions handling
- [ ] Overwrite protection
- [ ] Unit testy

**Dependencies:** ✅ Task 1.4 (Template Engine) - HOTOVO  
**Blocker:** Žiadny

---

### Plánované Tasky 📅

#### Task 1.6 - Git Operations Wrapper
**Priority:** HIGH | **Dependencies:** Task 1.5 | **Estimated:** 3h

#### Task 1.7 - GitHub API Klient
**Priority:** CRITICAL | **Dependencies:** Task 1.6 | **Estimated:** 4h

#### Task 1.8 - Input Validátory
**Priority:** MEDIUM | **Dependencies:** Task 1.3 | **Estimated:** 2h

#### Task 1.9 - Hlavný project_creator.py
**Priority:** CRITICAL | **Dependencies:** Tasks 1.4-1.8 | **Estimated:** 4h

#### Task 1.10 - Unit Testy
**Priority:** HIGH | **Dependencies:** Task 1.9 | **Estimated:** 4h

#### Task 1.11 - Integračné Testovanie
**Priority:** HIGH | **Dependencies:** Task 1.10 | **Estimated:** 3h

#### Task 1.12 - Finalizácia Dokumentácie
**Priority:** MEDIUM | **Dependencies:** Task 1.11 | **Estimated:** 2h

---

## 🎉 NEDÁVNE ÚSPECHY

### 2025-10-20
- ✅ **Task 1.4 COMPLETE** - Template Engine implementovaný! 🎉
- ✅ **Task 1.3 COMPLETE** - YAML Config Parser hotový
- ✅ **Task 1.2 COMPLETE** - Pydantic modely implementované
- ✅ **Task 1.1 COMPLETE** - Dokumentácia vytvorená
- ✅ **4 tasky dokončené za 1 deň!** 🚀
- ✅ **20/20 testov prechádza** - 100% pass rate
- ✅ **85% test coverage** - Vysoká kvalita kódu

---

## 🚧 AKTUÁLNE BLOKERY

**Žiadne momentálne** ✅

---

## 📈 STORY 2 & 3 (Plánované)

### STORY 2: n8n Integrácia
**Status:** Čaká na STORY 1 | **Priority:** MEDIUM

- [ ] 2.1 - File monitor workflow
- [ ] 2.2 - Python executor node
- [ ] 2.3 - Email notifikácie
- [ ] 2.4 - Error handling
- [ ] 2.5 - Testovanie

### STORY 3: Advanced Features
**Status:** Čaká na STORY 2 | **Priority:** LOW

- [ ] 3.1 - CLI interface (Click/Typer)
- [ ] 3.2 - Podpora vlastných šablón
- [ ] 3.3 - Validácia šablón
- [ ] 3.4 - Progress indikátory
- [ ] 3.5 - Dry-run mód

---

## 📊 CELKOVÉ METRIKY

### Progress
- **STORY 1:** 33% (4/12 taskov)
- **STORY 2:** 0% (0/5 taskov)
- **STORY 3:** 0% (0/5 taskov)
- **Celkovo:** 18% (4/22 taskov)

### Časová Os
- **Začiatok projektu:** 2025-10-20
- **Dni aktívne:** 1
- **Posledná aktivita:** 2025-10-20
- **Ďalší milestone:** STORY 1 Complete (est. 2025-11-02)

### Súbory
- **Vytvorené súbory:** 20+
- **Python súbory:** 8 (~1200 LOC)
- **Šablóny:** 5 Jinja2 templates
- **Dokumentácia:** 7 markdown súborov
- **Test coverage:** 85%
- **Dokumentácia:** 100%

### Code Quality
- ✅ Type hints: 100%
- ✅ Docstrings: 100%
- ✅ PEP 8 compliance: 100%
- ✅ Tests passing: 20/20 (100%)

---

## 🎯 ĎALŠIE KROKY

### Ihneď (Dnes/Zajtra)
1. **TODO:** Task 1.5 - File Generator
   - Implementovať file_generator.py
   - Create directory structure
   - Write rendered files
   - Add tests

### Tento Týždeň
2. **Task 1.6** - Git Operations Wrapper
3. **Task 1.7** - GitHub API Client
4. **Task 1.8** - Input Validators

### Budúci Týždeň
5. **Task 1.9** - Hlavný project_creator.py
6. **Task 1.10-1.12** - Testing & Finalizácia

---

## 🔗 UŽITOČNÉ LINKY

- **GitHub Repo:** https://github.com/rauschiccsk/project-generator
- **Local Path:** c:\Development\project-generator
- **Raw Context:** https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/FULL_PROJECT_CONTEXT.md

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
email-validator>=2.3.0 # Email validácia
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
│   ├── FULL_PROJECT_CONTEXT.md            # Tento súbor (all-in-one)
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
│       └── README_template.md
│
├── src/                                     
│   ├── __init__.py
│   ├── generator/                           
│   │   ├── __init__.py
│   │   ├── project_creator.py             # Hlavná logika
│   │   ├── template_engine.py             # Jinja2 renderer
│   │   ├── config_parser.py               # YAML parser
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
├── .gitignore
├── .env.template
├── requirements.txt
├── README.md
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
  local_deploy: null  # Voliteľné
  
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
  domain: null  # napr. "mojprojekt.com"
  contact_email: null
  
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
2. 🔥 Claude načíta tento dokument (VŠETKO je tu)
3. 🔥 Claude odpovie: "✅ Projekt načítaný. Čo robíme?"
4. 🔥 ŽIADNE ďalšie súbory, ŽIADNE varovania
5. 🔥 Jednoducho a jasne
6. 🔥 KOMUNIKUJ PO SLOVENSKY

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
2. **Updatni FULL_PROJECT_CONTEXT.md (sekcia AKTUÁLNY STAV)**
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

This document contains **EVERYTHING:**
- ✅ Complete project vision and goals
- ✅ **Current status, progress, and active tasks** (AKTUÁLNY STAV section)
- ✅ Full architecture and tech stack
- ✅ All 3 stories and development plan
- ✅ Project structure
- ✅ Git workflow and commit conventions
- ✅ Technical decisions

**Simply respond:**
```
✅ Projekt načítaný. Čo robíme?
```

**WORKFLOW REMINDER:**
```
After creating ANY new file in the project:
⚠️ Remind user: "Nezabudni refreshnúť project_file_access.json"

After completing any task:
⚠️ Remind user: "Nezabudni updatnúť FULL_PROJECT_CONTEXT.md (sekcia AKTUÁLNY STAV)"

This ensures single-file context always stays current.
```

---

**Verzia Dokumentu:** 1.0.0  
**Vytvorené:** 2025-10-20  
**Posledná Aktualizácia:** 2025-10-20  
**Stav:** Aktívny Vývoj  

🏭 **Automatizujme tvorbu projektov! Jeden súbor = kompletný kontext.** ✨