import numpy as np
import h5py

def convert_npy_to_h5(npy_file, h5_file, dataset_name="ftir_dataset"):
    data = np.load(npy_file)
    with h5py.File(h5_file, "w") as f:
        f.create_dataset(dataset_name, data=data)
