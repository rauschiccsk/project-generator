# 🏭 PROJECT-GENERATOR - FULL PROJECT CONTEXT

**Automated Python project creation with complete documentation infrastructure**

**Last Updated:** 2025-10-20  
**Version:** 0.1.0  
**Status:** Initial Setup Complete - Ready for Development

---

## 🤖 INSTRUCTIONS FOR CLAUDE

**When you see this document at the start of a conversation:**

1. This document contains everything needed to work on the project
2. Respond with: **"✅ Projekt načítaný. Čo robíme?"**
3. Wait for user's instructions
4. Check the CURRENT PROJECT STATUS section below for latest progress

**User should provide just this one URL:**
```
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/FULL_PROJECT_CONTEXT.md
```

---

## 📊 CURRENT PROJECT STATUS

### GitHub Repository
```
URL: https://github.com/rauschiccsk/project-generator
Branch: main
Local: c:\Development\project-generator
```

### Overview
- **Project:** Project Generator
- **Phase:** Initial Setup Complete
- **Overall Progress:** 16% (Task 1.1 complete, 1/12 tasks in STORY 1)
- **Active Story:** STORY 1 - Core Generator
- **Last Session:** 2025-10-20
- **Next Milestone:** Task 1.2 - Pydantic Models

### Recent Achievements
- ✅ 2025-10-20: Project structure created
- ✅ 2025-10-20: Git repository initialized
- ✅ 2025-10-20: GitHub repository created (rauschiccsk/project-generator)
- ✅ 2025-10-20: Complete documentation created
- ✅ 2025-10-20: Configuration system designed (YAML)
- ✅ 2025-10-20: File access generator created
- ✅ 2025-10-20: Single-URL loading verified

### Active Tasks
- [x] **STORY 1 Task 1.1** - Project setup and documentation ✅ COMPLETE
- [ ] **STORY 1 Task 1.2** - Pydantic models (ProjectConfig) ← NEXT
- [ ] **STORY 1 Task 1.3** - YAML config parser

### Progress: STORY 1 - Core Generator
```
[██░░░░░░░░░░] 16% (2/12 tasks)

✅ 1.1 - Project setup and documentation
⏳ 1.2 - Pydantic models (ProjectConfig)
⏳ 1.3 - YAML config parser
⏳ 1.4 - Template engine (Jinja2)
⏳ 1.5 - File generator logic
⏳ 1.6 - Git operations wrapper
⏳ 1.7 - GitHub API client
⏳ 1.8 - Input validators
⏳ 1.9 - Main project_creator.py
⏳ 1.10 - Unit tests (80%+ coverage)
⏳ 1.11 - Integration testing
⏳ 1.12 - Documentation finalization
```

---

## 🎯 PROJECT OVERVIEW

### Problem
- Creating a new project takes **3+ hours**
- Dozens of commits for basic setup
- Repetitive work (docs/, git, config, templates)
- Inconsistent structure between projects

### Solution
**Project Generator** - automated tool that creates in **30 seconds**:
- ✅ Complete Python project with documentation
- ✅ GitHub repository
- ✅ Git initialization + first commit
- ✅ Raw URL ready for Claude
- ✅ All necessary config files

### Workflow
```
YAML config → Python Generator → GitHub repo → Raw URL → ✅ Ready!
```

---

## 🏗️ ARCHITECTURE

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

---

## 💾 TECH STACK

### Core Technologies
```yaml
Language: Python 3.11+
Templating: Jinja2
Config: YAML (PyYAML)
Validation: Pydantic
GitHub API: PyGithub
Git: GitPython
Testing: pytest
IDE: PyCharm
```

### Dependencies
```python
pydantic>=2.5.0       # Data validation
jinja2>=3.1.2         # Template engine
pyyaml>=6.0.1         # YAML parsing
pygithub>=2.1.1       # GitHub API client
GitPython>=3.1.40     # Git operations
python-dotenv>=1.0.0  # Environment variables
pytest>=7.4.3         # Testing
black>=23.12.0        # Code formatter
```

---

## 📁 PROJECT STRUCTURE

