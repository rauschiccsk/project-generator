# 🏭 PROJECT-GENERATOR - FULL PROJECT CONTEXT

**Automatizácia tvorby nových Python projektov**

**Last Updated:** 2025-10-20  
**Version:** 0.1.0  
**Status:** Initial Setup Phase

---

## 🤖 INSTRUCTIONS FOR CLAUDE

**When you see this document at the start of a conversation:**

### 1. IMMEDIATELY Fetch These URLs (in this order):

Use the `web_fetch` tool to load these files RIGHT NOW:

```
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/SYSTEM_PROMPT.md
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/MASTER_CONTEXT.md
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/PROJECT_STATUS.md
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/project_file_access.json
```

**CRITICAL:** 
- Use `web_fetch` tool with each URL individually
- Do NOT ask user for URLs - fetch them immediately and automatically
- These files MUST be loaded before responding to user

### 2. Language & Communication

**IMPORTANT:** Communicate with the user in **SLOVAK language** (slovenčina).
- All responses, explanations, and questions should be in Slovak
- Code comments for business logic should be in Slovak  
- Technical terms can remain in English where appropriate
- Variable/function names in English (PEP 8)
- User's name: **ICC**

### 3. After Successfully Loading All Files

Respond with:
```
✅ Projekt načítaný!
📊 Status: [current phase from PROJECT_STATUS.md]
🎯 Progress: [percentage from PROJECT_STATUS.md]
⚙️ Aktuálny task: [current task from PROJECT_STATUS.md]

Čo robíme?
```

### 4. ALWAYS Check Status Before Work

Before starting ANY work:
- 🔥 **CHECK** PROJECT_STATUS.md for current story/task
- 🔥 **VERIFY** what was completed in last session
- 🔥 **ASK** user which task to work on
- 🔥 **NEVER** assume project structure without checking files

### 5. Git Workflow (After Every Change)

```bash
git add .
git commit -m "descriptive message in English"
git push origin main
```

**Update documentation after EVERY session:**
- Update PROJECT_STATUS.md with progress
- Create session note in docs/sessions/YYYY-MM-DD-description.md
- Update project_file_access.json if files added/removed
- Commit and push all changes

**GitHub Repository:**
```
URL: https://github.com/rauschiccsk/project-generator
Branch: main
Local path: c:\Development\project-generator
```

---

## 🎯 PROJECT OVERVIEW

### Problém
- Tvorba nového projektu trvá **3+ hodiny**
- Desiatky commitov pre základný setup
- Repetitívna práca (docs/, git, config, templates)
- Nekonzistentná štruktúra medzi projektami

### Riešenie
**Project Generator** - automatizovaný nástroj, ktorý za **30 sekúnd** vytvorí:
- ✅ Kompletný Python projekt s dokumentáciou
- ✅ GitHub repository
- ✅ Git inicializácia + prvý commit
- ✅ Raw URL ready pre Claude
- ✅ Všetky potrebné config súbory

### Workflow
```
YAML config → Python Generator → GitHub repo → Raw URL → ✅ Ready!
```

---

## 🏗️ ARCHITEKTÚRA

### High-Level Design

```
┌──────────────────────┐
│  YAML Config File    │
│  (user fills in)     │
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
│  Local Project Created       │
│  c:\Development\new-project  │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  GitHub API                  │
│  ├─ Create Repository        │
│  ├─ Upload Files             │
│  └─ Initial Commit           │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  Output:                     │
│  ✅ Project ready            │
│  📧 Email notification       │
│  🔗 Raw URL generated        │
└──────────────────────────────┘
```

### Optional: n8n Automation

```
┌──────────────────┐
│  configs/queue/  │
│  (YAML dropped)  │
└────────┬─────────┘
         │
         ▼
┌──────────────────────┐
│  n8n Workflow        │
│  ├─ File Monitor     │
│  ├─ Execute Python   │
│  └─ Email Result     │
└──────────────────────┘
```

---

## 💾 TECH STACK

### Core Technologies
```yaml
Language: Python 3.11+
Templating: Jinja2
Config: YAML (PyYAML)
Validation: Pydantic
GitHub API: requests / PyGithub
Testing: pytest
IDE: PyCharm
```

