# Superpowers Skills

> Complete software development workflow for coding agents

Converted from [obra/superpowers](https://github.com/obra/superpowers) - Claude Code superpowers library.

## Installation

```bash
# Copy all superpowers skills
cp -r . ~/.factory/skills/superpowers/

# Or copy individual skills
cp -r brainstorming ~/.factory/skills/
```

## Skills Overview

### Core Workflow

| Skill | Description |
|-------|-------------|
| brainstorming | Interactive design refinement before coding |
| writing-plans | Create detailed implementation plans |
| executing-plans | Batch execution with human checkpoints |
| subagent-driven-development | Fast iteration with two-stage review |

### Testing & Debugging

| Skill | Description |
|-------|-------------|
| test-driven-development | RED-GREEN-REFACTOR cycle |
| systematic-debugging | 4-phase root cause analysis |
| verification-before-completion | Ensure fixes are actually fixed |

### Code Review

| Skill | Description |
|-------|-------------|
| requesting-code-review | Pre-review checklist |
| receiving-code-review | Responding to feedback |

### Git Workflow

| Skill | Description |
|-------|-------------|
| using-git-worktrees | Parallel development branches |
| finishing-a-development-branch | Merge/PR decision workflow |

### Advanced

| Skill | Description |
|-------|-------------|
| dispatching-parallel-agents | Concurrent subagent workflows |
| writing-skills | Create new skills |
| using-superpowers | Introduction to the system |

## Philosophy

- **Test-Driven Development** - Write tests first, always
- **Systematic over ad-hoc** - Process over guessing
- **Complexity reduction** - Simplicity as primary goal
- **Evidence over claims** - Verify before declaring success

## Credits

Original: [obra/superpowers](https://github.com/obra/superpowers) by Jesse Vincent

License: MIT
