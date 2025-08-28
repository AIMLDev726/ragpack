#!/usr/bin/env python3
"""
Performance check script for ragpackai.

This script helps diagnose and fix performance issues with ragpackai loading times.
"""

import time
import sys
import os
from pathlib import Path

def time_import(module_name):
    """Time how long it takes to import a module."""
    start_time = time.time()
    try:
        __import__(module_name)
        end_time = time.time()
        return end_time - start_time, None
    except ImportError as e:
        end_time = time.time()
        return end_time - start_time, str(e)

def check_dependencies():
    """Check all dependencies and their import times."""
    print("🔍 Checking ragpackai dependencies and import times...\n")
    
    dependencies = [
        ("ragpackai", "Core ragpackai library"),
        ("langchain", "LangChain framework"),
        ("langchain_openai", "LangChain OpenAI integration"),
        ("langchain_chroma", "LangChain Chroma integration"),
        ("langchain_community", "LangChain community integrations"),
        ("openai", "OpenAI Python client"),
        ("chromadb", "ChromaDB vector database"),
        ("sentence_transformers", "Sentence Transformers"),
        ("faiss", "FAISS similarity search"),
        ("tqdm", "Progress bars"),
        ("pydantic", "Data validation"),
        ("cryptography", "Encryption support"),
    ]
    
    total_time = 0
    slow_imports = []
    missing_deps = []
    
    for module, description in dependencies:
        import_time, error = time_import(module)
        total_time += import_time
        
        if error:
            print(f"❌ {module:<20} - MISSING: {error}")
            missing_deps.append(module)
        elif import_time > 1.0:
            print(f"🐌 {module:<20} - {import_time:.2f}s (SLOW) - {description}")
            slow_imports.append((module, import_time))
        elif import_time > 0.5:
            print(f"⚠️  {module:<20} - {import_time:.2f}s (MODERATE) - {description}")
        else:
            print(f"✅ {module:<20} - {import_time:.2f}s - {description}")
    
    print(f"\n📊 Total import time: {total_time:.2f}s")
    
    return slow_imports, missing_deps

def check_system_info():
    """Check system information that might affect performance."""
    print("\n🖥️  System Information:")
    print(f"   Python version: {sys.version}")
    print(f"   Platform: {sys.platform}")
    
    # Check if running in virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("   Environment: Virtual environment ✅")
    else:
        print("   Environment: System Python ⚠️")
    
    # Check available memory
    try:
        import psutil
        memory = psutil.virtual_memory()
        print(f"   Available RAM: {memory.available / (1024**3):.1f} GB")
        if memory.available < 2 * (1024**3):  # Less than 2GB
            print("   ⚠️  Low memory detected - this may affect performance")
    except ImportError:
        print("   Memory info: Not available (install psutil for details)")

def provide_recommendations(slow_imports, missing_deps):
    """Provide performance recommendations."""
    print("\n💡 Performance Recommendations:")
    
    if missing_deps:
        print("\n❌ Missing Dependencies:")
        print("   Install missing dependencies with:")
        print(f"   pip install {' '.join(missing_deps)}")
    
    if slow_imports:
        print("\n🐌 Slow Import Analysis:")
        for module, import_time in slow_imports:
            if module == "sentence_transformers":
                print(f"   • {module} ({import_time:.2f}s): Consider using lighter embedding models")
            elif module == "chromadb":
                print(f"   • {module} ({import_time:.2f}s): ChromaDB can be slow on first import")
            elif module == "langchain":
                print(f"   • {module} ({import_time:.2f}s): LangChain has many dependencies")
            else:
                print(f"   • {module} ({import_time:.2f}s): Consider updating or reinstalling")
    
    print("\n🚀 General Performance Tips:")
    print("   1. Use a virtual environment to avoid dependency conflicts")
    print("   2. Keep dependencies updated: pip install --upgrade ragpackai")
    print("   3. Consider using lighter embedding models for faster startup")
    print("   4. Use SSD storage for better I/O performance")
    print("   5. Ensure sufficient RAM (4GB+ recommended)")
    
    print("\n⚡ ragpackai Specific Optimizations:")
    print("   • ragpackai now uses lazy imports to improve startup time")
    print("   • Heavy dependencies are only loaded when needed")
    print("   • Consider using 'openai:text-embedding-3-small' for faster embeddings")

def test_ragpackai_performance():
    """Test ragpackai specific performance."""
    print("\n🧪 Testing ragpackai Performance:")
    
    try:
        # Test basic import
        start_time = time.time()
        import ragpackai
        import_time = time.time() - start_time
        print(f"   Basic import: {import_time:.2f}s")
        
        # Test version access
        start_time = time.time()
        version = ragpackai.get_version()
        version_time = time.time() - start_time
        print(f"   Version check: {version_time:.3f}s - v{version}")
        
        # Test lazy loading
        start_time = time.time()
        pack_class = ragpackai.ragpackai
        class_time = time.time() - start_time
        print(f"   Class access: {class_time:.3f}s")
        
        print("   ✅ ragpackai loaded successfully with optimized imports")
        
    except Exception as e:
        print(f"   ❌ Error testing ragpackai: {e}")

def main():
    """Main performance check function."""
    print("🚀 ragpackai Performance Diagnostic Tool")
    print("=" * 50)
    
    # Check system info
    check_system_info()
    
    # Check dependencies
    slow_imports, missing_deps = check_dependencies()
    
    # Test ragpackai performance
    test_ragpackai_performance()
    
    # Provide recommendations
    provide_recommendations(slow_imports, missing_deps)
    
    print("\n" + "=" * 50)
    print("🎯 Performance check complete!")
    
    if missing_deps:
        print("⚠️  Please install missing dependencies before using ragpackai")
        return 1
    elif slow_imports:
        print("⚠️  Some dependencies are loading slowly - see recommendations above")
        return 0
    else:
        print("✅ All dependencies are loading efficiently!")
        return 0

if __name__ == "__main__":
    sys.exit(main())