# Pandemic Simulation

This project simulates the spread of an epidemic in a city over a given number of days. It models interactions between individuals and buildings such as schools, hospitals, and shops, tracking infection, immunity, and overall health within a population.

## Features
- Simulates a city with multiple building types (schools, hospitals, shops).
- Tracks the health status of individuals (healthy, sick, immune).
- Models infection spread within buildings based on visitor interactions.
- Visualizes the simulation results using graphs.

## Prerequisites
To run this simulation, ensure you have the following installed:
- Python 3.x
- Required libraries: 
  - `matplotlib`

Install dependencies using pip:
```bash
pip install matplotlib
```

## Project Structure
```
Classes/
  Building.py         # Base class for buildings
  Individual.py       # Individual class representing a person
  Data.py             # Class to collect and store simulation data
  Day.py              # Class representing a day in the simulation
  School.py           # Subclass of Building for schools
  Hospital.py         # Subclass of Building for hospitals
  Shop.py             # Subclass of Building for shops
  constants.py        # Constants for simulation parameters
index.py               # Main simulation script
```

## Constants
Define key simulation parameters in `Classes/constants.py`:
- `INFECTION_DURATION`: Duration an individual remains sick (in days).
- `INFECTION_RATE`: Probability of infection when visiting a building.
- `INITIAL_INFECTED`: Initial number of infected individuals.
- `DAY_COUNT`: Total number of days for the simulation.
- `POPULATION_LEN`: Total population size.

## How It Works
1. **City Initialization**:
   - The city is populated with schools, hospitals, and shops.
   - Each building has a capacity limit for visitors.

2. **Individual Initialization**:
   - Individuals are created with unique IDs.
   - A subset of individuals are initialized as infected.

3. **Daily Simulation**:
   - Individuals visit random buildings based on availability.
   - Infected individuals can spread the infection to others in the same building.
   - Health status updates for all individuals (e.g., transitioning from sick to immune).

4. **Data Logging and Visualization**:
   - Health statistics (e.g., sick, immune) are logged daily.
   - Results are plotted at the end of the simulation.

## Usage
Run the simulation using the following command:
```bash
python index.py
```

## Example Output
The simulation outputs daily logs showing the progress of the epidemic, followed by a graph:
- **Population Curve**: Tracks the total population.
- **Sick Individuals**: Tracks the number of currently infected individuals.
- **Immune Individuals**: Tracks individuals who have gained immunity.

## Customization
You can modify simulation parameters in `Constants/constants.py` to:
- Change population size.
- Adjust infection duration and rate.
- Modify the number of buildings or their capacities.
- Adjust the city configuration

## Visualization
A graph is generated at the end of the simulation to visualize:
- Total population
- Sick individuals
- Immune individuals

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the Python community for providing libraries like `matplotlib` that make data visualization straightforward.
