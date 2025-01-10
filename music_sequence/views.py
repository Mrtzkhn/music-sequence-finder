from django.shortcuts import render, redirect
import numpy as np

from utils.genetic_algorithm import GeneticAlgorithm
from utils.midi_util import save_to_midi
from .models import MidiFile


def index(request):
    if request.method == 'POST':

        MidiFile.objects.all().delete()

        data = request.POST

        config = {
            "target_sequence": list(map(int, data.get('target_sequence').split(', '))),
            "population_size": int(data.get('population_size')),
            "generations": int(data.get('generations')),
            "mutation_rate": float(data.get('mutation_rate')),
        }

        ga = GeneticAlgorithm(config)

        for gen in range(ga.generations):
            # Calculate fitness
            fitness_scores = [GeneticAlgorithm.calculate_fitness(ind, ga.target) for ind in ga.population]
            # Select best individual
            best_idx = np.argmax(fitness_scores)
            best_sequence = ga.population[best_idx]

            midi_file = MidiFile(pk=gen, title=f'gen_{gen}', fitness=fitness_scores[best_idx],
                                 sequence=best_sequence, audio=f'melody/gen_{gen}.mid')
            midi_file.save()
            save_to_midi(ga.population[best_idx], f"media/melody/gen_{gen}.mid")
            print(f"Generation {gen} sequence: {best_sequence} with fitness = {fitness_scores[best_idx]}")

            # Create new population
            new_population = []
            while len(new_population) < ga.population_size:
                # Select parents
                parent1_idx, parent2_idx = ga.roulette_selection(fitness_scores)
                parent1, parent2 = ga.population[parent1_idx], ga.population[parent2_idx]
                # Crossover
                child1, child2 = ga.crossover(parent1, parent2)
                # Mutate
                ga.mutate(child1)
                ga.mutate(child2)
                new_population.extend([child1, child2])

            ga.population = new_population

        # Final result
        best_idx = np.argmax(fitness_scores)
        best_sequence = ga.population[best_idx]

        midi_file = MidiFile(pk=ga.generations, title=f'gen_best', fitness=fitness_scores[best_idx],
                             sequence=best_sequence, audio='melody/gen_best.mid')
        midi_file.save()
        save_to_midi(best_sequence, "media/melody/gen_best.mid")
        print(f"Best sequence: {best_sequence} with fitness = {fitness_scores[best_idx]}")

        # saving the original
        midi_file = MidiFile(pk=ga.generations+1, title=f'original', sequence=config["target_sequence"],
                             audio='melody/original.mid')
        midi_file.save()
        save_to_midi(config['target_sequence'], "media/melody/original.mid")
        print(f"original sequence: {config['target_sequence']}")

        return redirect('result')

    return render(request, 'index.html', {})


def result(request):
    midi_files = MidiFile.objects.all()
    return render(request, 'result.html', {'midi_files': midi_files})


