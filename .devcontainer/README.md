# Devcontainer

## Goal
This `.devcontainer` configuration provides a consistent, containerized development environment. It ensures that all developers and AI agents have the exact same system dependencies, configurations, and tools available, streamlining the development process and reducing setup friction.

## Main Tools Included
This environment comes pre-configured with the following AI-assisted development tools:
- **[Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)**: An interactive AI CLI tool by Anthropic.
- **[Gemini CLI](https://github.com/google/gemini-cli)**: Google's AI-powered CLI agent specializing in software engineering workflows.
- **RTK (Rust Token Killer)**: A token-optimized CLI proxy that provides significant savings on dev operations and AI context.

## Recommended Usage

This `.devcontainer` is designed to be used as a git submodule. To set it up in a new repository or update an existing one:

1. **Add the submodule:**
   ```bash
   git submodule add https://github.com/AlexandreKavalerski/devcontainer-claude-code-macos .devcontainer
   ```

2. **Enable recursive submodule updates** so that pulling changes automatically updates the devcontainer:
   ```bash
   git config submodule.recurse true
   ```

## Repository Setup

When using these AI tools, they often generate local state, logs, and downloaded skills. It is highly recommended to add the following entries to your project's `.gitignore` to keep your repository clean:

```gitignore
# AI Agents & CLI Tools
tmpclaude*
.agents/
.claude/
skills-lock.json
```