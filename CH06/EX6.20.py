# 6.20 (Geometry: display angles) Rewrite Listing 2.9, ComputeDistance.py, using the
# following function for computing the distance between two points.
# def distance(x1, y1, x2, y2):

def distance(x1, y1, x2, y2):
    distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    return distance


def main():
    x1, y1, x2, y2 = eval(input("Enter x1,y1,x2,y2: "))
    print("The distance is", distance(x1, y1, x2, y2))

main()