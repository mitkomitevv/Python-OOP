from Exercise.python_oop_exam_2023_12_19.project.climbers.base_climber import BaseClimber
from Exercise.python_oop_exam_2023_12_19.project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    MIN_STRENGTH = 75

    def __init__(self, name: str):
        super().__init__(name, strength=self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MIN_STRENGTH

    def climb(self, peak: BasePeak):
        multiplier = 1.3 if peak.difficulty_level == "Advanced" else 2.5
        self.strength -= 30.0 * multiplier
        self.conquered_peaks.append(peak.name)
