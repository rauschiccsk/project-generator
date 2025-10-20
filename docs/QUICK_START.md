# 🚀 QUICK START - Project Generator

**Get up and running in 5 minutes**

---

## 📋 Prerequisites

Before starting, ensure you have:

- ✅ **Python 3.11+** installed
- ✅ **Git** installed and configured
- ✅ **GitHub account** with Personal Access Token
- ✅ **PyCharm** (optional, but recommended)
- ✅ **Windows** (c:\Development\ path structure)

---

## ⚡ Installation

### Step 1: Clone Repository

```bash
# Clone the project
git clone https://github.com/rauschiccsk/project-generator.git

# Navigate to directory
cd project-generator
```

### Step 2: Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt
```

**Dependencies installed:**
- `pydantic>=2.0.0` - Data validation
- `jinja2>=3.1.0` - Template engine
- `pyyaml>=6.0` - YAML parsing
- `pygithub>=2.1.0` - GitHub API
- `requests>=2.31.0` - HTTP client
- `python-dotenv>=1.0.0` - Environment variables
- `pytest>=7.4.0` - Testing framework

### Step 3: Configure Environment

```bash
# Copy environment template
cp .env.template .env

# Edit .env file
notepad .env
```

**Required in `.env`:**
```bash
# GitHub API
GITHUB_TOKEN=ghp_your_token_here
GITHUB_USERNAME=your-username

# Paths
DEV_ROOT=c:\Development
```

**Get GitHub Token:**
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `workflow`
4. Copy token to `.env`

---

## 🎯 First Project Generation

### Step 1: Create Configuration

```bash
# Copy template
cp configs/config_template.yaml configs/my_first_project.yaml

# Edit configuration
notepad configs/my_first_project.yaml
```

### Step 2: Configure Your Project

```yaml
# ===================================
# MY FIRST PROJECT - Configuration
# ===================================

project:
  name: "My First Generated Project"
  slug: "my-first-project"
  description: "Testing the project generator"

github:
  username: "your-github-username"  # ⚠️ CHANGE THIS
  repo_name: "my-first-project"
  visibility: "private"

developer:
  name: "Your Name"                 # ⚠️ CHANGE THIS
  email: "your@email.com"           # ⚠️ CHANGE THIS

paths:
  local_dev: "c:\\Development\\my-first-project"

tech_stack:
  backend:
    - "fastapi"
  databases:
    - "postgresql"

features:
  include_auth: true
  include_tests: true
  include_api_docs: true
```

### Step 3: Generate Project

```bash
# Run generator
python src/generator/project_creator.py --config configs/my_first_project.yaml
```

**Expected Output:**
```
🏭 Project Generator v0.1.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Configuration loaded: my_first_project.yaml
✅ Validation passed
🔨 Generating project structure...
📝 Creating documentation...
🔧 Generating source files...
🧪 Setting up tests...
📦 Creating GitHub repository...
🚀 Pushing to GitHub...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Project "My First Generated Project" created!

📁 Local: c:\Development\my-first-project
🔗 GitHub: https://github.com/your-username/my-first-project
📄 Context: https://raw.githubusercontent.com/your-username/my-first-project/main/docs/FULL_PROJECT_CONTEXT.md

⏱️ Generation time: 28.3 seconds
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 4: Verify Project

```bash
# Navigate to new project
cd c:\Development\my-first-project

# Check structure
dir

# Open in PyCharm
pycharm .
```

---

## 📂 What Was Created?

Your new project contains:

