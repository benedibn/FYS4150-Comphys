import numpy as np
import matplotlib.pyplot as plt
import sys
import os

plot_filename = sys.argv[1]
infile_filename = sys.argv[2]

if infile_filename == "twoelectrons":
    with open("twoelectrons_omega_0.txt", "r") as infile:
        infile.readline()
        infile.readline()
        infile.readline()
        u_omega0 = infile.readline()
        u_omega0 = u_omega0.split()
    with open("twoelectrons_omega_1.txt", "r") as infile:
        infile.readline()
        infile.readline()
        infile.readline()
        u_omega1 = infile.readline()
        u_omega1 = u_omega1.split()
    with open("twoelectrons_omega_2.txt", "r") as infile:
        infile.readline()
        infile.readline()
        infile.readline()
        u_omega2 = infile.readline()
        u_omega2 = u_omega2.split()
    with open("twoelectrons_omega_3.txt", "r") as infile:
        infile.readline()
        infile.readline()
        infile.readline()
        u_omega3 = infile.readline()
        u_omega3 = u_omega3.split()
    n = len(u_omega0)
    for i in range(n):
        u_omega0[i] = float(u_omega0[i])
        u_omega1[i] = float(u_omega1[i])
        u_omega2[i] = float(u_omega2[i])
        u_omega3[i] = float(u_omega3[i])
    rho = np.linspace(0,5,n)
    plt.plot(rho, u_omega0, rho, u_omega1, rho, u_omega2, rho, u_omega3)
    plt.legend([r"$\omega = 0.01$", r"$\omega = 0.5$", r"$\omega = 1$", r"$\omega = 5$"])
    plt.xlabel(r"$\rho$")
    plt.ylabel(r"$u(\rho)$")
    plt.title("two electrons problem for N = " + str(n))
    plt.savefig(plot_filename)
    plt.show()
else:
    with open(infile_filename, "r") as infile:
        k = int(infile.readline())
        arma_lambda = infile.readline()
        arma_lambda = arma_lambda.split()
        jacobi_lambda = infile.readline()
        jacobi_lambda = jacobi_lambda.split()
        min_eigvec_jacobi = infile.readline()
        min_eigvec_jacobi = min_eigvec_jacobi.split()
    n = len(arma_lambda)
    for i in range (n):
        arma_lambda[i] = float(arma_lambda[i])
        jacobi_lambda[i] = float(jacobi_lambda[i])
        min_eigvec_jacobi[i] = float(min_eigvec_jacobi[i])

    min_eigvec_jacobi = [0] + min_eigvec_jacobi + [0]
    N = len(min_eigvec_jacobi)

    rho = np.linspace(0,1,N)
    h = (rho[-1] - rho[0])/(N-1)
    """
    def analytical_eigenvalues(N):
        anal_lambda = np.zeros(N)
        for j in range(1,N):
            d = 2/h**2
            a = -1/h**2
            anal_lambda[j-1] = d + 2*a*np.cos(j*np.pi/(N-1))
        return anal_lambda
    """
    def analytical_eigenvectors(N):
        u = np.zeros(N)
        for k in range(0,N):
            u[k] = np.sin(k*np.pi/(N-1))
        u = u/np.linalg.norm(u)
        return u

    title = infile_filename.strip(".txt")
    plt.plot(rho, min_eigvec_jacobi, label = 'Numerical solution')
    if title == "bucklingbeam":
        plt.plot(rho,analytical_eigenvectors(N), ":" ,label = 'Analytical solution')
    plt.legend()
    plt.title(title)
    plt.xlabel('rho')
    plt.ylabel('u(rho)')
    plt.savefig(plot_filename)
    plt.show()
