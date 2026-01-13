# Droid Skills

> A collection of skills for [Factory Droid](https://factory.ai/)

## Available Skills

| Skill | Description |
|-------|-------------|
| [planning-with-files](skills/planning-with-files/) | Manus-style file-based planning for complex tasks |

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
    └── planning-with-files/
        ├── SKILL.md
        └── templates/
```

## Contributing

Feel free to submit PRs to add new skills!

## License

MIT License
