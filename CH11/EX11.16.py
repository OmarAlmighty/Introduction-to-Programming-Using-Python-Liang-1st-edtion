# 11.16 (Sort a list of points on y-coordinates) Write the following function to sort a list
# of points on their y-coordinates. Each point is a list of two values for x- and ycoordinates.
# # Returns a new list of points sorted on the y-coordinates
# def sort(points):
# For example, the points [[4, 2], [1, 7], [4, 5], [1, 2], [1, 1], [4, 1]] will be sorted
# to [[1, 1], [4, 1], [1, 2], [4, 2], [4, 5], [1, 7]]. Write a test program that displays
# the sorted result for points [[4, 34], [1, 7.5], [4, 8.5], [1, -4.5], [1, 4.5],
# [4, 6.6]] using print(list).

# Returns a new list of points sorted on the y-coordinates
def sort(points):  # insertion sort
    for i in range(1, len(points)):
        current = points[i]
        j = i - 1
        while j >= 0 and current[1] < points[j][1]:
            points[j + 1] = points[j]
            j -= 1
        points[j + 1] = current


points = [[4, 34], [1, 7.5], [4, 8.5], [1, -4.5], [1, 4.5], [4, 6.6]]

sort(points)
print(points)
