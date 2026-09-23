from observation import Observation
from participant import Participant
from report import Report
from session import Session

from data_generator import available_scenarios, generate_fitness_data


def main():
    # print("Available scenarios:", available_scenarios())

    profile, observations = generate_fitness_data(
        participant_id="P001",
        scenario="recovery",
        seed=42,
        number_of_windows=10,
    )

    profile, session = new_fitness_session(profile, observations)

    print(session.calculate_summary())


def new_fitness_session(profile_in, observations_in):
    """Creates a new session bla bla

    Args:
        bla bla
    
    Returns:
        bla bla
        
    """
    profile = Participant(profile_in["participant_id"], profile_in["baseline_heart_rate"], profile_in["baseline_skin_response"], profile_in["baseline_temperature"])

    observations = [
        Observation(obs["timestamp"], obs["heart_rate"], obs["skin_response"], obs["temperature"], obs["activity_level"], obs["signal_quality"])
        for obs in observations_in
    ]

    session = Session(profile)

    for obs in observations:
        session.add_single_observation(obs) 

    return profile, session





    '''
    print("\nParticipant profile")
    print(profile)

    print("\nObservations")
    for observation in observations:
        print(observation)

    # Your program should convert these dictionaries into your own objects,
    # validate them, analyze the complete session, and produce a report.
    '''

if __name__ == "__main__":
    main()
    

