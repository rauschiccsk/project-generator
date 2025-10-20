# 🏭 PROJECT GENERATOR - MASTER KONTEXT

**Rýchly Referenčný Návod**

---

## 🎯 Čo je to?

**One-command Python project generator** ktorý vytvorí kompletný projekt za 30 sekúnd:
- ✅ Plná štruktúra projektu
- ✅ GitHub repository
- ✅ Dokumentačná infraštruktúra
- ✅ Git inicializovaný a commitnutý
- ✅ Hotové pre Claude

**Rieši:** 3+ hodiny manuálneho setupu → 30 sekúnd automatizovane

---

## 🚀 Rýchly Štart

```bash
# 1. Klonovanie
git clone https://github.com/rauschiccsk/project-generator.git
cd project-generator

# 2. Setup
pip install -r requirements.txt
cp .env.template .env  # Pridaj GitHub token

# 3. Konfigurácia
cp configs/config_template.yaml configs/moj_projekt.yaml
# Uprav moj_projekt.yaml s detailami projektu

# 4. Generovanie
python src/generator/project_creator.py --config configs/moj_projekt.yaml

# Hotovo! ✅
```

---

## 📋 Kľúčové Súbory

| Súbor | Účel | Umiestnenie |
|------|---------|----------|
| **FULL_PROJECT_CONTEXT.md** | Kompletná dokumentácia | `docs/` |
| **PROJECT_STATUS.md** | Sledovanie vývoja | `docs/` |
| **SYSTEM_PROMPT.md** | Claude inštrukcie | `docs/` |
| **QUICK_START.md** | Návod na začiatok | `docs/` |
| **project_file_access.json** | Manifest súborov | `docs/` |
| **config_template.yaml** | Konfig šablóna projektu | `configs/` |
| **project_creator.py** | Hlavný generátor | `src/generator/` |

---

## 💾 Tech Stack

```yaml
Jazyk: Python 3.11+
Templates: Jinja2
Config: YAML (PyYAML)
Validácia: Pydantic
GitHub: PyGithub
Testovanie: pytest
```

---

## 🏗️ Architektúra

```
YAML Config → Python Generator → GitHub API → ✅ Hotovo!
     ↓              ↓                ↓
  Parse &      Generuj        Vytvor Repo
  Validuj      Súbory         & Push
```

---

## 📊 Stav Vývoja

**Aktuálna Fáza:** STORY 1 - Core Generator  
**Progress:** ~8%  
**Ďalej:** Pydantic modely, YAML parser, template engine

**Stories:**
1. **Core Generator** ⚙️ (Aktuálne) - 2 týždne
2. **n8n Integrácia** 🤖 - 3-5 dní
3. **Pokročilé Features** 🚀 - 1 týždeň

---

## 📁 Vygenerovaná Štruktúra Projektu

Každý vygenerovaný projekt obsahuje:

```
novy-projekt/
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

## 🎯 Kritériá Úspechu

**MVP:**
- ✅ Jeden príkaz vytvorí celý projekt
- ✅ GitHub repo automaticky
- ✅ Všetky súbory z šablón
- ✅ Čas generovania < 60 sekúnd
- ✅ Raw URL funkčné pre Claude

---

## ⚙️ Príklad Konfigurácie

```yaml
project:
  name: "Môj Nový Projekt"
  slug: "moj-novy-projekt"
  description: "Popis projektu"

github:
  username: "tvoj-username"
  repo_name: "moj-novy-projekt"
  visibility: "private"

developer:
  name: "Tvoje Meno"
  email: "tvoj@email.com"

tech_stack:
  backend: ["fastapi"]
  databases: ["postgresql"]
```

---

## 🔧 Bežné Úlohy

### Začni Vývojovú Session
1. Načítaj project context
2. Over PROJECT_STATUS.md
3. Vyber task na ktorom pracuješ

### Vygeneruj Nový Projekt
```bash
python src/generator/project_creator.py --config configs/moj_projekt.yaml
```

### Spusti Testy
```bash
pytest tests/ -v
```

### Aktualizuj Dokumentáciu
```bash
python scripts/generate_project_access.py
```

---

## 📞 Zdroje

- **GitHub:** https://github.com/rauschiccsk/project-generator
- **Lokálne:** c:\Development\project-generator
- **Context URL:** https://raw.githubusercontent.com/rauschiccsk/project-generator/main/docs/FULL_PROJECT_CONTEXT.md
- **Vývojár:** ICC (rausch@icc.sk)

---

## 🎓 Inšpirácia

- **supplier_invoice_loader** - Multi-customer vzory
- **orthodox-portal** - Dokumentačná štruktúra

Oba projekty dokázali že "single raw URL" workflow funguje perfektne.

---

**Verzia:** 0.1.0  
**Aktualizované:** 2025-10-20  
**Stav:** Aktívny Vývoj

🏭 **Automatizuj. Generuj. Vytváraj.**