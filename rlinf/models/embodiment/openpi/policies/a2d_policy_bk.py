import dataclasses

import einops
import numpy as np
from openpi import transforms
from openpi.models import model as _model


def _parse_image(image) -> np.ndarray:
    image = np.asarray(image)
    if np.issubdtype(image.dtype, np.floating):
        image = (255 * image).astype(np.uint8)
    if image.shape[0] == 3:
        image = einops.rearrange(image, "c h w -> h w c")
    return image


_A2D_STATE_INDICES = np.array(
    [0, 1]
    + list(range(14, 20))
    + list(range(20, 28))
    + list(range(28, 42)),
    dtype=np.int32,
)

_PI05_ACTION_DIM = 32


def _extract_state(state: np.ndarray) -> np.ndarray:
    return np.asarray(state)[..., _A2D_STATE_INDICES]


@dataclasses.dataclass(frozen=True)
class A2DInputs(transforms.DataTransformFn):
    model_type: _model.ModelType

    def __call__(self, data: dict) -> dict:
        base_image = _parse_image(data["observation.images.top_head"])
        left_hand_image = _parse_image(data["observation.images.hand_left"])
        right_hand_image = _parse_image(data["observation.images.hand_right"])

        images = {
            "base_0_rgb": base_image,
            "left_wrist_0_rgb": left_hand_image,
            "right_wrist_0_rgb": right_hand_image,
        }

        match self.model_type:
            case _model.ModelType.PI0 | _model.ModelType.PI05:
                image_masks = {
                    "base_0_rgb": np.True_,
                    "left_wrist_0_rgb": np.True_,
                    "right_wrist_0_rgb": np.True_,
                }
            case _model.ModelType.PI0_FAST:
                image_masks = {
                    "base_0_rgb": np.True_,
                    "left_wrist_0_rgb": np.True_,
                    "right_wrist_0_rgb": np.True_,
                }
            case _:
                raise ValueError(f"Unsupported model type: {self.model_type}")

        state = _extract_state(data["observation.state"])

        inputs = {
            "state": state,
            "image": images,
            "image_mask": image_masks,
        }

        if "action" in data:
            inputs["actions"] = np.asarray(data["action"][..., :_PI05_ACTION_DIM])

        if "prompt" in data:
            if isinstance(data["prompt"], bytes):
                data["prompt"] = data["prompt"].decode("utf-8")
            inputs["prompt"] = data["prompt"]

        return inputs


@dataclasses.dataclass(frozen=True)
class A2DOutputs(transforms.DataTransformFn):
    def __call__(self, data: dict) -> dict:
        return {"actions": np.asarray(data["actions"][..., :_PI05_ACTION_DIM])}
