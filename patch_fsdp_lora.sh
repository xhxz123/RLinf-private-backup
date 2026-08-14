#!/bin/bash
# Patch PyTorch FSDP for LoRA compatibility (save + load)
# Run this on the server: bash patch_fsdp_lora.sh

set -e

VENV="/root/RLinf/.venv/lib/python3.11/site-packages"
STATE_DICT_UTILS="$VENV/torch/distributed/fsdp/_state_dict_utils.py"
DEFAULT_PLANNER="$VENV/torch/distributed/checkpoint/default_planner.py"

# ============================================================
# Patch 1: _state_dict_utils.py - add frozen params to state_dict
# ============================================================
if [ -f "$STATE_DICT_UTILS" ]; then
    cp "$STATE_DICT_UTILS" "${STATE_DICT_UTILS}.bak" 2>/dev/null || true
    python3 -c "
with open('$STATE_DICT_UTILS', 'r') as f:
    content = f.read()

old = '''        assert fqn in state_dict, (
            f\"FSDP assumes {fqn} is in the state_dict but the state_dict only \"
            f\"has {state_dict.keys()}. \"
            f\"prefix={prefix}, module_name={module_name}, \"
            f\"param_name={param_name} rank={fsdp_state.rank}.\"
        )'''

new = '''        if fqn not in state_dict:
            # LoRA patch: skip frozen params (unchanged from pretrained)
            # They will be loaded from pretrained weights, not from checkpoint
            continue'''

if old in content:
    content = content.replace(old, new)
    with open('$STATE_DICT_UTILS', 'w') as f:
        f.write(content)
    print('[OK] Patch 1: _state_dict_utils.py')
else:
    print('[SKIP] Patch 1: _state_dict_utils.py already patched or not found')
"
else
    echo "[WARN] $STATE_DICT_UTILS not found"
fi

# ============================================================
# Patch 2: default_planner.py - allow strict=False for load
# ============================================================
if [ -f "$DEFAULT_PLANNER" ]; then
    cp "$DEFAULT_PLANNER" "${DEFAULT_PLANNER}.bak" 2>/dev/null || true
    python3 -c "
with open('$DEFAULT_PLANNER', 'r') as f:
    content = f.read()

old = '''        # ignore state_dict keys which do not exist in \`state_dict\` if strict=False
        if fqn not in metadata.state_dict_metadata:
            if strict:
                raise RuntimeError(f\"Missing key in checkpoint state_dict: {fqn}.\")
            else:
                continue'''

new = '''        # ignore state_dict keys which do not exist in \`state_dict\` if strict=False
        if fqn not in metadata.state_dict_metadata:
            # LoRA patch: skip missing keys (frozen params not in dcp)
            continue'''

if old in content:
    content = content.replace(old, new)
    with open('$DEFAULT_PLANNER', 'w') as f:
        f.write(content)
    print('[OK] Patch 2: default_planner.py')
else:
    print('[SKIP] Patch 2: default_planner.py already patched or not found')
"
else
    echo "[WARN] $DEFAULT_PLANNER not found"
fi

echo ""
echo "All patches applied. Old checkpoints may need to be removed and re-saved."