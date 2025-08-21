import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
from scipy.interpolate import make_interp_spline

# Parameters
timesteps = 50
np.random.seed(0)

# Generate sample data
misinfo_data = np.random.rand(timesteps) * 0.4

# Normalise so that at each time point, total sum = 1
components = np.vstack([misinfo_data,
                        np.random.rand(timesteps) * 0.3,
                        np.random.rand(timesteps) * 0.2,
                        np.random.rand(timesteps) * 0.4])
sums = components.sum(axis=0)
sums[sums == 0] = 1
components_normalized = components / sums

# Assign normalized data
misinfo_data = components_normalized[0]
fact_check_data = components_normalized[1]
user_correction_data = components_normalized[2]
official_correction_data = components_normalized[3]

# Define phase boundaries
phase_boundaries = {
    'Preparation': (0, timesteps // 3),
    'Development': (timesteps // 3, 2 * timesteps // 3),
    'Escalation': (2 * timesteps // 3, timesteps)
}

# Create directory for frames
frames_dir = 'corrected_clipping'
os.makedirs(frames_dir, exist_ok=True)

def smooth_curve(x, y, num_points=200):
    """Create a smooth curve and clip to ensure values stay within [0, 1]."""
    if len(x) <= 3:
        y_clipped = np.clip(y, 0, 1)
        return x, y_clipped
    else:
        spline = make_interp_spline(x, y, k=3)
        x_new = np.linspace(x.min(), x.max(), num_points)
        y_new = spline(x_new)
        y_new_clipped = np.clip(y_new, 0, 1)
        return x_new, y_new_clipped

def plot_layers(end_idx, phase_name, save_path):
    plt.figure(figsize=(12,6))
    t = np.arange(end_idx)

    # Data slices
    misinfo_slice = misinfo_data[:end_idx]
    fact_slice = fact_check_data[:end_idx]
    user_slice = user_correction_data[:end_idx]
    official_slice = official_correction_data[:end_idx]

    # Plot layers in reverse order for stacking
    y_official = np.cumsum([misinfo_slice, fact_slice, user_slice, official_slice], axis=0)[-1]
    x_official, y_official_smooth = smooth_curve(t, y_official)
    plt.fill_between(x_official, y_official_smooth, label='Official correction', color='#5293BB', alpha=0.8)

    y_user = np.cumsum([misinfo_slice, fact_slice, user_slice], axis=0)[-1]
    x_user, y_user_smooth = smooth_curve(t, y_user)
    plt.fill_between(x_user, y_user_smooth, label='User correction', color='#3776A1', alpha=0.8)

    y_fact = np.cumsum([misinfo_slice, fact_slice], axis=0)[-1]
    x_fact, y_fact_smooth = smooth_curve(t, y_fact)
    plt.fill_between(x_fact, y_fact_smooth, label='Fact-check', color='#1B5886', alpha=0.8)

    # Misinformation (top)
    x_mis, y_mis = smooth_curve(t, misinfo_slice)
    plt.fill_between(x_mis, y_mis, label='Misinformation', color='#003A6B', alpha=0.8)

    plt.xlabel('Time Step')
    plt.ylabel('Proportion')
    plt.title(f'{phase_name} Phase: Smoothed Layers up to Time {end_idx-1}')
    plt.legend(loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

# Generate frames for each phase step
cumulative_indices = []
for pname, (start, end) in phase_boundaries.items():
    cumulative_indices.extend(range(start, end))
cumulative_indices = sorted(set(cumulative_indices))

frames = []
for idx, current_idx in enumerate(cumulative_indices, 1):
    phase_name = ''
    for pname, (s, e) in phase_boundaries.items():
        if s <= current_idx < e:
            phase_name = pname
            break
    filename = os.path.join(frames_dir, f'frame_{idx:03d}.png')
    plot_layers(current_idx + 1, phase_name, filename)
    frames.append(filename)

print(f"Frames saved in '{frames_dir}/'.")

# Create GIF
gif_path = 'corrected_clipping.gif'
cmd = [
    'convert',  # Ensure ImageMagick is installed
    '-delay', '100',
    '-loop', '0'
]
for filename in frames:
    cmd.append(filename)
cmd.append(gif_path)

print("Creating GIF...")
try:
    subprocess.run(cmd, check=True)
    print(f"GIF created successfully: {gif_path}")
except subprocess.CalledProcessError:
    print("Error: Ensure ImageMagick is installed and 'convert' command is available.")