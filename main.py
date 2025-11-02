import matplotlib.pyplot as plt
from pygbm.gbm_simulator import GBMSimulator

if __name__ == "__main__":
    y0 = 1.0
    mu = 0.05
    sigma = 0.2
    T = 1.0
    N = 200

    simulator = GBMSimulator(y0, mu, sigma)
    t, y = simulator.simulate_path(T, N)

    plt.plot(t, y, label="GBM Path")
    plt.xlabel("Time")
    plt.ylabel("Y(t)")
    plt.title("Simulated Geometric Brownian Motion Path")
    plt.legend()
    plt.show()
    