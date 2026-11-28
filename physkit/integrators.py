"""Numerical integration solvers for classical mechanics."""

import numpy as np


def simulate_vertical_fall(
    height: float = 56.0,
    mass: float = 1.5,
    area: float = 0.008,
    cd: float = 0.8,
    rho: float = 1.225,
    g: float = 9.81,
    dt: float = 0.01,
    t_max: float = 24.0,
) -> dict:
    """
    Simulate 1D vertical free fall with quadratic air drag using Euler-Cromer.

    Parameters
    ----------
    height : float
        Initial drop height above ground (m).
    mass : float
        Object mass (kg).
    area : float
        Cross-sectional area facing airflow (m^2).
    cd : float
        Dimensionless drag coefficient (0.0 for vacuum).
    rho : float
        Fluid density (kg/m^3). Standard sea-level air is 1.225 kg/m^3.
    g : float
        Gravitational acceleration (m/s^2).
    dt : float
        Simulation time step (s).
    t_max : float
        Total simulation duration (s).

    Returns
    -------
    dict
        Time-series arrays for t, y (height), d (distance fallen),
        v (downward speed), a (downward acceleration), plus impact metrics.
    """
    n_steps = int(np.ceil(t_max / dt)) + 1
    t = np.linspace(0.0, (n_steps - 1) * dt, n_steps)
    y = np.zeros(n_steps)
    d = np.zeros(n_steps)
    v = np.zeros(n_steps)
    a = np.zeros(n_steps)

    y[0] = height
    drag_factor = 0.5 * rho * cd * area / mass
    a[0] = g

    t_impact = None
    v_impact = 0.0

    for i in range(n_steps - 1):
        if y[i] <= 0.0:
            # Object has already reached the ground
            y[i + 1] = 0.0
            d[i + 1] = height
            v[i + 1] = 0.0
            a[i + 1] = 0.0
            continue

        # 1. Compute net downward acceleration from Newton's 2nd Law
        a_curr = g - drag_factor * (v[i] ** 2)
        a[i] = a_curr

        # 2. Euler-Cromer update: update velocity first, then position
        v_next = v[i] + a_curr * dt
        y_next = y[i] - v_next * dt

        if y_next <= 0.0:
            y[i + 1] = 0.0
            d[i + 1] = height
            v[i + 1] = 0.0
            a[i + 1] = 0.0
            if t_impact is None:
                t_impact = t[i + 1]
                v_impact = v_next
        else:
            y[i + 1] = y_next
            d[i + 1] = height - y_next
            v[i + 1] = v_next

    return {
        "t": t,
        "y": y,
        "d": d,
        "v": v,
        "a": a,
        "t_impact": t_impact,
        "v_impact": v_impact,
    }