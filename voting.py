# Jaswanth Kattubavi Sreenivasulu
# 201760526

from typing import Dict, List, Union
from openpyxl import Workbook
from collections import defaultdict, Counter

def generate_preferences(sheet: Workbook) -> Dict[int, List[int]]:
    """
    In this method we generate a preference profile based on the given sheet.
    Return: We return a dictionary representing agent preferences.
    """
    agent_pref = {}

    for agent_index, values in enumerate(sheet.iter_rows(values_only=True), start=1):
        preference_tracker = defaultdict(list)

        for preference_idx, value in enumerate(values, start=1):
            preference_tracker[value].append(preference_idx)

        sorted_preferences = sorted(
            preference_tracker.items(),
            key=lambda x: (len(x[1]), x[0]),
            reverse=True
        )

        preferences = [p_idx for val, indices in sorted_preferences for p_idx in sorted(indices, reverse=True)]

        agent_pref[agent_index] = preferences

    return agent_pref


def apply_tie_break(winners: List[int], preferences: Dict[int, List[int]], tie_break: Union[str, int]) -> int:
    """
    We apply tie-breaking rules to determine the winner among the tied alternatives.
    Returns: We return the winner among tied alternatives.
    """
    if tie_break in {"max", "min"}:
        return getattr(__builtins__, tie_break)(winners)
    elif isinstance(tie_break, int):
        return dictatorship(preferences, tie_break)

    else:
        raise ValueError("Invalid tie_break option")


def dictatorship(pref_profile: Dict[int, List[int]], agent: int) -> int:
    """
    Determine the winner according to the Dictatorship rule.
    Returns: We return the winner according to Dictatorship rule.
    """
    agent_preference = pref_profile.get(agent)

    if agent_preference is not None:
        return agent_preference[0]
    else:
        raise ValueError("Invalid agent!")

def plurality(preferences: Dict[int, List[int]], tie_break: Union[int, str]) -> int:

    """
    We determine the winner according to the Plurality rule.
    Returns:We return the winner according to the Plurality rule.
    """
    votes_count = Counter(preference[0] for preference in preferences.values())
    max_votes = max(votes_count.values())
    winning_candidates = [candidate for candidate, votes in votes_count.items() if votes == max_votes]
    if len(winning_candidates) == 1:
        return winning_candidates[0]
    return apply_tie_break(winning_candidates, preferences, tie_break)

def veto(preferences: Dict[int, List[int]], tie_break: Union[int, str]) -> int:
    """
    We determine the winner according to the Veto rule.
    Returns:We return the winner according to the Veto rule.
    """
    alternative_points = Counter(vote for votes in preferences.values() for vote in votes[:-1])

    max_points = max(alternative_points.values())
    winner_candidates = [alt for alt, points in alternative_points.items() if points == max_points]

    if len(winner_candidates) == 1:
        return winner_candidates[0]

    return apply_tie_break(winner_candidates, preferences, tie_break)


def borda(preferences: Dict[int, List[int]], tie_break: Union[int, str]) -> int:
    """
    Determine the winner according to the Borda rule.
    Returns: We return the winner according to the Borda rule.
    """
    alternative_scores = defaultdict(int)

    for votes in preferences.values():
        for position, vote in enumerate(reversed(votes)):
            alternative_scores[vote] += position

    max_score = max(alternative_scores.values())
    winning_candidates = [alt for alt, score in alternative_scores.items() if score == max_score]

    if len(winning_candidates) == 1:
        return winning_candidates[0]

    return apply_tie_break(winning_candidates, preferences, tie_break)


def harmonic(preferences: Dict[int, List[int]], tie_break: Union[int, str]) -> int:
    """
    We determine the winner according to the Harmonic rule.
    Returns: We return the winner according to the Harmonic rule.
    """
    alternative_scores = calculate_harmonic_scores(preferences)

    max_score = max(alternative_scores.values())
    winning_candidates = [alternative for alternative, score in alternative_scores.items() if score == max_score]

    if len(winning_candidates) == 1:
        return winning_candidates[0]

    return apply_tie_break(winning_candidates, preferences, tie_break)

def calculate_harmonic_scores(preferences: Dict[int, List[int]]) -> defaultdict:
    """
    Calculate Harmonic scores for each alternative.
    Returns:Here we return harmonic scores for each alternative.
    """
    alternative_scores = defaultdict(float)

    for votes in preferences.values():
        alternative_scores.update(
            (vote, alternative_scores[vote] + 1 / weight) for weight, vote in enumerate(votes, start=1))

    return alternative_scores


def scoring_rule(preferences: Dict[int, List[int]], score_vector: List[int], tie_break: Union[int, str]) -> int:
    """
    Here we determine the winner using the Scoring Rule.
    Returns:We return the winner according to the Scoring Rule.
    """
    num_alternatives = len(score_vector)

    if any(len(votes) != num_alternatives for votes in preferences.values()):
        print("Incorrect input: Inconsistent number of alternatives in preferences.")
        return -1

    alternative_scores = defaultdict(int)

    for votes in preferences.values():
        for alternative, score in zip(votes, score_vector):
            alternative_scores[alternative] += score

    max_score_for_alternative = max(alternative_scores.values())
    winning_candidates = [alternative for alternative, scores in alternative_scores.items() if scores == max_score_for_alternative]

    if len(winning_candidates) == 1:
        return winning_candidates[0]

    return apply_tie_break(winning_candidates, preferences, tie_break)


def range_voting(sheet: Workbook, tie_break: Union[int, str]) -> int:
    """
    Here we determine the winner using Range Voting.
    Returns: We return the winner according to Range Voting.
    """
    values = list(sheet.iter_rows(values_only=True))
    alternative_max_sums = [sum(row) for row in zip(*values)]
    max_points = max(alternative_max_sums)
    winner_candidates = [agent_id for agent_id, alt_sum in enumerate(alternative_max_sums, start=1) if alt_sum == max_points]

    if len(winner_candidates) == 1:
        return winner_candidates[0]

    return apply_tie_break(winner_candidates, sheet, tie_break)

def STV(preferences: Dict[int, List[int]], tie_break: Union[int, str]) -> int:
    """
    Here we determine the winner using Single Transferable Vote (STV).
    Returns: We return the winner according to Single Transferable Vote (STV).
    """
    while any(preferences.values()):
        top_alternative_counts = Counter(votes[0] for votes in preferences.values())
        least_votes_for_alternative = min(top_alternative_counts.values())
        eliminated_alternatives = [
            alternative for alternative, votes in top_alternative_counts.items() if votes == least_votes_for_alternative
        ]

        preferences = {
            agent_id: [pref for pref in agent_prefs if pref not in eliminated_alternatives]
            for agent_id, agent_prefs in preferences.items()
        }

    if len(eliminated_alternatives) == 1:
        return eliminated_alternatives[0]

    return apply_tie_break(eliminated_alternatives, preferences, tie_break)
