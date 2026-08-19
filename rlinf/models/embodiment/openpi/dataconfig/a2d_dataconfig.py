import dataclasses
import pathlib

import openpi.models.model as _model
import openpi.transforms as _transforms
from openpi.training.config import DataConfig, DataConfigFactory, ModelTransformFactory
from typing_extensions import override

from rlinf.models.embodiment.openpi.policies import a2d_policy


@dataclasses.dataclass(frozen=True)
class LeRobotA2DDataConfig(DataConfigFactory):
    """Data config for A2D (Genie G01) robot in LeRobot v2 format.

    The A2D dataset contains:
    - State: 163-dim (extracted subset: 2 effector + 14 joint = 16 dims)
    - Action: 36-dim (extracted subset: 2 effector + 14 joint = 16 dims)
    - Images: observation.images.top_head (base),
              observation.images.hand_left (left wrist),
              observation.images.hand_right (right wrist)
    - Action key: "action" (LeRobot v2 style, not "actions")
    """

    default_prompt: str | None = None
    extra_delta_transform: bool = False

    @override
    def create(
        self, assets_dirs: pathlib.Path, model_config: _model.BaseModelConfig
    ) -> DataConfig:
        # No repack needed: A2DInputs directly accesses the LeRobot v2 dot-notation keys.
        repack_transform = _transforms.Group()

        data_transforms = _transforms.Group(
            inputs=[a2d_policy.A2DInputs(model_type=model_config.model_type)],
            outputs=[a2d_policy.A2DOutputs()],
        ).push(
            # Match the immutable ``pi05_agibot_g01`` serving contract:
            # train joints 0:14 as action - current_state, but leave the two
            # gripper commands absolute.  During local inference the inverse
            # transform restores absolute joint targets before A2DOutputs.
            inputs=[
                _transforms.DeltaActions(a2d_policy.A2D_JOINT_ACTION_MASK)
            ],
            outputs=[
                _transforms.AbsoluteActions(a2d_policy.A2D_JOINT_ACTION_MASK)
            ],
        )

        model_transforms = ModelTransformFactory(
            default_prompt=self.default_prompt
        )(model_config)

        return dataclasses.replace(
            self.create_base_config(assets_dirs, model_config),
            repack_transforms=repack_transform,
            data_transforms=data_transforms,
            model_transforms=model_transforms,
            action_sequence_keys=("action",),
        )