```
my-first-project/
│
├── docs/                                 # 📚 Complete documentation
│   ├── FULL_PROJECT_CONTEXT.md          # Single source of truth
│   ├── PROJECT_STATUS.md                # Development tracking
│   ├── SYSTEM_PROMPT.md                 # Claude instructions
│   ├── MASTER_CONTEXT.md                # Quick reference
│   ├── QUICK_START.md                   # Getting started
│   ├── project_file_access.json         # Files manifest
│   ├── architecture/                    # Design docs
│   │   ├── README.md
│   │   ├── system-overview.md
│   │   └── database-schema.md
│   ├── sessions/                        # Session notes
│   │   └── session_template.md
│   └── troubleshooting/                 # Known issues
│       └── README.md
│
├── src/                                  # 🐍 Python application
│   ├── __init__.py
│   ├── main.py                          # FastAPI app
│   ├── config.py                        # Configuration
│   ├── database.py                      # Database connection
│   ├── models/                          # Pydantic models
│   │   ├── __init__.py
│   │   └── user.py
│   └── api/                             # API routes
│       ├── __init__.py
│       └── routes.py
│
├── tests/                                # 🧪 Test suite
│   ├── __init__.py
│   ├── conftest.py                      # pytest fixtures
│   └── test_main.py                     # Sample tests
│
├── config/                               # ⚙️ Configuration
│   └── config_template.py
│
├── requirements.txt                      # Python dependencies
├── .gitignore                           # Git ignore patterns
├── .env.template                        # Environment variables template
├── README.md                            # Project overview
├── CHANGELOG.md                         # Version history
└── LICENSE                              # MIT License
```

---

## 🔄 Using with Claude

### Load Project in New Chat

Simply paste the raw URL:
```
https://raw.githubusercontent.com/your-username/my-first-project/main/docs/FULL_PROJECT_CONTEXT.md
```

Claude will automatically:
1. Load all project files
2. Understand project structure
3. Check current status
4. Ask what to work on

---

## 🧪 Testing

### Run Tests
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test
pytest tests/test_main.py -v
```

---

## 🔧 Common Operations

### Generate Another Project

```bash
# Create new config
cp configs/config_template.yaml configs/another_project.yaml

# Edit configuration
notepad configs/another_project.yaml

# Generate
python src/generator/project_creator.py --config configs/another_project.yaml
```

### Update Documentation

```bash
# Regenerate project_file_access.json
python scripts/generate_project_access.py
```

### Validate Templates

```bash
# Check Jinja2 templates for errors
python scripts/validate_templates.py
```

---

## 🐛 Troubleshooting

### GitHub Token Issues

**Error:** `Bad credentials`
```bash
# Verify token in .env
cat .env | grep GITHUB_TOKEN

# Test token manually
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
```

### Path Issues

**Error:** `Directory not found`
```bash
# Verify DEV_ROOT exists
echo %DEV_ROOT%
mkdir c:\Development
```

### Import Errors

**Error:** `ModuleNotFoundError`
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

---

## 📚 Next Steps

1. **Read FULL_PROJECT_CONTEXT.md** - Complete documentation
2. **Check PROJECT_STATUS.md** - Current development state
3. **Explore Templates** - See `src/templates/` directory
4. **Run Tests** - Ensure everything works
5. **Generate Real Project** - Create your actual project

---

## 💡 Tips

- 🎯 **Start small** - Generate a simple project first
- 📝 **Keep configs** - Save YAML configs for reuse
- 🔄 **Iterate** - Regenerate projects to refine templates
- 🧪 **Test first** - Run generator tests before creating projects
- 📚 **Document** - Every generated project has full docs

---

## 🎓 Examples

Check `configs/examples/` for real-world configurations:
- `monastier_online.yaml` - FastAPI + PostgreSQL + Auth
- `supplier_invoice.yaml` - Multi-customer architecture

---

## 📞 Need Help?

- 📖 **Docs:** `docs/FULL_PROJECT_CONTEXT.md`
- 🐛 **Issues:** https://github.com/rauschiccsk/project-generator/issues
- 📧 **Email:** rausch@icc.sk
- 💬 **Ask Claude:** Load project context and ask questions

---

**Version:** 1.0.0  
**Last Updated:** 2025-10-20  
**Estimated Time:** 5 minutes setup + 30 seconds per project

🚀 **Ready to generate projects! Have fun!**