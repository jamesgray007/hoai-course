#!/usr/bin/env python3
"""
Setup Validation Script for Hands-on AI for Leaders Course

This script validates your local development environment to ensure you're
ready to work with the course materials. It checks:
- Python version compatibility
- Required packages installation
- API key configuration
- Virtual environment setup
- File structure

Run this script after following the setup instructions in docs/local_setup.md

Usage:
    python check_setup.py

Author: James Gray
Last Updated: 2025-10-11
"""

import sys
import os
from pathlib import Path
from typing import List, Tuple

# ANSI color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def print_header(text: str) -> None:
    """Print a formatted section header."""
    print(f"\n{BLUE}{'=' * 60}{RESET}")
    print(f"{BLUE}{text}{RESET}")
    print(f"{BLUE}{'=' * 60}{RESET}")


def print_success(text: str) -> None:
    """Print a success message."""
    print(f"{GREEN}✓ {text}{RESET}")


def print_error(text: str) -> None:
    """Print an error message."""
    print(f"{RED}✗ {text}{RESET}")


def print_warning(text: str) -> None:
    """Print a warning message."""
    print(f"{YELLOW}⚠ {text}{RESET}")


def check_python_version() -> bool:
    """Check if Python version is 3.10 or higher."""
    print_header("Checking Python Version")

    version = sys.version_info
    version_string = f"{version.major}.{version.minor}.{version.micro}"

    if version.major >= 3 and version.minor >= 10:
        print_success(f"Python {version_string} detected (3.10+ required)")
        return True
    else:
        print_error(f"Python {version_string} detected. Version 3.10+ required")
        print(f"  Please upgrade Python: https://www.python.org/downloads/")
        return False


def check_virtual_environment() -> bool:
    """Check if running inside a virtual environment."""
    print_header("Checking Virtual Environment")

    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )

    if in_venv:
        print_success("Running inside a virtual environment")
        return True
    else:
        print_warning("Not running in a virtual environment")
        print("  It's recommended to use a virtual environment (.venv)")
        print("  See docs/local_setup.md for setup instructions")
        return False


def check_required_packages() -> Tuple[bool, List[str]]:
    """Check if required Python packages are installed."""
    print_header("Checking Required Packages")

    required_packages = {
        'openai': 'OpenAI API client',
        'agents': 'OpenAI Agents SDK (openai-agents)',
        'dotenv': 'Environment variable management (python-dotenv)',
        'httpx': 'HTTP client for API requests',
    }

    missing_packages = []
    all_installed = True

    for package, description in required_packages.items():
        try:
            __import__(package)
            print_success(f"{package:15} - {description}")
        except ImportError:
            print_error(f"{package:15} - {description} [NOT INSTALLED]")
            missing_packages.append(package)
            all_installed = False

    if missing_packages:
        print(f"\n  Install missing packages:")
        if 'agents' in missing_packages:
            print(f"    pip install openai-agents")
            missing_packages.remove('agents')
        if 'dotenv' in missing_packages:
            print(f"    pip install python-dotenv")
            missing_packages.remove('dotenv')
        for pkg in missing_packages:
            print(f"    pip install {pkg}")

    return all_installed, missing_packages


def check_env_file() -> Tuple[bool, List[str]]:
    """Check if .env file exists and contains required API keys."""
    print_header("Checking Environment Configuration")

    env_path = Path('.env')

    if not env_path.exists():
        print_error(".env file not found in project root")
        print("  1. Copy .env.example to .env")
        print("  2. Add your API keys to .env")
        print("  See .env.example for required keys")
        return False, []

    print_success(".env file found")

    # Load and check .env contents
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print_warning("python-dotenv not installed, cannot validate keys")
        return True, []

    required_keys = {
        'OPENAI_API_KEY': 'Required for all weeks',
        'VECTOR_STORE_ID': 'Required for Week 4 file search',
    }

    optional_keys = {
        'PERPLEXITY_API_KEY': 'Optional for Week 3',
        'GOOGLE_API_KEY': 'Optional for Week 3',
        'ANTHROPIC_API_KEY': 'Optional for Week 3',
    }

    missing_keys = []

    print("\n  Required API Keys:")
    for key, description in required_keys.items():
        value = os.getenv(key)
        if value and not value.startswith('your-') and not value.startswith('sk-your'):
            print_success(f"{key:20} - {description}")
        else:
            print_error(f"{key:20} - {description} [NOT SET]")
            missing_keys.append(key)

    print("\n  Optional API Keys:")
    for key, description in optional_keys.items():
        value = os.getenv(key)
        if value and not value.startswith('your-'):
            print_success(f"{key:20} - {description}")
        else:
            print_warning(f"{key:20} - {description} [NOT SET]")

    if missing_keys:
        print("\n  Add missing keys to your .env file")
        print("  See .env.example for instructions")

    return len(missing_keys) == 0, missing_keys


def check_project_structure() -> bool:
    """Check if expected project directories exist."""
    print_header("Checking Project Structure")

    required_dirs = [
        'src/week-1',
        'src/week-2',
        'src/week-3',
        'src/week-4',
        'docs',
    ]

    all_exist = True

    for dir_path in required_dirs:
        path = Path(dir_path)
        if path.exists() and path.is_dir():
            print_success(f"Directory found: {dir_path}")
        else:
            print_error(f"Directory missing: {dir_path}")
            all_exist = False

    return all_exist


def print_summary(checks: dict) -> None:
    """Print a summary of all checks."""
    print_header("Setup Validation Summary")

    passed = sum(1 for v in checks.values() if v)
    total = len(checks)

    for check_name, result in checks.items():
        if result:
            print_success(check_name)
        else:
            print_error(check_name)

    print(f"\n{BLUE}Result: {passed}/{total} checks passed{RESET}\n")

    if passed == total:
        print_success("Your setup is complete! You're ready to start the course.")
        print("\n  Next steps:")
        print("  - Review the README.md for course structure")
        print("  - Start with Week 1 prompt templates")
        print("  - Join the course community for support")
    else:
        print_warning("Please address the issues above before starting")
        print("\n  Resources:")
        print("  - Setup guide: docs/local_setup.md")
        print("  - Example environment: .env.example")
        print("  - Course support: Maven platform community")


def main() -> None:
    """Run all validation checks."""
    print(f"\n{BLUE}{'=' * 60}{RESET}")
    print(f"{BLUE}Hands-on AI for Leaders - Setup Validation{RESET}")
    print(f"{BLUE}{'=' * 60}{RESET}")

    checks = {
        "Python Version": check_python_version(),
        "Virtual Environment": check_virtual_environment(),
        "Required Packages": check_required_packages()[0],
        "Environment Configuration": check_env_file()[0],
        "Project Structure": check_project_structure(),
    }

    print_summary(checks)

    # Exit with appropriate code
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Validation cancelled by user{RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{RED}Error during validation: {e}{RESET}")
        sys.exit(1)
