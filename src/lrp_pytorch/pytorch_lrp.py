from utils import *

def run_forward(image_path, maskedNodes_dict):
    # Load image
    X, mean, std = load_process_image(image_path)  

    # Load model  
    model = torchvision.models.vgg16(pretrained=True); model.eval()


    # Get layers
    layers = get_layers(model)
    del model

    # mask the corresponding nodes
    if isinstance(maskedNodes_dict, dict):
        for layerID, node_indices_List in maskedNodes_dict.items():

            if layerID < 37:
                layerToMask = layers[layerID]            
                layers[layerID] = mask_forward_layer(layerToMask, indicesList = node_indices_List)

    # compute the activations     
    L = len(layers)
    A = [X] + [None] * L

    get_activations(A,X,L,layers)          
    out = check_prediction(A)
    return A, layers, mean, std, out



def run_to_Layer(image_path, stopLayer, config, target_class,classLRP, savingNode, lrp, saveIntermmediate):    
    
    A, layers, mean, std, out  = run_forward(image_path = image_path, maskedNodes_dict = "None")

    if lrp is False:
        print(out, flush = True)

    if lrp is True:
        
        R, L = lrp_R_Initialize(A, target_class, layers, contrastive_signal = False, classLRP = classLRP)   

        # prepare layer_method_obj
        allLayer_methodObj = get_method_obj(config)
       
        for layerStep in range(stopLayer, L)[::-1]: #layerStep  range is [0,37]            
            
            lrp_R_backPropagation_step(A, R, layerStep, mean, std, allLayer_methodObj[layerStep], layers, contrastive_signal = False, classLRP =classLRP)
          
        for layerStep in range(1, stopLayer)[::-1]:        

            lrp_R_backPropagation_step(A, R, layerStep, mean, std, allLayer_methodObj[layerStep], layers, contrastive_signal = False, classLRP =classLRP)
                
        lrp_backPropagation_last(A, R, mean, std, layers)

        
        

        #------- saving heatmaps and data ----------                
        if saveIntermmediate == True:
            utils.heatmapSave(np.array(R[0][0]).sum(axis=0), 3.5, 3.5, 'output')            
            print("0", flush = True)

            save_intermediateLayer_relevance_heatmaps(R, stopLayer = 0)        
            print("1", flush = True)
        else:
            utils.heatmapSave(np.array(R[0][0]).sum(axis=0), 3.5, 3.5, 'output')
 
      

        
   
            

if __name__ == '__main__':

    # logging.basicConfig(level=# logging.INFO, filename='app.log', filemode='+a',format='%(name)s - %(levelname)s - %(asctime)s -%(message)s')              
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-i', '--input', help="path of input image", required=True)
    parser.add_argument('-c', '--config', help="configuration object", required=True)
    parser.add_argument('-l', '--lrp', help="Boolean lrp", required = True)
    parser.add_argument('-t', '--classIndex', help="target class", required = True)
    parser.add_argument('-s', '--stoplayer', help="stop layer", required = True)
    parser.add_argument('-n', '--nodes', help="node objects", required = True)
    parser.add_argument('-m', '--saveIntermmediate', help="Boolean to save intermmediate result", required= True)

    args = parser.parse_args()

    if args.input and args.config and args.lrp and args.classIndex and args.stoplayer and args.nodes:
           
        image_path = args.input
        config = json.loads(args.config)
        method_updating(config)
        lrp = True if args.lrp == "True" else False
        class_index = int(args.classIndex)
        target_class = class_index
        classLRP =  'None'   
        stopLayer = int(args.stoplayer)
        selected_nodes = args.nodes if args.nodes != "All" else "All"
        saveIntermmediate = True if args.saveIntermmediate == "True" else False
       
        # # logging.info(args.config)
        # cudaInfo = "using cuda" if cuda else "No cuda"
        # logging.info(cudaInfo)

        try:
            run_to_Layer(image_path, stopLayer, config, target_class, classLRP, selected_nodes, lrp, saveIntermmediate)
        except Exception as e:   

            # logging.error("Exception occurred", exc_info=True)
            pass
        # logging.info("done")
        
        


        