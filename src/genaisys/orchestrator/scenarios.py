from dataclasses import dataclass
from enum import Enum


class ScenarioType(Enum):
    MARKET_ANALYSIS = 1
    SENTIMENT_ANALYSIS = 2
    SEMANTIC_SEARCH = 3

# Creates __init__, string representation, comparison helpers
# class Scenario:
#     def __init__(self, scenario_number, name, description):
#         self.scenario_number = scenario_number
#         self.name = name
#         self.description = description
@dataclass # shortcut to create simple classes that mainly store data
class Scenario:
    scenario_number: int
    name: str
    description: str


SCENARIOS = [
    # Market
    Scenario(
        scenario_number=1,
        name="Market Analysis",
        description=(
            "Market Semantic analysis. You will be provided with a market survey "
            "on a given range of products. The term 'market' must be in the user "
            "or system input. Your task is to provide an analysis."
        )
    ),
    # Sentiment
    Scenario(
        scenario_number=2,
        name="Sentiment Analysis",
        description=(
            "Sentiment analysis. Read the content and classify it as an opinion. "
            "If it is not an opinion, stop there. If it is an opinion, perform "
            "a sentiment analysis and provide a score with the label: "
            "'Analysis score:' followed by a value between 0 and 1. Add an explanation."
        )
    ),
    # Semantic analysis
    Scenario(
        scenario_number=3,
        name="Semantic Search",
        description=(
            "Semantic analysis. This is not an analysis but a semantic search. "
            "Provide more information on the topic."
        )
    )
]


def get_scenario(scenario_number: int) -> Scenario | None:
    """Retrieve a scenario by its number."""
    for scenario in SCENARIOS:
        if scenario.scenario_number == scenario_number:
            return scenario
    return None