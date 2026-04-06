import pandas as pd
from scipy.signal import find_peaks


def detect_peaks(data: pd.DataFrame, min_height=None, min_distance: int = 5) -> pd.DataFrame:

    intensity = data["intensity"].values
    peak_indices, properties = find_peaks(intensity, height=min_height, distance=min_distance)

    peaks_df = pd.DataFrame({
        "wavelength": data.iloc[peak_indices]["wavelength"].values,
        "intensity": data.iloc[peak_indices]["intensity"].values
    })

    return peaks_df