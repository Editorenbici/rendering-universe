"""
Alexandroff One-Point Compactification Visualization
ℝ ∪ {∞} ≈ S¹

Best geometric image for ∞=1 in the Render Universe framework:
- The infinite line is completed by a *single point*.
- The result is compact (closed and bounded in the topological sense).
- R = ∞ and the "total" structure coincide.

Run: python 00_alexandroff_compactification.py
Saves: rendering-universe/paper/figures/alexandroff_compactification.png (or current dir)

This is for post-stacking conceptual work. Not to be included in the current paper.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Optional: try to save to paper/figures if it exists
out_dir = Path("rendering-universe/paper/figures")
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "alexandroff_compactification.png"

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: The real line (open, "infinite")
ax1 = axes[0]
ax1.set_xlim(-5, 5)
ax1.set_ylim(-1, 1)
ax1.axhline(0, color='black', linewidth=2)
ax1.annotate('', xy=(4.5, 0), xytext=(-4.5, 0),
             arrowprops=dict(arrowstyle='->', color='black', lw=2))
ax1.text(4.2, 0.25, r'$+\infty$', fontsize=14, ha='center')
ax1.text(-4.2, 0.25, r'$-\infty$', fontsize=14, ha='center')
ax1.set_title('ℝ — open, unbounded (potential / transfinite direction)', fontsize=11)
ax1.axis('off')

# Mark some points
for x, label in [(-2, '-2'), (0, '0'), (2, '2')]:
    ax1.plot(x, 0, 'ko', markersize=8)
    ax1.text(x, -0.4, label, ha='center', fontsize=10)

ax1.text(0, -0.8, 'No last point. Endless process.', ha='center', style='italic')

# Right: One-point compactification → circle
ax2 = axes[1]
theta = np.linspace(0, 2*np.pi, 200)
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax2.plot(circle_x, circle_y, 'b-', linewidth=2, label='S¹ (compact)')

# Stereographic-style: North pole = ∞
ax2.plot(0, 1, 'ro', markersize=12, zorder=5)
ax2.text(0.15, 1.15, r'$\infty$', fontsize=16, color='red', fontweight='bold')

# Project a few points from the line (via stereographic intuition)
# Simple illustrative mapping (not exact projection coords, but clear)
points = [(-2, '−2'), (0, '0'), (2, '+2')]
for x, label in points:
    # Approximate positions on circle for visualization
    # (real stereographic would map from line to circle minus north pole)
    phi = np.arctan(x) * 0.9   # squash a bit for viz
    px = np.sin(phi)
    py = -np.cos(phi) + 0.15   # shift so 0 maps near bottom-ish
    ax2.plot(px, py, 'ko', markersize=8)
    ax2.text(px + 0.12, py - 0.15, label, fontsize=10)

ax2.set_aspect('equal')
ax2.set_xlim(-1.6, 1.6)
ax2.set_ylim(-1.6, 1.6)
ax2.set_title('ℝ ∪ {∞}  ≅  S¹  (Alexandroff compactification)', fontsize=11)
ax2.axis('off')

# Add arrow / explanation
ax2.annotate('', xy=(0, 0.6), xytext=(0.8, 0.3),
             arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
ax2.text(0.85, 0.35, 'one point\ncloses\neverything', fontsize=9, ha='left', color='gray')

fig.suptitle('∞ = 1  —  The infinite is absorbed; the whole becomes complete and closed\n'
             '(No "outside". Total without requiring transfinite cardinal.)',
             fontsize=13, y=1.02)

plt.tight_layout()
plt.savefig(out_path, dpi=200, bbox_inches='tight')
print(f"Saved visualization to: {out_path.resolve()}")

# Also show a quick text version for terminal
print("\n" + "="*60)
print("TEXT DIAGRAM (one-point compactification)")
print("="*60)
print("""
      ∞ (the single extra point)
         /\\
        /  \\
       /    \\
      /      \\
     /   S¹   \\
    /          \\
   /____________\\
          |
          |
   −∞ ... −2 −1 0 +1 +2 ... +∞     ← open real line
          |
   Add one point at infinity → the line becomes a circle.
   The structure is now compact (total, closed).
   R=∞ (continuum) and the completed whole are the same object.
""")
print("="*60)

plt.show()  # comment out if running headless
