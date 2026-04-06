import matplotlib.pyplot as plt
import pandas as pd


def plot_spectrum(data: pd.DataFrame, peaks: pd.DataFrame, output_path: str) -> None:
   
    plt.figure(figsize=(15, 8))
    plt.plot(data["wavelength"], data["intensity"], color="blue")
    plt.scatter(peaks["wavelength"], peaks["intensity"], marker="*", s=80, label="Highest Peaks", color="red")
    for i in range(len(peaks)):
        plt.annotate(f"{peaks.iloc[i]['wavelength']} nm",
                     (peaks.iloc[i]['wavelength'], peaks.iloc[i]['intensity']),
                     textcoords="offset points",
                     xytext=(0,10),
                     ha='center')
    plt.title("Optical Spectrum")
    plt.xlabel("Wavelength(nm)")
    plt.ylabel("Intensity a.u.)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=250)
    plt.close()
    