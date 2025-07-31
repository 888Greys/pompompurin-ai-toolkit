# 🍮 Contributing to PompomPurin's AI Toolkit

Thank you for your interest in contributing! This project thrives on community contributions and we're excited to have you join us.

## 🌟 Ways to Contribute

### 🐛 **Bug Reports**
- Use GitHub Issues to report bugs
- Include detailed reproduction steps
- Provide environment information
- Add relevant error messages or logs

### 💡 **Feature Requests**
- Describe the problem you're trying to solve
- Explain your proposed solution
- Consider creating a PRP for complex features
- Discuss implementation approaches

### 📝 **Documentation Improvements**
- Fix typos and grammar
- Add missing documentation
- Improve existing explanations
- Create new examples and tutorials

### 🔧 **Code Contributions**
- Add new Claude commands
- Improve existing functionality
- Create new PRP templates
- Enhance the demo projects

### 🎯 **PRP Examples**
- Share real-world PRPs you've created
- Document successful implementation patterns
- Contribute domain-specific templates
- Add validation strategies

## 🚀 Getting Started

### 1. **Fork and Clone**
```bash
# Fork the repository on GitHub
git clone https://github.com/your-username/pompompurin-ai-toolkit.git
cd pompompurin-ai-toolkit
```

### 2. **Set Up Development Environment**
```bash
# Install dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### 3. **Create a Feature Branch**
```bash
git checkout -b feature/your-amazing-feature
```

### 4. **Make Your Changes**
Follow our development guidelines below.

### 5. **Test Your Changes**
```bash
# Run tests
pytest task-api/tests/ -v

# Check code quality
ruff check .
ruff format .
mypy task-api/app --ignore-missing-imports
```

### 6. **Submit a Pull Request**
- Write a clear description of your changes
- Reference any related issues
- Include tests for new functionality
- Update documentation as needed

## 📋 Development Guidelines

### **PRP Methodology for Contributions**
We use our own PRP methodology for developing new features:

1. **Create a PRP** for significant changes
2. **Include comprehensive context** about the change
3. **Define validation loops** for testing
4. **Follow the implementation blueprint**

### **Code Style**
- **Python**: Follow PEP 8, use type hints
- **Line Length**: 88 characters (Black default)
- **Imports**: Use absolute imports, group logically
- **Documentation**: Include docstrings for public functions

### **Commit Messages**
Use conventional commit format:
```
type(scope): description

feat(commands): add new PRP creation command
fix(api): resolve authentication token validation
docs(readme): update installation instructions
test(api): add comprehensive auth tests
```

### **Testing Requirements**
- **Unit Tests**: Required for all new functionality
- **Integration Tests**: For API endpoints and workflows
- **PRP Validation**: Ensure PRPs follow required structure
- **Documentation Tests**: Verify examples work correctly

## 🎯 Contribution Areas

### **High Priority**
- [ ] Additional Claude commands for specific frameworks
- [ ] More comprehensive PRP templates
- [ ] Integration guides for other AI tools
- [ ] Performance optimization examples
- [ ] Security best practices documentation

### **Medium Priority**
- [ ] Additional demo projects (mobile, data science, etc.)
- [ ] Improved error handling and debugging tools
- [ ] Better CI/CD integration examples
- [ ] Multi-language support for commands

### **Nice to Have**
- [ ] Visual PRP builder tool
- [ ] Command-line interface for PRP management
- [ ] Integration with project management tools
- [ ] Advanced analytics and metrics

## 📚 Creating New Commands

### **Command Structure**
```markdown
# Command Name

Brief description of what the command does.

## Arguments: $ARGUMENTS

Detailed explanation of expected arguments.

## Implementation

[Your command implementation here]

## Example Usage

```bash
/your-command argument1 argument2
```

## Expected Output

Description of what users should expect.
```

### **Command Categories**
- **PRPs/**: PRP creation and execution
- **code-quality/**: Review and refactoring
- **development/**: Core development utilities
- **git-operations/**: Git workflow commands
- **typescript/**: Language-specific commands

### **Testing Commands**
```bash
# Test in Claude Code
# 1. Copy command to .claude/commands/
# 2. Open Claude Code
# 3. Type / and test your command
# 4. Verify expected behavior
```

## 🧪 Creating New PRPs

### **PRP Template Checklist**
- [ ] **Goal**: Clear, specific objective
- [ ] **Why**: Business value and user impact
- [ ] **What**: Detailed requirements and success criteria
- [ ] **Context**: Comprehensive documentation and examples
- [ ] **Implementation**: Step-by-step blueprint
- [ ] **Validation**: Executable tests and checks

### **PRP Quality Standards**
- **Context Completeness**: Include all necessary documentation
- **Executable Validation**: All validation steps must be runnable
- **Real-world Examples**: Use actual code patterns and file paths
- **Error Handling**: Plan for common failure scenarios

## 🔍 Review Process

### **Pull Request Review**
1. **Automated Checks**: CI must pass
2. **Code Review**: Maintainer review required
3. **Testing**: Manual testing of new features
4. **Documentation**: Verify docs are updated

### **Review Criteria**
- **Functionality**: Does it work as intended?
- **Quality**: Follows coding standards and best practices?
- **Testing**: Adequate test coverage?
- **Documentation**: Clear and complete?
- **PRP Compliance**: Follows our methodology?

## 🎉 Recognition

### **Contributors**
All contributors are recognized in:
- GitHub contributors list
- Release notes for significant contributions
- Special mentions for outstanding contributions

### **Maintainer Path**
Active contributors may be invited to become maintainers:
- Consistent high-quality contributions
- Understanding of project vision
- Community engagement and support
- Technical expertise in relevant areas

## 📞 Getting Help

### **Questions?**
- **GitHub Discussions**: For general questions
- **Issues**: For specific problems or bugs
- **Discord/Slack**: Real-time community chat (if available)

### **Stuck?**
- Review existing PRPs for examples
- Check the demo project implementation
- Ask in discussions before creating issues
- Reference our troubleshooting guides

## 🏆 Best Practices

### **Before Contributing**
1. **Search existing issues** to avoid duplicates
2. **Read the documentation** thoroughly
3. **Understand the PRP methodology**
4. **Start small** with your first contribution

### **During Development**
1. **Follow the PRP process** for significant changes
2. **Write tests first** (TDD approach)
3. **Document as you go**
4. **Ask for feedback early**

### **After Submission**
1. **Respond to review feedback** promptly
2. **Update your PR** based on suggestions
3. **Help test others' contributions**
4. **Share your experience** with the community

## 📜 Code of Conduct

### **Our Standards**
- **Be respectful** and inclusive
- **Provide constructive feedback**
- **Focus on the code, not the person**
- **Help others learn and grow**
- **Celebrate successes together**

### **Unacceptable Behavior**
- Harassment or discrimination
- Trolling or inflammatory comments
- Personal attacks or insults
- Publishing private information
- Other unprofessional conduct

### **Enforcement**
Violations may result in:
- Warning and guidance
- Temporary suspension
- Permanent ban from the project

## 🙏 Thank You!

Your contributions make this project better for everyone. Whether you're fixing a typo, adding a feature, or sharing your PRP experiences, every contribution matters.

**Happy contributing, and may your code be as sweet as pudding!** 🍮✨

---

*For questions about contributing, please open a GitHub Discussion or reach out to the maintainers.*