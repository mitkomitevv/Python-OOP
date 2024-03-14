from typing import List
from climbers.arctic_climber import ArcticClimber
from climbers.summit_climber import SummitClimber
from peaks.arctic_peak import ArcticPeak
from peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    PEAK_TYPE = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        try:
            next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            self.climbers.append(self.CLIMBER_TYPES[climber_type](climber_name))
            return f"{climber_name} is successfully registered as a {climber_type}."

        return f"{climber_name} has been already registered."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPE:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(self.PEAK_TYPE[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        if set(peak.get_recommended_gear()) == set(gear):
            return f"{climber_name} is prepared to climb {peak_name}."

        missing_gear = set(gear).symmetric_difference(set(peak.get_recommended_gear()))
        climber.is_prepared = False
        return (f"{climber_name} is not prepared to climb {peak_name}. "
                f"Missing gear: {', '.join(sorted(missing_gear))}.")

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        result = [f"Total climbed peaks: {len(self.peaks)}\n"
                  "**Climber's statistics:**"]

        sorted_climbers = sorted(self.climbers, key=lambda c: (-len(c.conquered_peaks), c.name))

        result.append('\n'.join(str(c) for c in sorted_climbers if c.conquered_peaks))

        return '\n'.join(result)
