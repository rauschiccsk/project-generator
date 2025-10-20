"""
YAML Config Parser pre Project Generator.

Načíta a validuje YAML konfiguračný súbor pomocou Pydantic modelov.
"""

from pathlib import Path
from typing import Optional
import yaml
from pydantic import ValidationError

from src.models.project_config import ProjectConfig


class ConfigParserError(Exception):
    """Vlastná výjimka pre chyby parsera."""
    pass


class ConfigParser:
    """
    Parser pre YAML konfiguračné súbory.

    Načíta YAML súbor a validuje ho pomocou Pydantic ProjectConfig modelu.
    """

    def __init__(self, config_path: Path | str):
        """
        Inicializuje parser s cestou ku config súboru.

        Args:
            config_path: Cesta k YAML config súboru

        Raises:
            ConfigParserError: Ak súbor neexistuje alebo nie je YAML
        """
        self.config_path = Path(config_path)
        self._validate_path()

    def _validate_path(self) -> None:
        """Validuje že config súbor existuje a je YAML."""
        if not self.config_path.exists():
            raise ConfigParserError(
                f"Config súbor neexistuje: {self.config_path}"
            )

        if not self.config_path.is_file():
            raise ConfigParserError(
                f"Cesta nie je súbor: {self.config_path}"
            )

        if self.config_path.suffix.lower() not in ['.yaml', '.yml']:
            raise ConfigParserError(
                f"Súbor musí mať príponu .yaml alebo .yml: {self.config_path}"
            )

    def parse(self) -> ProjectConfig:
        """
        Načíta a sparsuje YAML config.

        Returns:
            ProjectConfig objekt s validovanými dátami

        Raises:
            ConfigParserError: Pri chybách čítania alebo parsovania
        """
        try:
            raw_data = self._load_yaml()
            config = self._validate_config(raw_data)
            return config

        except yaml.YAMLError as e:
            raise ConfigParserError(
                f"Chyba v YAML syntaxi: {str(e)}"
            ) from e

        except ValidationError as e:
            raise ConfigParserError(
                f"Validačná chyba v konfigurácii:\n{self._format_validation_error(e)}"
            ) from e

        except Exception as e:
            raise ConfigParserError(
                f"Neočakávaná chyba pri parsovaní: {str(e)}"
            ) from e

    def _load_yaml(self) -> dict:
        """
        Načíta YAML súbor do dictionary.

        Returns:
            Dictionary s YAML dátami

        Raises:
            yaml.YAMLError: Pri chybách v YAML syntaxi
        """
        with open(self.config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if data is None:
            raise ConfigParserError("Config súbor je prázdny")

        if not isinstance(data, dict):
            raise ConfigParserError(
                f"Config musí obsahovať YAML dictionary, nie {type(data).__name__}"
            )

        return data

    def _validate_config(self, data: dict) -> ProjectConfig:
        """
        Validuje raw data pomocou Pydantic modelu.

        Args:
            data: Raw dictionary z YAML

        Returns:
            Validovaný ProjectConfig objekt

        Raises:
            ValidationError: Pri validačných chybách
        """
        return ProjectConfig(**data)

    def _format_validation_error(self, error: ValidationError) -> str:
        """
        Formátuje Pydantic validation error do čitateľného textu.

        Args:
            error: ValidationError z Pydantic

        Returns:
            Formátovaný error message
        """
        errors = []
        for err in error.errors():
            loc = " -> ".join(str(x) for x in err['loc'])
            msg = err['msg']
            errors.append(f"  • {loc}: {msg}")

        return "\n".join(errors)

    @staticmethod
    def parse_file(config_path: Path | str) -> ProjectConfig:
        """
        Jednoduchý helper pre rýchle parsovanie.

        Args:
            config_path: Cesta k YAML config súboru

        Returns:
            ProjectConfig objekt

        Example:
            >>> config = ConfigParser.parse_file("configs/my_project.yaml")
        """
        parser = ConfigParser(config_path)
        return parser.parse()

    @staticmethod
    def validate_yaml_string(yaml_string: str) -> tuple[bool, Optional[str]]:
        """
        Validuje YAML string bez ukladania do súboru.

        Args:
            yaml_string: YAML string na validáciu

        Returns:
            Tuple (is_valid, error_message)

        Example:
            >>> is_valid, error = ConfigParser.validate_yaml_string(yaml_text)
            >>> if not is_valid:
            ...     print(f"Chyba: {error}")
        """
        try:
            data = yaml.safe_load(yaml_string)

            if data is None:
                return False, "YAML je prázdny"

            if not isinstance(data, dict):
                return False, f"YAML musí byť dictionary, nie {type(data).__name__}"

            # Validuj cez Pydantic
            ProjectConfig(**data)
            return True, None

        except yaml.YAMLError as e:
            return False, f"YAML syntax error: {str(e)}"

        except ValidationError as e:
            errors = []
            for err in e.errors():
                loc = " -> ".join(str(x) for x in err['loc'])
                errors.append(f"{loc}: {err['msg']}")
            return False, "\n".join(errors)

        except Exception as e:
            return False, f"Neočakávaná chyba: {str(e)}"


def load_config(config_path: Path | str) -> ProjectConfig:
    """
    Convenience funkcia pre načítanie configu.

    Args:
        config_path: Cesta k YAML config súboru

    Returns:
        ProjectConfig objekt

    Example:
        >>> from src.generator.config_parser import load_config
        >>> config = load_config("configs/monastier_online.yaml")
        >>> print(config.project.name)
    """
    return ConfigParser.parse_file(config_path)


# Example použitia:
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python config_parser.py <config.yaml>")
        sys.exit(1)

    try:
        config = load_config(sys.argv[1])
        print("✅ Config validovaný úspešne!")
        print(f"\nProjekt: {config.project.name}")
        print(f"Slug: {config.project.slug}")
        print(f"GitHub: https://github.com/{config.github.username}/{config.github.repo_name}")
        print(f"Lokálna cesta: {config.paths.local_dev}")

    except ConfigParserError as e:
        print(f"❌ Chyba: {e}")
        sys.exit(1)