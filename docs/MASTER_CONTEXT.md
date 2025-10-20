# 🏭 PROJECT GENERATOR - Master Context

**Quick Reference Guide**

---

## 🎯 What Is This?

**One-command Python project generator** that creates a complete project in 30 seconds:
- ✅ Full project structure
- ✅ GitHub repository
- ✅ Documentation infrastructure
- ✅ Git initialized and committed
- ✅ Ready for Claude collaboration

**Solves:** 3+ hours of manual project setup → 30 seconds automated

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/rauschiccsk/project-generator.git
cd project-generator

# 2. Setup
pip install -r requirements.txt
cp .env.template .env  # Add GitHub token

# 3. Configure
cp configs/config_template.yaml configs/my_project.yaml
# Edit my_project.yaml with your project details

# 4. Generate
python src/generator/project_creator.py --config configs/my_project.yaml

# Done! ✅
```

---

## 📋 Key Files

| File | Purpose | Location |
|------|---------|----------|
| **FULL_PROJECT_CONTEXT.md** | Complete documentation | `docs/` |
| **PROJECT_STATUS.md** | Development tracking | `docs/` |
| **SYSTEM_PROMPT.md** | Claude instructions | `docs/` |
| **QUICK_START.md** | Getting started guide | `docs/` |
| **project_file_access.json** | Files manifest | `docs/` |
| **config_template.yaml** | Project config template | `configs/` |
| **project_creator.py** | Main generator | `src/generator/` |

---

## 💾 Tech Stack

```yaml
Language: Python 3.11+
Templates: Jinja2
Config: YAML (PyYAML)
Validation: Pydantic
GitHub: PyGithub
Testing: pytest
```

---

## 🏗️ Architecture

```
YAML Config → Python Generator → GitHub API → ✅ Ready!
     ↓              ↓                ↓
  Parse &      Generate        Create Repo
  Validate      Files          & Push
```

---

## 📊 Development Status

**Current Phase:** STORY 1 - Core Generator  
**Progress:** ~10%  
**Next:** Pydantic models, YAML parser, template engine

**Stories:**
1. **Core Generator** ⚙️ (Current) - 2 weeks
2. **n8n Integration** 🤖 - 3-5 days
3. **Advanced Features** 🚀 - 1 week

---

## 📁 Generated Project Structure

Every generated project includes:

```
new-project/
├── docs/
│   ├── FULL_PROJECT_CONTEXT.md
│   ├── PROJECT_STATUS.md
│   ├── architecture/
│   └── sessions/
├── src/
│   ├── main.py
│   ├── config.py
│   └── models/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🎯 Success Criteria

**MVP:**
- ✅ Single command creates full project
- ✅ GitHub repo created automatically
- ✅ All files generated from templates
- ✅ Generation time < 60 seconds
- ✅ Raw URL functional for Claude

---

## ⚙️ Configuration Example

```yaml
project:
  name: "My New Project"
  slug: "my-new-project"
  description: "Project description"

github:
  username: "your-username"
  repo_name: "my-new-project"
  visibility: "private"

developer:
  name: "Your Name"
  email: "your@email.com"

tech_stack:
  backend: ["fastapi"]
  databases: ["postgresql"]
```

---

## 🔧 Common Tasks

### Start Development Session
1. Load project context
2. Check `PROJECT_STATUS.md`
3. Choose task to work on

### Generate New Project
```bash
python src/generator/project_creator.py --config configs/my_project.yaml
```

### Run Tests
```bash
pytest tests/ -v
```

### Update Documentation
```bash
python scripts/generate_project_access.py
```

---

## 📞 Resources

- **GitHub:** https://github.com/rauschiccsk/project-generator
- **Local:** c:\Development\project-generator
- **Context URL:** https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/FULL_PROJECT_CONTEXT.md
- **Developer:** ICC (rausch@icc.sk)

---

## 🎓 Inspired By

- **supplier_invoice_loader** - Multi-customer patterns
- **orthodox-portal** - Documentation structure

Both projects proved the "single raw URL" workflow works perfectly.

---

**Version:** 0.1.0  
**Updated:** 2025-10-20  
**Status:** Active Development

🏭 **Automate. Generate. Build.**