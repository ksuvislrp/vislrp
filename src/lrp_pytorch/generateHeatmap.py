
from utils import *


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--layerid', help="layerid", required=True)
    parser.add_argument('-n', '--nodeid', help="nodeid", required=True)
    parser.add_argument('-d', '--dataX', help="dataX", required=True)
    args = parser.parse_args()

    if args.layerid and args.nodeid and args.dataX:

        layerID = args.layerid
        print("args.nodeid:", type(args.nodeid),args.nodeid)
        nodeID = args.nodeid #if args.nodeid == "All" else int(args.nodeid)

        #### the args.dataX contains a string "R" or "A" for relevance or activation
        dataX = args.dataX
        save_intermediateNode_heatmaps(layerID = layerID, nodeID = nodeID, typeX = dataX)


