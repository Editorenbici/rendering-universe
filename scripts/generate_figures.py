
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import os

# Create figures directory
output_dir = r"c:\Users\Patricio\Downloads\universo render\Finales\Final_Paper\figures"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set style
plt.style.use('dark_background')
dpi = 300

# 1. THE PIXEL (Phase I)
def generate_pixel():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_facecolor('black')
    
    # Create a glowing pixel effect
    x = np.linspace(-2, 2, 500)
    y = np.linspace(-2, 2, 500)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    
    # Intensity function (Gaussian glow)
    Z = np.exp(-10 * (X**2 + Y**2))     # Central pixel
    Z += 0.2 * np.exp(-2 * R)           # Outer glow
    
    # Custom blue-white colormap
    colors = [(0, 0, 0), (0, 0, 0.5), (0, 0.5, 1), (1, 1, 1)]
    cmap = LinearSegmentedColormap.from_list('cosmic_pixel', colors)
    
    ax.imshow(Z, cmap=cmap, extent=[-2, 2, -2, 2], origin='lower')
    ax.axis('off')
    
    # Add a sharp "pixel" border
    rect = plt.Rectangle((-0.1, -0.1), 0.2, 0.2, linewidth=1, edgecolor='white', facecolor='none', alpha=0.5)
    ax.add_patch(rect)
    
    outfile = os.path.join(output_dir, "universe_pixel_stage.png")
    plt.savefig(outfile, bbox_inches='tight', pad_inches=0, dpi=dpi)
    print(f"Generated: {outfile}")
    plt.close()

# 2. THE STRUCTURE (Phase II - Filaments)
def generate_structure():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_facecolor('black')
    
    # Generate random nodes
    np.random.seed(42)
    num_nodes = 200
    x = np.random.rand(num_nodes) * 10
    y = np.random.rand(num_nodes) * 10
    
    # Connect close nodes
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            dist = np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if dist < 1.0:
                alpha = 1.0 - dist
                ax.plot([x[i], x[j]], [y[i], y[j]], color='#4B0082', alpha=alpha*0.6, linewidth=0.5)
    
    # Plot nodes
    ax.scatter(x, y, s=5, c='#00BFFF', alpha=0.8, edgecolors='none')
    
    # Add a "grid" overlay to imply rendering
    ax.grid(True, color='#222222', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.axis('off')
    
    outfile = os.path.join(output_dir, "universe_structure_stage.png")
    plt.savefig(outfile, bbox_inches='tight', pad_inches=0, dpi=dpi)
    print(f"Generated: {outfile}")
    plt.close()

# 3. THE 8K UNIVERSE (Phase III)
def generate_8k_galaxy():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_facecolor('black')
    
    # Background stars
    num_stars = 2000
    sx = np.random.rand(num_stars) * 10
    sy = np.random.rand(num_stars) * 10
    sizes = np.random.rand(num_stars) * 2
    colors = np.random.rand(num_stars)
    ax.scatter(sx, sy, s=sizes, c=colors, cmap='coolwarm', alpha=0.6)
    
    # Main galaxy (Spiral approximation)
    theta = np.linspace(0, 4*np.pi, 500)
    # Arm 1
    r1 = 0.5 + 0.5*theta
    x1 = 5 + r1 * np.cos(theta) + np.random.normal(0, 0.1, 500)
    y1 = 5 + r1 * np.sin(theta) + np.random.normal(0, 0.1, 500)
    # Arm 2
    r2 = 0.5 + 0.5*theta
    x2 = 5 + r2 * np.cos(theta + np.pi) + np.random.normal(0, 0.1, 500)
    y2 = 5 + r2 * np.sin(theta + np.pi) + np.random.normal(0, 0.1, 500)
    
    ax.scatter(x1, y1, s=10, c='#FFD700', alpha=0.5)
    ax.scatter(x2, y2, s=10, c='#1E90FF', alpha=0.5)
    
    # Central bulge
    ax.scatter(5, 5, s=200, c='white', alpha=0.8, edgecolors='#FFD700', linewidth=2)
    
    ax.axis('off')
    
    outfile = os.path.join(output_dir, "universe_8k_stage.png")
    plt.savefig(outfile, bbox_inches='tight', pad_inches=0, dpi=dpi)
    print(f"Generated: {outfile}")
    plt.close()

if __name__ == "__main__":
    print("Generating figures...")
    generate_pixel()
    generate_structure()
    generate_8k_galaxy()
    print("Done.")
