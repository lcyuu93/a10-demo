# A10 DevSecOps Demo Project

This is a small Python CLI demo project used to practice DevSecOps fundamentals:

- Static analysis with Flake8 (linting)
- Software Composition Analysis (SCA) with GitHub Dependabot
- Security-focused static analysis (SAST) with Semgrep

The app simulates a very simple "expense calculator" with intentionally imperfect code:
- Hard-coded configuration values
- An unsafe `eval`-based expression evaluator
- Some style issues for linting tools to catch
