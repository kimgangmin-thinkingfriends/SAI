from datetime import datetime

from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Relighting(Base):
    __tablename__ = "relightings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    image_filename: Mapped[str] = mapped_column(String, nullable=False)
    prompt: Mapped[str] = mapped_column(String, nullable=False)
    bg_source: Mapped[str] = mapped_column(String, nullable=False)
    seed: Mapped[int] = mapped_column(Integer, nullable=False)
    image_width: Mapped[int] = mapped_column(Integer, nullable=False)
    image_height: Mapped[int] = mapped_column(Integer, nullable=False)
    steps: Mapped[int] = mapped_column(Integer, nullable=False)
    cfg: Mapped[float] = mapped_column(Float, nullable=False)
    highres_scale: Mapped[float] = mapped_column(Float, nullable=False)
    highres_denoise: Mapped[float] = mapped_column(Float, nullable=False)
    lowres_denoise: Mapped[float] = mapped_column(Float, nullable=False)
    a_prompt: Mapped[str] = mapped_column(String, nullable=True)
    n_prompt: Mapped[str] = mapped_column(String, nullable=True)
    num_samples: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)