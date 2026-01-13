#!/usr/bin/env python3
"""
Markdown table formatter for Droid.
Formats tables with proper alignment after file edits.
"""
import json
import sys
import re
import os

try:
    from wcwidth import wcswidth
except ImportError:
    def wcswidth(s):
        return len(s)

def get_string_width(text):
    """Calculate display width, stripping markdown but preserving code content."""
    code_blocks = []
    
    def save_code(match):
        code_blocks.append(match.group(1))
        return f"\x00CODE{len(code_blocks)-1}\x00"
    
    text_with_placeholders = re.sub(r'`(.+?)`', save_code, text)
    
    visual_text = text_with_placeholders
    prev = ""
    while visual_text != prev:
        prev = visual_text
        visual_text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', visual_text)
        visual_text = re.sub(r'\*\*(.+?)\*\*', r'\1', visual_text)
        visual_text = re.sub(r'\*(.+?)\*', r'\1', visual_text)
        visual_text = re.sub(r'~~(.+?)~~', r'\1', visual_text)
        visual_text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', visual_text)
        visual_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', visual_text)
    
    def restore_code(match):
        idx = int(match.group(1))
        return code_blocks[idx] if idx < len(code_blocks) else ""
    
    visual_text = re.sub(r'\x00CODE(\d+)\x00', restore_code, visual_text)
    
    width = wcswidth(visual_text)
    return width if width >= 0 else len(visual_text)

def is_table_row(line):
    trimmed = line.strip()
    return trimmed.startswith("|") and trimmed.endswith("|") and len(trimmed.split("|")) > 2

def is_separator_row(line):
    trimmed = line.strip()
    if not trimmed.startswith("|") or not trimmed.endswith("|"):
        return False
    cells = trimmed.split("|")[1:-1]
    return len(cells) > 0 and all(re.match(r'^\s*:?-+:?\s*$', c) for c in cells)

def is_valid_table(lines):
    if len(lines) < 2:
        return False
    rows = [line.split("|")[1:-1] for line in lines]
    if not rows or not rows[0]:
        return False
    col_count = len(rows[0])
    if not all(len(row) == col_count for row in rows):
        return False
    return any(is_separator_row(line) for line in lines)

def get_alignment(cell):
    trimmed = cell.strip()
    left = trimmed.startswith(":")
    right = trimmed.endswith(":")
    if left and right:
        return "center"
    if right:
        return "right"
    return "left"

def pad_cell(text, width, align):
    display_width = get_string_width(text)
    padding = max(0, width - display_width)
    if align == "center":
        left_pad = padding // 2
        right_pad = padding - left_pad
        return " " * left_pad + text + " " * right_pad
    elif align == "right":
        return " " * padding + text
    else:
        return text + " " * padding

def format_separator_cell(width, align):
    if align == "center":
        return ":" + "-" * max(1, width - 2) + ":"
    if align == "right":
        return "-" * max(1, width - 1) + ":"
    return "-" * width

def format_table(lines):
    separator_indices = {i for i, line in enumerate(lines) if is_separator_row(line)}
    rows = [[c.strip() for c in line.split("|")[1:-1]] for line in lines]
    
    if not rows:
        return lines
    
    col_count = max(len(row) for row in rows)
    
    alignments = ["left"] * col_count
    for idx in separator_indices:
        for col, cell in enumerate(rows[idx]):
            if col < col_count:
                alignments[col] = get_alignment(cell)
    
    col_widths = [3] * col_count
    for i, row in enumerate(rows):
        if i in separator_indices:
            continue
        for col, cell in enumerate(row):
            if col < col_count:
                col_widths[col] = max(col_widths[col], get_string_width(cell))
    
    result = []
    for i, row in enumerate(rows):
        cells = []
        for col in range(col_count):
            cell = row[col] if col < len(row) else ""
            align = alignments[col]
            if i in separator_indices:
                cells.append(format_separator_cell(col_widths[col], align))
            else:
                cells.append(pad_cell(cell, col_widths[col], align))
        result.append("| " + " | ".join(cells) + " |")
    
    return result

def format_markdown_tables(text):
    lines = text.split("\n")
    result = []
    i = 0
    
    while i < len(lines):
        if is_table_row(lines[i]):
            table_lines = [lines[i]]
            i += 1
            while i < len(lines) and is_table_row(lines[i]):
                table_lines.append(lines[i])
                i += 1
            
            if is_valid_table(table_lines):
                result.extend(format_table(table_lines))
            else:
                result.extend(table_lines)
        else:
            result.append(lines[i])
            i += 1
    
    return "\n".join(result)

if __name__ == "__main__":
    try:
        input_data = json.load(sys.stdin)
        file_path = input_data.get("tool_input", {}).get("file_path", "")
        
        if not file_path.endswith((".md", ".mdx")):
            sys.exit(0)
        
        if not os.path.exists(file_path):
            sys.exit(0)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        formatted = format_markdown_tables(content)
        
        if formatted != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(formatted)
            print(f"[md-table-formatter] Formatted tables in {file_path}")
        
    except Exception as e:
        sys.exit(0)
