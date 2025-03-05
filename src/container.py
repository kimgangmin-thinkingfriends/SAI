from dependency_injector import containers, providers

from service.relighting_service import RelightingService
from repository.relighting_repo import RelightingRepo


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["routers", "service"])

    relighting_repo = providers.Singleton(RelightingRepo)
    relighting_service = providers.Singleton(RelightingService, relighting_repo=relighting_repo)
    

