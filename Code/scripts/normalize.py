import numpy as np
def normalize_hyperspectral_cube(cube: np.ndarray, wavenumbers: np.ndarray, target_wavenumber: float = 1650.0) -> np.ndarray:
    """
    Normalizes a hyperspectral cube by the absorbance at a target wavenumber (default: 1650 cm-1 - Amide I band).
    
    Parameters:
        cube (np.ndarray): Hyperspectral cube of shape (rows, cols, bands)
        wavenumbers (np.ndarray): Array of wavenumbers of shape (bands,)
        target_wavenumber (float): The wavenumber to normalize by (default: 1650 cm-1)

    Returns:
        np.ndarray: Normalized hyperspectral cube of same shape as input
    """

    # Find index of the band closest to target wavenumber
    target_idx = np.argmin(np.abs(wavenumbers - target_wavenumber))
    print(f"[INFO] Normalizing by wavenumber ~{wavenumbers[target_idx]} cm-1 at index {target_idx}")

    # Extract absorbance at target wavenumber
    target_abs = cube[:, :, target_idx]

    # Avoid division by zero
    target_abs_safe = np.where(target_abs == 0, 1e-10, target_abs)

    # Normalize cube
    normalized_cube = cube / target_abs_safe[:, :, np.newaxis]

    return normalized_cube