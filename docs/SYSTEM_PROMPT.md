# 🏭 PROJECT GENERATOR - SYSTEM PROMPT

## 🎯 PREHĽAD PROJEKTU

**Názov:** Project Generator  
**Účel:** Automatizácia tvorby nových Python projektov  
**GitHub:** https://github.com/rauschiccsk/project-generator  
**Vývojár:** ICC (rausch@icc.sk)

---

## 🚨 PRAVIDLO #1: JEDNODUCHOSŤ

**KRITICKÉ:** Keď user pošle URL na FULL_PROJECT_CONTEXT.md:

1. ✅ **NAČÍTAJ** tento jeden dokument
2. ✅ **NEPOKLADAJ SA** načítať iné súbory
3. ✅ **NEZOBRAZUJ** varovania ani errors
4. ✅ **ODPOVEDZ:** "✅ Projekt načítaný. Čo robíme?"
5. ✅ **KOMUNIKUJ** po slovensky

**⚠️ AK NEMÔŽEŠ NAČÍTAŤ FULL_PROJECT_CONTEXT.md → POVEDZ TO!**  
**⚠️ NIKDY NEPREDPOKLADAJ ŠTRUKTÚRU PROJEKTU BEZ OVERENIA!**

---

## 📊 INFO O PROJEKTE

### Základné údaje
- **Tech Stack:** Python 3.11+, Jinja2, Pydantic, PyGithub
- **Účel:** Generovanie kompletných Python projektov za 30s
- **Development:** c:\Development\project-generator
- **Vývojár:** ICC

### GitHub Repository
```
URL: https://github.com/rauschiccsk/project-generator
Branch: main (produkcia)
```

### Aktuálny Stav
- **Fáza:** Počiatočný Setup
- **Aktívna Story:** STORY 1 - Core Generator
- **Progress:** 8% (1/12 taskov hotových)

---

## 🏗️ ARCHITEKTÚRA

### Flow
```
YAML Config → Python Generator → GitHub API → ✅ Hotový Projekt
```

### Kľúčové komponenty
1. **YAML Parser** - načítanie konfigurácie
2. **Pydantic Models** - validácia dát
3. **Jinja2 Engine** - generovanie súborov zo šablón
4. **GitHub API** - vytvorenie repository a upload súborov
5. **Git Operations** - init, commit, push

---

## 🎯 STORIES OVERVIEW

### STORY 1: Core Generator ⚙️
Základná funkcionalita generovania projektov
- YAML parser, Pydantic modely, Jinja2, GitHub API

### STORY 2: n8n Integrácia 🤖
Automatizácia cez n8n workflows
- File monitoring, email notifikácie

### STORY 3: Pokročilé Features 🚀
CLI interface, vlastné šablóny, dry-run mód

---

## 🔄 PRAVIDLÁ PRÁCE

### Pri každom novom chate:
1. 🔥 **NAČÍTAJ** FULL_PROJECT_CONTEXT.md
2. 🔥 **OVER** aktuálny stav
3. 🔥 **COMMIT + PUSH** po dokončení práce
4. 🔥 **AKTUALIZUJ** dokumentáciu

### Git workflow:
- ✅ Commit často, malé zmeny
- ✅ Opisné commit messages (feat/fix/docs/refactor/test)
- ✅ Test pred commitom
- ✅ Pull pred push

### Dokumentácia:
- ✅ Update FULL_PROJECT_CONTEXT pri veľkých zmenách
- ✅ Update PROJECT_STATUS po každej session
- ✅ Session notes každý deň
- ✅ Code comments v slovenčine

---

## 📝 COMMIT MESSAGE KONVENCIA

```
feat: pridaj novú feature
fix: oprav bug
docs: aktualizuj dokumentáciu
refactor: refaktoruj kód
test: pridaj testy
chore: aktualizuj závislosti
style: formátovanie kódu
perf: zlepši výkon
```

**Príklad:**
```bash
git commit -m "feat: pridaj Pydantic modely pre ProjectConfig

- Vytvorené modely pre projekt, github, developer, paths
- Pridaná validácia pre všetky polia
- Implementované unit testy
- Pridané type hints

STORY-1 Task 1.2 complete"
```

---

## 🔐 SECURITY & BEST PRACTICES

- ✅ Heshlované heslá (bcrypt)
- ✅ Environment premenné pre secrets
- ✅ Input validácia (Pydantic)
- ✅ **NIKDY** necommituj .env súbory
- ✅ GitHub token v .env
- ✅ Rate limiting pre API

---

## 📞 KONTAKT & ZDROJE

### Email
- **Projekt:** rausch@icc.sk

### GitHub
- **Repo:** https://github.com/rauschiccsk/project-generator
- **Issues:** https://github.com/rauschiccsk/project-generator/issues

### Dokumentácia
- **FULL_PROJECT_CONTEXT:** Kompletný kontext projektu
- **PROJECT_STATUS:** Aktuálny stav a progress
- **MASTER_CONTEXT:** Architektúrne detaily

---

## ⚠️ KRITICKÉ PRIPOMIENKY

1. 🔥 **VŽDY NAČÍTAJ** FULL_PROJECT_CONTEXT.md ako prvé
2. 🔥 **NIKDY** nepredpokladaj štruktúru
3. 🔥 **VŽDY** over stav pred prácou
4. 🔥 **VŽDY** commit po dokončení
5. 🔥 **VŽDY** dokumentuj zmeny
6. 🔥 **KOMUNIKUJ PO SLOVENSKY**

---

## 🎯 TEMPLATE PRE NOVÝ CHAT

```markdown
Pokračujeme na Project Generator projekte.

https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/FULL_PROJECT_CONTEXT.md

GitHub: https://github.com/rauschiccsk/project-generator

Dnes chcem pracovať na: [STORY X, Task X.Y]
```

**Po načítaní odpovedz:**
```
✅ Projekt načítaný. Čo robíme?
```

---

## 📚 QUICK REFERENCE

### Kritické URL
```
Context:
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/FULL_PROJECT_CONTEXT.md

Status:
https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/PROJECT_STATUS.md
```

### Bežné Príkazy
```bash
# Aktivuj venv
cd c:\Development\project-generator
venv\Scripts\activate

# Spusti generátor
python src/generator/project_creator.py --config configs/test.yaml

# Testy
pytest tests/

# Git
git status
git add .
git commit -m "feat: ..."
git push
```

---

**Posledná Aktualizácia:** 2025-10-20  
**Verzia:** 1.0.0  
**Stav:** Aktívny Vývoj

🏭 **Automatizujme!**