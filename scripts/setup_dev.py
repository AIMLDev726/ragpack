#!/usr/bin/env python3
"""
Development Setup Script for ragpackai

This script helps set up a development environment for ragpackai.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print(f"❌ Python 3.9+ required, found {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def setup_virtual_environment():
    """Set up virtual environment."""
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    print("🔧 Creating virtual environment...")
    if platform.system() == "Windows":
        command = "python -m venv venv"
    else:
        command = "python3 -m venv venv"
    
    return run_command(command, "Virtual environment creation")

def install_dependencies():
    """Install development dependencies."""
    if platform.system() == "Windows":
        pip_command = "venv\\Scripts\\pip"
    else:
        pip_command = "venv/bin/pip"
    
    commands = [
        (f"{pip_command} install --upgrade pip", "Upgrading pip"),
        (f"{pip_command} install -e .", "Installing ragpackai in development mode"),
        (f"{pip_command} install -e .[dev]", "Installing development dependencies"),
        (f"{pip_command} install -e .[all]", "Installing all optional dependencies"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    return True

def setup_pre_commit():
    """Set up pre-commit hooks."""
    if platform.system() == "Windows":
        pre_commit_command = "venv\\Scripts\\pre-commit"
    else:
        pre_commit_command = "venv/bin/pre-commit"
    
    return run_command(f"{pre_commit_command} install", "Setting up pre-commit hooks")

def create_env_file():
    """Create a sample .env file."""
    env_file = Path(".env")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    env_content = """# ragpackai Development Environment Variables
# Copy this file and add your actual API keys

# OpenAI (required for most examples)
OPENAI_API_KEY=your_openai_api_key_here

# Google AI (optional)
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CLOUD_PROJECT=your_google_cloud_project

# Groq (optional)
GROQ_API_KEY=your_groq_api_key_here

# Cerebras (optional)
CEREBRAS_API_KEY=your_cerebras_api_key_here

# Development settings
ragpackai_DEBUG=true
ragpackai_LOG_LEVEL=DEBUG
"""
    
    try:
        env_file.write_text(env_content)
        print("✅ Created sample .env file")
        print("💡 Edit .env file with your actual API keys")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def run_tests():
    """Run the test suite to verify setup."""
    if platform.system() == "Windows":
        pytest_command = "venv\\Scripts\\pytest"
    else:
        pytest_command = "venv/bin/pytest"
    
    return run_command(f"{pytest_command} tests/ -v", "Running test suite")

def print_next_steps():
    """Print next steps for the developer."""
    print("\n" + "="*60)
    print("🎉 Development environment setup complete!")
    print("="*60)
    
    if platform.system() == "Windows":
        activate_command = "venv\\Scripts\\activate"
    else:
        activate_command = "source venv/bin/activate"
    
    print(f"\n📋 Next steps:")
    print(f"1. Activate virtual environment:")
    print(f"   {activate_command}")
    print(f"\n2. Edit .env file with your API keys:")
    print(f"   # Add your OpenAI API key and other provider keys")
    print(f"\n3. Run examples:")
    print(f"   python examples/basic_usage.py")
    print(f"   jupyter notebook examples/01_getting_started.ipynb")
    print(f"\n4. Run tests:")
    print(f"   pytest tests/ -v")
    print(f"\n5. Code formatting:")
    print(f"   black ragpackai tests examples")
    print(f"   flake8 ragpackai tests examples")
    print(f"\n6. Build package:")
    print(f"   python -m build")
    print(f"\n💡 See CONTRIBUTING.md for detailed development guidelines")

def main():
    """Main setup function."""
    print("🚀 ragpackai Development Environment Setup")
    print("="*50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Setup steps
    steps = [
        ("Python version check", lambda: True),  # Already done
        ("Virtual environment setup", setup_virtual_environment),
        ("Dependency installation", install_dependencies),
        ("Pre-commit hooks setup", setup_pre_commit),
        ("Environment file creation", create_env_file),
        ("Test suite verification", run_tests),
    ]
    
    failed_steps = []
    
    for step_name, step_function in steps:
        if step_name == "Python version check":
            continue  # Already done
            
        if not step_function():
            failed_steps.append(step_name)
    
    if failed_steps:
        print(f"\n❌ Setup completed with {len(failed_steps)} failed steps:")
        for step in failed_steps:
            print(f"   - {step}")
        print("\n💡 You may need to fix these issues manually")
    else:
        print("\n✅ All setup steps completed successfully!")
    
    print_next_steps()

if __name__ == "__main__":
    main()