### Dependencies
```
pydantic>=2.0.0       # Data validation
jinja2>=3.1.0         # Template engine
pyyaml>=6.0          # YAML parsing
pygithub>=2.1.0       # GitHub API client
requests>=2.31.0      # HTTP client
python-dotenv>=1.0.0  # Environment variables
pytest>=7.4.0         # Testing
```

### Optional (n8n integration)
```
- n8n server (already exists)
- Email SMTP (Gmail)
```

---

## 📁 PROJECT STRUCTURE

```
c:\Development\project-generator/
│
├── docs/                                    
│   ├── FULL_PROJECT_CONTEXT.md            # This file
│   ├── SYSTEM_PROMPT.md                   # Claude instructions
│   ├── MASTER_CONTEXT.md                  # Quick reference
│   ├── QUICK_START.md                     # Getting started
│   ├── PROJECT_STATUS.md                  # Development tracking
│   ├── project_file_access.json           # GitHub files manifest
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
│   │   ├── project_creator.py             # Main logic
│   │   ├── template_engine.py             # Jinja2 renderer
│   │   ├── github_client.py               # GitHub API
│   │   └── validators.py                  # Input validation
│   │
│   ├── models/                              
│   │   ├── __init__.py
│   │   └── project_config.py              # Pydantic models
│   │
│   └── templates/                           # Jinja2 templates
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
│   ├── config_template.yaml               # Template for new projects
│   ├── examples/
│   │   ├── monastier_online.yaml
│   │   └── supplier_invoice.yaml
│   ├── queue/                             # n8n monitor (optional)
│   ├── processed/                         # Processed configs
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

## 📝 YAML CONFIG FORMAT

### Example: configs/config_template.yaml

```yaml
# ===================================
# PROJECT GENERATOR - Configuration
# ===================================

# === BASIC INFO ===
project:
  name: "My New Project"
  slug: "my-new-project"
  description: "Brief description of the project"
  
# === GITHUB ===
github:
  username: "rauschiccsk"
  repo_name: "my-new-project"
  visibility: "private"  # "public" or "private"
  
# === DEVELOPER ===
developer:
  name: "ICC"
  email: "rausch@icc.sk"
  
# === PATHS ===
paths:
  local_dev: "c:\\Development\\my-new-project"
  local_deploy: ""  # Optional
  
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
    
# === OPTIONAL INFO ===
optional:
  domain: ""  # e.g., "myproject.com"
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

## 🚀 USAGE

### Basic Usage

```bash
# 1. Copy template
cp configs/config_template.yaml configs/my_project.yaml

# 2. Edit YAML file (fill in your project details)
notepad configs/my_project.yaml

# 3. Run generator
python src/generator/project_creator.py --config configs/my_project.yaml

# 4. Wait ~30 seconds...

# 5. Output:
✅ Projekt "My New Project" vytvorený!
📁 Path: c:\Development\my-new-project
🔗 GitHub: https://github.com/rauschiccsk/my-new-project
📄 Raw URL: https://raw.githubusercontent.com/.../FULL_PROJECT_CONTEXT.md
⏱️ Time: 28.3s
```

### Programmatic Usage

```python
from pathlib import Path
from src.generator.project_creator import ProjectCreator

# Load config and create project
creator = ProjectCreator(Path("configs/my_project.yaml"))
result = creator.create_project()

if result.success:
    print(f"✅ Project created: {result.github_url}")
else:
    print(f"❌ Error: {result.error_message}")
```

---

## 🎯 GENERATED FILES

Every generated project will contain:

### Documentation
- `docs/FULL_PROJECT_CONTEXT.md` - Single source of truth
- `docs/PROJECT_STATUS.md` - Development tracking
- `docs/project_file_access.json` - GitHub files manifest
- `docs/architecture/` - Architecture docs
- `docs/sessions/` - Session notes template
- `README.md` - Project overview

### Python Code
- `src/main.py` - FastAPI application skeleton
- `src/config.py` - Configuration management
- `src/database.py` - Database connection
- `src/models/` - Pydantic models
- `src/api/` - API routes

### Configuration
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore patterns
- `.env.template` - Environment variables template
- `config/config_template.py` - Config template

### Testing
- `tests/conftest.py` - pytest fixtures
- `tests/test_main.py` - Sample tests

---

## 🔐 ENVIRONMENT VARIABLES

### .env file

