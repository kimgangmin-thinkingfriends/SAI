from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=False)
class Relighting:
    id: int | None
    image_filename: str
    prompt: str
    bg_source: str
    seed: int
    image_width: int
    image_height: int
    steps: int
    cfg: float
    highres_scale: float
    highres_denoise: float
    lowres_denoise: float
    num_samples: int
    a_prompt: str
    n_prompt: str
    created_at: datetime
