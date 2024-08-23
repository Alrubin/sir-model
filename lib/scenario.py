from typing import Union

import numpy as np
from scipy.integrate import odeint

from config import GraphLayoutSettings
from components.main_graph import ScatterLine, MainGraph
from lib.disease import SIRDisease
from lib.model import SIRModel
from lib.population import SIRPopulationState, build_sir_population
import pandas as pd


class Scenario:
    def __init__(self, initial_conditions: SIRPopulationState, disease: Union[None, SIRDisease] = None):
        self.initial_conditions = initial_conditions
        self.disease = disease

    def compute_evolution(self, n_days):
        population_evolution = [self.initial_conditions]
        if n_days != 0:
            time_grid = np.linspace(start=0, stop=n_days, num=n_days)
            model = SIRModel(disease=self.disease)
            population_evolution += [build_sir_population(*population) for population in
                                     odeint(model, self.initial_conditions.array(), time_grid)]

        return population_evolution


def update_scenario(S0, I0, R0, n_days):
    initial_conditions = build_sir_population(susceptibles=S0, infected=I0, removed=R0)

    scenario = Scenario(initial_conditions=initial_conditions,
                        disease=None
                        )

    population_evolution = [item.array() for item in scenario.compute_evolution(n_days)]

    df = pd.DataFrame(population_evolution, columns=["S", "I", "R"])
    df["Giorno"] = range(n_days + 1)

    graph = MainGraph([
        ScatterLine(df['Giorno'], df['S'], 'Suscettibili', 'royalblue'),
        ScatterLine(df['Giorno'], df['I'], 'Infetti', 'red'),
        ScatterLine(df['Giorno'], df['R'], 'Rimossi', 'green')
    ],
        GraphLayoutSettings()
    ).build()

    return graph
