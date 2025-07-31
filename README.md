# 🍮 PompomPurin's AI Engineering Toolkit
## PRP (Product Requirement Prompts) Framework

*Sweet AI-assisted development that's as delightful as pudding!*

[![GitHub Stars](https://img.shields.io/github/stars/pompompurin/pompompurin-ai-toolkit?style=social)](https://github.com/pompompurin/pompompurin-ai-toolkit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> **"Making AI development as smooth and sweet as Pompompurin's favorite pudding!"** 🍮✨

A comprehensive collection of AI engineering resources and prompts for building production-ready software with **Claude Code**, **Qodo AI**, and other AI development tools. This toolkit enables **one-pass implementation success** through structured prompts and comprehensive validation.

---

## 🌟 What Makes This Special?

### 🎯 **PRP Methodology**
**PRP = PRD + Curated Codebase Intelligence + Agent Runbook**

The minimum viable packet an AI needs to ship production-ready code on the first pass.

### 🚀 **28+ Pre-configured Commands**
Ready-to-use slash commands for Claude Code covering every aspect of development.

### 🧪 **Validation-First Approach**
Every PRP includes executable validation loops ensuring production quality.

### 📚 **Comprehensive Documentation**
Curated AI documentation, templates, and real-world examples.

---

## ⚡ My Modern Development Stack

*Why I chose these tools and why you should too*

### **🐍 Python Environment & Packages**
**I use Mamba + UV because speed matters when you're building fast**

- **Mamba** - I switched from conda because it's 10x faster for environment management
- **UV** - I replaced pip entirely. UV installs packages 10-100x faster than pip
- **Why this combo**: Environment creation in seconds, not minutes. Dependency resolution that actually works.

```bash
# My typical setup
mamba create -n myproject python=3.12  # Lightning fast
mamba activate myproject
uv pip install -r requirements.txt     # Blazing fast installs
```

### **🐳 Containerization & Orchestration**
**I dockerize everything because consistency is king**

- **Docker + BuildKit** - I always enable BuildKit for parallel builds and better caching
- **Docker Compose v2** - I use `COMPOSE_BAKE=true` for even faster builds
- **Devcontainers** - I prefer this for team consistency over "works on my machine"

```bash
# My docker setup
export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=true
COMPOSE_BAKE=true docker-compose up --build
```

### **🏗️ Build Systems & Monorepos**
**I use Turborepo because it makes large projects manageable**

- **Turborepo** - I chose this over Nx because it's simpler and faster for most use cases
- **Earthly** - I use this for complex Dockerfiles because the syntax is cleaner
- **esbuild** - I replaced Webpack because build times dropped from minutes to seconds

### **🔧 Code Quality & Speed**
**I optimized my toolchain to eliminate waiting**

- **Ruff** - I replaced Black, isort, flake8, and pylint with this one tool. 100x faster.
- **Biome** - I switched from Prettier + ESLint for JS/TS. One tool, zero config, blazing fast.
- **Pre-commit** - I use this to catch issues before they hit CI

### **🧪 Testing & Quality Assurance**
**I test everything, but efficiently**

- **Pytest-xdist** - I run tests in parallel because waiting is wasteful
- **Testcontainers** - I test against real databases, not mocks
- **Hypothesis** - I use property-based testing to find edge cases I'd never think of

### **📊 Monitoring & Observability**
**I monitor everything because debugging blind is painful**

- **Sentry** - I catch errors before users report them
- **Grafana + Prometheus** - I visualize performance metrics
- **OpenTelemetry** - I trace requests across services

### **🚀 Why This Stack Works**

I've tried every tool combination, and this stack gives me:
- **10x faster** development cycles
- **Zero configuration** headaches
- **Consistent environments** across team and deployment
- **Production-ready** code from day one

---

## 🚀 Quick Start (5 Minutes)

### Option 1: Use with Your Existing Project
```bash
# Clone the toolkit
git clone https://github.com/pompompurin/pompompurin-ai-toolkit.git
cd pompompurin-ai-toolkit

# Copy commands to your project
cp -r .claude/commands /path/to/your-project/.claude/
cp -r PRPs/templates /path/to/your-project/PRPs/

# Start using slash commands in Claude Code!
```

### Option 2: Start Fresh with the Toolkit
```bash
# Clone and enter
git clone https://github.com/pompompurin/pompompurin-ai-toolkit.git
cd pompompurin-ai-toolkit

# Install dependencies (for Python projects)
pip install -r requirements.txt  # or use uv/poetry

# Open in Claude Code and start building!
```

### Option 3: Try the Demo Project
```bash
# Navigate to the example Task API
cd task-api

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.main:app --reload

# Visit http://localhost:8000/docs to see it in action!
```

---

## 🛠�� Available Commands

### 📋 **PRP Creation & Execution**
- `/prp-base-create` - Generate comprehensive PRPs with research
- `/prp-base-execute` - Execute PRPs against codebase  
- `/prp-planning-create` - Create planning documents with diagrams
- `/prp-spec-create` - Advanced specification creation
- `/prp-task-create` - Create specific development tasks

### 🔍 **Code Quality & Review**
- `/review-general` - General code review
- `/review-staged-unstaged` - Review git changes
- `/refactor-simple` - Simple refactoring tasks

### 🌿 **Git & GitHub Operations**
- `/new-dev-branch` - Create development branches
- `/smart-commit` - Intelligent commit messages
- `/create-pr` - Create pull requests
- `/conflict-resolver-general` - Resolve git conflicts

### 🚀 **Development Utilities**
- `/prime-core` - Prime Claude with project context
- `/onboarding` - Team member onboarding
- `/debug-RCA` - Root cause analysis and debugging
- `/api-contract-define` - Define API contracts

### 💻 **Language-Specific**
- `/TS-create-base-prp` - TypeScript-specific PRP creation
- `/TS-execute-base-prp` - TypeScript PRP execution
- `/TS-review-general` - TypeScript code review

---

## 🎯 How to Use This Toolkit

### 1. **Planning Phase**
```bash
# Create high-level planning
/prp-planning-create "Build a task management app"

# Generate detailed PRP
/prp-base-create "User authentication with JWT"
```

### 2. **Development Phase**
```bash
# Create development branch
/new-dev-branch

# Execute your PRP
/prp-base-execute PRPs/user-auth.md

# Use Qodo AI in VS Code for implementation
```

### 3. **Quality Assurance**
```bash
# Review your code
/review-general

# Run validation loops from PRP
pytest tests/ -v
```

### 4. **Deployment**
```bash
# Smart commit with detailed messages
/smart-commit

# Create pull request
/create-pr
```

---

## 📖 PRP Structure & Best Practices

### **Essential PRP Components**

```markdown
## Goal
What you're building and why it matters

## Why  
Business value and user impact

## What
Specific deliverables and success criteria

## All Needed Context
- Documentation URLs with specific sections
- Code examples from existing codebase
- Known gotchas and pitfalls
- Library versions and constraints

## Implementation Blueprint
Step-by-step plan with pseudocode and tasks

## Validation Loop
Executable commands for testing and validation
```

### **Golden Rules**
1. **Context is King** - Include ALL necessary documentation and examples
2. **Make it Executable** - Validation loops must be runnable by AI
3. **Reference Reality** - Use actual file paths and code patterns
4. **Plan for Failure** - Include error handling and edge cases

---

## 🏗️ Project Structure

```
pompompurin-ai-toolkit/
├── 🍮 README.md                    # You are here!
├── ⚙️ .claude/
│   └── commands/                   # 28+ slash commands
│       ├── PRPs/                   # PRP creation & execution
│       ├── code-quality/           # Review & refactoring
│       ├── development/            # Core dev utilities
│       ├── git-operations/         # Git workflow commands
│       └── typescript/             # TS-specific commands
├── 📚 PRPs/
│   ├── templates/                  # PRP templates
│   ├── scripts/                    # PRP runner utilities
│   ├── ai_docs/                    # Curated AI documentation
│   └── *.md                        # Example PRPs
├── 🚀 task-api/                    # Complete demo project
│   ├── app/                        # FastAPI implementation
│   ├── tests/                      # Comprehensive test suite
│   └── README.md                   # Project documentation
└── 📋 CLAUDE.md                    # Project guidelines
```

---

## 🎮 Demo Project: Task Management API

Explore a complete implementation showcasing the PRP methodology:

### **What's Included**
- ✅ **FastAPI Backend** with JWT authentication
- ✅ **SQLAlchemy ORM** with SQLite database
- ✅ **Full CRUD Operations** for task management
- ✅ **Comprehensive Test Suite** with pytest
- ✅ **API Documentation** with OpenAPI/Swagger
- ✅ **Production-Ready Structure** with error handling

### **Try It Out**
```bash
cd task-api
pip install -r requirements.txt
uvicorn app.main:app --reload
open http://localhost:8000/docs
```

### **Learn from the PRPs**
- `PRPs/task-api-planning.md` - Architecture planning
- `PRPs/task-api-core.md` - Detailed implementation PRP
- `PRPs/task-api-contract.md` - API specification
- `PRPs/task-api-debug.md` - Troubleshooting guide
- `PRPs/task-api-onboarding.md` - Team onboarding

---

## 🔧 Integration with AI Tools

### **Claude Code Integration**
1. Open your project in Claude Code
2. Type `/` to see available commands
3. Use commands to create and execute PRPs
4. Let Claude implement following your blueprints

### **Qodo AI Integration**
1. Install Qodo AI extension in VS Code
2. Use PRPs as specifications for Qodo
3. Generate tests with Qodo based on PRP validation loops
4. Review Qodo's output using PRP quality criteria

### **Universal Compatibility**
Works with any AI coding assistant:
- GitHub Copilot
- Cursor
- Codeium
- And more!

---

## 🌍 Use Cases & Examples

### **Web Applications**
- React/Vue/Angular frontends
- FastAPI/Django/Flask backends
- Full-stack applications

### **Mobile Development**
- React Native apps
- Flutter applications
- Native iOS/Android

### **Data & AI Projects**
- Machine learning pipelines
- Data analysis workflows
- AI model deployment

### **Infrastructure & DevOps**
- Cloud deployments
- CI/CD pipelines
- Monitoring systems

### **Games & Interactive Media**
- Web games
- Game development tools
- Interactive visualizations

---

## 📚 Learning Resources

### **Getting Started**
1. **Read the Demo PRPs** - See real-world examples
2. **Try the Task API** - Hands-on experience
3. **Create Your First PRP** - Start small and iterate
4. **Join the Community** - Share your experiences

### **Advanced Topics**
- **Custom Command Creation** - Extend the toolkit
- **Team Workflows** - Scale across organizations
- **CI/CD Integration** - Automate PRP execution
- **Multi-Agent Coordination** - Complex project management

### **Best Practices**
- **Context Engineering** - Maximize AI effectiveness
- **Validation Strategies** - Ensure production quality
- **Documentation Patterns** - Maintainable knowledge
- **Security Considerations** - Safe AI development

---

## 🤝 Contributing

We love contributions! Here's how to get involved:

### **Ways to Contribute**
- 🐛 **Report Bugs** - Help us improve
- 💡 **Suggest Features** - Share your ideas
- 📝 **Improve Documentation** - Make it clearer
- 🔧 **Add Commands** - Extend functionality
- 🎯 **Share PRPs** - Real-world examples

### **Getting Started**
```bash
# Fork the repository
git clone https://github.com/your-username/pompompurin-ai-toolkit.git

# Create a feature branch
git checkout -b feature/amazing-new-command

# Make your changes and test
# Follow the PRP methodology for new features!

# Submit a pull request
```

### **Contribution Guidelines**
1. **Follow PRP Methodology** - Use our own tools!
2. **Include Tests** - Validate your contributions
3. **Update Documentation** - Keep it current
4. **Be Respectful** - Kind and constructive feedback

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

### **What This Means**
- ✅ **Free to use** for personal and commercial projects
- ✅ **Modify and distribute** as needed
- ✅ **No warranty** - use at your own risk
- ✅ **Attribution appreciated** but not required

---

## 🙏 Acknowledgments

### **Special Thanks**
- **Rasmus Widing** - Original PRP methodology creator
- **Claude AI** - Powering the development experience
- **Qodo AI** - Enhancing code generation capabilities
- **The Community** - Feedback, contributions, and support

### **Inspiration**
This toolkit was inspired by the need for structured, context-rich AI development that produces production-ready code. The PRP methodology bridges the gap between traditional requirements and AI-assisted implementation.

---

## 📞 Support & Community

### **Get Help**
- 📖 **Documentation** - Check the PRPs and guides
- 🐛 **Issues** - Report bugs on GitHub
- 💬 **Discussions** - Join community conversations
- 📧 **Direct Contact** - Reach out for complex questions

### **Stay Updated**
- ⭐ **Star the Repository** - Get notified of updates
- 👀 **Watch Releases** - New features and improvements
- 🐦 **Follow Updates** - Social media announcements

### **Support the Project**
If you find this toolkit valuable:

- ⭐ **Star the repository** - Show your support
- 🔄 **Share with others** - Spread the word
- 💝 **Contribute** - Make it even better
- ☕ **Buy me a coffee** - [Support the maintainer](https://coff.ee/wirasm)

---

## 🎉 Ready to Build Something Amazing?

The PompomPurin AI Engineering Toolkit is your gateway to **sweet, efficient, and production-ready AI development**. Whether you're building your first app or scaling enterprise systems, our PRP methodology and comprehensive command library will help you succeed.

### **Start Your Journey**
```bash
git clone https://github.com/pompompurin/pompompurin-ai-toolkit.git
cd pompompurin-ai-toolkit
# Open in Claude Code and type "/" to see the magic! ✨
```

**Happy coding, and may your development be as smooth as pudding!** 🍮💻✨

---

*Made with 💖 and lots of ☕ by the PompomPurin community*