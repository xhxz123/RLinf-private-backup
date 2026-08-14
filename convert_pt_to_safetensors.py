import torch
import safetensors.torch
import os

pt_path = "/root/autodl-tmp/logs/20260705-12:25:28-realworld_sft_openpi/realworld_sft_openpi/checkpoints/global_step_12000/actor/model_state_dict/full_weights.pt"
output_dir = "/root/RLinf/checkpoints"

os.makedirs(output_dir, exist_ok=True)

checkpoint = torch.load(pt_path, map_location="cpu")

if isinstance(checkpoint, dict):
    if "model_state_dict" in checkpoint:
        state_dict = checkpoint["model_state_dict"]
    elif "state_dict" in checkpoint:
        state_dict = checkpoint["state_dict"]
    else:
        state_dict = checkpoint
else:
    state_dict = checkpoint.state_dict()

output_path = os.path.join(output_dir, "model.safetensors")
safetensors.torch.save_file(state_dict, output_path)

print(f"Done! Saved to: {output_path}")
print(f"Keys: {len(state_dict)}")
print(f"File size: {os.path.getsize(output_path) / (1024**2):.2f} MB")
