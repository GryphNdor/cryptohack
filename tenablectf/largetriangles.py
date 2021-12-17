import math

distances = {}

def VerifyTriangle(a,b,c):
  if ((distances[a][0] == distances[b][0]) or (distances[a][0] == distances[c][0]) ) :
    print(a,b,c)
    print(math.pow(c,2) < math.pow(b,2) + math.pow(a,2))
    return (math.pow(c,2) < (math.pow(b,2) + math.pow(a,2)))
  

def FindLargestTriangleArea(points):
  for i in points:
    for j in points:
      if(i != j):
        print(i,j)
        dist_form = math.sqrt(math.pow(i[0]-j[0],2) + math.pow(i[1]-j[1],2) +math.pow(i[2]-j[2],2))
        distances[dist_form] = [i,j]
  print(distances)

  high_to_low = sorted(distances, reverse=True)
  areas = []
  for i in range(1,len(high_to_low)-1):
    if VerifyTriangle(high_to_low[i+1],high_to_low[i], high_to_low[0]):
      # print(distances[high_to_low[i]])
      s = (high_to_low[i] + high_to_low[i+1] + high_to_low[0])/2
      area = math.sqrt(s*(s-high_to_low[i])*(s-high_to_low[i+1])*(s-high_to_low[0]))
      areas.append(area)
    
  print(areas)
  return sorted(areas, reverse=True)[0]
  # return largest area

# Reading space delimited points from stdin
# and building list of 3D points
# points_data = input()
points_data = "-21,59,-93 -4,91,-2 1,61,2, 0,44,1, -21,59,-93"
points = []
for point in points_data.split(' '):
  point_xyz = point.split(',')
  points.append([int(point_xyz[0]), int(point_xyz[1]), int(point_xyz[2])])

# Compute Largest Triangle and Print Area rounded to nearest whole number
area = FindLargestTriangleArea(points)
print(int(round(area)))