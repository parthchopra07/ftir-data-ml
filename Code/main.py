from scripts import config, load_utils, preprocess, pca_utils, convert, normalize
import numpy as np

# Load and prepare
header = load_utils.load_envi_header(config.envi_header_path)
wl = np.array(header.get("wavelength", []), dtype=np.float32)
cube = load_utils.load_cube(config.data_path)
baseline = load_utils.load_baseline(config.baseline_path)

#Print details
print("Shape of your cube", cube.shape)
print("List of wavelengths in your cube",wl)
print("Baseline anchor cubes in your cube", baseline)

# Baseline Correction
bl_corrected = preprocess.baseline_correction(cube, wl, baseline)

# Normalise
normalized_cube= normalize.normalize_hyperspectral_cube(bl_corrected,wl,baseline)

# PCA
pca_cube= pca_utils.incremental_pca_npy(normalized_cube,config.output_pca_path) #Default set to 16 components

# Convert to HDF5
convert.convert_npy_to_h5(config.final_output_path, "output.h5")

