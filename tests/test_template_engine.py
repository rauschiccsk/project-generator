"""
Pytest testy pre Template Engine.

Spustenie:
    pytest tests/test_template_engine.py -v
    pytest tests/test_template_engine.py::test_load_config -v
"""

import pytest
from pathlib import Path
from src.models.project_config import ProjectConfig
from src.generator.template_engine import TemplateEngine
from jinja2.exceptions import TemplateNotFound


# === FIXTURES ===

@pytest.fixture
def config_path():
    """Vráti cestu k test configu."""
    return Path("configs/config_template.yaml")


@pytest.fixture
def project_config(config_path):
    """Načíta ProjectConfig z YAML súboru."""
    return ProjectConfig.from_yaml(config_path)


@pytest.fixture
def template_engine():
    """Vytvorí TemplateEngine inštanciu."""
    return TemplateEngine()


# === TESTY CONFIG LOADING ===

def test_config_file_exists(config_path):
    """Test či config súbor existuje."""
    assert config_path.exists(), f"Config súbor neexistuje: {config_path}"


def test_load_config(config_path):
    """Test načítania konfigurácie z YAML."""
    config = ProjectConfig.from_yaml(config_path)

    assert config is not None, "Config je None"
    assert config.project is not None, "project sekcia je None"
    assert config.project.name, "project.name je prázdne"
    assert config.github.username, "github.username je prázdne"


def test_config_structure(project_config):
    """Test štruktúry načítaného configu."""
    # Základné sekcie
    assert hasattr(project_config, 'project')
    assert hasattr(project_config, 'github')
    assert hasattr(project_config, 'developer')
    assert hasattr(project_config, 'paths')
    assert hasattr(project_config, 'tech_stack')

    # Project info
    assert project_config.project.name
    assert project_config.project.slug
    assert project_config.project.description

    # GitHub info
    assert project_config.github.username == "rauschiccsk"
    assert project_config.github.repo_name
    assert project_config.github.visibility in ['public', 'private']

    # Developer info
    assert project_config.developer.name
    assert project_config.developer.email


# === TESTY TEMPLATE ENGINE ===

def test_create_template_engine(template_engine):
    """Test vytvorenia Template Engine."""
    assert template_engine is not None
    assert template_engine.templates_dir.exists()
    assert template_engine.env is not None


def test_templates_directory_exists(template_engine):
    """Test že templates priečinok existuje."""
    assert template_engine.templates_dir.exists()
    assert template_engine.templates_dir.is_dir()


def test_validate_templates(template_engine):
    """Test validácie existujúcich šablón."""
    validation = template_engine.validate_templates()

    assert isinstance(validation, dict)
    assert len(validation) > 0

    # Vypíš ktoré šablóny chýbajú
    missing = [name for name, exists in validation.items() if not exists]
    if missing:
        pytest.fail(f"Chýbajúce šablóny: {', '.join(missing)}")


def test_no_missing_templates(template_engine):
    """Test že všetky potrebné šablóny existujú."""
    missing = template_engine.get_missing_templates()

    assert len(missing) == 0, (
            f"Chýbajúce šablóny:\n" +
            "\n".join(f"  - {t}" for t in missing)
    )


def test_load_template(template_engine):
    """Test načítania jednotlivej šablóny."""
    template = template_engine.load_template("project_files/readme.md.j2")
    assert template is not None


def test_load_nonexistent_template(template_engine):
    """Test že neexistujúca šablóna vyvolá error."""
    with pytest.raises(TemplateNotFound):
        template_engine.load_template("nonexistent/template.j2")


# === TESTY RENDEROVANIE ===

def test_render_readme(template_engine, project_config):
    """Test renderovania README šablóny."""
    content = template_engine.render_from_config(
        "project_files/readme.md.j2",
        project_config
    )

    assert content
    assert len(content) > 100
    assert project_config.project.name in content
    assert project_config.github.username in content


def test_render_requirements(template_engine, project_config):
    """Test renderovania requirements.txt šablóny."""
    content = template_engine.render_from_config(
        "project_files/requirements.txt.j2",
        project_config
    )

    assert content
    assert "# " in content  # Komentáre

    # Skontroluj tech stack závislosti
    if 'fastapi' in project_config.tech_stack.backend:
        assert 'fastapi' in content.lower()


