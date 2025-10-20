"""
Pydantic modely pre validáciu konfigurácie projektu.

Tento modul obsahuje všetky potrebné modely pre parsovanie a validáciu
YAML konfigurácie nového projektu.
"""

from typing import Optional, List, Union
from pathlib import Path
from pydantic import BaseModel, Field, field_validator, EmailStr
import re
import yaml


class ProjectInfo(BaseModel):
    """Základné informácie o projekte."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Názov projektu (ľudsky čitateľný)"
    )
    slug: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="URL-friendly názov projektu (lowercase, pomlčky)"
    )
    description: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Krátky popis projektu"
    )

    @field_validator('slug')
    @classmethod
    def validate_slug(cls, v: str) -> str:
        """
        Validácia slug formátu.

        Slug musí byť:
        - lowercase
        - len alfanumerické znaky a pomlčky
        - nemôže začínať ani končiť pomlčkou
        """
        if not re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', v):
            raise ValueError(
                "Slug musí byť lowercase, alfanumerický a môže obsahovať pomlčky "
                "(napr. 'moj-novy-projekt')"
            )
        return v


class GitHubConfig(BaseModel):
    """Konfigurácia GitHub repository."""

    username: str = Field(
        ...,
        min_length=1,
        max_length=39,
        description="GitHub username"
    )
    repo_name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Názov GitHub repository"
    )
    visibility: str = Field(
        default="private",
        description="Viditeľnosť repozitára (public/private)"
    )

    @field_validator('visibility')
    @classmethod
    def validate_visibility(cls, v: str) -> str:
        """Validácia visibility hodnoty."""
        if v not in ['public', 'private']:
            raise ValueError("Visibility musí byť 'public' alebo 'private'")
        return v

    @field_validator('repo_name')
    @classmethod
    def validate_repo_name(cls, v: str) -> str:
        """
        Validácia GitHub repo name.

        Repo name musí byť validný GitHub názov.
        """
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError(
                "Repo name môže obsahovať len alfanumerické znaky, "
                "pomlčky a podčiarkovníky"
            )
        return v


class DeveloperInfo(BaseModel):
    """Informácie o vývojárovi."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Meno vývojára alebo organizácie"
    )
    email: EmailStr = Field(
        ...,
        description="Kontaktný email vývojára"
    )


class PathsConfig(BaseModel):
    """Konfigurácia ciest k projektom."""

    local_dev: str = Field(
        ...,
        description="Cesta k development prostrediu"
    )
    local_deploy: Optional[str] = Field(
        default=None,
        description="Cesta k deployment prostrediu (voliteľné)"
    )

    @field_validator('local_dev', 'local_deploy')
    @classmethod
    def validate_path(cls, v: Optional[str]) -> Optional[str]:
        """Validácia že cesta existuje alebo je validný formát."""
        if v is None:
            return v

        # Kontrola základného formátu cesty
        try:
            Path(v)
        except Exception:
            raise ValueError(f"Neplatný formát cesty: {v}")

        return v


class TechStackConfig(BaseModel):
    """Konfigurácia technologického stacku."""

    backend: List[str] = Field(
        default_factory=list,
        description="Backend technológie (napr. fastapi, django)"
    )
    frontend: List[str] = Field(
        default_factory=list,
        description="Frontend technológie (napr. react, jinja2)"
    )
    databases: List[str] = Field(
        default_factory=list,
        description="Databázy (napr. postgresql, mongodb)"
    )
    automation: List[str] = Field(
        default_factory=list,
        description="Automatizačné nástroje (napr. n8n, airflow)"
    )

    @field_validator('backend', 'frontend', 'databases', 'automation')
    @classmethod
    def validate_tech_list(cls, v: List[str]) -> List[str]:
        """Validácia že technológie sú lowercase."""
        return [tech.lower().strip() for tech in v if tech.strip()]


class OptionalInfo(BaseModel):
    """Voliteľné informácie o projekte."""

    domain: Optional[str] = Field(
        default=None,
        description="Doménové meno projektu (ak existuje)"
    )
    contact_email: Optional[EmailStr] = Field(
        default=None,
        description="Kontaktný email pre projekt"
    )

    @field_validator('domain')
    @classmethod
    def validate_domain(cls, v: Optional[str]) -> Optional[str]:
        """Validácia domain formátu."""
        if v is None or v == "":
            return None

        # Základná validácia domain formátu
        domain_pattern = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        if not re.match(domain_pattern, v):
            raise ValueError(
                f"Neplatný formát domény: {v}. "
                "Očakávaný formát: example.com"
            )
        return v


