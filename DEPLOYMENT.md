# RAGPack Deployment Guide

This guide covers deploying RAGPack to PyPI and setting up the GitHub repository for public release.

## Pre-Deployment Checklist

### ✅ Code Quality
- [ ] All tests pass: `pytest tests/ -v`
- [ ] Code formatting: `black ragpack tests examples scripts`
- [ ] Linting: `flake8 ragpack tests examples scripts`
- [ ] Type checking: `mypy ragpack --ignore-missing-imports`
- [ ] Security scan: `bandit -r ragpack`

### ✅ Documentation
- [ ] README.md is comprehensive and up-to-date
- [ ] All example notebooks work correctly
- [ ] API documentation is complete
- [ ] CHANGELOG.md is updated
- [ ] License file is present

### ✅ Package Configuration
- [ ] Version numbers are consistent across files
- [ ] pyproject.toml is properly configured
- [ ] Dependencies are correctly specified
- [ ] Entry points are working
- [ ] Package metadata is accurate

### ✅ Examples and Tests
- [ ] All example scripts run without errors
- [ ] Jupyter notebooks execute completely
- [ ] Test coverage is adequate (>80%)
- [ ] Integration tests with real APIs work
- [ ] CLI commands function properly

## PyPI Deployment

### 1. Test PyPI Deployment

First, deploy to Test PyPI to verify everything works:

```bash
# Build and upload to Test PyPI
python scripts/build_and_publish.py --target test-pypi

# Test installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ ragpack

# Verify installation
python -c "import ragpack; print(ragpack.get_version())"
```

### 2. Production PyPI Deployment

Once Test PyPI deployment is successful:

```bash
# Build and upload to production PyPI
python scripts/build_and_publish.py --target pypi

# Verify installation from PyPI
pip install ragpack
python -c "import ragpack; print(ragpack.get_version())"
```

### 3. Post-Deployment Verification

- [ ] Package installs correctly: `pip install ragpack`
- [ ] Basic functionality works: `python -c "from ragpack import RAGPack; print('OK')"`
- [ ] CLI is available: `ragpack --help`
- [ ] Examples run with fresh installation
- [ ] Documentation links work

## GitHub Repository Setup

### 1. Repository Configuration

- [ ] Repository is public
- [ ] Description and topics are set
- [ ] README displays correctly
- [ ] License is visible
- [ ] Releases section is configured

### 2. GitHub Actions

- [ ] CI workflow runs on push/PR
- [ ] All tests pass in CI environment
- [ ] Multiple Python versions tested
- [ ] Multiple operating systems tested
- [ ] Security scans complete

### 3. Branch Protection

- [ ] Main branch is protected
- [ ] Require PR reviews
- [ ] Require status checks
- [ ] Require up-to-date branches
- [ ] Restrict pushes to main

### 4. Issue Templates

- [ ] Bug report template
- [ ] Feature request template
- [ ] Pull request template
- [ ] Contributing guidelines

## Release Process

### 1. Version Bump

1. Update version in `pyproject.toml`
2. Update version in `ragpack/__init__.py`
3. Update `CHANGELOG.md` with new version
4. Commit changes: `git commit -m "Bump version to X.Y.Z"`

### 2. Create Release

1. Tag the release: `git tag -a vX.Y.Z -m "Release X.Y.Z"`
2. Push tag: `git push origin vX.Y.Z`
3. Create GitHub release from tag
4. Attach build artifacts to release

### 3. Deploy to PyPI

1. GitHub Actions will automatically deploy on release
2. Or manually deploy: `python scripts/build_and_publish.py --target pypi`

### 4. Post-Release

- [ ] Verify PyPI package is available
- [ ] Test installation from PyPI
- [ ] Update documentation if needed
- [ ] Announce release on relevant channels

## Monitoring and Maintenance

### Package Health

- [ ] Monitor PyPI download statistics
- [ ] Track GitHub stars and forks
- [ ] Monitor issue reports
- [ ] Review security advisories

### Continuous Improvement

- [ ] Regular dependency updates
- [ ] Performance monitoring
- [ ] User feedback integration
- [ ] Feature roadmap updates

## Troubleshooting

### Common Issues

**Build Failures:**
- Check Python version compatibility
- Verify all dependencies are available
- Ensure tests pass locally first

**Upload Failures:**
- Verify PyPI credentials
- Check package name availability
- Ensure version number is unique

**Installation Issues:**
- Test in clean virtual environment
- Check dependency conflicts
- Verify platform compatibility

### Getting Help

- Check GitHub Issues for similar problems
- Review PyPI packaging documentation
- Contact maintainers for support

## Security Considerations

- [ ] No API keys in repository
- [ ] Secure handling of credentials
- [ ] Regular security updates
- [ ] Vulnerability disclosure process

## Success Metrics

Track these metrics post-deployment:

- PyPI download counts
- GitHub stars and forks
- Issue resolution time
- Community contributions
- User satisfaction feedback

---

**Ready for deployment?** Follow this checklist step by step to ensure a smooth release process!