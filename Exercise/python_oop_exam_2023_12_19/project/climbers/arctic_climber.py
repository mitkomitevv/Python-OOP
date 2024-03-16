from Exercise.python_oop_exam_2023_12_19.project.climbers.base_climber import BaseClimber
from Exercise.python_oop_exam_2023_12_19.project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    MIN_STRENGTH = 100

    def __init__(self, name: str):
        super().__init__(name, strength=self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MIN_STRENGTH

    def climb(self, peak: BasePeak):
        multiplier = 2.0 if peak.difficulty_level == "Extreme" else 1.5
        self.strength -= 20.0 * multiplier
        self.conquered_peaks.append(peak.name)
