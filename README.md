## Visual Designer LRPs
### Description
VisLRPDesigner is a visual designer application for layerwise relevance propagation (LRP) rules[1,2]
- **Paper:**  https://doi.org/10.1111/cgf.14302
- **Code and Data:** https://github.com/ksuvislrp/vislrp


## Running VisLRPDesigner user interface Locally
### Getting code ready
- Download or clone this repository:
```bash
git clone https://github.com/ksuvislrp/vislrp.git
```

- This project is written in python 3.7.3 and PyTorch 1.3.1. The dependencies can be installed by running:
```
pip install -r requirement.txt
```
- VisLRPDesigner requires npm to run


### Getting Start within `VisLRPDesigner` repo, run
```
yarn install
```
### Start Program
```
npm start
```
<!-- ### Packaging application
```
npm run package
```
### Make for production
```
npm run make
```

### Useful Resources
None -->


### Model and input data
- [VGG-16](https://arxiv.org/abs/1409.1556) model pretrained by [ImageNet](http://www.image-net.org/) in [torchvision](https://pytorch.org/) is deployed in this application.
- The visualization system is built with [Node.js](https://nodejs.org/en/) and [D3.js](https://d3js.org/).



## Citation
```
@article{https://doi.org/10.1111/cgf.14302,
author = {Huang, Xinyi and Jamonnak, Suphanut and Zhao, Ye and Wu, Tsung Heng and Xu, Wei},
title = {A Visual Designer of Layer-wise Relevance Propagation Models},
journal = {Computer Graphics Forum},
volume = {40},
number = {3},
pages = {227-238},
doi = {https://doi.org/10.1111/cgf.14302},
url = {https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14302},
eprint = {https://onlinelibrary.wiley.com/doi/pdf/10.1111/cgf.14302},
year = {2021}
}

```
		

## License
MIT License. See [`LICENSE.md`](LICENSE.md).




## References
[1] Bach, S., Binder, A., Montavon, G., Klauschen, F., Müller, K.R. and Samek, W., 2015. On pixel-wise explanations for non-linear classifier decisions by layer-wise relevance propagation. PloS one, 10(7), p.e0130140.  
[2] Montavon, G., Binder, A., Lapuschkin, S., Samek, W. and Müller, K.R., 2019. Layer-wise relevance propagation: an overview. In Explainable AI: interpreting, explaining and visualizing deep learning (pp. 193-209). Springer, Cham. 
For implementing lrp methods in the paper, we partially followed the tutorial of http://heatmapping.org
