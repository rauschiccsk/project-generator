"""
Generate project_file_access.json for GitHub raw URLs

This script scans the project directory and creates a JSON file
with all project files and their GitHub raw URLs.
"""

import json
import os
from pathlib import Path
from typing import List, Dict

# Configuration
GITHUB_USERNAME = "rauschiccsk"
GITHUB_REPO = "project-generator"
GITHUB_BRANCH = "main"
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_FILE = PROJECT_ROOT / "docs" / "project_file_access.json"

# Files and directories to ignore
IGNORE_PATTERNS = {
    "__pycache__",
    ".git",
    ".idea",
    "venv",
    ".venv",  # Virtual environment
    "env",
    ".env",
    "ENV",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    ".hypothesis",
    "htmlcov",
    "*.pyc",
    "*.pyo",
    "*.pyd",
    "*.so",
    "*.egg",
    "*.egg-info",
    ".env",
    ".env.local",
    "*.log",
    ".DS_Store",
    "Thumbs.db",
    "node_modules",
    "dist",
    "build",
    "*.tmp",
    "*.temp",
    "*.swp",
    "*.swo",
    "configs/queue",
    "configs/processed",
    "examples/example_generated_project",
}


def should_ignore(path: Path) -> bool:
    """Check if path should be ignored"""
    path_str = str(path)

    # Check if path contains any ignored directory
    parts = path.parts
    for part in parts:
        if part in IGNORE_PATTERNS:
            return True

    # Check exact filename matches
    if path.name in IGNORE_PATTERNS:
        return True

    # Check patterns with wildcards
    for pattern in IGNORE_PATTERNS:
        if "*" in pattern:
            ext = pattern.replace("*", "")
            if path_str.endswith(ext):
                return True

    return False


def get_all_files(root_dir: Path) -> List[Path]:
    """Get all project files, excluding ignored patterns"""
    files = []

    for item in root_dir.rglob("*"):
        if item.is_file() and not should_ignore(item):
            files.append(item)

    return sorted(files)


def generate_raw_url(relative_path: str) -> str:
    """Generate GitHub raw URL for a file"""
    # Replace backslashes with forward slashes for URL
    url_path = relative_path.replace("\\", "/")
    return f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{url_path}"


def create_file_structure(files: List[Path], root: Path) -> Dict:
    """Create nested dictionary structure from file paths"""
    structure = {
        "project": "project-generator",
        "github_repo": f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}",
        "branch": GITHUB_BRANCH,
        "generated_at": "",  # Will be filled by caller
        "total_files": len(files),
        "files": []
    }

    for file_path in files:
        relative_path = file_path.relative_to(root)
        relative_str = str(relative_path)

        file_info = {
            "path": relative_str,
            "name": file_path.name,
            "size": file_path.stat().st_size,
            "raw_url": generate_raw_url(relative_str)
        }

        structure["files"].append(file_info)

    return structure


def main():
    """Main function"""
    print("🔍 Scanning project files...")
    print(f"   Root directory: {PROJECT_ROOT}")
    print(f"   Ignoring: {', '.join(sorted([p for p in IGNORE_PATTERNS if not p.startswith('*')]))}")

    # Get all files
    files = get_all_files(PROJECT_ROOT)
    print(f"   Found {len(files)} files (after filtering)")

    # Show some examples
    if len(files) > 0:
        print(f"\n📄 Sample files:")
        for f in files[:5]:
            rel = f.relative_to(PROJECT_ROOT)
            print(f"   - {rel}")
        if len(files) > 5:
            print(f"   ... and {len(files) - 5} more")

    # Create structure
    print("\n📝 Creating file structure...")
    structure = create_file_structure(files, PROJECT_ROOT)

    # Add timestamp
    from datetime import datetime
    structure["generated_at"] = datetime.now().isoformat()

    # Write to JSON
    print(f"💾 Writing to {OUTPUT_FILE}...")
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(structure, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Done! Generated {OUTPUT_FILE}")
    print(f"   Total files: {structure['total_files']}")
    print(f"   File size: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")
    print(f"\n📄 Raw URL:")
    print(f"   {generate_raw_url('docs/project_file_access.json')}")

    # Warning if too many files
    if structure['total_files'] > 100:
        print(f"\n⚠️  WARNING: {structure['total_files']} files might be too many!")
        print(f"   Consider adding more patterns to IGNORE_PATTERNS")


if __name__ == "__main__":
    main()