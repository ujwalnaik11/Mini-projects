from RRTbase import RRTGraph
from RRTbase import RRTMap
from cv2 import waitKey

def main():
    dimensions=(512,512)  # map dimetions
    # start and coords
    start=(0,0)
    goal=(510,510)
    map=RRTMap(start,goal ,dimensions )
    graph=RRTGraph(start,goal,dimensions)
    # make obstacles randomly
    obstacles=graph.makeobs()
    # draw the map
    map.drawMap(obstacles)
    i=1 # iteration counter
    while(not graph.path_to_goal(goal)):
        # biasing the tree
        if i%10 == 0 :
            X,Y,Parent=graph.bias(goal)
            map.drawNode([X[-1],Y[-1]], nodeType="N")
            map.drawEdge( (X[-1],Y[-1]) , (X[Parent[-1]],Y[Parent[-1]])  )
            map.refreshMap()
        # expanding  the tree
        else:
            X,Y,Parent=graph.expand()
            map.drawNode([X[-1], Y[-1]], nodeType="N")
            map.drawEdge((X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]))
            map.refreshMap()
        i+=1
    # extract the coordinates of the path waypoints
    graph.path_to_goal(goal)
    # draw the path
    map.drawPath(graph.getPathCoords())

    waitKey(0)


if __name__ == '__main__':
    main()

