# 🧠 git-smart-commit

> Never write a commit message again. Let your changes speak for themselves.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**git-smart-commit** analyzes your staged changes and generates intelligent, conventional commit messages automatically. Stop staring at `git commit -m ""` wondering what to write.

## ✨ Features

- 🎯 **Analyzes your changes** - Understands what you modified
- 📝 **Conventional commits** - Follows industry standards (feat, fix, docs, etc.)
- 🎨 **Interactive mode** - Review and edit before committing
- ⚡ **Zero config** - Works out of the box
- 🔍 **Smart scoping** - Detects project modules automatically
- 📊 **Change statistics** - Shows what you're committing

## 🚀 Quick Start

### Installation

```bash
# Using pip
pip install git-smart-commit

# Or download and run directly
curl -o git-smart-commit https://raw.githubusercontent.com/YOUR_USERNAME/git-smart-commit/main/git_smart_commit.py
chmod +x git-smart-commit
```

### Usage

```bash
# Stage your changes as usual
git add .

# Run git-smart-commit instead of git commit
git-smart-commit

# Or use the alias
gsc
```

## 📸 Demo

```
🔍 Analyzing staged changes...

============================================================
📝 SUGGESTED COMMIT MESSAGE
============================================================

feat(api): add 3 files and update 2 files

Changed files:
  ✨ api/users.py
  ✨ api/auth.py
  ✨ api/models.py
  ♻️ tests/test_api.py
  ♻️ README.md

Stats: +243 -18

============================================================

Available commit types:
👉 1. feat       - A new feature
   2. fix        - A bug fix
   3. docs       - Documentation only changes
   4. style      - Changes that do not affect code meaning
   5. refactor   - Code change that neither fixes a bug nor adds a feature
   ...

Options:
  [Enter] - Use suggested message
  [1-10]  - Change commit type
  [e]     - Edit message manually
  [q]     - Quit without committing

Your choice: ▊
```

## 🎯 How It Works

1. **Analyzes staged files** - Checks what you've added with `git add`
2. **Detects patterns** - Identifies if you're adding features, fixing bugs, updating docs, etc.
3. **Generates message** - Creates a conventional commit message
4. **Interactive review** - Lets you confirm, edit, or change the type
5. **Commits** - Runs `git commit` with the final message

## 📋 Commit Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Code style changes (formatting) |
| `refactor` | Code refactoring |
| `perf` | Performance improvements |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks |
| `ci` | CI/CD changes |
| `build` | Build system or dependency changes |

## 🔧 Configuration (Optional)

Create a `.git-smart-commit.json` in your project root:

```json
{
  "default_type": "feat",
  "auto_commit": false,
  "include_stats": true,
  "max_files_in_body": 10
}
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (coming soon!)
5. Commit using git-smart-commit 😉
6. Push and create a Pull Request

## 📝 Roadmap

- [ ] Add configuration file support
- [ ] Integration with popular Git GUIs
- [ ] VS Code extension
- [ ] AI-powered message generation (optional OpenAI integration)
- [ ] Git hook integration
- [ ] Message templates
- [ ] Multi-language support

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 🌟 Show Your Support

If this tool saves you time, give it a ⭐️ on GitHub!

## 💬 Feedback

Found a bug? Have a feature request? [Open an issue](https://github.com/YOUR_USERNAME/git-smart-commit/issues)

---

Made with ❤️ by developers who were tired of writing commit messages
