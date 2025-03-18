Simulating Neural System Evolution in Simple Organisms Using Conway’s Game of Life
📌 Project Overview
This project explores how different neural architectures influence behavior by simulating the evolution of a simplified nervous system within Conway’s Game of Life (GoL). Inspired by the neural structure of C. elegans, we model adaptive neural networks that evolve to optimize sensorimotor functions in a dynamic environment.

We implement Genetic Algorithms (GA) to evolve neural connections, integrating Hebbian Learning for synapse optimization. The simulation runs in a Python-based cellular automata environment, using GoL as a foundation for organism interactions.

📜 Table of Contents
Installation
How It Works
Project Structure
Usage
Results & Visualization
Contributors
References
🚀 Installation
Prerequisites
Ensure you have the following installed:

Python 3.8+
pip (Python package manager)
Install Dependencies
Clone this repository and install required libraries:

bash
Copy
Edit
git clone https://github.com/your-repo-url.git
cd your-repo-name
pip install -r requirements.txt
🔬 How It Works
1. Conway’s Game of Life (GoL) Environment
The cellular automata represents a simplified digital world where organisms evolve over time. Each cell follows GoL rules, determining its survival based on neighboring states.

2. Neural Network Model
Each "organism" has a simplified neural network modeled using binary threshold neurons, inspired by Hopfield Networks. The connections evolve using Genetic Algorithms.

3. Genetic Algorithm (GA) Evolution
Fitness Function: Organisms are evaluated based on survival and behavior efficiency.
Selection: The best-performing organisms propagate.
Crossover & Mutation: New neural structures emerge via genetic variation.
4. Learning Mechanism: Hebbian Learning (Optional)
Strengthens frequently used synapses: "Neurons that fire together wire together."
Enables adaptive changes to organism responses over generations.
📂 Project Structure
bash
Copy
Edit
/repo-name
│── /src
│   ├── game_of_life.py         # Conway's Game of Life implementation
│   ├── neural_network.py       # Neural network model
│   ├── genetic_algorithm.py    # Genetic algorithm for evolving networks
│   ├── visualization.py        # Visual output for evolution
│   ├── main.py                 # Entry point for running simulations
│── /docs
│   ├── literature_review.md    # Summary of research materials
│   ├── methodology.md          # Explanation of approach and implementation
│── /results
│   ├── evolution_output.json   # Recorded fitness and network evolution data
│   ├── graphs/                 # Plots of results
│── README.md                   # Project documentation
│── requirements.txt             # Dependencies
│── LICENSE                      # License information
🛠️ Usage
Run the main simulation:

bash
Copy
Edit
python src/main.py
To visualize evolution:

bash
Copy
Edit
python src/visualization.py
📊 Results & Visualization
Fitness over generations: Tracks how organisms improve their survival capabilities.
Neural architecture evolution: Shows how neural structures change over time.
Animated Conway’s GoL simulation: Provides a visual of evolving organisms.
All results are stored in the /results folder.

👥 Contributors
Hemant - Genetic Algorithm Implementation, Conway’s Game of Life
Angie - Neural Network Development, Visualization
📚 References
This project incorporates bio-inspired computing concepts from the COMP5400 module:

Evolutionary Computation – Genetic Algorithms, Co-evolution​Evolution-1​Evolution-2
Artificial Neural Networks – Hopfield & Hebbian Learning​Hebbian-Learning​COMP5400M 10 Hopfield
Swarm Intelligence – Self-organization and Emergent Behavior​swarm_intelligence_2​swarm_intelligence_1
Cellular Automata – Conway’s Game of Life​lec1-2025
For a deeper dive, check the docs/ folder.

📝 License
This project is licensed under MIT License. See the LICENSE file for details.