def test_render_gitignore(template_engine, project_config):
    """Test renderovania .gitignore šablóny."""
    content = template_engine.render_from_config(
        "project_files/gitignore.j2",
        project_config
    )

    assert content
    assert "__pycache__" in content
    assert ".env" in content
    assert "*.py[cod]" in content


def test_render_full_context(template_engine, project_config):
    """Test renderovania FULL_PROJECT_CONTEXT.md šablóny."""
    content = template_engine.render_from_config(
        "project_files/full_context.md.j2",
        project_config
    )

    assert content
    assert len(content) > 1000

    # Kľúčové sekcie
    assert "KOMPLETNÝ KONTEXT PROJEKTU" in content
    assert "INSTRUCTIONS FOR CLAUDE" in content
    assert project_config.project.name.upper() in content
    assert project_config.github.username in content
    assert "Tech Stack" in content


def test_render_project_status(template_engine, project_config):
    """Test renderovania PROJECT_STATUS.md šablóny."""
    content = template_engine.render_from_config(
        "project_files/project_status.md.j2",
        project_config
    )

    assert content
    assert "PROJECT STATUS" in content
    assert project_config.project.name in content


def test_render_all_templates(template_engine, project_config):
    """Test renderovania všetkých šablón naraz."""
    all_files = template_engine.render_all_templates(project_config)

    assert isinstance(all_files, dict)
    assert len(all_files) > 0

    # Očakávané súbory
    expected_files = [
        "FULL_PROJECT_CONTEXT.md",
        "PROJECT_STATUS.md",
        "README.md",
        "requirements.txt",
        ".gitignore"
    ]

    for expected_file in expected_files:
        assert expected_file in all_files, f"Chýba súbor: {expected_file}"
        assert all_files[expected_file], f"Súbor je prázdny: {expected_file}"


def test_rendered_content_not_empty(template_engine, project_config):
    """Test že všetky vyrenderované súbory majú obsah."""
    all_files = template_engine.render_all_templates(project_config)

    for filename, content in all_files.items():
        assert content, f"Súbor {filename} je prázdny"
        assert len(content) > 10, f"Súbor {filename} je príliš krátky"


# === TESTY CUSTOM FILTERS ===

def test_slugify_filter(template_engine):
    """Test custom slugify filtra."""
    result = template_engine._slugify("My New Project")
    assert result == "my-new-project"

    result = template_engine._slugify("Test_With_Underscores")
    assert result == "test-with-underscores"


# === INTEGRATION TESTY ===

def test_full_workflow(config_path):
    """Integration test celého workflow."""
    # 1. Načítaj config
    config = ProjectConfig.from_yaml(config_path)
    assert config is not None

    # 2. Vytvor engine
    engine = TemplateEngine()
    assert engine is not None

    # 3. Validuj šablóny
    missing = engine.get_missing_templates()
    assert len(missing) == 0

    # 4. Renderuj všetky šablóny
    files = engine.render_all_templates(config)
    assert len(files) >= 5

    # 5. Skontroluj že obsahujú správne dáta
    readme = files["README.md"]
    assert config.project.name in readme
    assert config.github.username in readme


# === HELPER PRE DEBUGGING ===

def test_print_config_info(project_config):
    """Helper test pre debugging - vypíše info o configu."""
    print("\n" + "=" * 60)
    print("📋 CONFIG INFO:")
    print("=" * 60)
    print(f"Project Name: {project_config.project.name}")
    print(f"Slug: {project_config.project.slug}")
    print(f"GitHub: {project_config.github.username}/{project_config.github.repo_name}")
    print(f"Developer: {project_config.developer.name}")
    print(f"Backend: {', '.join(project_config.tech_stack.backend)}")
    print(f"Frontend: {', '.join(project_config.tech_stack.frontend)}")
    print("=" * 60)


def test_print_templates_status(template_engine):
    """Helper test pre debugging - vypíše status šablón."""
    validation = template_engine.validate_templates()

    print("\n" + "=" * 60)
    print("📄 TEMPLATES STATUS:")
    print("=" * 60)

    for template, exists in validation.items():
        status = "✅" if exists else "❌"
        print(f"{status} {template}")

    print("=" * 60)
    print(f"Templates dir: {template_engine.templates_dir}")
    print("=" * 60)