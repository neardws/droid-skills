# Planning with Files

> Manus-style file-based planning skill for Factory Droid

Converted from [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) Claude Code plugin.

## Installation

### 1. Install the Skill

```bash
# Personal skill
cp -r . ~/.factory/skills/planning-with-files/

# Or project skill
cp -r . <your-repo>/.factory/skills/planning-with-files/
```

### 2. Install Hooks (Optional but Recommended)

Merge the hooks from `hooks.json` into your settings:

```bash
# Edit your settings file
# ~/.factory/settings.json (personal) or .factory/settings.json (project)
```

Add the hooks configuration from `hooks.json` to your settings.

The hooks provide:
- **SessionStart**: Reminder to create planning files
- **PreToolUse**: Auto-reads task_plan.md before Write/Edit/Bash operations
- **PostToolUse**: Reminds to update status after file changes
- **Stop**: Verifies all phases are complete before finishing

## The Core Pattern

```
Context Window = RAM (volatile, limited)
Filesystem = Disk (persistent, unlimited)

→ Anything important gets written to disk.
```

## Files Created

For every complex task, create THREE files in your project:

| File | Purpose |
|------|---------|
| `task_plan.md` | Track phases and progress |
| `findings.md` | Store research and findings |
| `progress.md` | Session log and test results |

## Key Rules

1. **Create Plan First** - Never start without `task_plan.md`
2. **The 2-Action Rule** - Save findings after every 2 view/browser operations
3. **Read Before Decide** - Re-read plan before major decisions
4. **Log ALL Errors** - They help avoid repetition
5. **Never Repeat Failures** - Track attempts, mutate approach

## When to Use

**Use for:** Multi-step tasks, research, building projects

**Skip for:** Simple questions, single-file edits, quick lookups

## Credits

- Original: [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)
- Based on [Manus Context Engineering](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
