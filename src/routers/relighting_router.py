from fastapi import APIRouter, status, File, Form, UploadFile, Depends
from dependency_injector.wiring import inject, Provide

from container import Container
from service.relighting_service import RelightingService

router = APIRouter(prefix="/api/relighting", tags=["relighting"])

@router.post("", status_code=status.HTTP_201_CREATED)
@inject
async def image_relighting(
    image: UploadFile = File(...),
    prompt: str = Form(...),
    bg_source: str = Form(...),
    seed: int = Form(...),
    image_width: int = Form(...),
    image_height: int = Form(...),
    steps: int = Form(...),
    cfg: float = Form(...),
    highres_scale: float = Form(...),
    highres_denoise: float = Form(...),
    lowres_denoise: float = Form(...),
    num_samples: int = Form(...),
    a_prompt: str = Form(...),
    n_prompt: str = Form(...),
    relighting_service: RelightingService = Depends(Provide[Container.relighting_service])
):
    return await relighting_service.image_relighting(
        image=image,
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
        n_prompt=n_prompt
    )