class FeaturesConfig(BaseModel):
    """Konfigurácia feature flags."""

    include_auth: bool = Field(
        default=True,
        description="Zahrnutie autentifikácie"
    )
    include_api_docs: bool = Field(
        default=True,
        description="Zahrnutie API dokumentácie"
    )
    include_tests: bool = Field(
        default=True,
        description="Zahrnutie testov"
    )
    include_docker: bool = Field(
        default=False,
        description="Zahrnutie Docker konfigurácie"
    )
    include_cicd: bool = Field(
        default=False,
        description="Zahrnutie CI/CD pipeline"
    )


class ProjectConfig(BaseModel):
    """
    Hlavný konfiguračný model projektu.

    Tento model reprezentuje kompletnú konfiguráciu nového projektu
    načítanú z YAML súboru.
    """

    project: ProjectInfo = Field(
        ...,
        description="Základné informácie o projekte"
    )
    github: GitHubConfig = Field(
        ...,
        description="GitHub konfigurácia"
    )
    developer: DeveloperInfo = Field(
        ...,
        description="Informácie o vývojárovi"
    )
    paths: PathsConfig = Field(
        ...,
        description="Cesty k projektom"
    )
    tech_stack: TechStackConfig = Field(
        default_factory=TechStackConfig,
        description="Technologický stack"
    )
    optional: OptionalInfo = Field(
        default_factory=OptionalInfo,
        description="Voliteľné informácie"
    )
    features: FeaturesConfig = Field(
        default_factory=FeaturesConfig,
        description="Feature flags"
    )

    class Config:
        """Pydantic konfigurácia."""
        str_strip_whitespace = True  # Automaticky trim whitespace
        validate_assignment = True  # Validuj aj pri assignment
        extra = "ignore"  # Ignoruj extra polia v YAML

    def get_full_github_url(self) -> str:
        """Získaj plnú GitHub URL repository."""
        return f"https://github.com/{self.github.username}/{self.github.repo_name}"

    def get_local_project_path(self) -> Path:
        """Získaj Path objekt pre lokálny projekt."""
        return Path(self.paths.local_dev) / self.project.slug

    def get_raw_url_base(self) -> str:
        """Získaj base URL pre raw GitHub súbory."""
        return (
            f"https://raw.githubusercontent.com/"
            f"{self.github.username}/{self.github.repo_name}/main"
        )

    @classmethod
    def from_yaml(cls, yaml_path: Union[str, Path]) -> "ProjectConfig":
        """
        Načíta ProjectConfig z YAML súboru.

        Args:
            yaml_path: Cesta k YAML súboru (str alebo Path objekt)

        Returns:
            ProjectConfig objekt

        Raises:
            FileNotFoundError: Ak YAML súbor neexistuje
            yaml.YAMLError: Ak YAML má neplatnú syntax
            ValueError: Ak YAML dáta neprechádzajú Pydantic validáciou

        Example:
            >>> config = ProjectConfig.from_yaml("configs/moj_projekt.yaml")
            >>> print(config.project.name)
            Môj Nový Projekt
        """
        # Konvertuj na Path objekt ak je to string
        if isinstance(yaml_path, str):
            yaml_path = Path(yaml_path)

        # Skontroluj existenciu súboru
        if not yaml_path.exists():
            raise FileNotFoundError(
                f"YAML konfiguračný súbor nebol nájdený: {yaml_path}"
            )

        # Načítaj a parsuj YAML
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(
                f"Chyba pri parsovaní YAML súboru {yaml_path}: {str(e)}"
            )

        # Skontroluj či YAML obsahuje dáta
        if data is None:
            raise ValueError(
                f"YAML súbor je prázdny alebo neobsahuje validné dáta: {yaml_path}"
            )

        # Vytvor ProjectConfig pomocou Pydantic validácie
        try:
            return cls(**data)
        except Exception as e:
            raise ValueError(
                f"Chyba pri validácii YAML konfigurácie: {str(e)}"
            )

    def to_yaml(self, output_path: Union[str, Path]) -> None:
        """
        Uloží ProjectConfig do YAML súboru.

        Args:
            output_path: Cesta kam uložiť YAML súbor

        Raises:
            IOError: Ak sa nepodarí zapísať súbor

        Example:
            >>> config = ProjectConfig(...)
            >>> config.to_yaml("configs/export.yaml")
        """
        if isinstance(output_path, str):
            output_path = Path(output_path)

        # Vytvor priečinok ak neexistuje
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Konvertuj model na dict a ulož ako YAML
        data = self.model_dump(mode='json', exclude_none=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(
                data,
                f,
                default_flow_style=False,
                allow_unicode=True,
                sort_keys=False
            )

    def to_dict(self) -> dict:
        """
        Konvertuje ProjectConfig na dictionary.

        Returns:
            Dictionary reprezentácia konfigurácie

        Example:
            >>> config = ProjectConfig.from_yaml("config.yaml")
            >>> data = config.to_dict()
            >>> print(data['project']['name'])
        """
        return self.model_dump(mode='json', exclude_none=True)