```bash
# GitHub API
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxx
GITHUB_USERNAME=rauschiccsk

# Email Notifications (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=automation@isnex.ai
SMTP_PASSWORD=xxxxxxxxxxxx
SMTP_FROM=automation@isnex.ai

# Paths
DEV_ROOT=c:\Development
DEPLOY_ROOT=c:\Deployment
```

---

## 📊 DEVELOPMENT ROADMAP

### STORY 1: Core Generator ⚙️ (Current)
**Priority:** CRITICAL  
**Estimated:** 2 weeks  

- [x] 1.1 - Project setup and documentation ✅
- [ ] 1.2 - Pydantic models (ProjectConfig)
- [ ] 1.3 - YAML config parser
- [ ] 1.4 - Template engine (Jinja2)
- [ ] 1.5 - File generator logic
- [ ] 1.6 - Git operations wrapper
- [ ] 1.7 - GitHub API client
- [ ] 1.8 - Input validators
- [ ] 1.9 - Main project_creator.py
- [ ] 1.10 - Unit tests (80%+ coverage)
- [ ] 1.11 - Integration testing
- [ ] 1.12 - Documentation finalization

### STORY 2: n8n Integration 🤖
**Priority:** MEDIUM  
**Estimated:** 3-5 days  

- [ ] 2.1 - File monitor workflow
- [ ] 2.2 - Python executor node
- [ ] 2.3 - Email notifications
- [ ] 2.4 - Error handling
- [ ] 2.5 - Testing

### STORY 3: Advanced Features 🚀
**Priority:** LOW  
**Estimated:** 1 week  

- [ ] 3.1 - CLI interface (Click/Typer)
- [ ] 3.2 - Custom templates support
- [ ] 3.3 - Template validation
- [ ] 3.4 - Progress indicators
- [ ] 3.5 - Dry-run mode

---

## 🔧 TECHNICAL DECISIONS

### Why YAML over JSON?
- ✅ Human-readable
- ✅ Comments support
- ✅ Less verbose
- ✅ Standard for configs

### Why Jinja2?
- ✅ Powerful templating
- ✅ Widely used
- ✅ Python native
- ✅ Good documentation

### Why PyGithub?
- ✅ Official GitHub client
- ✅ High-level API
- ✅ Well maintained
- ✅ Easy to use

### Why Pydantic?
- ✅ Type validation
- ✅ Data parsing
- ✅ Error messages
- ✅ FastAPI integration

---

## ⚠️ CRITICAL REMINDERS

### For Every New Chat:
1. 🔥 **ALWAYS** load GitHub files first (use web_fetch)
2. 🔥 **NEVER** assume project structure
3. 🔥 **ALWAYS** check PROJECT_STATUS.md
4. 🔥 **ALWAYS** commit + push after work
5. 🔥 **ALWAYS** update session notes
6. 🔥 **COMMUNICATE** in Slovak language

### Git Rules:
- ✅ Commit often, small changes
- ✅ Descriptive commit messages
- ✅ Test before commit
- ✅ Pull before push
- ✅ Feature branches for new features

### Code Standards:
- ✅ PEP 8 style guide
- ✅ Type hints everywhere
- ✅ Docstrings for all functions
- ✅ Comments in Slovak for business logic
- ✅ English variable/function names

---

## ✅ SUCCESS CRITERIA

### MVP (Minimum Viable Product)
- ✅ Single command creates full project
- ✅ All template files generated
- ✅ GitHub repository created automatically
- ✅ Raw URL functional
- ✅ Generation time < 60 seconds
- ✅ Zero manual steps after execution

### V1.0 Release
- ✅ n8n webhook integration
- ✅ Email notifications
- ✅ Error handling
- ✅ Input validation
- ✅ Unit tests 80%+
- ✅ Complete documentation

---

## 📞 CONTACT

- **Developer:** ICC (rausch@icc.sk)
- **GitHub:** https://github.com/rauschiccsk/project-generator
- **Local Path:** c:\Development\project-generator

---

## 🎓 INSPIRATION

This project is based on successful patterns from:
- **supplier_invoice_loader** - Multi-customer architecture
- **orthodox-portal** - Documentation structure
- Both projects have proven the "single raw URL" workflow

---

**Document Version:** 0.1.0  
**Created:** 2025-10-20  
**Status:** Active Development - Initial Setup  
**Next Session:** STORY 1.2 - Pydantic Models

🏭 **Let's automate project creation!**