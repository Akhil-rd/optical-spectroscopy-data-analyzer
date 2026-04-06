from pathlib import Path

from load_data import load_spectrum
from detect_peaks import detect_peaks
from plot_spectrum import plot_spectrum


def main():
    project_root = Path(__file__).resolve().parent.parent

    input_file = project_root / "data" / "sample_spectrum.csv"
    output_plot = project_root / "results" / "spectrum_plot.png"
    output_peaks = project_root / "results" / "detected_peaks.csv"

    data = load_spectrum(str(input_file))

    # Adjust min_height if you want stricter or looser peak detection
    peaks = detect_peaks(data, min_height=10000, min_distance=2)

    peaks.to_csv(output_peaks, index=False)
    plot_spectrum(data, peaks, str(output_plot))

    print("Analysis completed successfully.")
    print(f"Loaded {len(data)} data points.")
    print(f"Detected {len(peaks)} peaks.")
    print(f"Plot saved to: {output_plot}")
    print(f"Peaks saved to: {output_peaks}")
    print("Peak wavelengths:")
    print(peaks)

if __name__ == "__main__":
    main()