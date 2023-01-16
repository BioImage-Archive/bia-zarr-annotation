from pydantic import BaseModel
from typing import List, Optional


class ChannelRendering(BaseModel):
    colormap_start: List[float]
    colormap_end: List[float]
    scale_factor: float = 1.0


class RenderingInfo(BaseModel):
    channel_renders: List[ChannelRendering]
    default_z: Optional[int]
    default_t: Optional[int]


