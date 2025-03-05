from sqlalchemy.orm import Session

from domain.relighting import Relighting as RelightingVO
from models.relighting import Relighting

class RelightingRepo:
    def save(self, relight_vo: RelightingVO, session: Session) -> Relighting:
        relighting = Relighting(
            image_filename=relight_vo.image_filename,
            prompt=relight_vo.prompt,
            bg_source=relight_vo.bg_source,
            seed=relight_vo.seed,
            image_width=relight_vo.image_width,
            image_height=relight_vo.image_height,
            steps=relight_vo.steps,
            cfg=relight_vo.cfg,
            highres_scale=relight_vo.highres_scale,
            highres_denoise=relight_vo.highres_denoise,
            lowres_denoise=relight_vo.lowres_denoise,
            num_samples=relight_vo.num_samples,
            a_prompt=relight_vo.a_prompt,
            n_prompt=relight_vo.n_prompt,
            created_at=relight_vo.created_at
        )

        session.add(relighting)

        return relighting