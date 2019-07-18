import cv2
import numpy as np

def order_points(pts):
    pts = np.array(pts)
    points = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    points[0] = pts[np.argmin(s)]
    points[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    points[1] = pts[np.argmin(diff)]
    points[3] = pts[np.argmax(diff)]
    return points

def get_roi(clicks):
    points = order_points(clicks)
    (tl, tr, br, bl) = points
    widthA = np.sqrt(((br[0]-bl[0])**2) + ((br[1]-bl[1])**2))
    widthB = np.sqrt(((tr[0]-tl[0])**2) + ((tr[1]-tl[1])**2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0]-br[0])**2) + ((tr[1]-br[1])**2))
    heightB = np.sqrt(((tl[0]-bl[0])**2) + ((tl[1]-bl[1])**2))
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array([[0, 0],[maxWidth-1, 0],[maxWidth-1, maxHeight-1],[0, maxHeight-1]], dtype="float32")

    return maxWidth,maxHeight,points,dst

def DFSUtil(self, v, visited):

    # Mark the current node as visited and print it
    visited[v] = True
    print
    v,

    # Recur for all the vertices adjacent to this vertex
    for i in self.graph[v]:
        if visited[i] == False:
            self.DFSUtil(i, visited)

            # The function to do DFS traversal. It uses

# recursive DFSUtil()
def DFS(self, v):

    # Mark all the vertices as not visited
    visited = [False] * (len(self.graph))

    # Call the recursive helper function to print
    # DFS traversal
    self.DFSUtil(v, visited) 