# Fuzzy-Ad-Hoc-Network-Simulation
Real-Time Fuzzy Ad Hoc Network Simulation
The provided code integrates Python's Pygame library for real-time visualization and scikit-fuzzy for fuzzy logic control, creating an ad hoc network simulation. Pygame initializes a 600x600 window where nodes, represented as circles, can move randomly within bounds, visually indicating their connectivity through lines to neighbors. Each node's behavior, including movements and communications (broadcasts, receptions, and decisions), is determined through fuzzy logic controllers. These controllers use fuzzy sets and rules defined on inputs like 'signal_strength' and 'traffic_load' to produce decisions influencing the nodes' actions in the network. The network class manages these nodes, updating their states and redrawing them at a rate controlled by a 60 Hz clock. The simulation logs movements, message broadcasts, and fuzzy decisions to the console, providing insights into the dynamic interactions within the network, all aimed at demonstrating potential real-world applications in dynamic and decentralized network environments.
![Fuzzy Ad Hoc](https://github.com/user-attachments/assets/587d0ed1-20e9-472b-b2df-936cec44a285)
Key Functions of the Ad Hoc Network Simulation:
Node Initialization: Each node is initialized with a unique ID, position, neighbors, and routing information.
Movement: Nodes move randomly within the window boundaries, simulating mobility in an ad hoc network.
Drawing: Nodes are drawn as circles, and connections to their neighbors are shown as lines.
Neighbor Update: Nodes periodically update their list of neighbors based on proximity.
Message Broadcasting: Nodes can broadcast messages to their neighbors, simulating ad hoc network communication.
Message Reception: Nodes can receive messages, with their actions influenced by fuzzy logic decisions.
Fuzzy Logic Decision Making: Uses fuzzy logic to make decisions based on signal strength and traffic load.
Real-Time Visualization: Pygame updates the display in real-time to reflect node movements and interactions.
Console Logging: Logs all significant node activities, including movements, broadcasts, receptions, and fuzzy logic decisions to the console for real-time monitoring.
Network Management: The network class manages the overall state, updating and redrawing nodes at a controlled frame rate.
