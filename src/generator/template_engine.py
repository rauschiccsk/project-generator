"""
Template Engine pre Project Generator.

Používa Jinja2 na renderovanie projektových šablón.
"""

from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, Template, TemplateNotFound
from jinja2.exceptions import TemplateError

from src.models.project_config import ProjectConfig


class TemplateEngine:
    """
    Jinja2 Template Engine pre generovanie projektových súborov.

    Načítava šablóny z src/templates/ a renderuje ich s dátami
    z ProjectConfig modelu.
    """

    def __init__(self, templates_dir: Optional[Path] = None):
        """
        Inicializácia Template Engine.

        Args:
            templates_dir: Cesta k priečinku so šablónami.
                          Ak None, použije sa src/templates/
        """
        if templates_dir is None:
            # Relatívna cesta od tohto súboru
            base_dir = Path(__file__).parent.parent
            templates_dir = base_dir / "templates"

        self.templates_dir = templates_dir

        # Jinja2 Environment setup
        self.env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            trim_blocks=True,  # Odstrániť prázdne riadky
            lstrip_blocks=True,  # Odstrániť whitespace pred blokom
            keep_trailing_newline=True  # Zachovať newline na konci
        )

        # Custom filters (voliteľné)
        self.env.filters['slugify'] = self._slugify
        self.env.filters['uppercase'] = str.upper
        self.env.filters['lowercase'] = str.lower
        self.env.filters['date'] = self._date_filter

    @staticmethod
    def _slugify(text: str) -> str:
        """
        Konvertuje text na slug (lowercase, pomlčky namiesto medzier).

        Args:
            text: Vstupný text

        Returns:
            Slug verzia textu
        """
        return text.lower().replace(' ', '-').replace('_', '-')

    @staticmethod
    def _date_filter(value: str, format: str = "%Y-%m-%d") -> str:
        """
        Date filter pre Jinja2.

        Args:
            value: Hodnota (ignorovaná, vždy použije aktuálny dátum)
            format: Formát dátumu

        Returns:
            Formátovaný dátum
        """
        from datetime import datetime
        return datetime.now().strftime(format)

    def load_template(self, template_name: str) -> Template:
        """
        Načíta Jinja2 šablónu.

        Args:
            template_name: Názov šablóny (relatívna cesta v templates/)
                          napr. "project_files/readme.md.j2"

        Returns:
            Jinja2 Template objekt

        Raises:
            TemplateNotFound: Ak šablóna neexistuje
        """
        try:
            return self.env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(
                f"Šablóna '{template_name}' nebola nájdená v {self.templates_dir}"
            )

    def render_template(
            self,
            template_name: str,
            context: Dict[str, Any]
    ) -> str:
        """
        Renderuje šablónu s poskytnutým kontextom.

        Args:
            template_name: Názov šablóny
            context: Dictionary s dátami pre šablónu

        Returns:
            Vyrenderovaný obsah ako string

        Raises:
            TemplateNotFound: Ak šablóna neexistuje
            TemplateError: Ak nastane chyba pri renderovaní
        """
        try:
            template = self.load_template(template_name)
            return template.render(**context)
        except TemplateError as e:
            raise TemplateError(
                f"Chyba pri renderovaní '{template_name}': {str(e)}"
            )

    def render_from_config(
            self,
            template_name: str,
            config: ProjectConfig
    ) -> str:
        """
        Renderuje šablónu z ProjectConfig modelu.

        Args:
            template_name: Názov šablóny
            config: ProjectConfig objekt s dátami projektu

        Returns:
            Vyrenderovaný obsah
        """
        # Konvertuj Pydantic model na dict pre Jinja2
        context = config.model_dump()
        return self.render_template(template_name, context)

    def render_all_templates(
            self,
            config: ProjectConfig
    ) -> Dict[str, str]:
        """
        Renderuje všetky projektové šablóny.

        Args:
            config: ProjectConfig s dátami projektu

        Returns:
            Dictionary kde kľúč je názov súboru a hodnota je obsah
            Formát: {
                "FULL_PROJECT_CONTEXT.md": "...",
                "README.md": "...",
                ...
            }
        """
        templates_map = {
            # Dokumentácia
            "FULL_PROJECT_CONTEXT.md": "project_files/full_context.md.j2",
            "PROJECT_STATUS.md": "project_files/project_status.md.j2",
            "README.md": "project_files/readme.md.j2",

            # Konfigurácia
            "requirements.txt": "project_files/requirements.txt.j2",
            ".gitignore": "project_files/gitignore.j2",
        }

        rendered_files = {}

        for output_name, template_name in templates_map.items():
            try:
                rendered_files[output_name] = self.render_from_config(
                    template_name,
                    config
                )
            except TemplateError as e:
                # Log error ale pokračuj s ďalšími šablónami
                print(f"⚠️ Chyba pri renderovaní {output_name}: {e}")
                continue

        return rendered_files

    def validate_templates(self) -> Dict[str, bool]:
        """
        Validuje či všetky potrebné šablóny existujú.

        Returns:
            Dictionary kde kľúč je názov šablóny a hodnota je bool (existuje?)
        """
        required_templates = [
            "project_files/full_context.md.j2",
            "project_files/project_status.md.j2",
            "project_files/readme.md.j2",
            "project_files/requirements.txt.j2",
            "project_files/gitignore.j2",
        ]

        validation_results = {}

        for template in required_templates:
            template_path = self.templates_dir / template
            validation_results[template] = template_path.exists()

        return validation_results

    def get_missing_templates(self) -> list[str]:
        """
        Vráti zoznam chýbajúcich šablón.

        Returns:
            List názvov šablón ktoré neexistujú
        """
        validation = self.validate_templates()
        return [name for name, exists in validation.items() if not exists]


# Helper funkcia pre rýchle použitie
def render_project_files(config: ProjectConfig) -> Dict[str, str]:
    """
    Jednoduchá helper funkcia pre renderovanie projektových súborov.

    Args:
        config: ProjectConfig objekt

    Returns:
        Dictionary vyrenderovaných súborov

    Example:
        >>> config = ProjectConfig.from_yaml("config.yaml")
        >>> files = render_project_files(config)
        >>> print(files["README.md"])
    """
    engine = TemplateEngine()
    return engine.render_all_templates(config)