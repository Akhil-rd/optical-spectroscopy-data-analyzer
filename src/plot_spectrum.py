import matplotlib.pyplot as plt

def plot_spectrum(data, output_path=None):
    plt.figure(figsize=(10, 6))
    plt.plot(data["wavelength"], data["intensity"])
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Intensity (a.u.)")
    plt.title("Optical Spectrum")
    plt.grid(True)

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches="tight")

    plt.show()