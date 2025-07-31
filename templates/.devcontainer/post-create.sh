#!/bin/bash

# Post-create script for PompomPurin AI Toolkit devcontainer
echo "🍮 Setting up PompomPurin AI Toolkit development environment..."

# Install UV for blazing fast package management
echo "📦 Installing UV (super fast Python package manager)..."
pip install uv

# Install mamba for fast environment management
echo "🐍 Installing mamba (fast conda replacement)..."
conda install mamba -n base -c conda-forge -y

# Install development dependencies with UV
echo "⚡ Installing dependencies with UV (this will be fast!)..."
uv pip install -e ".[dev,container,monitoring]"

# Set up pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
pre-commit install

# Install Turborepo for monorepo management
echo "🏗️ Installing Turborepo..."
npm install -g turbo @turbo/gen

# Set up Git configuration
echo "📝 Setting up Git configuration..."
git config --global init.defaultBranch main
git config --global pull.rebase false

# Create useful aliases
echo "🚀 Setting up useful aliases..."
cat >> ~/.bashrc << 'EOF'

# PompomPurin AI Toolkit aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Modern development stack aliases
alias uv-install='uv pip install'
alias uv-sync='uv pip sync requirements.txt'
alias mamba-create='mamba create'
alias mamba-activate='mamba activate'

# Docker with BuildKit
alias docker-build='DOCKER_BUILDKIT=1 docker build'
alias docker-compose-build='COMPOSE_DOCKER_CLI_BUILD=true DOCKER_BUILDKIT=1 docker-compose build'
alias compose-bake='COMPOSE_BAKE=true docker-compose'

# Code quality shortcuts
alias lint='ruff check .'
alias format='ruff format .'
alias type-check='mypy .'
alias test='pytest -v'
alias test-cov='pytest --cov=app --cov-report=html'
alias test-parallel='pytest -n auto'

# Quick development commands
alias dev='uvicorn app.main:app --reload --host 0.0.0.0'
alias dev-debug='uvicorn app.main:app --reload --host 0.0.0.0 --log-level debug'

# PRP workflow shortcuts
alias prp-create='echo "Use /prp-base-create in Claude Code"'
alias prp-execute='echo "Use /prp-base-execute in Claude Code"'

echo "🍮 PompomPurin AI Toolkit environment ready!"
EOF

# Source the new aliases
source ~/.bashrc

# Create a welcome message
cat > ~/.welcome << 'EOF'
🍮 Welcome to PompomPurin's AI Engineering Toolkit!

Your modern development environment is ready with:
✅ UV - Lightning-fast Python package management
✅ Mamba - Blazing-fast environment management  
✅ Ruff - All-in-one linting and formatting
✅ Docker + BuildKit - Optimized containerization
✅ Turborepo - Smart monorepo builds
✅ Pre-commit hooks - Quality gates
✅ Qodo AI - AI coding assistant
✅ Full monitoring stack - Prometheus, Grafana, Jaeger

Quick commands:
- lint          # Check code quality
- format        # Format code
- test          # Run tests
- dev           # Start development server
- compose-bake  # Fast Docker Compose builds

Happy coding! May your development be as smooth as pudding! 🍮✨
EOF

# Display welcome message
cat ~/.welcome

echo "🎉 Setup complete! Your PompomPurin AI Toolkit is ready to use!"