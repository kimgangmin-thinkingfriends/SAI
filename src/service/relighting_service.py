from datetime import datetime
import os

from fastapi import UploadFile
import numpy as np
from PIL import Image

from database import SessionLocal
from domain.relighting import Relighting
from config import get_settings, Settings
from ic_light.relighting import process_relight
from repository.relighting_repo import RelightingRepo
from utils import row_to_dict

class RelightingService:
    def __init__(self, relighting_repo: RelightingRepo):
        self.relighting_repo: RelightingRepo = relighting_repo
        self.settings: Settings = get_settings()

    async def image_relighting(
        self,
        image: UploadFile,
        prompt: str,
        bg_source: str,
        seed: int,
        image_width: int,
        image_height: int,
        steps: int,
        cfg: float,
        highres_scale: float,
        highres_denoise: float,
        lowres_denoise: float,
        num_samples: int,
        a_prompt: str,
        n_prompt: str,
    ):
        session = SessionLocal()

        try:
            with open(f"{self.settings.input_image_path}/{image.filename}", "wb") as f:
                f.write(await image.read())

            numpy_image = np.array(Image.open(image.file))

            _, result = process_relight(
                input_fg=numpy_image,
                prompt=prompt,
                image_width=image_width,
                image_height=image_height,
                num_samples=num_samples,
                seed=seed,
                steps=steps,
                a_prompt=a_prompt,
                n_prompt=n_prompt,
                cfg=cfg,
                highres_scale=highres_scale,
                highres_denoise=highres_denoise,
                lowres_denoise=lowres_denoise,
                bg_source=bg_source
            )

            Image.fromarray(result[0]).save(f"{self.settings.output_image_path}/{image.filename}")

            now = datetime.now()
            relighting = Relighting(
                id=None,
                image_filename=image.filename,
                prompt=prompt,
                bg_source=bg_source,
                seed=seed,
                image_width=image_width,
                image_height=image_height,
                steps=steps,
                cfg=cfg,
                highres_scale=highres_scale,
                highres_denoise=highres_denoise,
                lowres_denoise=lowres_denoise,
                num_samples=num_samples,
                a_prompt=a_prompt,
                n_prompt=n_prompt,
                created_at=now,
            )
            saved_entity = self.relighting_repo.save(relighting, session)
            session.commit()
            session.refresh(saved_entity)

            return Relighting(**row_to_dict(saved_entity))
        except Exception as e:
            if os.path.exists(f"{self.settings.input_image_path}/{image.filename}"):
                os.remove(f"{self.settings.input_image_path}/{image.filename}")
            if os.path.exists(f"{self.settings.output_image_path}/{image.filename}"):
                os.remove(f"{self.settings.output_image_path}/{image.filename}")
            session.rollback()
            raise e
        finally:
            session.close()