# 🤖 SYSTEM PROMPT - Project Generator

## 📋 FOR CLAUDE: Project Loading Instructions

**When you see the FULL_PROJECT_CONTEXT.md URL at the start of conversation:**

### 1. Load Required Files
Immediately fetch these files from GitHub:
```
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/MASTER_CONTEXT.md
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/PROJECT_STATUS.md
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/project_file_access.json
```

### 2. Confirm Loading
After loading all files, respond with:
```
✅ Project Generator načítaný!
📊 Status: [current status from PROJECT_STATUS.md]
🎯 Ready to work. Čo robíme?
```

### 3. Always Check Status First
**Before ANY work:**
- Check `PROJECT_STATUS.md` for current story/task
- Verify what was completed in last session
- Ask user which task to work on

---

## 🔧 Working Rules

### Code Standards
- ✅ **PEP 8** style guide
- ✅ **Type hints** everywhere
- ✅ **Docstrings** for all functions/classes
- ✅ **English** for variable/function names
- ✅ **Slovak** comments for business logic
- ✅ **pytest** for testing (80%+ coverage target)

### Git Workflow
```bash
# Before starting work
git pull origin main

# During work (small commits)
git add .
git commit -m "feat: descriptive message"

# After completion
git push origin main
```

### Commit Message Format
```
feat: add new feature
fix: bug fix
docs: documentation update
test: add tests
refactor: code refactoring
style: formatting changes
```

### Documentation Updates
**After EVERY session:**
1. ✅ Update `PROJECT_STATUS.md` with progress
2. ✅ Create session note in `docs/sessions/YYYY-MM-DD-description.md`
3. ✅ Update `project_file_access.json` if files added/removed
4. ✅ Commit and push changes

---

## 📁 Project Structure Reference

```
project-generator/
│
├── docs/                           # 📚 Documentation
│   ├── FULL_PROJECT_CONTEXT.md    # Complete context
│   ├── SYSTEM_PROMPT.md           # This file
│   ├── MASTER_CONTEXT.md          # Quick reference
│   ├── QUICK_START.md             # Getting started
│   ├── PROJECT_STATUS.md          # Development tracking
│   ├── project_file_access.json   # Files manifest
│   ├── architecture/              # Design docs
│   └── sessions/                  # Session notes
│
├── src/                           # 🐍 Python source
│   ├── generator/                 # Core generator logic
│   ├── models/                    # Pydantic models
│   └── templates/                 # Jinja2 templates
│
├── tests/                         # 🧪 Test suite
├── configs/                       # ⚙️ Configuration files
├── scripts/                       # 🔧 Utility scripts
└── n8n_workflows/                # 🤖 Automation
```

---

## 🎯 Current Development Phase

**STORY 1: Core Generator** (In Progress)
- Building the fundamental project generation engine
- Target: Complete project creation in < 60 seconds
- Focus: YAML → Python → GitHub → Ready

**Priority Tasks:**
1. Pydantic models for config validation
2. YAML parser
3. Jinja2 template engine
4. File generation logic
5. GitHub API integration

---

## ⚠️ Critical Reminders

### For EVERY Chat Session:
1. 🔥 **LOAD** all files from GitHub first
2. 🔥 **CHECK** PROJECT_STATUS.md before starting
3. 🔥 **COMMIT** changes frequently
4. 🔥 **UPDATE** documentation after work
5. 🔥 **PUSH** to GitHub at session end

### Never Assume:
- ❌ Don't assume file structure without checking
- ❌ Don't skip documentation updates
- ❌ Don't make large uncommitted changes
- ❌ Don't work on multiple stories simultaneously

### Always:
- ✅ Test code before committing
- ✅ Update tests with new features
- ✅ Keep commits small and focused
- ✅ Write clear commit messages
- ✅ Ask if uncertain about direction

---

## 💡 Quick Commands

### Start New Session
```python
# 1. Load project context
# 2. Check PROJECT_STATUS.md
# 3. Ask: "Which task should I work on?"
```

### End Session
```python
# 1. Update PROJECT_STATUS.md
# 2. Create session note
# 3. Commit all changes
# 4. Push to GitHub
# 5. Confirm: "✅ Session completed, changes pushed"
```

---

## 📞 Contact & Resources

- **Developer:** ICC (rausch@icc.sk)
- **GitHub:** https://github.com/rauschiccsk/project-generator
- **Local Path:** c:\Development\project-generator
- **Tech Stack:** Python 3.11+, Jinja2, Pydantic, PyGithub

---

## 🎓 Project Philosophy

**Goal:** Automate the boring stuff
- No more 3+ hour project setups
- One command → Complete project
- Consistent structure across all projects
- Ready for Claude collaboration

**Inspired by:**
- `supplier_invoice_loader` - Architecture patterns
- `orthodox-portal` - Documentation structure

---

**Version:** 1.0.0  
**Last Updated:** 2025-10-20  
**Status:** Active Development

🤖 **Ready to build! Let's automate project creation!**