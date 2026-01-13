#!/bin/bash
# Check if all phases in task_plan.md are complete

PLAN_FILE="${FACTORY_PROJECT_DIR}/task_plan.md"

if [ ! -f "$PLAN_FILE" ]; then
    exit 0
fi

# Count pending and in_progress phases
INCOMPLETE=$(grep -c "Status:.*\(pending\|in_progress\)" "$PLAN_FILE" 2>/dev/null || echo "0")

if [ "$INCOMPLETE" -gt 0 ]; then
    echo "[planning-with-files] Warning: $INCOMPLETE phase(s) still incomplete in task_plan.md" >&2
    echo "Please verify all phases are complete before finishing." >&2
    exit 2
fi

exit 0
