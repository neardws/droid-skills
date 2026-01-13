# Planning with Files - Droid Skill

> Manus-style file-based planning skill for [Factory Droid](https://factory.ai/)

This is a **Factory Droid skill** converted from the popular [planning-with-files](https://github.com/OthmanAdi/planning-with-files) Claude Code plugin.

## What is this?

A skill that implements persistent markdown files as "working memory on disk" - the context engineering pattern that made Manus worth $2B.

## Installation

Copy the skill to your Droid skills directory:

```bash
# Personal skill (follows you across projects)
cp -r . ~/.factory/skills/planning-with-files/

# Or project skill (shared with team)
cp -r . <your-repo>/.factory/skills/planning-with-files/
```

Restart `droid` to load the skill.

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

**Use for:**
- Multi-step tasks (3+ steps)
- Research tasks
- Building/creating projects
- Tasks spanning many tool calls

**Skip for:**
- Simple questions
- Single-file edits
- Quick lookups

## Structure

```
planning-with-files-droid/
├── SKILL.md              # Main skill definition
├── README.md             # This file
└── templates/
    ├── task_plan.md      # Phase tracking template
    ├── findings.md       # Research storage template
    └── progress.md       # Session logging template
```

## Credits

- Original Claude Code plugin: [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)
- Based on [Manus Context Engineering](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## License

MIT License
