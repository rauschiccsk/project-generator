# 🏭 Project Generator

**Automated Python project creation with complete documentation infrastructure**

Generate a fully-configured Python project in 30 seconds, complete with documentation, GitHub repository, and ready-to-use Claude context.

---

## 🎯 What It Does

**Problem:**
- Creating a new project takes 3+ hours
- Dozens of commits for basic setup
- Repetitive work (docs, git, configs, templates)

**Solution:**
- ✅ One command → Complete project in 30 seconds
- ✅ Automatic GitHub repository creation
- ✅ Pre-configured documentation structure
- ✅ Ready-to-use raw URL for Claude
- ✅ Consistent project structure

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/rauschiccsk/project-generator.git
cd project-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.template .env
# Edit .env with your GitHub token and other settings
```

### 4. Create Project Config

```bash
cp configs/config_template.yaml configs/my_project.yaml
# Edit my_project.yaml with your project details
```

### 5. Generate Project

```bash
python src/generator/project_creator.py --config configs/my_project.yaml
```

### 6. Result

```
✅ Projekt "My Project" vytvorený!
📁 Local: c:\Development\my-project
🔗 GitHub: https://github.com/your-username/my-project
📄 Context: https://raw.githubusercontent.com/.../FULL_PROJECT_CONTEXT.md
⏱️ Time: 28.3s
```

---

## 📝 Configuration

### Minimal Config Example

```yaml
project:
  name: "My New Project"
  slug: "my-new-project"
  description: "Brief description"
  
github:
  username: "your-github-username"
  repo_name: "my-new-project"
  visibility: "private"
  
developer:
  name: "Your Name"
  email: "your@email.com"
  
paths:
  local_dev: "c:\\Development\\my-new-project"
  
tech_stack:
  backend: ["fastapi"]
  databases: ["postgresql"]
  
features:
  include_auth: true
  include_tests: true
```

See `configs/config_template.yaml` for full options.

---

## 📂 What Gets Generated

Every project includes:

### Documentation
```
docs/
├── FULL_PROJECT_CONTEXT.md    # Complete project documentation
├── PROJECT_STATUS.md           # Development tracking
├── project_file_access.json    # GitHub files manifest
├── architecture/               # Architecture docs
├── sessions/                   # Session notes templates
└── troubleshooting/            # Known issues
```

### Python Code Structure
```
src/
├── main.py                     # FastAPI application
├── config.py                   # Configuration
├── database.py                 # Database connection
├── models/                     # Pydantic models
└── api/                        # API routes
```

### Configuration Files
```
requirements.txt                # Python dependencies
.gitignore                      # Git ignore patterns
.env.template                   # Environment variables
config/config_template.py       # Config template
```

### Testing
```
tests/
├── conftest.py                 # pytest fixtures
└── test_main.py                # Sample tests
```

---

## 🔧 Features

- ✅ **YAML Configuration** - Simple, human-readable config
- ✅ **Jinja2 Templates** - Customizable file generation
- ✅ **GitHub Integration** - Automatic repository creation
- ✅ **Git Operations** - Automatic init, commit, push
- ✅ **Input Validation** - Pydantic-based validation
- ✅ **PyCharm Ready** - Works with PyCharm IDE
- ✅ **Claude Integration** - Single raw URL loads everything

### Optional Features
- 🤖 **n8n Automation** - Automatic workflow triggers
- 📧 **Email Notifications** - Get notified when done
- 🐳 **Docker Support** - Docker configs (optional)
- 🔄 **CI/CD** - GitHub Actions (optional)

---

## 🛠️ Requirements

- Python 3.11+
- Git
- GitHub account + Personal Access Token
- PyCharm (recommended)

---

## 📊 Project Status

**Version:** 0.1.0  
**Status:** Initial Setup  
**Progress:** 8% (STORY 1 in progress)

See [PROJECT_STATUS.md](docs/PROJECT_STATUS.md) for detailed progress.

---

## 📚 Documentation

- **[FULL_PROJECT_CONTEXT.md](docs/FULL_PROJECT_CONTEXT.md)** - Complete project documentation
- **[PROJECT_STATUS.md](docs/PROJECT_STATUS.md)** - Development tracking
- **[Architecture](docs/architecture/)** - System design docs

---

## 🎯 Roadmap

### STORY 1: Core Generator (Current)
- [x] Project setup ✅
- [ ] Pydantic models
- [ ] Template engine
- [ ] File generator
- [ ] GitHub integration

### STORY 2: n8n Integration
- [ ] File monitor workflow
- [ ] Email notifications
- [ ] Error handling

### STORY 3: Advanced Features
- [ ] CLI interface
- [ ] Custom templates
- [ ] Progress indicators

---

## 🤝 Contributing

This is a personal automation tool, but suggestions are welcome!

---

## 📞 Contact

- **Developer:** ICC (rausch@icc.sk)
- **GitHub:** https://github.com/rauschiccsk/project-generator

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🎓 Inspired By

This project automates patterns from:
- **supplier_invoice_loader** - Multi-customer architecture
- **orthodox-portal** - Documentation structure

Both projects proved the "single raw URL for Claude" workflow.

---

**🏭 Automate. Generate. Build.**