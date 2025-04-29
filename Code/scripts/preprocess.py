from scipy.interpolate import interp1d
import numpy as np

def baseline_correction(cube: np.ndarray, wavelengths: np.ndarray, anchor_wavelengths: np.ndarray) -> np.ndarray:
    """
    Perform baseline correction on hyperspectral cube using baseline anchor wavelengths.

    Parameters:
        cube : ndarray
            Hyperspectral data cube (rows, cols, bands)
        wavelengths : ndarray
            1D array of all band wavelengths (size=bands)
        anchor_wavelengths : ndarray
            1D array of wavelengths used for baseline

    Returns:
        corrected_cube : ndarray
            Baseline corrected data cube
    """
    rows, cols, bands = cube.shape
    corrected_cube = np.zeros_like(cube)

    # Convert anchor wavelengths to nearest band indices
    anchor_indices = np.array([np.argmin(np.abs(wavelengths - wl)) for wl in anchor_wavelengths])

    band_indices = np.arange(bands)

    for i in range(rows):
        for j in range(cols):
            spectrum = cube[i, j, :]
            baseline_values = spectrum[anchor_indices]

            baseline_func = interp1d(anchor_indices, baseline_values, kind='linear', fill_value='extrapolate')
            baseline = baseline_func(band_indices)

            corrected_cube[i, j, :] = spectrum - baseline
    # Print progress every 100 rows (or whatever you like)
        if (i + 1) % 100 == 0 or i == rows - 1:
            print(f"Processed {i+1}/{rows} rows ({(i+1)/rows*100:.2f}%)")

    print("Baseline correction completed.")        

    return corrected_cube