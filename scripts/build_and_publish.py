#!/usr/bin/env python3
"""
Build and Publish Script for RAGPack

This script automates the process of building and publishing RAGPack to PyPI.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import argparse

def run_command(command, description, check=True):
    """Run a command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"⚠️ {description} completed with warnings")
            if result.stdout.strip():
                print(f"   stdout: {result.stdout.strip()}")
            if result.stderr.strip():
                print(f"   stderr: {result.stderr.strip()}")
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"   stdout: {e.stdout}")
        if e.stderr:
            print(f"   stderr: {e.stderr}")
        return False

def clean_build_artifacts():
    """Clean previous build artifacts."""
    artifacts = ["build", "dist", "*.egg-info"]
    
    for pattern in artifacts:
        if pattern == "*.egg-info":
            # Find and remove .egg-info directories
            for path in Path(".").glob("*.egg-info"):
                if path.is_dir():
                    print(f"🧹 Removing {path}")
                    shutil.rmtree(path)
        else:
            path = Path(pattern)
            if path.exists():
                print(f"🧹 Removing {path}")
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()

def check_version_consistency():
    """Check that version is consistent across files."""
    # Read version from pyproject.toml
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        print("❌ pyproject.toml not found")
        return False
    
    pyproject_content = pyproject_path.read_text()
    
    # Extract version from pyproject.toml
    import re
    version_match = re.search(r'version = "([^"]+)"', pyproject_content)
    if not version_match:
        print("❌ Version not found in pyproject.toml")
        return False
    
    pyproject_version = version_match.group(1)
    
    # Read version from __init__.py
    init_path = Path("ragpack/__init__.py")
    if not init_path.exists():
        print("❌ ragpack/__init__.py not found")
        return False
    
    init_content = init_path.read_text()
    init_version_match = re.search(r'__version__ = "([^"]+)"', init_content)
    if not init_version_match:
        print("❌ Version not found in ragpack/__init__.py")
        return False
    
    init_version = init_version_match.group(1)
    
    if pyproject_version != init_version:
        print(f"❌ Version mismatch: pyproject.toml={pyproject_version}, __init__.py={init_version}")
        return False
    
    print(f"✅ Version consistency check passed: {pyproject_version}")
    return True

def run_quality_checks():
    """Run code quality checks."""
    checks = [
        ("black --check ragpack tests examples scripts", "Code formatting check"),
        ("flake8 ragpack tests examples scripts", "Linting check"),
        ("mypy ragpack --ignore-missing-imports", "Type checking"),
    ]
    
    all_passed = True
    for command, description in checks:
        if not run_command(command, description, check=False):
            all_passed = False
    
    return all_passed

def run_tests():
    """Run the test suite."""
    return run_command("pytest tests/ -v --tb=short", "Running test suite")

def build_package():
    """Build the package."""
    return run_command("python -m build", "Building package")

def check_package():
    """Check the built package."""
    return run_command("twine check dist/*", "Checking package")

def upload_to_test_pypi():
    """Upload to Test PyPI."""
    return run_command(
        "twine upload --repository testpypi dist/*",
        "Uploading to Test PyPI"
    )

def upload_to_pypi():
    """Upload to PyPI."""
    return run_command("twine upload dist/*", "Uploading to PyPI")

def main():
    """Main build and publish function."""
    parser = argparse.ArgumentParser(description="Build and publish RAGPack")
    parser.add_argument(
        "--target", 
        choices=["build", "test-pypi", "pypi"], 
        default="build",
        help="Target for the build (default: build)"
    )
    parser.add_argument(
        "--skip-checks", 
        action="store_true",
        help="Skip quality checks and tests"
    )
    parser.add_argument(
        "--skip-clean", 
        action="store_true",
        help="Skip cleaning build artifacts"
    )
    
    args = parser.parse_args()
    
    print("🚀 RAGPack Build and Publish Script")
    print("="*50)
    print(f"Target: {args.target}")
    print(f"Skip checks: {args.skip_checks}")
    print(f"Skip clean: {args.skip_clean}")
    print()
    
    # Step 1: Clean build artifacts
    if not args.skip_clean:
        clean_build_artifacts()
    
    # Step 2: Check version consistency
    if not check_version_consistency():
        print("❌ Version consistency check failed")
        sys.exit(1)
    
    # Step 3: Run quality checks
    if not args.skip_checks:
        print("\n📋 Running quality checks...")
        if not run_quality_checks():
            print("❌ Quality checks failed")
            response = input("Continue anyway? (y/N): ")
            if response.lower() != 'y':
                sys.exit(1)
        
        # Step 4: Run tests
        print("\n🧪 Running tests...")
        if not run_tests():
            print("❌ Tests failed")
            response = input("Continue anyway? (y/N): ")
            if response.lower() != 'y':
                sys.exit(1)
    
    # Step 5: Build package
    print("\n📦 Building package...")
    if not build_package():
        print("❌ Package build failed")
        sys.exit(1)
    
    # Step 6: Check package
    print("\n🔍 Checking package...")
    if not check_package():
        print("❌ Package check failed")
        sys.exit(1)
    
    # Step 7: Upload based on target
    if args.target == "test-pypi":
        print("\n🚀 Uploading to Test PyPI...")
        if not upload_to_test_pypi():
            print("❌ Upload to Test PyPI failed")
            sys.exit(1)
        print("\n✅ Successfully uploaded to Test PyPI!")
        print("💡 Test installation with:")
        print("   pip install --index-url https://test.pypi.org/simple/ ragpack")
        
    elif args.target == "pypi":
        print("\n⚠️ WARNING: You are about to upload to the PRODUCTION PyPI!")
        response = input("Are you sure you want to continue? (y/N): ")
        if response.lower() != 'y':
            print("❌ Upload cancelled")
            sys.exit(1)
        
        print("\n🚀 Uploading to PyPI...")
        if not upload_to_pypi():
            print("❌ Upload to PyPI failed")
            sys.exit(1)
        print("\n✅ Successfully uploaded to PyPI!")
        print("💡 Install with:")
        print("   pip install ragpack")
        
    else:  # build only
        print("\n✅ Package built successfully!")
        print("💡 Next steps:")
        print("   - Test upload: python scripts/build_and_publish.py --target test-pypi")
        print("   - Production upload: python scripts/build_and_publish.py --target pypi")
    
    # Show build artifacts
    dist_path = Path("dist")
    if dist_path.exists():
        print(f"\n📁 Build artifacts in {dist_path}:")
        for file in dist_path.iterdir():
            size = file.stat().st_size / 1024  # KB
            print(f"   - {file.name} ({size:.1f} KB)")

if __name__ == "__main__":
    main()