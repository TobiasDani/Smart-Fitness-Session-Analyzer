class Session:
    def __init__(self, participant):
        self.participant = participant
        self.observations = []
        self.rejected_observations = 0
        self.classification


    def add_single_observation(self, observation):
        if observation.is_valid():
            self.observations.append(observation)
        else:
            self.rejected_observations += 1


    def calculate_summary(self):
        attributes = [
            "heart_rate",
            "skin_response",
            "temperature",
            "activity_level",
            "signal_quality",
        ]

        summary = {}

        for field in attributes:
            values = [getattr(obs, field) for obs in self.observations]

            summary[field] = {
                "average": sum(values) / len(values),
                "minimum": min(values),
                "maximum": max(values),
            }

        return summary
