# Smart Fitness Session Analyzer

## Project information
- Selected option: Option A - Smart Fitness Session Analyzer
- Student name: Tobias Danielsen
- Student number: s385486
- Repository: https://github.com/TobiasDani/Smart-Fitness-Session-Analyzer

## Short description
This project reads simulated fitness data, validates each measurement window, compares the session with the participant's baseline values, classifies the session, and prints a readable summary report.

## Class design
- `Participant`: stores the participant ID and baseline values.
- `Observation`: represents one measurement window and validates whether the data is acceptable.
- `Session`: holds all observations for one session, tracks rejected values, and performs the main analysis.
- `Report`: turns the computed results into a readable report.

## Design choices
- Composition is used instead of inheritance. A `Session` contains a `Participant`, and a `Session` also contains many `Observation` objects. This matches the real structure of the data and keeps the code clearer and easier to maintain.
- Encapsulation is shown through the protected-style `classification` field in `Session`, which is controlled through a property.
- A `staticmethod` is used in `Participant` to validate baseline values without creating an instance.
- Inheritance and method overriding are not used because the application has no meaningful "is-a" relationship between participants, observations, sessions and reports. Composition is more suitable for this data model.

## Classification and assumptions

The program uses a simple rule-based system designed for the simulated dataset:
- `resting`: average activity is below 0.2 and average heart rate is no more than 8 BPM above baseline
- `moderate activity`: activity is above the resting range without meeting the high activity threshold
- `high activity`: average activity is at least 0.65 or average heart rate is at least 30 BPM above baseline
- `recovering`: heart rate drops by more than 8 BPM and activity drops by more than 0.10 between the first and second half of the session
- `insufficient data`: fewer than 3 valid observations or average signal quality is below 0.6

Observation values outside the accepted ranges are rejected before analysis.

## Installation and running
This project uses only the Python standard library.

Clone the repository and run it from the project root:

```bash
git clone https://github.com/TobiasDani/Smart-Fitness-Session-Analyzer.git
cd Smart-Fitness-Session-Analyzer
python main.py
```

If your system uses `python3` instead, run:

```bash
python3 main.py
```

Run the tests with:

```bash
python tests.py
```

## Example output
```text
Fitness Session Report
------------------------------
Total observations: 10
Usable observations: 10
Rejected observations: 0
Classification: recovering

Heart rate
Average: 112.8
Minimum: 79
Maximum: 141
Difference from baseline: +34.8

Explanation: The session shows a clear drop in heart rate and activity toward the end, which is consistent with recovery.
```

## Known limitations
- The classification is rule-based and intentionally simple.
- It is designed for the simulated dataset and assignment requirements, not for real-world medical or training analysis.
- Recovery detection depends on comparing the early and late parts of the session, so very short sessions may be less reliable.
- If one value in an observation is missing, or outside the accepted range, the entire observation is rejected rather than partially used.