```
c:\Development\project-generator/
│
├── docs/                                    
│   ├── FULL_PROJECT_CONTEXT.md            # This file - Single source of truth
│   ├── project_file_access.json           # Generated file list
│   ├── architecture/                       # Architecture docs (future)
│   └── sessions/                           # Session notes (future)
│
├── src/                                     
│   ├── __init__.py
│   ├── generator/                           
│   │   ├── __init__.py
│   │   ├── project_creator.py             # Main logic (TODO)
│   │   ├── template_engine.py             # Jinja2 renderer (TODO)
│   │   ├── github_client.py               # GitHub API (TODO)
│   │   └── validators.py                  # Input validation (TODO)
│   │
│   ├── models/                              
│   │   ├── __init__.py
│   │   └── project_config.py              # Pydantic models (TODO)
│   │
│   └── templates/                           # Jinja2 templates (TODO)
│       ├── project_files/
│       └── docs_structure/
│
├── tests/                                   
│   ├── __init__.py
│   └── fixtures/
│
├── scripts/                                 
│   └── generate_project_access.py         # ✅ Complete
│
├── configs/                                 
│   ├── config_template.yaml               # ✅ Complete
│   ├── examples/
│   │   ├── monastier_online.yaml          # ✅ Complete
│   │   └── supplier_invoice.yaml          # ✅ Complete
│   ├── queue/                             
│   └── processed/                         
│
├── .gitignore                              # ✅ Complete
├── .env.template                           # ✅ Complete
├── requirements.txt                        # ✅ Complete
├── README.md                               # ✅ Complete
└── LICENSE                                 # TODO
```

---

## 📝 YAML CONFIG FORMAT

### Example Configuration

```yaml
# ===================================
# PROJECT GENERATOR - Configuration
# ===================================

project:
  name: "My New Project"
  slug: "my-new-project"
  description: "Brief description of the project"
  
github:
  username: "rauschiccsk"
  repo_name: "my-new-project"
  visibility: "private"
  
developer:
  name: "ICC"
  email: "rausch@icc.sk"
  
paths:
  local_dev: "c:\\Development\\my-new-project"
  
tech_stack:
  backend: ["fastapi", "sqlalchemy"]
  frontend: ["jinja2", "tailwindcss"]
  databases: ["postgresql", "redis"]
  automation: ["n8n"]
    
features:
  include_auth: true
  include_api_docs: true
  include_tests: true
  include_docker: false
```

Full template: `configs/config_template.yaml`

---

## 🚀 USAGE (FUTURE)

### Planned Usage

```bash
# 1. Copy template
cp configs/config_template.yaml configs/my_project.yaml

# 2. Edit config
notepad configs/my_project.yaml

# 3. Generate project
python src/generator/project_creator.py --config configs/my_project.yaml

# 4. Output
✅ Project created in ~30 seconds
📁 Local: c:\Development\my-new-project
🔗 GitHub: https://github.com/user/my-new-project
📄 Raw URL: https://raw.githubusercontent.com/.../FULL_PROJECT_CONTEXT.md
```

---

## 🔐 ENVIRONMENT VARIABLES

### .env Configuration

```bash
# GitHub API
GITHUB_TOKEN=github_pat_xxxxxxxxxxxxx
GITHUB_USERNAME=rauschiccsk

# Paths
DEV_ROOT=c:\Development
DEPLOY_ROOT=c:\Deployment

# Email (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=automation@isnex.ai
SMTP_PASSWORD=xxxxxxxxxxxx
```

Template: `.env.template`

---

## 📊 DEVELOPMENT ROADMAP

### STORY 1: Core Generator ⚙️ (In Progress - 16%)
**Priority:** CRITICAL  
**Estimated:** 2 weeks  
**Status:** 🔄 Task 1.1 complete, Task 1.2 next

**Completed:**
- [x] 1.1 - Project setup and documentation ✅

**Next Up:**
- [ ] 1.2 - Pydantic models (ProjectConfig)
  - Create `src/models/project_config.py`
  - ProjectConfig, TechStack, ProjectFeatures classes
  - Validation rules
  - Unit tests

**Remaining:**
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
**Status:** ⏳ Planned  
**Depends On:** STORY 1

### STORY 3: Advanced Features 🚀
**Priority:** LOW  
**Status:** ⏳ Planned  
**Depends On:** STORY 1, STORY 2

