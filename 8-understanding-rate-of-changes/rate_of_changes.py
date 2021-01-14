import numpy as np


def volume(t):
    return (t - 4) ** 3 / 64 + 3.3


def flow_rate(t):
    return 3 * (t - 4) ** 2 / 64


def average_flow_rate(v, t1, t2):
    return (v(t2) - v(t1)) / (t2 - t1)


def interval_flow_rates(v, t1, t2, dt):
    return [(t, average_flow_rate(v, t, t + dt)) for t in np.arange(t1, t2, dt)]
