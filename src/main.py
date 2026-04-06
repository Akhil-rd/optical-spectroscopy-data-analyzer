from load_data import load_spectrum
from plot_spectrum import plot_spectrum
from detect_peaks import detect_peaks

def main():
    file_path = "../data/sample_spectrum.csv"

    data = load_spectrum(file_path)
    plot_spectrum(data, output_path="../results/spectrum_plot.png")

    peak_data = detect_peaks(data, height_threshold=50)
    peak_data.to_csv("../results/detected_peaks.csv", index=False)

    print("Detected peaks:")
    print(peak_data)

if __name__ == "__main__":
    main()