---

## 🔧 TECHNICAL DECISIONS

### Key Design Choices

**YAML vs JSON:**
- ✅ Human-readable, comments support
- ✅ Less verbose than JSON
- ✅ Standard for configurations

**Jinja2 Templating:**
- ✅ Powerful, widely used
- ✅ Python native
- ✅ Good documentation

**PyGithub Library:**
- ✅ Official GitHub client
- ✅ High-level API
- ✅ Well maintained

**Pydantic Validation:**
- ✅ Type safety
- ✅ Automatic parsing
- ✅ Clear error messages
- ✅ FastAPI integration

---

## 📞 GITHUB & CONTACT

### Repository Information
```
GitHub: https://github.com/rauschiccsk/project-generator
Branch: main
Local: c:\Development\project-generator
```

### Developer
- **Name:** ICC
- **Email:** rausch@icc.sk
- **GitHub:** @rauschiccsk

### Raw URLs
```
FULL_PROJECT_CONTEXT.md:
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/FULL_PROJECT_CONTEXT.md

project_file_access.json:
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/project_file_access.json
```

---

## ⚠️ CRITICAL REMINDERS

### For Every New Chat:
1. 🔥 Load this document using the raw URL above
2. 🔥 Check CURRENT PROJECT STATUS section
3. 🔥 Never assume project structure without checking
4. 🔥 Always commit + push after completing work
5. 🔥 Update this document when making significant changes

### Git Workflow:
- ✅ Commit often, small changes
- ✅ Descriptive commit messages
- ✅ Test before commit
- ✅ Pull before push

### Code Standards:
- ✅ PEP 8 style guide
- ✅ Type hints everywhere
- ✅ Docstrings for all functions
- ✅ Slovak comments for business logic
- ✅ English variable/function names

---

## ✅ SUCCESS CRITERIA

### MVP Goals
- ✅ Single command creates complete project
- ✅ GitHub repository auto-created
- ✅ Raw URL functional for Claude
- ✅ Generation time < 60 seconds
- ✅ Zero manual steps

### V1.0 Goals
- ✅ All STORY 1 tasks complete
- ✅ 80%+ test coverage
- ✅ Complete documentation
- ✅ Production ready

---

## 🎓 INSPIRATION

Based on successful patterns from:
- **supplier_invoice_loader** - Multi-customer architecture, single-URL loading
- **orthodox-portal** - Documentation structure, project organization

Both projects proved the "one raw URL for Claude" workflow.

---

## 📝 LATEST SESSION NOTES

### Session: 2025-10-20 - Initial Setup

**Duration:** ~2 hours  
**Focus:** Project foundation and documentation

**Completed:**
- ✅ Project structure created
- ✅ Git initialized and first commit
- ✅ GitHub repository created
- ✅ Complete documentation written
- ✅ YAML configuration system designed
- ✅ File access generator script created
- ✅ Single-URL loading pattern implemented
- ✅ All basic files committed and pushed

**Key Decisions:**
- Use YAML for configuration (human-readable)
- Pydantic for validation (type safety)
- Jinja2 for templating (powerful, standard)
- Single FULL_PROJECT_CONTEXT.md (no multi-file loading)

**Next Session:**
- Start Task 1.2: Pydantic models
- Create `src/models/project_config.py`
- Define ProjectConfig data model
- Add validation rules
- Write unit tests

---

## 🔗 QUICK FILE LOCATIONS

### Documentation
- This file: `docs/FULL_PROJECT_CONTEXT.md`
- File listing: `docs/project_file_access.json`

### Configuration
- Template: `configs/config_template.yaml`
- Examples: `configs/examples/`

### Source Code (TODO)
- Models: `src/models/project_config.py`
- Generator: `src/generator/project_creator.py`
- Templates: `src/templates/`

### Tests (TODO)
- Unit tests: `tests/`

### Scripts
- File generator: `scripts/generate_project_access.py` ✅

---

**Document Version:** 0.1.0  
**Created:** 2025-10-20  
**Last Updated:** 2025-10-20  
**Status:** Active Development - Task 1.1 Complete  
**Next Task:** 1.2 - Pydantic Models

🏭 **One URL. Complete Project. Ready to Build.**