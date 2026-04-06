from scipy.signal import find_peaks
import pandas as pd

def detect_peaks(data, height_threshold=50):
    peaks, properties = find_peaks(data["intensity"], height=height_threshold)

    peak_data = pd.DataFrame({
        "wavelength": data["wavelength"].iloc[peaks].values,
        "intensity": data["intensity"].iloc[peaks].values
    })

    return peak_data