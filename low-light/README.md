# Low Light Enhancement

A list of low light image reconstruction related works.

## Hight Review

- Liu, J., Xu, D., Yang, W., Fan, M. and Huang, H., **Benchmarking Low-Light Image Enhancement and Beyond**. International Journal of Computer Vision, pp.1-32.
- [Low-Light Image and Video Enhancement Using Deep Learning: A Survey](https://github.com/Li-Chongyi/Lighting-the-Darkness-in-the-Deep-Learning-Era-Open)
  - [[中文版本综述]](https://li-chongyi.github.io/PDF/Low_Light_Image_and_Video_Enhancement_Using_Deep_Learning__A_Survey.pdf)
  - [[Platform] Lighting the Darkness in the Deep Learning Era](http://mc.nankai.edu.cn/ll/)
  - [[Project]](https://github.com/Li-Chongyi/Lighting-the-Darkness-in-the-Deep-Learning-Era-Open/) **A sound survey including methods with codes and datasets !**
  - [[Dataset] LoLi-Phone (3.4G)](https://drive.google.com/file/d/1QS4FgT5aTQNYy-eHZ_A89rLoZgx_iysR/view)

## Traditional Methods

- [**LIME**] LIME: Low-light image Enhancement via Illumination Map Estimation (TIP 2017/ ACM 2016)
  - Guo X, Li Y, Ling H. LIME: Low-light image enhancement via illumination map estimation[J]. IEEE Transactions on image processing, 2016, 26(2): 982-993.
  - [[Project page]](https://sites.google.com/view/xjguo/lime)
  - [[MATLAB code]](https://drive.google.com/open?id=0BwVzAzXoqrSXb3prWUV1YzBjZzg)
  - [[Dataset]](https://drive.google.com/open?id=0BwVzAzXoqrSXb3prWUV1YzBjZzg)
  - [[PDF]](https://www3.cs.stonybrook.edu/~hling/publication/LIME-tip.pdf)

- [**BIMEF**] A Bio-Inspired Multi-Exposure Fusion Framework for Low-light Image Enhancement
  - Submitted to IEEE Transactions on Cybernetics
  - [[Project page]](https://baidut.github.io/BIMEF/)
  - [[Matlab code]](https://github.com/baidut/BIMEF)
  - [[PDF]](https://arxiv.org/pdf/1711.00591.pdf)
  - The code for the comparison method is also provided, see [[here]](https://github.com/baidut/BIMEF/tree/master/lowlight)

- A New Image Contrast Enhancement Algorithm Using Exposure Fusion Framework (CAIP'2017)
  - Ying Z, Li G, Ren Y, et al. A new image contrast enhancement algorithm using exposure fusion framework[C]//International Conference on Computer Analysis of Images and Patterns. Springer, Cham, 2017: 36-46.
  - [[Project]](https://baidut.github.io/2017/08/22/caip2017fuse2/)
  - [[Matlab code]](https://baidut.github.io/2017/08/22/caip2017fuse2/)

- [**NPE**] Naturalness Preserved Enhancement Algorithm for Non-Uniform Illumination Images (TIP 2013)
  - Wang S, Zheng J, Hu H M, et al. Naturalness preserved enhancement algorithm for non-uniform illumination images[J]. IEEE Transactions on Image Processing, 2013, 22(9): 3538-3548.
  - [[Project page]](http://blog.sina.com.cn/s/blog_a0a06f190101cvon.html)
  - [[Matlab code]](https://s/096l3uy9vowgs4r/Code.rar)
  - [[NPE dataset]](http://s/39gjz7oe1a0rlhk/original%20images%20in%20the%20paper.rar)

- [**SRIE**] A weighted variational model for simultaneous reflectance and illumination estimation (CVPR 2016)
  - Fu X, Zeng D, Huang Y, et al. A weighted variational model for simultaneous reflectance and illumination estimation[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2016: 2782-2790.
  - [[Matlab code]](https://xueyangfu.github.io/paper/2016/cvpr/Matlab_implementation.zip)
  - [[PDF]](https://xueyangfu.github.io/paper/2016/cvpr/cvpr2016.pdf)

- [**MF**] A Fusion-based Enhancing Method for Weakly Illuminated Images
  - Fu X, Zeng D, Huang Y, et al. A fusion-based enhancing method for weakly illuminated images[J]. Signal Processing, 2016, 129: 82-96.
  - [[Project page]](https://xueyangfu.github.io/projects/sp2016.html)
  - [[Matlab code]](https://xueyangfu.github.io/paper/2016/SP/Matlab_code.zip)
  - [[PDF]](https://xueyangfu.github.io/paper/2016/SP/SP2016.pdf)

- [**LR3M**] LR3M: Robust Low-Light Enhancement via Low-Rank Regularized Retinex Model (TIP 2020)
  - Ren, Xutong, et al. "Lr3m: Robust low-light enhancement via low-rank regularized retinex model." IEEE Transactions on Image Processing 29 (2020): 5862-5876.
  - [[MATLAB code]](https://github.com/tonghelen/LR3M-Method)
  - [[PDF]](https://tonghelen.github.io/att/LR3M.pdf)

## Deep Learning Methods

- [**DPED**] DSLR-Quality Photos on Mobile Devices with Deep Convolutional Networks (ICCV 2017)
  - [[Tensorflow code]](https://github.com/aiff22/DPED)
  - [[Project page]](https://people.ee.ethz.ch/~ihnatova/#title)

- [**RetinexNet**] Deep Retinex Decomposition for Low-Light Enhancement (BMVC 2018)
  - Wei C, Wang W, Yang W, et al. Deep retinex decomposition for low-light enhancement[J]. arXiv preprint arXiv:1808.04560, 2018.
  - [[Project page]](https://daooshee.github.io/BMVC2018website/)
  - [[Tensorflow code]](https://github.com/weichen582/RetinexNet)
  - [[Dataset]](https://daooshee.github.io/BMVC2018website/)
  - [[PDF]](https://arxiv.org/pdf/1808.04560)

- [**GLADNet**] GLADNet: Low-Light Enhancement Network with Global Awareness. (FG'18 Workshop FOR-LQ 2018)
  - Wang, Wenjing, et al. "GLADNet: Low-light enhancement network with global awareness." 2018 13th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2018). IEEE, 2018.
  - [[Project page]](https://daooshee.github.io/fgworkshop18Gladnet/)
  - [[Tensorflow code]](https://github.com/weichen582/GLADNet)
  - [[Dataset]](https://daooshee.github.io/fgworkshop18Gladnet/)
  - [[PDF]](http://39.96.165.147/Pub%20Files/2018/wwj_fg2018.pdf)

- [**MBLLEN**] MBLLEN: Low-light Image/Video Enhancement Using CNNs (BMVC 2018)
  - Lv F, Lu F, Wu J, et al. MBLLEN: Low-Light Image/Video Enhancement Using CNNs[C]//BMVC. 2018: 220.
  - [[Project page]](http://phi-ai.org/project/MBLLEN/default.htm)
  - [[Tensorflow code]](https://github.com/Lvfeifan/MBLLEN)
  - [[PDF]](http://bmvc2018.org/contents/papers/0700.pdf)

- Attention-guided Low-light Image Enhancement. arXiv:1908.00682.
  - Feifan Lv, Yu Li and Feng Lu. Attention-guided Low-light Image Enhancement. arXiv:1908.00682.
  - [[Project page]](http://phi-ai.org/project/AgLLNet/default.htm) [[No released code]]
  - [[PDF]](https://arxiv.org/abs/1908.00682)
  - 参见[**AgLLNet**] TIP没中，改投的IJCV，太水了

- [**SID**] Learning to see in the dark (CVPR 2018)
  - Chen, Chen, et al. "Learning to see in the dark." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018.
  - [[Project page]](https://cchen156.github.io/SID.html)
  - [[Tensorflow code]](https://github.com/cchen156/Learning-to-See-in-the-Dark)
  - [[Dataset]](https://github.com/cchen156/Learning-to-See-in-the-Dark)
  - [[PDF]](https://cchen156.github.io/paper/18CVPR_SID.pdf)

- Deep Photo Enhancer: Unpaired learning for image enhancement from photographs with GANs (CVPR 2018 spotlight)
  - Chen, Yu-Sheng, et al. "Deep photo enhancer: Unpaired learning for image enhancement from photographs with gans." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018.
  - [[Github with no code release]](https://github.com/nothinglo/Deep-Photo-Enhancer)
  - [[PDF]](https://www.csie.ntu.edu.tw/~cyy/publications/papers/Chen2018DPE.pdf)
  - [[Non-official TF2 code]](https://github.com/MrRobot2211/deep-photo-enhance-t2)

- LightenNet: a convolutional neural network for weakly illuminated image enhancement (Pattern Recognition Letter 2018)
  - [[Project]](https://li-chongyi.github.io/proj_lowlight.html)
  - [[code]](https://github.com/Li-Chongyi/Low-Light-Codes)

- [**HybridNet**]Low-Light Image Enhancement via a Deep Hybrid Network (TIP 2019)
  - Ren W, Liu S, Ma L, et al. Low-light image enhancement via a deep hybrid network[J]. IEEE Transactions on Image Processing, 2019, 28(9): 4364-4375.
  - [[Caffe code]](https://drive.google.com/drive/folders/1Tx6x6m8dkU0HG8h3a02_TiGbGGIh6s8Y)

- [**DeepUPE**] Underexposed Photo Enhancement Using Deep Illumination Estimation （CVPR 2019）
  - Wang R, Zhang Q, Fu C W, et al. Underexposed photo enhancement using deep illumination estimation[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019: 6849-6857.
  - [[Tensorflow code]](https://github.com/wangruixing/DeepUPE)
  - [[PDF]](https://openaccess.thecvf.com/content_CVPR_2019/papers/Wang_Underexposed_Photo_Enhancement_Using_Deep_Illumination_Estimation_CVPR_2019_paper.pdf)

- Progressive Retinex: Mutually Reinforced Illumination-Noise Perception Network for Low Light Image Enhancement (ACMMM2019)
  - Wang, Yang, et al. "Progressive retinex: Mutually reinforced illumination-noise perception network for low-light image enhancement." Proceedings of the 27th ACM International Conference on Multimedia. 2019.
  - [[PDF]](https://arxiv.org/pdf/1911.11323.pdf)

- [**KinD**] Kindling the Darkness: A Practical Low-light Image Enhancer （ACM MM 2019）
  - Zhang, Yonghua, Jiawan Zhang, and Xiaojie Guo. "Kindling the darkness: A practical low-light image enhancer." Proceedings of the 27th ACM international conference on multimedia. 2019.
  - [[Tensorflow code]](https://github.com/zhangyhuaee/KinD)
  - [[PDF]](https://arxiv.org/pdf/1905.04161.pdf)

- [**RDGAN**] RDGAN: Retinex Decomposition Based Adversarial Learning for Low-Light Enhancement (ICME 2019)
  - Wang, Junyi, et al. "RDGAN: Retinex decomposition based adversarial learning for low-light enhancement." 2019 IEEE International Conference on Multimedia and Expo (ICME). IEEE, 2019.
  - [[Tensorflow code]](https://github.com/WangJY06/RDGAN)

- [**Low-lightgan**] Low-lightgan: Low-light enhancement via advanced generative adversarial network with (ICIP2019)
  - Kim, Guisik, Dokyeong Kwon, and Junseok Kwon. "Low-lightgan: Low-light enhancement via advanced generative adversarial network with task-driven training." 2019 IEEE International Conference on Image Processing (ICIP). IEEE, 2019.

- [**Zero-DCE**] Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement (CVPR'2020)
  - [[Project]](https://li-chongyi.github.io/Proj_Zero-DCE.html)
  - [[PyTorch code]](https://github.com/Li-Chongyi/Zero-DCE)
  - [[PDF]](https://openaccess.thecvf.com/content_CVPR_2020/papers/Guo_Zero-Reference_Deep_Curve_Estimation_for_Low-Light_Image_Enhancement_CVPR_2020_paper.pdf)
  - **TPAMI version** 👇

- Learning to Enhance Low-Light Image via Zero-Reference Deep Curve Estimation (TPAMI 2021)
  - Li, Chongyi, Chunle Guo, and Chen Change Loy. "Learning to enhance low-light image via zero-reference deep curve estimation." arXiv preprint arXiv:2103.00860 (2021).
  - [[Pytorch code]](https://github.com/Li-Chongyi/Zero-DCE_extension)
  - [[PDF]](https://arxiv.org/pdf/2103.00860.pdf)

- [**DeepLPF**] DeepLPF: Deep Local Parametric Filters for Image Enhancement (CVPR'2020)
  - Moran, Sean, et al. "Deeplpf: Deep local parametric filters for image enhancement." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.
  - [[PyTorch code]](https://github.com/sjmoran/DeepLPF)
  - [[PDF]](https://openaccess.thecvf.com/content_CVPR_2020/papers/Moran_DeepLPF_Deep_Local_Parametric_Filters_for_Image_Enhancement_CVPR_2020_paper.pdf)

- From Fidelity to Perceptual Quality: A Semi-Supervised Approach for Low-Light Image Enhancement (CVPR 2020)
  - Yang W, Wang S, Fang Y, et al. From fidelity to perceptual quality: A semi-supervised approach for low-light image enhancement[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020: 3063-3072.
  - [[PyTorch code]](https://github.com/flyywh/CVPR-2020-Semi-Low-Light)
  - [[PDF]](https://openaccess.thecvf.com/content_CVPR_2020/papers/Yang_From_Fidelity_to_Perceptual_Quality_A_Semi-Supervised_Approach_for_Low-Light_CVPR_2020_paper.pdf)

- [**EEMEF**]EEMEFN: Low Light Image Enhancement via Edge Enhanced MultiExposure Fusion Network (AAAI 2020)
  - Zhu, Minfeng, et al. "Eemefn: Low-light image enhancement via edge-enhanced multi-exposure fusion network." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 34. No. 07. 2020.
  - [[TensorFlow code]](https://github.com/MinfengZhu/EEMEFN)
  - [[PDF]](https://ojs.aaai.org/index.php/AAAI/article/view/7013/6867)

- [**L3Fnet**] Harnessing Multi-View Perspective of Light Fields for Low-Light Imaging (TIP'2020)
  - Lamba, Mohit, Kranthi Kumar Rachavarapu, and Kaushik Mitra. "Harnessing multi-view perspective of light fields for low-light imaging." IEEE Transactions on Image Processing 30 (2020): 1501-1513.
  - [[Project]](https://mohitlamba94.github.io/L3Fnet/)
  - [[Pytorch code]](https://github.com/MohitLamba94/L3Fnet)
  - [[L3F Dataset]](https://mohitlamba94.github.io/L3Fnet/)
  - [[Mohit Lamba]](https://mohitlamba94.github.io/about-me/)

- [**LLPackNet**] Towards Fast and Light-Weight Restoration of Dark Images (BMVC 2020)
  - [[Project]](https://mohitlamba94.github.io/LLPackNet/)
  - [[PyTorch code]](https://github.com/MohitLamba94/LLPackNet)
  - [[PDF]](https://www.bmvc2020-conference.com/assets/papers/0145.pdf)
  - [[arxiv version with supplementary]](https://arxiv.org/abs/2011.14133)
  - [[Mohit Lamba]](https://mohitlamba94.github.io/about-me/)

- [**Enlightengan**] Enlightengan: Deep light enhancement without paired supervision (TIP2021)
  - Jiang Y, Gong X, Liu D, et al. Enlightengan: Deep light enhancement without paired supervision[J]. IEEE Transactions on Image Processing, 2021, 30: 2340-2349.
  - [[PyTorch Code]](https://github.com/VITA-Group/EnlightenGAN)
  - [[PDF]](https://arxiv.org/pdf/1906.06972.pdf)

- Sparse Gradient Regularized Deep Retinex Network for Robust Low-Light Image Enhancement (TIP 2021)
  - Yang W, Wang W, Huang H, et al. Sparse gradient regularized deep retinex network for robust low-light image enhancement[J]. IEEE Transactions on Image Processing, 2021, 30: 2072-2086.
  - [[PDF]](http://39.96.165.147/Pub%20Files/2021/ywh_tip21.pdf)

- [**ReLLIE**]ReLLIE: Deep Reinforcement Learning for Customized Low-Light Image Enhancement (ACM MM 2021)
  - [[PDF]](https://arxiv.org/pdf/2107.05830.pdf)

- Restoring Extremely Dark Images in Real Time (CVPR'2021)
  - Lamba, Mohit, and Kaushik Mitra. "Restoring Extremely Dark Images in Real Time." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021.
  - The followup of LLPackNet in BMVC 2020.
  - [[Project]](https://mohitlamba94.github.io/Restoring-Extremely-Dark-Images-In-Real-Time/)
  - [[PyTorch code]](https://github.com/MohitLamba94/Restoring-Extremely-Dark-Images-In-Real-Time)
  - [[PDF]](https://openaccess.thecvf.com/content/CVPR2021/papers/Lamba_Restoring_Extremely_Dark_Images_in_Real_Time_CVPR_2021_paper.pdf)
  - [[Mohit Lamba]](https://mohitlamba94.github.io/about-me/)

- [**MIRNet**] Learning Enriched Features for Real Image Restoration and Enhancement (ECCV 2020)
  - [[TensorFlow code]](https://github.com/swz30/MIRNet)

- Nighttime visibility enhancement by increasing the dynamic range and suppression of light effects (CVPR'2021)
  - Sharma A, Tan R T. Nighttime Visibility Enhancement by Increasing the Dynamic Range and Suppression of Light Effects[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021: 11977-11986.
  - [[PDF]](https://openaccess.thecvf.com/content/CVPR2021/papers/Sharma_Nighttime_Visibility_Enhancement_by_Increasing_the_Dynamic_Range_and_Suppression_CVPR_2021_paper.pdf)

- Learning temporal consistency for low light video enhancement from single images (CVPR'2021)
  - Zhang F, Li Y, You S, et al. Learning Temporal Consistency for Low Light Video Enhancement From Single Images[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021: 4967-4976
  - [[PyTorch code]](https://github.com/zkawfanx/StableLLVE)
  - [[PDF]](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhang_Learning_Temporal_Consistency_for_Low_Light_Video_Enhancement_From_Single_CVPR_2021_paper.pdf)

- [**RAUS**] Retinex-Inspired Unrolling with Cooperative Prior Architecture Search for Low-Light Image Enhancement (CVPR'2021)
  - Liu R, Ma L, Zhang J, et al. Retinex-inspired unrolling with cooperative prior architecture search for low-light image enhancement[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021: 10561-10570.
  - [[PDF]](https://openaccess.thecvf.com/content/CVPR2021/papers/Liu_Retinex-Inspired_Unrolling_With_Cooperative_Prior_Architecture_Search_for_Low-Light_Image_CVPR_2021_paper.pdf)
  - [[PyTorch code]](https://github.com/KarelZhang/RUAS)

- [**AgLLNet**] Attention Guided Low-light Image Enhancement with a Large Scale Low-light Simulation Dataset (IJCV 2021)
  - Lv F, Li Y, Lu F. Attention guided low-light image enhancement with a large scale low-light simulation dataset[J]. International Journal of Computer Vision, 2021, 129(7): 2175-2193.
  - [[Projet]](http://www.phi-ai.org/project/AgLLNet/default.htm)
  - [[TensorFlow code (only for testing)]](https://github.com/yu-li/AGLLNet)
  - [[Synthetic Dataset(Baidu Drive password: os9v)]](https://pan.baidu.com/s/1SID1MOQJjQjV99QeHy1hPg)
  - [[PDF]](https://arxiv.org/pdf/1908.00682.pdf)

- Learning Multi-Scale Photo Exposure Correction (CVPR 2021)
  - [[PyTorch code]](https://github.com/mahmoudnafifi/Exposure_Correction)
  - [[Paper]](https://openaccess.thecvf.com/content/CVPR2021/papers/Afifi_Learning_Multi-Scale_Photo_Exposure_Correction_CVPR_2021_paper.pdf)

- Ultra-High-Definition Low-Light Image Enhancement: A Benchmark and Transformer-Based Method （AAAI 2023）
- [[Project]](https://taowangzj.github.io/projects/LLFormer/)
- [[code]](https://github.com/taowangzj/llformer)
- [[Paper]](https://arxiv.org/abs/2212.11548)
- [[Dataset]](https://taowangzj.github.io/projects/LLFormer/))


## Low-light Denoising

- [**ELD**] A Physics-based Noise Formation Model for Extreme Low-light Raw Denoising (CVPR 2020)
  - [[PDF]](https://openaccess.thecvf.com/content_CVPR_2020/papers/Wei_A_Physics-Based_Noise_Formation_Model_for_Extreme_Low-Light_Raw_Denoising_CVPR_2020_paper.pdf)
  - [[PyTorch code]](https://github.com/Vandermode/ELD)
  - [[Dataset]](https://github.com/Vandermode/ELD)

- Deep Denoising of Flash and No-Flash Pairs for Photography in Low-Light Environments(CVPR'2021)
  - Xia, Zhihao, et al. "Deep Denoising of Flash and No-Flash Pairs for Photography in Low-Light Environments." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021.
  - [[PDF]](https://openaccess.thecvf.com/content/CVPR2021/papers/Xia_Deep_Denoising_of_Flash_and_No-Flash_Pairs_for_Photography_in_CVPR_2021_paper.pdf)

- Extreme Low-Light Environment-Driven Image Denoising over Permanently Shadowed Lunar Regions with a Physical Noise Model (CVPR'2021)
  - Moseley, Ben, et al. "Extreme Low-Light Environment-Driven Image Denoising Over Permanently Shadowed Lunar Regions With a Physical Noise Model." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021.
  - [[PDF]](https://openaccess.thecvf.com/content/CVPR2021/papers/Moseley_Extreme_Low-Light_Environment-Driven_Image_Denoising_Over_Permanently_Shadowed_Lunar_Regions_CVPR_2021_paper.pdf)

## Video

- [**SIDGAN**] Low Light Video Enhancement using Synthetic Data Produced with an Intermediate Domain (ECCV'2020)
  - Triantafyllidou, Danai, et al. "Low Light Video Enhancement Using Synthetic Data Produced with an Intermediate Domain Mapping." European Conference on Computer Vision. Springer, Cham, 2020.
  - [[TensorFlow code]](https://github.com/sjmoran/SIDGAN)
  - [[PDF]](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123580103.pdf)  

## color & contrast enhencement

- Learning Image-adaptive 3D Lookup Tables for High Performance Photo Enhancement in Real-time (TPAMI'2021)
  - Zeng, Hui, Jianrui Cai, Lida Li, Zisheng Cao, and Lei Zhang. "Learning image-adaptive 3D lookup tables for high performance photo enhancement in real-time." IEEE Transactions on Pattern Analysis and Machine Intelligence (2020).
  - [[PyTorch code]](https://github.com/HuiZeng/Image-Adaptive-3DLUT)
  - [[Dataset onedrive]](https://connectpolyu-my.sharepoint.com/personal/16901447r_connect_polyu_hk/_layouts/15/onedrive.aspx?originalPath=aHR0cHM6Ly9jb25uZWN0cG9seXUtbXkuc2hhcmVwb2ludC5jb20vOmY6L2cvcGVyc29uYWwvMTY5MDE0NDdyX2Nvbm5lY3RfcG9seXVfaGsvRXFOR3VRVUtaZTlDdjNmUEcwOE9tR0VCYkhNVVhleTJhVTAzRTIxZEZad0p5Zz9ydGltZT1sQm8wazR0UjJVZw&id=%2Fpersonal%2F16901447r%5Fconnect%5Fpolyu%5Fhk%2FDocuments%2Fimage%5Fadaptive%5Flut)
  - [[PDF]](https://www4.comp.polyu.edu.hk/~cslzhang/paper/PAMI_LUT.pdf) [[Supplementary]](https://www4.comp.polyu.edu.hk/~cslzhang/paper/Supplement_LUT.pdf)

## Metrics

- **SSIM**
- **PSNR**
- **NIQE** [[code]](https://github.com/csjunxu/Bovik_NIQE_SPL2013)
- **LOE (Lightness Order Error)**
- **VIF (Visual Information Fidelity)** [[Project Page]](https://live.ece.utexas.edu/research/quality/VIF.htm)
- **PI** [[code]](https://github.com/chaoma99/sr-metric)


## Links

- [baidut/BIMEF](https://github.com/baidut/BIMEF)
- [OpenCE](https://github.com/baidut/OpenCE)
- [daooshee/Image-Processing-Datasets](https://github.com/daooshee/Image-Processing-Datasets)
- <https://paperswithcode.com/task/low-light-image-enhancement>
- [dawnlh/low-light-image-enhancement-resources](https://github.com/dawnlh/low-light-image-enhancement-resources)
- [cxtalk/You-Can-See-Clearly-Now](https://github.com/cxtalk/You-Can-See-Clearly-Now)
- [rockeyben/Low-Light](https://github.com/rockeyben/Low-Light)
- [简介近期的一些基于深度学习的图像/视频增强方法](https://zhuanlan.zhihu.com/p/164328373)
- [Low-light Image Analysis by Ke Xu](https://xinyangdut.github.io/enhancement/index.html)
## Applications

- Delta Sampling R-BERT for limited data and low-light action recognition (CVPRW 2021)
  - [[PDF]](https://openaccess.thecvf.com/content/CVPR2021W/UG2/papers/Hira_Delta_Sampling_R-BERT_for_Limited_Data_and_Low-Light_Action_Recognition_CVPRW_2021_paper.pdf)

- DarkLight Networks for Action Recognition in the Dark (CVPRW 2021)
  - [[PDF]](https://openaccess.thecvf.com/content/CVPR2021W/UG2/papers/Chen_DarkLight_Networks_for_Action_Recognition_in_the_Dark_CVPRW_2021_paper.pdf)
