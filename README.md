# Droid Skills

> A collection of skills for [Factory Droid](https://factory.ai/)

## Available Skills

| Skill | Description |
|-------|-------------|
| [planning-with-files](skills/planning-with-files/) | Manus-style file-based planning for complex tasks |
| [md-table-formatter](skills/md-table-formatter/) | Auto-format Markdown tables with proper alignment |
| [superpowers](skills/superpowers/) | Complete development workflow (14 skills) |

## Installation

Copy specific skills to your Droid skills directory:

```bash
# Personal skill (follows you across projects)
cp -r skills/<skill-name> ~/.factory/skills/

# Or project skill (shared with team)
cp -r skills/<skill-name> <your-repo>/.factory/skills/
```

Restart `droid` to load the skill.

## Structure

```
droid-skills/
├── README.md
├── LICENSE
└── skills/
    ├── planning-with-files/
    ├── md-table-formatter/
    └── superpowers/
        ├── brainstorming/
        ├── writing-plans/
        ├── executing-plans/
        ├── test-driven-development/
        ├── systematic-debugging/
        └── ... (14 skills total)
```

## Contributing

Feel free to submit PRs to add new skills!

## License

MIT License
