# Markdown Table Formatter

> Auto-format Markdown tables with proper alignment

Converted from [franlol/opencode-md-table-formatter](https://github.com/franlol/opencode-md-table-formatter).

## Installation

### 1. Install the Skill

```bash
cp -r . ~/.factory/skills/md-table-formatter/
```

### 2. Install Hook

Add to `~/.factory/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "~/.factory/skills/md-table-formatter/scripts/format-tables.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### 3. Optional: Install wcwidth

For better CJK/emoji support:
```bash
pip install wcwidth
```

## Features

- Auto-formats tables after Write/Edit on .md files
- Supports alignment: `:---` (left), `:---:` (center), `---:` (right)
- Handles unicode, emoji, CJK characters
- Preserves markdown inside `` `code` `` blocks

## Credits

Original: [franlol/opencode-md-table-formatter](https://github.com/franlol/opencode-md-table-formatter)
