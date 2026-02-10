
import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = "figures"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

plt.style.use('dark_background')
dpi = 300

def generate_fnl_plot():
    ell = np.linspace(2, 200, 500)
    # Predicted fNL: -3.2 at low ell, decaying
    fnl_pred = -3.2 / (1 + (ell/60)**2)

    # Standard inflation: ~0
    fnl_inflation = np.zeros_like(ell)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(ell, fnl_inflation, 'w--', label=r'Standard Inflation ($f_{NL} \approx 0$)', alpha=0.5)
    ax.plot(ell, fnl_pred, 'r-', linewidth=2, label='Resolution Cosmology')

    # Error band at low ell
    ell_low = np.linspace(2, 30, 50)
    fnl_low = -3.2 * np.ones_like(ell_low)
    ax.fill_between(ell_low, fnl_low - 0.8, fnl_low + 0.8, color='red', alpha=0.2, label=r'Prediction: $-3.2 \pm 0.8$')

    ax.set_xlabel(r'Multipole $\ell$')
    ax.set_ylabel(r'$f_{NL}^{local}$')
    ax.set_title('Primordial Non-Gaussianity Prediction')
    ax.legend()
    ax.grid(True, alpha=0.2)
    ax.set_ylim(-5, 1)

    outfile = os.path.join(output_dir, "fig3_fNL.pdf")
    plt.savefig(outfile, bbox_inches='tight', dpi=dpi)
    print(f"Generated: {outfile}")
    plt.close()

if __name__ == "__main__":
    generate_fnl_plot()
