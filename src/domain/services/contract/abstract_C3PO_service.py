from abc import ABC, ABCMeta, abstractmethod


class AbstractC3POService(ABC):
    """
        An abstract base class that defines the structure for services calculating the odds of successful travel for the Millennium Falcon.

        This class uses the `ABC` module to enforce that subclasses must implement specific methods related to calculating the odds of success in a given scenario. It is designed to be inherited by other classes that provide the actual implementation of the `giveMeTheOdds` method.

        ...

        Methods
        -------
        giveMeTheOdds(empireJsonFilePath: str) -> None
            An abstract method that must be implemented by any subclass. It calculates the probability of successfully completing the journey based on a given scenario, which includes factors such as travel time, fuel, and potential obstacles.
        """

    __metaclass__ = ABCMeta


    @abstractmethod
    def giveMeTheOdds(self, empireJsonFilePath: str) -> None: raise NotImplementedError