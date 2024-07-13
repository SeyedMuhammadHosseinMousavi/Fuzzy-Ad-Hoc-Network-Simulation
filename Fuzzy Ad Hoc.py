import pygame
import random
import sys
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Ad Hoc Network Simulation with Fuzzy Logic")

# Fuzzy Logic Setup
signal_strength = ctrl.Antecedent(np.arange(0, 101, 1), 'signal_strength')
traffic_load = ctrl.Antecedent(np.arange(0, 101, 1), 'traffic_load')
decision = ctrl.Consequent(np.arange(0, 101, 1), 'decision')

signal_strength.automf(3)
traffic_load.automf(3)

decision['low'] = fuzz.trimf(decision.universe, [0, 0, 50])
decision['medium'] = fuzz.trimf(decision.universe, [25, 75, 100])
decision['high'] = fuzz.trimf(decision.universe, [50, 100, 100])

rule1 = ctrl.Rule(signal_strength['poor'] | traffic_load['good'], decision['low'])
rule2 = ctrl.Rule(signal_strength['average'] & traffic_load['average'], decision['medium'])
rule3 = ctrl.Rule(signal_strength['good'] & traffic_load['poor'], decision['high'])

routing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
routing = ctrl.ControlSystemSimulation(routing_ctrl)

class Node:
    def __init__(self, id, position):
        self.id = id
        self.position = np.array(position, dtype='float64')
        self.neighbors = []
        self.route_table = {}
        self.message_queue = []

    def move(self):
        old_position = self.position.copy()
        self.position += np.random.randint(-20, 21, size=2)
        self.position = np.clip(self.position, 0, 600)   
        print(f"Node {self.id} moved from {old_position} to {self.position}")

    def draw(self):
        pygame.draw.circle(screen, (0, 120, 255), self.position.astype(int), 10)
        for neighbor in self.neighbors:
            pygame.draw.line(screen, (255, 0, 0), self.position.astype(int), neighbor.position.astype(int), 1)

    def update_neighbors(self, nodes):
        old_neighbors = set(self.neighbors)
        self.neighbors = [node for node in nodes if node != self and np.linalg.norm(self.position - node.position) < 100]
        new_neighbors = set(self.neighbors)
        if old_neighbors != new_neighbors:
            print(f"Node {self.id} updated its neighbors")

    def broadcast(self, message, source):
        for neighbor in self.neighbors:
            if neighbor != source:
                neighbor.receive(message, self)
        print(f"Node {self.id} broadcasted message {message['type']}")

    def receive(self, message, sender):
        routing.input['signal_strength'] = np.random.randint(0, 101)
        routing.input['traffic_load'] = np.random.randint(0, 101)
        routing.compute()
        decision_value = routing.output['decision']
        print(f"Node {self.id} received message {message['type']} from Node {sender.id} with decision value: {decision_value}")

    def send(self, message, recipient):
        recipient.receive(message, self)
        print(f"Node {self.id} sends message {message['type']} to Node {message['destination']}")

class Network:
    def __init__(self, num_nodes):
        self.nodes = [Node(i, (random.randint(0, 600), random.randint(0, 600))) for i in range(num_nodes)]

    def update(self):
        for node in self.nodes:
            node.move()
            node.update_neighbors(self.nodes)

    def draw(self):
        for node in self.nodes:
            node.draw()

def main():
    clock = pygame.time.Clock()
    network = Network(10)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))  # Clear the screen
        network.update()  # Update the state of the network
        network.draw()  # Draw the network
        pygame.display.flip()  # Refresh the screen
        clock.tick(60)  # Limit the frame rate to 60 frames per second
        print("Tick")

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
