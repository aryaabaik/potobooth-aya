from PIL import Image
import json

def get_transparent_boxes(img_path):
    img = Image.open(img_path).convert('RGBA')
    width, height = img.size
    pixels = img.load()
    
    boxes = []
    visited = set()
    
    # Step through the image in chunks to find transparent areas
    for y in range(0, height, 10):
        for x in range(0, width, 10):
            if pixels[x, y][3] < 128 and (x, y) not in visited:
                # Found a potential box. Let's find its exact boundaries.
                
                # Scan left
                min_x = x
                while min_x > 0 and pixels[min_x-1, y][3] < 128:
                    min_x -= 1
                
                # Scan right
                max_x = x
                while max_x < width - 1 and pixels[max_x+1, y][3] < 128:
                    max_x += 1
                
                # Scan up
                min_y = y
                while min_y > 0 and pixels[x, min_y-1][3] < 128:
                    min_y -= 1
                
                # Scan down
                max_y = y
                while max_y < height - 1 and pixels[x, max_y+1][3] < 128:
                    max_y += 1
                
                # Verify it's a box with a minimum size
                if (max_x - min_x) > 50 and (max_y - min_y) > 50:
                    # Check if this box is already found (via different pixel)
                    is_new = True
                    for b in boxes:
                        if abs(b['x'] - min_x) < 20 and abs(b['y'] - min_y) < 20:
                            is_new = False
                            break
                    if is_new:
                        boxes.append({
                            'x': min_x,
                            'y': min_y,
                            'w': max_x - min_x + 1,
                            'h': max_y - min_y + 1
                        })
                
                # Mark this area as visited (roughly)
                for vy in range(min_y, max_y + 1, 10):
                    for vx in range(min_x, max_x + 1, 10):
                        visited.add((vx, vy))

    # sort by y coord
    boxes.sort(key=lambda b: b['y'])
    return boxes

if __name__ == '__main__':
    path = "c:/Users/DESKTOP/OneDrive/Documents/yayarya/cobacoba/frames/8.png"
    result = get_transparent_boxes(path)
    print(json.dumps(result, indent=2))
