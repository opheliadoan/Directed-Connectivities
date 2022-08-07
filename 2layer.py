from collections import deque, defaultdict
import itertools

class latticePath:
  def __init__(self, path, i, j):
    self.path = path 
    self.i = i 
    self.j = j

# find all lattice paths
def latticePaths(network):
  m = len(network)
  n = len(network[0])
  res = []

  q = deque()
  q.append(latticePath([network[m - 1][0]], m - 1, 0))

  while len(q) > 0:
    p = q.popleft()

    # print the path if reach destination
    if p.i == 0 and p.j == n - 1:
      res.append(tuple(p.path[1:]))

    # if reach the top layer, move right
    elif p.i == 0:
      temp = p.path[:]
      # update current path
      temp.append((network[p.i][p.j], network[p.i][p.j + 1]))
      q.append(latticePath(temp, p.i, p.j + 1))

    # if reach the last col, move up
    elif p.j == n - 1:
      temp = p.path[:]
      # update current path
      temp.append((network[p.i][p.j], network[p.i - 1][p.j]))
      q.append(latticePath(temp, p.i - 1, p.j))

    # both up and right movements are allowed
    else:
      temp = p.path[:]
      # update current path with up movement
      temp.append((network[p.i][p.j], network[p.i - 1][p.j]))
      q.append(latticePath(temp, p.i - 1, p.j))

      temp = temp[:-1]
      # update current path with right movement
      temp.append((network[p.i][p.j], network[p.i][p.j + 1]))
      q.append(latticePath(temp, p.i, p.j + 1))

  return res

# union sets
def unionSets(s):
  res = set()
  for el in s:
    res = res.union(set(el))
  return res

def generateSubsets(s, k):
  return map(set, itertools.combinations(s, k))

def findCoef(latticePaths):
  coef = defaultdict(int)
  coef[latticePathLen] = len(latticePaths)
  pie = -1

  for k in range(2, len(latticePaths) + 1):
    kSets = generateSubsets(latticePaths, k)
    for kSet in kSets:
      # print(kSet)
      # print(unionSets(kSet))
      # print(len(unionSets(kSet)))
      # print()
      totalSegments = len(unionSets(kSet))
      coef[totalSegments] += pie
    pie = 0 - pie

  return coef

# network = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
network = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
latticePathLen = len(network[0]) + len(network) - 2
latticeSet = latticePaths(network)
# print()
# print(generateSubsets(latticeSet, 2))
# print(findCoef(latticeSet))
coefList = findCoef(latticeSet)
polyStr = ''
for seg, count in list(coefList.items())[::-1]:
    polyStr += ' %d*p^%d +' % (count, seg)
  
print(polyStr[:-1]) #1*p^12 + -4*p^11 + 4*p^9 + 2*p^10 + 2*p^8 + -4*p^7 + -6*p^6 + 6*p^4