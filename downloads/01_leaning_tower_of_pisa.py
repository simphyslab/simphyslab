"""
In Silico Physics Lab — Experiment 01: The Leaning Tower of Pisa
Self-contained simulation of a falling hammer and feather in vacuum vs. air.

Requirements:
    pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Physical Constants & Object Properties (Edit these to experiment!)
TOWER_HEIGHT = 56.0      # m
GRAVITY = 9.81           # m/s^2 (Earth: 9.81, Moon: 1.62, Mars: 3.72)
AIR_DENSITY = 1.225      # kg/m^3

HAMMER = {"mass": 1.50, "area": 0.008, "cd": 0.80}
FEATHER = {"mass": 0.002, "area": 0.004, "cd": 1.20}

DT = 0.01                # Numerical time step (s)

# Automatically estimate enough simulation time for the feather to land
v_term_feather = np.sqrt(
    2.0 * FEATHER["mass"] * GRAVITY / (AIR_DENSITY * FEATHER["cd"] * FEATHER["area"])
)
T_MAX = float(
    np.ceil(np.sqrt(2.0 * TOWER_HEIGHT / GRAVITY) + (TOWER_HEIGHT / v_term_feather) + 1.5)
)


def simulate_fall(mass: float, area: float, cd: float, rho: float) -> dict:
    """Integrate Newton's 2nd Law (F_net = m*g - F_drag) via Euler-Cromer."""
    steps = int(np.ceil(T_MAX / DT)) + 1
    t = np.linspace(0.0, (steps - 1) * DT, steps)
    y = np.zeros(steps)
    v = np.zeros(steps)
    a = np.zeros(steps)

    y[0] = TOWER_HEIGHT
    a[0] = GRAVITY
    drag_k = 0.5 * rho * cd * area / mass

    for i in range(steps - 1):
        if y[i] <= 0.0:
            y[i + 1], v[i + 1], a[i + 1] = 0.0, 0.0, 0.0
            continue

        a_curr = GRAVITY - drag_k * (v[i] ** 2)
        a[i] = a_curr
        v_next = v[i] + a_curr * DT
        y_next = y[i] - v_next * DT

        if y_next <= 0.0:
            y[i + 1], v[i + 1], a[i + 1] = 0.0, 0.0, 0.0
        else:
            y[i + 1] = y_next
            v[i + 1] = v_next

    return {"t": t, "y": y, "d": TOWER_HEIGHT - y, "v": v, "a": a}


if __name__ == "__main__":
    ham_vac = simulate_fall(HAMMER["mass"], HAMMER["area"], 0.0, 0.0)
    fea_vac = simulate_fall(FEATHER["mass"], FEATHER["area"], 0.0, 0.0)
    ham_air = simulate_fall(HAMMER["mass"], HAMMER["area"], HAMMER["cd"], AIR_DENSITY)
    fea_air = simulate_fall(FEATHER["mass"], FEATHER["area"], FEATHER["cd"], AIR_DENSITY)

    fig, (ax_drop, ax_vel) = plt.subplots(1, 2, figsize=(10, 5))
    ax_drop.set_xlim(0, 4)
    ax_drop.set_ylim(0, TOWER_HEIGHT * 1.1)
    ax_drop.axvline(2.0, color="gray", linestyle="--")
    ax_drop.set_xticks([1.0, 3.0])
    ax_drop.set_xticklabels(["Vacuum", "Atmosphere"])
    ax_drop.set_ylabel("Altitude (m)")
    ax_drop.set_title(f"Leaning Tower of Pisa Drop ({TOWER_HEIGHT:.0f} m)")

    p_hv, = ax_drop.plot([0.7], [TOWER_HEIGHT], "s", markersize=11, color="#0B1F3A", label="Hammer")
    p_fv, = ax_drop.plot([1.3], [TOWER_HEIGHT], "^", markersize=11, color="#1C939A", label="Feather (Vacuum)")
    p_ha, = ax_drop.plot([2.7], [TOWER_HEIGHT], "s", markersize=11, color="#0B1F3A")
    p_fa, = ax_drop.plot([3.3], [TOWER_HEIGHT], "^", markersize=11, color="#D97706", label="Feather (Air)")
    ax_drop.legend(loc="lower center")

    t = ham_vac["t"]
    ax_vel.set_xlim(0, T_MAX)
    ax_vel.set_ylim(0, np.max(ham_vac["v"]) * 1.15)
    ax_vel.set_xlabel("Time (s)")
    ax_vel.set_ylabel("Downward Speed (m/s)")
    ax_vel.set_title("Velocity vs. Time")
    ax_vel.grid(True, linestyle="--", alpha=0.5)

    l_vac, = ax_vel.plot([], [], "--", color="#0B1F3A", label="Vacuum (Both)")
    l_ha, = ax_vel.plot([], [], "-", color="#0B1F3A", label="Hammer (Air)")
    l_fa, = ax_vel.plot([], [], "-", color="#D97706", label="Feather (Air)")
    ax_vel.legend()

    fig.tight_layout()
    frames = np.linspace(0, len(t) - 1, 90, dtype=int)

    def animate(idx):
        p_hv.set_data([0.7], [ham_vac["y"][idx]])
        p_fv.set_data([1.3], [fea_vac["y"][idx]])
        p_ha.set_data([2.7], [ham_air["y"][idx]])
        p_fa.set_data([3.3], [fea_air["y"][idx]])
        l_vac.set_data(t[: idx + 1], ham_vac["v"][: idx + 1])
        l_ha.set_data(t[: idx + 1], ham_air["v"][: idx + 1])
        l_fa.set_data(t[: idx + 1], fea_air["v"][: idx + 1])
        return p_hv, p_fv, p_ha, p_fa, l_vac, l_ha, l_fa

    ani = FuncAnimation(fig, animate, frames=frames, interval=50, blit=False)
    plt.show()