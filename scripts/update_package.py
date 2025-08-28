#!/usr/bin/env python3
"""
Update ragpackai to the latest version and check for improvements.
"""

import subprocess
import sys
import time

def run_command(command, description):
    """Run a command and return success status."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"❌ {description} failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} failed: {e}")
        return False

def check_current_version():
    """Check current installed version."""
    try:
        import ragpackai
        current_version = ragpackai.get_version()
        print(f"📦 Current version: {current_version}")
        return current_version
    except ImportError:
        print("❌ ragpackai not currently installed")
        return None

def update_ragpackai():
    """Update ragpackai to the latest version."""
    print("🚀 ragpackai Update Tool")
    print("=" * 40)
    
    # Check current version
    current_version = check_current_version()
    
    # Update to latest version
    if not run_command("pip install --upgrade ragpackai", "Updating ragpackai"):
        return False
    
    # Verify new version
    print("\n🔍 Verifying update...")
    try:
        # Clear module cache to get fresh import
        if 'ragpackai' in sys.modules:
            del sys.modules['ragpackai']
        
        import ragpackai
        new_version = ragpackai.get_version()
        print(f"📦 New version: {new_version}")
        
        if current_version and new_version != current_version:
            print(f"✅ Successfully updated from {current_version} to {new_version}")
        elif current_version == new_version:
            print("ℹ️  Already on the latest version")
        else:
            print("✅ ragpackai installed successfully")
            
    except Exception as e:
        print(f"❌ Error verifying update: {e}")
        return False
    
    return True

def test_performance():
    """Test import performance after update."""
    print("\n⚡ Testing import performance...")
    
    start_time = time.time()
    try:
        import ragpackai
        import_time = time.time() - start_time
        print(f"📊 Import time: {import_time:.2f}s")
        
        if import_time < 1.0:
            print("✅ Fast import performance!")
        elif import_time < 3.0:
            print("⚠️  Moderate import performance")
        else:
            print("🐌 Slow import performance - consider running performance check")
            
    except Exception as e:
        print(f"❌ Error testing performance: {e}")

def main():
    """Main update function."""
    if update_ragpackai():
        test_performance()
        print("\n🎯 Update complete!")
        print("\n💡 Next steps:")
        print("   • Run 'python scripts/performance_check.py' for detailed performance analysis")
        print("   • Check the changelog for new features and improvements")
        print("   • Test your existing code with the new version")
        return 0
    else:
        print("\n❌ Update failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())