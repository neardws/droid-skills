# Planning with Files

> Manus-style file-based planning skill for Factory Droid

Converted from [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) Claude Code plugin.

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
