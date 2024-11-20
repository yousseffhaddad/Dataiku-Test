from domain.exceptions.application_error import ApplicationError
from domain.exceptions.file_not_found import JsonFileNotFound
from domain.services.contract.abstract_C3PO_service import AbstractC3POService
from domain.services.contract.abstract_logger_service import AbstractLoggerService
import logging
from shared.helpers.json_reader import read_json_file

from collections import deque, defaultdict

class C3POService (AbstractC3POService):
    """
        A class used to calculate the odds of successful travel for the Millennium Falcon using BFS algorithm.

        ...

        Attributes
        ----------
        autonomy : int
            The maximum distance (in days of travel) the Millennium Falcon can cover without refueling.
        routes : list
            A list of routes between planets, including their travel times.
        graph : defaultdict
            A graph representation of the routes, where each planet is connected to its neighboring planets with travel times.
        logger : logging.Logger
            Logger instance for writing logs.

        Methods
        -------
        giveMeTheOdds(empireJsonFilePath: str) -> float
            Computes the probability of successfully reaching Endor without being captured by bounty hunters.
        _capture_probability(planet: str, day: int, bounty_hunters: dict) -> float
            Calculates the probability of not being captured by bounty hunters on a specific planet on a given day.
    """

    def __init__(self, millenniumFalconJsonFilePath,logger:AbstractLoggerService):
        self.logger: logging = logger.get_logger()

        try:
            self.logger.debug(f"Reading millenniumFalcon data from JSON file : {millenniumFalconJsonFilePath}.")
            falcon_data = read_json_file(millenniumFalconJsonFilePath)
        except FileNotFoundError:
            raise JsonFileNotFound(file_path=millenniumFalconJsonFilePath)
        except Exception as e:
            raise ApplicationError("Failed to read Millennium Falcon JSON file", str(e))

        self.logger.debug("Initializing C3POService with Falcon data.")
        self.autonomy = falcon_data['autonomy']
        self.routes = falcon_data['routes']

        if not self.autonomy or not self.routes:
            raise ApplicationError("Invalid Falcon data", "Missing 'autonomy' or 'routes' in the JSON file.")

        self.logger.debug("Building graph representation of the routes.")
        self.graph = defaultdict(list)
        for route in self.routes:
            self.graph[route['origin']].append((route['destination'], route['travelTime']))
            self.graph[route['destination']].append((route['origin'], route['travelTime']))

    def giveMeTheOdds(self, empireJsonFilePath) -> float:

        try:
            self.logger.debug(f"Reading Empire data from JSON file: {empireJsonFilePath}")
            empire_data = read_json_file(empireJsonFilePath)
        except FileNotFoundError:
            raise JsonFileNotFound(file_path=empireJsonFilePath)
        except Exception as e:
            raise ApplicationError("Failed to read Empire JSON file", str(e))
        countdown = empire_data['countdown']
        bounty_hunters = defaultdict(set)
        for hunter in empire_data['bounty_hunters']:
            bounty_hunters[hunter['planet']].add(hunter['day'])

        if countdown is None or not bounty_hunters:
            raise ApplicationError("Invalid Empire data", "Missing 'countdown' or 'bounty_hunters' in the JSON file.")

        # BFS initialization
        self.logger.debug("Starting BFS traversal to calculate odds.")
        queue = deque([(0, 'Tatooine', self.autonomy, 1.0)])  # (current day, planet, fuel, success probability)
        visited = {}  # Track the max probability for each state

        max_success_probability = 0.0

        while queue:
            current_day, current_planet, fuel, probability = queue.popleft()

            self.logger.debug(f"Exploring state: Day {current_day}, Planet {current_planet}, "f"Fuel {fuel}, Probability {probability}.")

            # Skip states visited with higher or equal probabilities
            state = (current_day, current_planet, fuel)
            if state in visited and visited[state] >= probability:
                self.logger.debug(f"Skipping state {state} as it has already been visited with higher probability.")
                continue
            visited[state] = probability

            # If reached Endor before countdown, update max success probability
            if current_planet == 'Endor' and current_day <= countdown:
                self.logger.debug(f"Reached Endor on Day {current_day} with probability {probability}.")
                max_success_probability = max(max_success_probability, probability)
                continue

            # Refuel option
            if fuel < self.autonomy:
                next_day = current_day + 1
                refuel_probability = probability * self._capture_probability(current_planet, next_day, bounty_hunters)
                self.logger.debug(f"Refueling on {current_planet} on Day {next_day} with probability {refuel_probability}.")
                queue.append((next_day, current_planet, self.autonomy, refuel_probability))

            # Wait option
            wait_day = current_day + 1
            if wait_day <= countdown:
                wait_probability = probability * self._capture_probability(current_planet, wait_day, bounty_hunters)
                self.logger.debug(f"Waiting on {current_planet} on Day {wait_day} with probability {wait_probability}.")
                queue.append((wait_day, current_planet, fuel, wait_probability))

            # Explore neighbors
            for neighbor, travel_time in self.graph[current_planet]:
                if fuel >= travel_time:  # Check if there is enough fuel
                    next_day = current_day + travel_time
                    if next_day <= countdown:  # Check if within countdown
                        travel_probability = probability * self._capture_probability(neighbor, next_day, bounty_hunters)
                        self.logger.debug(f"Traveling to {neighbor} on Day {next_day} with probability {travel_probability}.")
                        queue.append((next_day, neighbor, fuel - travel_time, travel_probability))

        self.logger.debug(f"Maximum success probability: {max_success_probability}")
        return round(max_success_probability, 6)

    def _capture_probability(self, planet, day, bounty_hunters):

        """Calculate the probability of not being captured on a planet on a specific day."""

        self.logger.debug(f"Calculating capture probability for {planet} on Day {day}.")
        if day in bounty_hunters[planet]:
            self.logger.debug(f"Bounty hunters present on {planet} on Day {day}.")
            return 0.9  # 10% chance of capture
        return 1.0  # No bounty hunters

