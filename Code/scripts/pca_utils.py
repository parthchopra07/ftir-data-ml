from sklearn.decomposition import PCA, IncrementalPCA
from sklearn.impute import SimpleImputer
import numpy as np

def incremental_pca_npy(npy_file, output_file, n_components=16, batch_size=5000):
    """
    Applies Incremental PCA on a hyperspectral cube stored as a .npy file while handling NaN values.

    Parameters:
    - npy_file (array): P .npy file containing hyperspectral data (H, W, Bands).
    - output_file (str): Path to save the transformed .npy file.
    - n_components (int): Number of principal components to retain.
    - batch_size (int): Number of pixels processed per batch.

    Saves the PCA-transformed hyperspectral cube as a new .npy file.
    """
    
    # Load hyperspectral cube
    hyperspectral_cube = npy_file
    
    # Get dimensions (H, W, Bands)
    H, W, B = hyperspectral_cube.shape
    print(f"Loaded hyperspectral cube of shape: {H}x{W}x{B}")

    # Reshape to (H*W, Bands)
    data_reshaped = hyperspectral_cube.reshape(-1, B)

    # Handle NaN values using mean imputation
    imputer = SimpleImputer(strategy="mean")
    data_reshaped = imputer.fit_transform(data_reshaped)

    # Define Incremental PCA
    ipca = IncrementalPCA(n_components=n_components)
   # print(ipca.componnets_)
    # Fit PCA in batches
    num_batches = len(data_reshaped) // batch_size + 1
    for i in range(num_batches):
        batch_start = i * batch_size
        batch_end = min((i + 1) * batch_size, len(data_reshaped))
        
        if batch_start < batch_end:  # Avoid empty batches
            batch = data_reshaped[batch_start:batch_end]
            ipca.partial_fit(batch)
            print(f"Epoch {i+1}/{num_batches} completed.")

    # Transform the entire dataset
    transformed_data = ipca.transform(data_reshaped)

    # Reshape back to (H, W, n_components)
    transformed_cube = transformed_data.reshape(H, W, n_components)

    # Save the PCA-transformed hyperspectral cube
    np.save(output_file, transformed_cube)
    print(f"PCA transformation completed and saved to {output_file}.")