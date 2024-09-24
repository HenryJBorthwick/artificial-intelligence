import numpy as np


def gradient_optimize(x0, gradient, step_factor, direction, iterations):
    # get initial point
    x = x0

    # begin iterations
    for _ in range(iterations):
        # compute gradient at current point using gradient function
        grad = gradient(x)

        # update point
        x = x + direction * step_factor * grad

    return x


# tests
def f(x):
    return x ** 2


def f_prime(x):
    return 2 * x


x0 = 2
x_star = gradient_optimize(x0, f_prime, 0.1, -1, 250)
print(f"x* = {x_star:.2f}, f(x*) = {f(x_star):.2f}")

print("\n")


def f(x):
    return 1 - x ** 2


def f_prime(x):
    return -2 * x


x0 = 2
x_star = gradient_optimize(x0, f_prime, 0.1, 1, 250)
print(f"x* = {x_star:.2f}, f(x*) = {f(x_star):.2f}")

print("\n")


# single maximum at x* = [1, -1] with f(x*) = 2
def f(x):
    return 2 - (1 - x[0]) ** 2 - (x[1] + 1) ** 2


def gradient_of_f(x):
    return np.array([2 * (1 - x[0]), -2 * (x[1] + 1)])


x_star = gradient_optimize(np.zeros(2), gradient_of_f, 0.1, 1, 250)

print(np.all(np.isclose(x_star, np.array([1, -1]))), np.isclose(f(x_star), 2))

print("\n")


def f(x):  # This function has two minimums
    return x ** 4 - x ** 3 - x ** 2 + 1


def f_prime(x):
    return 4 * x ** 3 - 3 * x ** 2 - 2 * x


x0 = -1  # if x < 0 we get stuck in a local minimum
x_star1 = gradient_optimize(-1, f_prime, 0.1, -1, 250)

x0 = 1  # if x > 0 we should converge to the global minimum
x_star2 = gradient_optimize(1, f_prime, 0.1, -1, 250)

print(f"x0 = -1, x* = {x_star1:.4f}, f(x*) = {f(x_star1):.4f}")
print(f"x0 = 1, x* = {x_star2:.4f}, f(x*) = {f(x_star2):.4f}")
