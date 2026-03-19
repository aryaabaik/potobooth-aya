from PIL import Image
import sys

def main():
    img = Image.open('c:/Users/DESKTOP/OneDrive/Documents/yayarya/cobacoba/frames/8.png').convert('RGBA')
    w, h = img.size
    pixels = img.load()
    
    mid_x = w // 2
    
    in_hole = False
    y_transitions = []
    
    for y in range(h):
        alpha = pixels[mid_x, y][3]
        if alpha < 255 and not in_hole:
            y_transitions.append(y)
            in_hole = True
        elif alpha == 255 and in_hole:
            y_transitions.append(y - 1)
            in_hole = False
            
    print(f"Y Transitions (mid_x={mid_x}):", y_transitions)
    
    if len(y_transitions) >= 2:
        mid_y = (y_transitions[0] + y_transitions[1]) // 2
        in_hole_x = False
        x_transitions = []
        for x in range(w):
            alpha = pixels[x, mid_y][3]
            if alpha < 255 and not in_hole_x:
                x_transitions.append(x)
                in_hole_x = True
            elif alpha == 255 and in_hole_x:
                x_transitions.append(x - 1)
                in_hole_x = False
        print(f"X Transitions (mid_y={mid_y}):", x_transitions)

if __name__ == '__main__':
    main()
