from dependency_injector import containers, providers
from domain.services.contract.abstract_C3PO_service import AbstractC3POService
from domain.services.contract.abstract_logger_service import AbstractLoggerService
from application.C3PO.C3POService import C3POService
from application.logger.loggerService import LoggerService

"""
    A container for managing the dependency injection of service instances in the application.

    This script uses the `dependency_injector` library to manage and inject dependencies for various services. The `Services` container registers concrete service classes that implement abstract service interfaces, such as `AbstractC3POService` and `AbstractLoggerService`. 
    These services are made available for dependency injection in the `Application` container, which acts as a central point for accessing services within the application.

    The services are registered as follows:
    - `logger_provider`: A singleton provider for the logger service (`LoggerService`) that implements the `AbstractLoggerService` interface.
    - `C3PO_Service`: A factory provider for the `C3POService` that implements the `AbstractC3POService` interface. It also takes a logger instance as a dependency, which is injected from the `logger_provider`.

    The `Application` container holds the `services` container, allowing other parts of the application to access the configured services.

    ...

    Attributes
    ----------
    logger_provider : providers.Singleton
        A provider for the logger service, ensuring a single instance of `LoggerService`.
    C3PO_Service : providers.Factory
        A factory provider for the `C3POService`, injecting the logger service as a dependency.

    """


class Services(containers.DeclarativeContainer):

    logger_provider = providers.Singleton(AbstractLoggerService.register(LoggerService))
    #C3POService
    C3PO_Service = providers.Factory(AbstractC3POService.register(C3POService),logger=logger_provider)

class Application(containers.DeclarativeContainer):

    services = providers.Container(Services)