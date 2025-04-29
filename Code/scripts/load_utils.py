import numpy as np
from spectral.io import envi

def load_envi_header(header_path):
    return envi.read_envi_header(header_path)

def parse_envi_header(header_path):
    with open(header_path, 'r') as f:
        lines = f.readlines()

    header = {}
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            header[key.strip()] = value.strip()

    height = int(header['lines'])
    width = int(header['samples'])
    bands = int(header['bands'])
    return height, width, bands

def load_cube(path):
    return np.lib.format.open_memmap(path)

def load_baseline(path):
    return np.float32(np.loadtxt(path))
