
import os
import math
import random

output_dir = r"c:\Users\Patricio\Downloads\universo render\Finales\Final_Paper\figures"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def write_svg(filename, width, height, shapes):
    with open(filename, 'w') as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" style="background-color:black">')
        for shape in shapes:
            f.write(shape)
        f.write('</svg>')
    print(f"Generated {filename}")

# 1. PIXEL (SVG)
def generate_pixel_svg():
    shapes = []
    # Glow
    for r in range(100, 0, -10):
        opacity = 0.05
        shapes.append(f'<circle cx="300" cy="300" r="{r}" fill="blue" fill-opacity="{opacity}" />')
    # Pixel
    shapes.append('<rect x="290" y="290" width="20" height="20" fill="white" stroke="cyan" stroke-width="2" />')
    
    write_svg(os.path.join(output_dir, "universe_pixel_stage.svg"), 600, 600, shapes)

# 2. STRUCTURE (SVG)
def generate_structure_svg():
    shapes = []
    nodes = []
    for _ in range(100):
        nodes.append((random.randint(50, 750), random.randint(50, 550)))
    
    # Connections
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            x1, y1 = nodes[i]
            x2, y2 = nodes[j]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            if dist < 100:
                opacity = 1 - (dist/100)
                shapes.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="purple" stroke-width="1" stroke-opacity="{opacity}" />')
    
    # Nodes
    for x, y in nodes:
        shapes.append(f'<circle cx="{x}" cy="{y}" r="2" fill="cyan" />')

    write_svg(os.path.join(output_dir, "universe_structure_stage.svg"), 800, 600, shapes)

# 3. GALAXY (SVG)
def generate_galaxy_svg():
    shapes = []
    # Stars
    for _ in range(1000):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        r = random.random() * 1.5
        op = random.random()
        shapes.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="white" fill-opacity="{op}" />')

    # Galaxy Arms
    center_x, center_y = 400, 300
    for i in range(600):
        angle = i * 0.1
        radius = i * 0.4
        x1 = center_x + radius * math.cos(angle) + random.uniform(-10, 10)
        y1 = center_y + radius * math.sin(angle) + random.uniform(-10, 10)
        x2 = center_x + radius * math.cos(angle + 3.14) + random.uniform(-10, 10)
        y2 = center_y + radius * math.sin(angle + 3.14) + random.uniform(-10, 10)
        
        shapes.append(f'<circle cx="{x1}" cy="{y1}" r="{random.random()*2}" fill="gold" fill-opacity="0.6" />')
        shapes.append(f'<circle cx="{x2}" cy="{y2}" r="{random.random()*2}" fill="cyan" fill-opacity="0.6" />')

    write_svg(os.path.join(output_dir, "universe_8k_stage.svg"), 800, 600, shapes)

if __name__ == "__main__":
    generate_pixel_svg()
    generate_structure_svg()
    generate_galaxy_svg()
