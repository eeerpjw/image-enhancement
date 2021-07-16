# Low Light Enhancement

A list of low light image reconstruction related works. 

## Hight Review

Liu, J., Xu, D., Yang, W., Fan, M. and Huang, H., Benchmarking Low-Light Image Enhancement and Beyond. International Journal of Computer Vision, pp.1-32.


## Traditional Methods
- [**LIME**] LIME: Low-light image Enhancement via Illumination Map Estimation (TIP 2017/ ACM 2016)[[Project page]](https://sites.google.com/view/xjguo/lime) [[MATLAB code]](https://drive.google.com/open?id=0BwVzAzXoqrSXb3prWUV1YzBjZzg) [[Dataset]](https://drive.google.com/open?id=0BwVzAzXoqrSXb3prWUV1YzBjZzg) [[PDF]](https://www3.cs.stonybrook.edu/~hling/publication/LIME-tip.pdf)

- [**BIMEF**] A Bio-Inspired Multi-Exposure Fusion Framework for Low-light Image Enhancement [[Project page]](https://baidut.github.io/BIMEF/) [[Matlab code]](https://github.com/baidut/BIMEF) The code for the comparison method is also provided, see [[here]](https://github.com/baidut/BIMEF/tree/master/lowlight)

- A New Image Contrast Enhancement Algorithm Using Exposure Fusion Framework [[Project]](https://baidut.github.io/2017/08/22/caip2017fuse2/) [[Matlab code]](https://baidut.github.io/2017/08/22/caip2017fuse2/)

- [**NPE**] Naturalness Preserved Enhancement Algorithm for Non-Uniform Illumination Images (TIP 2013) [[Project page]](http://blog.sina.com.cn/s/blog_a0a06f190101cvon.html) [[Matlab code]](https://s/096l3uy9vowgs4r/Code.rar) [[NPE dataset]](http://s/39gjz7oe1a0rlhk/original%20images%20in%20the%20paper.rar)

- [**SRIE**] A weighted variational model for simultaneous reflectance and illumination estimation (CVPR 2016) [[PDF]](https://xueyangfu.github.io/paper/2016/cvpr/cvpr2016.pdf) [[Matlab code]](https://xueyangfu.github.io/paper/2016/cvpr/Matlab_implementation.zip) [[Xueyang Fu (傅雪阳)]](https://xueyangfu.github.io/)

- [**MF**] A Fusion-based Enhancing Method for Weakly Illuminated Images (TIP 2013) [[Project page]](https://xueyangfu.github.io/projects/sp2016.html) [[PDF]](https://xueyangfu.github.io/paper/2016/SP/SP2016.pdf) [[Matlab code]](https://xueyangfu.github.io/paper/2016/SP/Matlab_code.zip)
- [**LR3M**] LR3M: Robust Low-Light Enhancement via Low-Rank Regularized Retinex Model (TIP 2020) [[MATLAB code]](https://github.com/tonghelen/LR3M-Method)

## Deep Learning Methods

- [**RetinexNet**] Deep Retinex Decomposition for Low-Light Enhancement (BMVC 2018) [[Project page]](https://daooshee.github.io/BMVC2018website/) [[Tensorflow code]](https://github.com/weichen582/RetinexNet) [[Dataset]](https://daooshee.github.io/BMVC2018website/) 
- [**GLADNet**] GLADNet: Low-Light Enhancement Network with Global Awareness. (FG'18 Workshop FOR-LQ 2018) [[Project page]](https://daooshee.github.io/fgworkshop18Gladnet/) [[Tensorflow code]](https://github.com/weichen582/GLADNet) [[Dataset]](https://daooshee.github.io/fgworkshop18Gladnet/)
- [**MBLLEN**] MBLLEN: Low-light Image/Video Enhancement Using CNNs (BMVC 2018)[[Project page]](http://phi-ai.org/project/MBLLEN/default.htm) [[Tensorflow code]](https://github.com/Lvfeifan/MBLLEN)
    - Feifan Lv, Yu Li and Feng Lu. Attention-guided Low-light Image Enhancement. arXiv:1908.00682. [[Paper]](https://arxiv.org/abs/1908.00682) and [[Project page]](http://phi-ai.org/project/AgLLNet/default.htm)
- [**SID**] Learning to see in the dark (CVPR 2018)[[Project page]](https://cchen156.github.io/SID.html) [[Tensorflow code]](https://github.com/cchen156/Learning-to-See-in-the-Dark) [[Dataset]](https://github.com/cchen156/Learning-to-See-in-the-Dark)
- Deep Photo Enhancer (CVPR 2018 spotlight) [[Github]](https://github.com/nothinglo/Deep-Photo-Enhancer) [[PDF]](https://www.csie.ntu.edu.tw/~cyy/publications/papers/Chen2018DPE.pdf)
- Low-Light Image Enhancement via a **Deep Hybrid Network** (TIP 2019) [[PDF]](https://ieeexplore.ieee.org/document/8692732) [[Caffe code]](https://drive.google.com/drive/folders/1Tx6x6m8dkU0HG8h3a02_TiGbGGIh6s8Y)
- [**DeepUPE**] Underexposed Photo Enhancement Using Deep Illumination Estimation （CVPR 2019）[[Tensorflow code]](https://github.com/wangruixing/DeepUPE)
- Progressive Retinex: Mutually Reinforced Illumination-Noise Perception Network for Low Light Image Enhancement (ACMMM2019) [[PDF]](https://arxiv.org/pdf/1911.11323.pdf)
- [**KinD**] Kindling the Darkness: A Practical Low-light Image Enhancer （ACM MM 2019）[[Tensorflow code]](https://github.com/zhangyhuaee/KinD)
- [**RDGAN**] RDGAN: Retinex Decomposition Based Adversarial Learning for Low-Light Enhancement (ICME 2019) [[Tensorflow code]](https://github.com/WangJY06/RDGAN)
- [[**Low-lightgan**]] Low-lightgan: Low-light enhancement via advanced generative adversarial network with (ICIP2019)
- [**Zero-DCE**] Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement (CVPR2020) [[PyTorch code]](https://github.com/Li-Chongyi/Zero-DCE)
- From Fidelity to Perceptual Quality: A Semi-Supervised Approach for Low-Light Image Enhancement (CVPR 2020) [[PDF]](https://openaccess.thecvf.com/content_CVPR_2020/papers/Yang_From_Fidelity_to_Perceptual_Quality_A_Semi-Supervised_Approach_for_Low-Light_CVPR_2020_paper.pdf)[[PyTorch code]](https://github.com/flyywh/CVPR-2020-Semi-Low-Light)
- [**EEMEF**]EEMEFN: Low Light Image Enhancement via Edge Enhanced MultiExposure Fusion Network (AAAI 2020) [[TensorFlow code]](https://github.com/MinfengZhu/EEMEFN)
- [**Enlightengan**] Enlightengan: Deep light enhancement without paired supervision (TIP2021) 
[[PyTorch Code]](https://github.com/VITA-Group/EnlightenGAN)
- Sparse Gradient Regularized Deep Retinex Network for Robust Low-Light Image Enhancement (TIP 2021)
- ReLLIE: Deep Reinforcement Learning for Customized Low-Light Image Enhancement (ACM MM 2021) 

## Low-light Denoising
- [**ELD**] A Physics-based Noise Formation Model for Extreme Low-light Raw Denoising (CVPR 2020) [[PDF]](https://openaccess.thecvf.com/content_CVPR_2020/papers/Wei_A_Physics-Based_Noise_Formation_Model_for_Extreme_Low-Light_Raw_Denoising_CVPR_2020_paper.pdf) [[PyTorch code]](https://github.com/Vandermode/ELD) [[Dataset]](https://github.com/Vandermode/ELD)


## Metrics

- **SSIM**
- **PSNR**
- **NIQE** [[code]](https://github.com/csjunxu/Bovik_NIQE_SPL2013)
- **LOE**
- **VIF**


## Applications


## Links

- [baidut/BIMEF](https://github.com/baidut/BIMEF)
- [OpenCE](https://github.com/baidut/OpenCE)
- [daooshee/Image-Processing-Datasets](https://github.com/daooshee/Image-Processing-Datasets)
- https://paperswithcode.com/task/low-light-image-enhancement
- [dawnlh/low-light-image-enhancement-resources](https://github.com/dawnlh/low-light-image-enhancement-resources)
- [cxtalk/You-Can-See-Clearly-Now](https://github.com/cxtalk/You-Can-See-Clearly-Now)
- [rockeyben/Low-Light](https://github.com/rockeyben/Low-Light)
- [简介近期的一些基于深度学习的图像/视频增强方法](https://zhuanlan.zhihu.com/p/164328373)

- [[Wenhan yang]](https://flyywh.github.io/Publication.html)
