import numpy as np
from scipy.integrate import odeint
from lib.disease import SIRDisease
from lib.model import SIRModel
from lib.population import SIRPopulationState, build_sir_population
import pandas as pd
import plotly.graph_objects as go
from dash import dcc

class Scenario:
    def __init__(self, initial_conditions: SIRPopulationState, disease: SIRDisease):
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
    disease = SIRDisease(transmission_rate=0.1, recovery_rate=0.1)

    scenario = Scenario(initial_conditions=initial_conditions,
                        disease=disease
                        )

    population_evolution = [item.array() for item in scenario.compute_evolution(n_days)]

    df = pd.DataFrame(population_evolution, columns=["S", "I", "R"])
    df["Giorno"] = range(n_days+1)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Giorno'], y=df['S'], mode='lines', name='Suscettibili', line=dict(color='royalblue', width=3)))
    fig.add_trace(go.Scatter(x=df['Giorno'], y=df['I'], mode='lines', name='Infetti', line=dict(color='red', width=3)))
    fig.add_trace(go.Scatter(x=df['Giorno'], y=df['R'], mode='lines', name='Rimossi', line=dict(color='green', width=3)))

    fig.update_layout(overwrite=True,
                      plot_bgcolor="#f8f9fa",
                      margin={"b": 0, "l": 20, "r": 20, "t": 0},
                      title={'y': 0.98, 'x': 0.08, 'xanchor': 'left', 'yanchor': 'top'},
                      height=350,
                      yaxis_title='Popolazione', font={"size": 18},
                      legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

    return dcc.Graph(figure=fig)
