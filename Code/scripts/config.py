import os

# Base directory
base_dir = "datasets"
print(os.getcwd())

# All data paths and constants using os.path.join
data_path = os.path.join(base_dir, "random_cube.npy")
baseline_path = os.path.join(base_dir, "baseline.txt")
envi_header_path = os.path.join(base_dir, "brc961-br1001.hdr")



output_pca_path = os.path.join(base_dir, "pca_cube.npy")
final_output_path = os.path.join(base_dir)

# Printing to verify
print(data_path)
print(baseline_path)
print(envi_header_path)
print(output_pca_path)
print(final_output_path)
