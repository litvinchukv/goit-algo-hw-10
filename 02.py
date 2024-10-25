import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Define the function to integrate
def f(x):
    return x ** 2


# Integration limits
a = 0  # Lower limit
b = 2  # Upper limit


# Monte Carlo method for integration
def monte_carlo_integrate(func, a, b, num_samples=10000):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = func(x_random)
    area_estimate = (b - a) * np.mean(y_random)
    return area_estimate


if __name__ == "__main__":
    # Monte Carlo integration
    monte_carlo_result = monte_carlo_integrate(f, a, b)

    # Analytical integration using scipy's quad
    quad_result, error = spi.quad(f, a, b)

    # Plot the function and shaded area
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    # Plot function curve
    ax.plot(x, y, 'r', linewidth=2)

    # Fill the area under the curve
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Graph settings
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

    # Output results
    print(monte_carlo_result)
    print(quad_result)
    print(error)