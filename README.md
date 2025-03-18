# Simulating Neural System Evolution in Simple Organisms Using Conway’s Game of Life

A Python project exploring how simple neural architectures can evolve and adapt within a **Conway’s Game of Life** environment. We combine **Genetic Algorithms** (GAs), **Hopfield-inspired** neuronal modeling, and optional **Hebbian Learning** to simulate evolving “organisms” in a cellular automaton world.

---

## Table of Contents
1. [Installation](#installation)  
2. [Overview](#overview)  
3. [Project Structure](#project-structure)  
4. [Usage](#usage)  
5. [Results & Visualization](#results--visualization)  
6. [Contributors](#contributors)  
7. [References](#references)  
8. [License](#license)

---

## Installation

### Prerequisites
- **Python** (3.8+ recommended)
- **pip** (Python package manager)

### Setup & Dependencies
```bash
# Clone the repository
git clone https://github.com/your-repo-url.git
cd your-repo-name

# Install dependencies
pip install -r requirements.txt
Overview
Game of Life Environment

Each cell follows GoL rules (birth, survival, death) based on neighbor states.
Serves as the “world” where digital organisms live.
Neural Network Model

Each organism uses a simplified binary-threshold network (optionally with Hebbian Learning).
Inspired by Hopfield Networks.
Genetic Algorithm (GA) Evolution

Fitness: Organisms are scored on survival and behavior efficiency.
Selection & Variation: Best performers reproduce; crossover & mutation generate new neural connections.
Optional Hebbian Learning

Synapses (“connections”) that fire together strengthen over time.
Allows in-run adaptation to environment dynamics.
Project Structure
bash
Copy
Edit
repo-name/
├─ src/
│  ├─ game_of_life.py         # Conway's Game of Life implementation
│  ├─ neural_network.py       # Neural network model (e.g., Hopfield-like)
│  ├─ genetic_algorithm.py    # GA for evolving neural parameters
│  ├─ visualization.py        # Plotting/animation utilities
│  └─ main.py                 # Entry point to run simulations
├─ docs/
│  ├─ literature_review.md    # Summaries of referenced papers/materials
│  ├─ methodology.md          # Detailed approach & design
├─ results/
│  ├─ evolution_output.json   # Fitness & network data logs
│  └─ graphs/                 # Any plots saved here
├─ README.md
├─ requirements.txt
└─ LICENSE
Usage
Run the Main Simulation
bash
Copy
Edit
python src/main.py
This launches the GoL environment, initializes organisms, and runs the genetic evolution loop.

Visualize Evolution
bash
Copy
Edit
python src/visualization.py
Generates plots or animations of:

Fitness over generations
Neural architecture changes
Live GoL playback (if supported)
Results & Visualization
After each simulation, you’ll find:

Fitness Logs: See how survival/behavior scores evolve.
Neural Architecture Evolution: Observe synaptic changes across generations.
Animated GoL: (Optional) track real-time changes to the GoL grid.
Artifacts typically appear in the results/ folder.

Contributors
Hemant – Genetic Algorithm & Game of Life integration
Angie – Neural Network implementation & visualization
References
This project builds on COMP5400 lecture material:

Genetic Algorithms & Co-evolution
[Evolution-1], [Evolution-2]
Neural Networks (Hopfield, Hebbian)
[Hebbian-Learning], [COMP5400M 10 Hopfield]
Swarm Intelligence & Self-organization
[swarm_intelligence_1], [swarm_intelligence_2]
Cellular Automata (GoL)
[lec1-2025]
See docs/ for more details.