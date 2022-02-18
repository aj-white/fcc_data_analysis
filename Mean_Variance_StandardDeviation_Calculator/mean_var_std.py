import numpy as np


def create_array_3_by_3(numbers: list) -> np.ndarray:
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    return np.array(numbers).reshape(3, 3)


def calc_mean_by_axis(arr: np.array):
    row_mean = arr.mean(axis=0)
    col_mean = arr.mean(axis=1)
    flat_mean = arr.flatten().mean()

    return [
        row_mean.tolist(),
        col_mean.tolist(),
        flat_mean,
    ]


def calc_var_by_axis(arr: np.array):
    row_var = np.var(arr, axis=0)
    col_var = np.var(arr, axis=1)
    flat_var = np.var(arr.flatten())

    return [
        row_var.tolist(),
        col_var.tolist(),
        flat_var,
    ]


def calc_std_by_axis(arr: np.array):
    row_std = np.std(arr, axis=0)
    col_std = np.std(arr, axis=1)
    flat_std = np.std(arr.flatten())

    return [
        row_std.tolist(),
        col_std.tolist(),
        flat_std,
    ]


def calc_max_by_axis(arr: np.array):
    row_max = arr.max(axis=0)
    col_max = arr.max(axis=1)
    flat_max = arr.flatten().max()

    return [
        row_max.tolist(),
        col_max.tolist(),
        flat_max,
    ]


def calc_min_by_axis(arr: np.array):
    row_min = arr.min(axis=0)
    col_min = arr.min(axis=1)
    flat_min = arr.flatten().min()

    return [
        row_min.tolist(),
        col_min.tolist(),
        flat_min,
    ]


def calc_sum_by_axis(arr: np.array):
    row_sum = arr.sum(axis=0)
    col_sum = arr.sum(axis=1)
    flat_sum = arr.flatten().sum()

    return [
        row_sum.tolist(),
        col_sum.tolist(),
        flat_sum,
    ]


def calculate(numbers):
    reshaped_arr = create_array_3_by_3(numbers)
    arr_stats = {}
    arr_stats["mean"] = calc_mean_by_axis(reshaped_arr)
    arr_stats["variance"] = calc_var_by_axis(reshaped_arr)
    arr_stats["standard deviation"] = calc_std_by_axis(reshaped_arr)
    arr_stats["max"] = calc_max_by_axis(reshaped_arr)
    arr_stats["min"] = calc_min_by_axis(reshaped_arr)
    arr_stats["sum"] = calc_sum_by_axis(reshaped_arr)

    return arr_stats
