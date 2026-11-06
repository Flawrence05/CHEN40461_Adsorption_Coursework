# libraries
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd

# Plt Consistency
plt.rcParams["figure.figsize"] = (8, 5)
plt.rcParams["font.size"] = 11
plt.rcParams["axes.grid"] = True

data = {
    "Romulus_N2": pd.read_csv("Data/Romulus_n2.csv"),
    "Romulus_O2": pd.read_csv("Data/Romulus_o2.csv"),
    "Remus_N2": pd.read_csv("Data/Remus_n2.csv"),
    "Remus_O2": pd.read_csv("Data/Remus_o2.csv")
}

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

plots = [
    ("Romulus_N2", axes[0, 0], "Romulus - Nitrogen"),
    ("Romulus_O2", axes[0, 1], "Romulus - Oxygen"),
    ("Remus_N2", axes[1, 0], "Remus - Nitrogen"),
    ("Remus_O2", axes[1, 1], "Remus - Oxygen")
]

for name, ax, title in plots:

    df = data[name]

    ax.scatter(
        df["P [Pa]"],
        df["q [mol kg-1]"],
        label="Experimental data"
    )

    ax.set_title(title)
    ax.set_xlabel("Pressure")
    ax.set_ylabel("Adsorption loading")
    ax.legend()

plt.tight_layout()
# plt.savefig("../results/figures/individual_isotherms.png", dpi=300)
plt.show()