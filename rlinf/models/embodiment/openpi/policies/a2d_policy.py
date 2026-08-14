import dataclasses

import einops
import numpy as np

from openpi import transforms
from openpi.models import model as _model


def make_a2d_example() -> dict:
    return {
        "observation.state": np.random.randn(163).astype(np.float32),
        "action": np.random.randn(36).astype(np.float32),
        "observation.images.top_head": np.random.randint(256, size=(224, 224, 3), dtype=np.uint8),
        "observation.images.hand_left": np.random.randint(256, size=(224, 224, 3), dtype=np.uint8),
        "observation.images.hand_right": np.random.randint(256, size=(224, 224, 3), dtype=np.uint8),
        "prompt": "Water Bottle Grasp and Place",
    }


def _parse_image(image) -> np.ndarray:
    image = np.asarray(image)
    if np.issubdtype(image.dtype, np.floating):
        image = (255 * image).astype(np.uint8)
    if image.shape[0] == 3:
        image = einops.rearrange(image, "c h w -> h w c")
    return image


#_A2D_STATE_INDICES = np.array(
    #[0, 1] + list(range(28, 42)),  # left/right effector (0,1) + joint positions (28-41) = 16 dims
    #dtype=np.int32,
#)

#_A2D_ACTION_INDICES = np.array(
    #[0, 1] + list(range(16, 30)),  # left/right effector (0,1) + joint positions (16-29) = 16 dims
    #dtype=np.int32,
#)
_A2D_STATE_INDICES = np.array(
    list(range(28, 42)) + [0, 1],
    dtype=np.int32,
)

_A2D_ACTION_INDICES = np.array(
    list(range(16, 30)) + [0, 1],
    dtype=np.int32,
)
_A2D_ACTION_DIM = 16  # 2 effector + 14 joint positions


def _extract_state(state: np.ndarray) -> np.ndarray:
    return np.asarray(state)[..., _A2D_STATE_INDICES]


def _extract_action(action: np.ndarray) -> np.ndarray:
    return np.asarray(action)[..., _A2D_ACTION_INDICES]


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
            inputs["actions"] = _extract_action(data["action"])
        # raw_state = np.asarray(data["observation.state"])
        # state = _extract_state(raw_state)

        # raw_action = None
        # action = None
        # if "action" in data:
        #     raw_action = np.asarray(data["action"])
        #     action = _extract_action(raw_action)

        # if not hasattr(self, "_diag_count"):
        #     object.__setattr__(self, "_diag_count", 0)

        # if self._diag_count < 5:
        #     print(
        #         "[A2D_DIAG][BEFORE_NORM] "
        #         f"raw_state_shape={raw_state.shape} "
        #         f"state_shape={state.shape} "
        #         f"raw_state_first={raw_state.reshape(-1, raw_state.shape[-1])[0].tolist()} "
        #         f"state_first={state.reshape(-1, state.shape[-1])[0].tolist()}",
        #         flush=True,
        #     )

        #     if action is not None:
        #         print(
        #             "[A2D_DIAG][BEFORE_NORM_ACTION] "
        #             f"raw_action_shape={raw_action.shape} "
        #             f"action_shape={action.shape} "
        #             f"raw_action_first={raw_action.reshape(-1, raw_action.shape[-1])[0].tolist()} "
        #             f"action_first={action.reshape(-1, action.shape[-1])[0].tolist()}",
        #             flush=True,
        #         )

        #     object.__setattr__(self, "_diag_count", self._diag_count + 1)

        # inputs = {
        #     "state": state,
        #     "image": images,
        #     "image_mask": image_masks,
        # }

        # if action is not None:
        #     inputs["actions"] = action

        if "prompt" in data:
            if isinstance(data["prompt"], bytes):
                data["prompt"] = data["prompt"].decode("utf-8")
            inputs["prompt"] = data["prompt"]

        return inputs


@dataclasses.dataclass(frozen=True)
class A2DOutputs(transforms.DataTransformFn):
    def __call__(self, data: dict) -> dict:
        # Model outputs _A2D_ACTION_DIM (16) dims directly
        return {"actions": np.asarray(data["actions"][..., :_A2D_ACTION_DIM])}
