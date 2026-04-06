# Optical Spectroscopy Data Analyzer

This project is a Python-based tool for analyzing optical spectroscopy data. It loads spectral data from CSV files, plots the spectrum, detects intensity peaks, and exports peak information for further analysis.

## Features
- Load spectroscopy data from CSV
- Plot intensity vs wavelength
- Detect peaks automatically
- Save plots and detected peaks

## Tools Used
- Python
- Pandas
- Matplotlib
- SciPy

## Project Structure
## Example Input
CSV file with columns:
- wavelength
- intensity

## Output
- Spectrum plot image
- CSV file containing detected peaks

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Go to the src folder:
   cd src

3. Run:
   python main.py

## Future Improvements
- Gaussian peak fitting
- Noise filtering
- Automatic report generation
- Support for multiple spectra