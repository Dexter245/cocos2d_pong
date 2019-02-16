"""
2-input XOR example -- this is most likely the simplest possible example.
"""

from __future__ import print_function

import sys

import neat

# 2-input XOR inputs and expected outputs.
import Main

xor_inputs = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
xor_outputs = [(0.0,), (1.0,), (1.0,), (0.0,)]

this = sys.modules[__name__]
this.gen: int = -1


def eval_genomes(genomes, config):
    i: int = 0
    best_genome = None
    best_net = None
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        if i == 0:
            this.gen += 1
            best_genome = genome
            best_net = net
            # genome.fitness = Main.get_score(net=net, fastmode=False, gen=this.gen)
            genome.fitness = Main.get_score(net=net, fastmode=True, gen=this.gen)
        else:
            genome.fitness = Main.get_score(net=net, fastmode=True, gen=this.gen)

        if genome.fitness > best_genome.fitness:
            best_genome = genome
            best_net = net

        print("fitness: " + str(genome.fitness))
        i += 1

    print("best fitness in gen " + str(this.gen) + ": " + str(best_genome.fitness))
    # net = neat.nn.FeedForwardNetwork.create(best, config)
    Main.get_score(net=best_net, fastmode=False, gen=this.gen)


# Load configuration.
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'neat_config1')

# Create the population, which is the top-level object for a NEAT run.
p = neat.Population(config)

# Add a stdout reporter to show progress in the terminal.
p.add_reporter(neat.StdOutReporter(False))

# Run until a solution is found.
winner = p.run(eval_genomes, 1000)

# Display the winning genome.
print("===================================================")
print('\nBest genome:\n{!s}'.format(winner))
# Show output of the most fit genome against training data.
print('\nOutput:')
winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
fitness = Main.get_score(net=winner_net, fastmode=False)
print("final fitness: " + str(fitness))
# for xi, xo in zip(xor_inputs, xor_outputs):
#     output = winner_net.activate(xi)
#     print("  input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))
