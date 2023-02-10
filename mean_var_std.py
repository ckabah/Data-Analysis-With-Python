import numpy as np


def calculate(input: list):
    if len(input) != 9:
        raise ValueError('List must contain nine numbers.')
    mx = np.array(input).reshape(3, 3)
    calculations = {}
    calculations["mean"] = [
        list(np.mean(mx, axis=0)),
        list(np.mean(mx, axis=1)),
        mx.mean()
    ]
    calculations["variance"] = [
        list(np.var(mx, axis=0)),
        list(np.var(mx, axis=1)),
        mx.var()
    ]
    calculations["standard deviation"] = [
        list(np.std(mx, axis=0)),
        list(np.std(mx, axis=1)),
        mx.std()
    ]
    calculations["max"] = [
        list(np.max(mx, axis=0)),
        list(np.max(mx, axis=1)),
        mx.max()
    ]
    calculations["min"] = [
        list(np.min(mx, axis=0)),
        list(np.min(mx, axis=1)),
        mx.min()
    ]
    calculations["sum"] = [
        list(np.sum(mx, axis=0)),
        list(np.sum(mx, axis=1)),
        mx.sum()
    ]
    return calculations