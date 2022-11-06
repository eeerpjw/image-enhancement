# Dataset

[comment]:<> (Anchor for Back to top)
<a id="head"/>

## Low Light Enhancement

- [**[LOL]**](https://daooshee.github.io/BMVC2018website/) ✅
- [**[LOL-v2]**](https://github.com/flyywh/CVPR-2020-Semi-Low-Light)
- [**[GladNet]**](https://daooshee.github.io/fgworkshop18Gladnet/) ✅
  - 实际上是Adobe Fivek生成的数据
- [**[vip-lowlight]**](https://uwaterloo.ca/vision-image-processing-lab/research-demos/vip-lowlight-dataset) ✅
  - 8 pics
  - .png
  - no-pair
  - low-light denoising

- [**[ReNOIR]**](http://adrianbarburesearch.blogspot.com/p/renoir-dataset.html) ✅
  - 500 pics and 120 scenes
  - 12-bit RAW and aligned
  - no-pair
  - low-light denoising
  - three cameras: Cannon T3i, Cannon S90 and a Xiaomi MI3 mobile phone

- [**[SID]**](http://vladlen.info/publications/learning-see-dark/) ✅
  - The file name contains the image information. For example, in "10019_00_0.033s.RAF", the first digit "1" means it is from the test set ("0" for training set and "2" for validation set); "0019" is the image ID; the following "00" is the number in the sequence/burst; "0.033s" is the exposure time 1/30 seconds.
  - misalignment with the ground-truth for image 10034, 10045, 10172
  - [github](https://github.com/cchen156/Learning-to-See-in-the-Dark)

- [**[ExDark]**](https://github.com/cs-chan/Exclusively-Dark-Image-Dataset) ✅
  - Exclusively Dark (ExDARK) dataset 分类和目标检测

- [**[MIT-Adobe FiveK]**](https://data.csail.mit.edu/graphics/fivek) ✅
  - 5,000 images
  - DNG format
  - Learning Photographic Global Tonal Adjustment with a Database of Input / Output Image Pairs (with ~4% low light images)
  - [[Project Site]](http://people.csail.mit.edu/vladb/photoadjust/)
  - Recommend [Preparing data for the MIT Adobe FiveK Dataset with Lightroom](https://github.com/yuanming-hu/exposure/wiki/Preparing-data-for-the-MIT-Adobe-FiveK-Dataset-with-Lightroom)
- [**[DNIM (Day-Night Matching)]**](http://users.umiacs.umd.edu/~hzhou/dnim.html) ✅
  - There are 17 image sequences containing 1722 images in total with the time stamp for each of these images
  - Evaluating Local Features for Day-Night Matching
  - N. Jacobs, N. Roman and R. Pless. Consistent temporal variations in many outdoor scenes. In: CVPR (2007)
  - H. Zhou, T. Sattler and D. Jacobs. Evaluating Local Features for Day-Night Matching. In: ECCV workshop (2016)

- [**[L3F Dataset]**](https://mohitlamba94.github.io/L3Fnet/) ✅
  - TODO

- [**[Image-Adaptive-3DLUT Dataset]**](https://github.com/HuiZeng/Image-Adaptive-3DLUT)
  - TODO

- [**[AgLLNet Dataset]**](http://www.phi-ai.org/project/AgLLNet/default.htm)
  - Synthetic data

- [**[DarkFace]**](https://flyywh.github.io/CVPRW2019LowLight/)
  - [[Project]](https://flyywh.github.io/CVPRW2019LowLight/)
  - [[eval tools]](https://github.com/Ir1d/DARKFACE_eval_tools)
  - related work [[HLA-Face]](https://github.com/daooshee/HLA-Face-Code)

- [LSRW]
  - R2RNet: Low-light Image Enhancement via Real-low to Real-normal Network
  - <https://github.com/abcdef2000/R2RNet>
  - <https://arxiv.org/abs/2106.14501>
  - download via [[BaiduNetDisk]](https://pan.baidu.com/s/1UxFllrtRSh4E8ir8LdTb9w)(code: wmr1)

- CID
  - 额，还是工大的
  - https://github.com/505030475/ExtremeLowLight


### Datasets for Test

- [**[VV]**](https://sites.google.com/site/vonikakis/datasets/challenging-dataset-for-enhancement) ✅
  - 24 images
  - Busting image enhancement and tone-mapping algorithms: A collection of the most challenging cases

- [**[DICM]**](http://mcl.korea.ac.kr/projects/LDR/LDR_TEST_IMAGES_DICM.zip) ✅
  - 69 images

- [**[LIME]**](https://drive.google.com/open?id=0BwVzAzXoqrSXb3prWUV1YzBjZzg) ✅
  - 10 images
  - [**[Project]**](https://sites.google.com/view/xjguo/lime)

- [**[NPE]**](http://blog.sina.com.cn/s/blog_a0a06f190101cvon.html) ✅
  - 84 images
  - The download link maybe unavaliable. Thanks to [baidut/BIMEF](https://github.com/baidut/BIMEF). The dataset can be found in the google drive link [[BIMEF folder]](https://drive.google.com/drive/folders/0B_FjaR958nw_djVQanJqeEhUM1k) （datasets_NPE-ex1.zip、datasets_NPE-ex2.zip、datasets_NPE-ex3.zip）

- [**[MEF]**](http://ivc.uwaterloo.ca/database/MEF/MEF-Database.php) ✅

- [[LoLi-Phone]](https://drive.google.com/file/d/1QS4FgT5aTQNYy-eHZ_A89rLoZgx_iysR/view)
  - [Low-Light Image and Video Enhancement Using Deep Learning: A Survey](https://github.com/Li-Chongyi/Lighting-the-Darkness-in-the-Deep-Learning-Era-Open)
  - [[Platform] Lighting the Darkness in the Deep Learning Era](http://mc.nankai.edu.cn/ll/)
  - [[Project]](https://github.com/Li-Chongyi/Lighting-the-Darkness-in-the-Deep-Learning-Era-Open/)
  - [[Dataset] LoLi-Phone (3.4G)](https://drive.google.com/file/d/1QS4FgT5aTQNYy-eHZ_A89rLoZgx_iysR/view)
  - [[Chongyi Li(李重仪)]](https://li-chongyi.github.io/)
  - the **videos** are taken by various phones' cameras under diverse illumination conditions and scenes

## Multi-exposure Image Dataset

- [**[SICE]**](https://github.com/csjcai/SICE) ✅

## HDR reconstruction

### Single Frame

- [**[SingleHDR]**](https://github.com/alex04072000/SingleHDR) ✅
  - Single-Image HDR Reconstruction by Learning to Reverse the Camera Pipeline (CVPR2020)
  - We collect two HDR image datasets, one with **synthetic** LDR images and the other with **real** LDR images, for training and evaluation.
  - [[Project]](https://alex04072000.github.io/SingleHDR/)

- HDRCNN test set
  - https://weber.itn.liu.se/~gabei62/hdrcnn/

- HDRTV1K
  - "We conduct a dataset using videos with 4K resolutions under HDR10 standard (10-bit, Rec.2020, PQ) and their counterpart SDR versions from Youtube. The dataset consists of a training set with 1235 image pairs and a test set with 117 image pairs. Please refer to the paper for the details on the processing of the dataset. The dataset can be downloaded from [Baidu Netdisk](https://pan.baidu.com/s/1OSLVoBioyen-zjvLmhbe2g) (access code: 6qvu) or [OneDrive](https://uofmacau-my.sharepoint.com/:f:/g/personal/yc17494_umac_mo/EteMb8FVYE5GqILE2mV-1W8B0-S_ynjt2gAgHkDH9LgkMg?e=EnBn3Q) (access code: HDRTVNet). We also provide the original Youtube links of these videos, which can be found in this [file](https://raw.githubusercontent.com/chxy95/HDRTVNet/master/video_links.txt). Note that we cannot provide the download links since we do not have the copyright to distribute." 
  - [[GitHub](https://github.com/chxy95/hdrtvnet)
  - A New Journey from SDRTV to HDRTV (ICCV 2021)
### Multiple Frames

- [**[HDRPS_Raws]**](http://markfairchild.org/HDR.html) ✅
  - [[Dataset 14.3GB]](http://markfairchild.org/files/HDRPS_Raws.zip)

- [**[NTIRE 2021 HDR]**](https://competitions.codalab.org/competitions/28161) ✅
  - The NTIRE 2021 HDR was built for the first challenge on high-dynamic range (HDR) imaging that was part of the New Trends in Image Restoration and Enhancement (NTIRE) workshop, held in conjunction with CVPR 2021. The challenge aims at estimating a HDR image from one or multiple respective low-dynamic range (LDR) observations, which might suffer from under- or over-exposed regions and different sources of noise.
  - The challenge is composed by two tracks: **In Track 1 only a single LDR image is provided as input**, whereas **in Track 2 three differently-exposed LDR images with inter-frame motion are available.** In both tracks, the ultimate goal is to achieve the best objective HDR reconstruction in terms of PSNR with respect to a ground-truth image, evaluated both directly and with a canonical tone mapping operation.
  - ⚠️ The dataset is a subset of images selected from the [HdM HDR dataset](https://hdr-2014.hdm-stuttgart.de/) (captured with a two Alexa Arri cameras with a mirror rig) where the respective LDR triplets are generated by applying a degradation model (e.g. exposure gain, noise addition and quantization, clipping) to three consecutive frames.

- [**[Kalantari SIG17HDR]**](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/) ✅
  - Deep High Dynamic Range Imaging of Dynamic Scenes (SIGGRAPH 2017)
  - [[Project]](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/)
  - [Dataset] [[Test set 405MB]](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/PaperData/SIGGRAPH17_HDR_Testset.zip) [[Training set 1.95GB]](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/PaperData/SIGGRAPH17_HDR_Trainingset.zip)
  - [[MATLAB Caffe Code]](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/PaperData/SIGGRAPH17_HDR_Code_v1.0.zip)

- [**[Deep-Deghosting-HDR]**](https://val.cds.iisc.ac.in/HDR/ICCP19/) ✅
  - A Fast, Scalable, and Reliable Deghosting Method for Extreme Exposure Fusion (ICCP 2019)
  - [[Project page]](https://val.cds.iisc.ac.in/HDR/ICCP19/)
  - [[TensorFlow code]](https://github.com/rajat95/Deep-Deghosting-HDR)
  - [[Training set]](https://www.kaggle.com/dataset/558d6f7da370e99824685b50488d9cb86fef812d31d68b9a64ec751b238978a6) [[Test set]](https://www.kaggle.com/dataset/a9c5c05e9d5bf0de30009eb0714b461867c8e4a7ebc1288d705644827e27501f)

- [**[Sensor-realistic Synthetic Data]**](https://drive.google.com/drive/folders/1Sr2Jth4DT8K7dwviGsMhfDuc1d53XX0Z) ✅
  - Sensor-Realistic Synthetic Data Engine for Multi-Frame High Dynamic Range Photography (CVPRW2020)
  - NTIRE'2O: Sensor-realistic Synthetic Data Engine for Multi-frame High Dynamic Range Photography
  - [[GitHub with no code]](https://github.com/nadir-zeeshan/sensor-realistic-synthetic-data)
  - [[Synthetic Dataset (Google drive)]](https://drive.google.com/drive/folders/1Sr2Jth4DT8K7dwviGsMhfDuc1d53XX0Z)

- [**[Scenes_TOG12]**](https://web.ece.ucsb.edu/~psen/hdrvideo) ✅
  - Robust Patch-Based HDR Reconstruction of Dynamic Scenes (TOG 2012)
  - [[Project]](https://web.ece.ucsb.edu/~psen/hdrvideo)
  - [[MATLAB code]](https://web.ece.ucsb.edu/~psen/HDR_stuff/PatchBasedHDR_MATLAB_v1.1.zip)
  - [[Dataset 394MB]](https://web.ece.ucsb.edu/~psen/HDR_stuff/Scenes.zip)
  - [[Paper]](https://web.ece.ucsb.edu/~psen/Papers/SIGASIA12_HDR_PatchBasedReconstruction_LoRes.pdf)

- An Objective Deghosting Quality Metric for HDR Images ✅
  - [[Project]](https://user.ceng.metu.edu.tr/~akyuz/files/eg2016/index.html)
  - [[dataset]](https://user.ceng.metu.edu.tr/~akyuz/files/eg2016/summary/index.html)  [[download]](https://user.ceng.metu.edu.tr/~akyuz/files/eg2016/files/dataset.zip)
  - [[code]](https://user.ceng.metu.edu.tr/~akyuz/files/eg2016/files/dqm_v2.tar.gz)
- The Laval Indoor HDR Dataset
  - This dataset contains 2100+ high resolution indoor panoramas, captured using a Canon 5D Mark III and a robotic panoramic tripod head. Each capture was multi-exposed (22 f-stops) and is fully HDR, without any saturation. Panoramas were stitched from 6 captures (60 degrees azimuth increment) and were captured in a wide variety of indoor environments.
  - [[Project]](http://indoor.hdrdb.com/#)
  - [[Paper]](http://vision.gel.ulaval.ca/~jflalonde/publications/projects/deepIndoorLight/index.html)


### Video

- High Speed and HDR Datasets
  - High Speed and High Dynamic Range Video with an Event Camera (TPAMI 2019)
  - [[Project]](http://rpg.ifi.uzh.ch/E2VID.html)
  - [[PyTorch code]](https://github.com/uzh-rpg/rpg_e2vid)
  - [[Paper]](http://rpg.ifi.uzh.ch/docs/TPAMI19_Rebecq.pdf)
  - [[Dataset]](http://rpg.ifi.uzh.ch/E2VID.html)

% TODO

- <https://github.com/guanyingc/DeepHDRVideo-Dataset>

## RAW Dataset

- [Zurich RAW to RGB Dataset](http://people.ee.ethz.ch/~ihnatova/pynet.html)
  - To get real data for RAW to RGB mapping problem, a large-scale dataset consisting of 20 thousand photos was collected using Huawei P20 smartphone capturing RAW photos (plus the resulting RGB images obtained with Huawei's built-in ISP), and a professional high-end Canon 5D Mark IV camera with Canon EF 24mm f/1.4L fast lens. RAW data was read from P20's 12.3 MP Sony Exmor IMX380 Bayer camera sensor - though this phone has a second 20 MP monochrome camera, it is only used by Huawei's internal ISP system, and the corresponding images cannot be retrieved with any public camera API. The photos were captured in automatic mode, and default settings were used throughout the whole collection procedure. The data was collected over several weeks in a variety of places and in various illumination and weather conditions.
  - Since the captured RAW-RGB image pairs are not perfectly aligned, they were first aligned globally using SIFT keypoints and RANSAC algorithm. Then, smaller patches of size 448×448 were extracted from the preliminary matched images using a non-overlapping sliding window. Two windows were moving in parallel along the two images from each RAW-RGB pair, and the position of the window on DSLR image was additionally adjusted with small shifts and rotations to maximize the cross-correlation between the observed patches. Patches with cross-correlation less than 0.9 were not included into the dataset to avoid large displacements. This procedure resulted in 48043 RAW-RGB image pairs (of size 448×448×1 and 448×448×3, respectively) that were later used for training, validation and testing the models. RAW image patches were additionally reshaped into the size of 224×224×4, where the four channels correspond to the four colors of the RGBG Bayer filer

- [**[RAISE]**](http://loki.disi.unitn.it/RAISE/)
  - Test only /without GT
  - RAISE is a challenging real-world image dataset, primarily designed for the evaluation of digital forgery detection algorithms. **It consists of 8156 high-resolution RAW images, uncompressed and guaranteed to be camera-native** (i.e., never touched or processed). All the images have been collected from 4 photographers over a period of 3 years (2011- 2014), capturing different scenes and moments in over 80 places in Europe employing 3 different cameras.
  - File, File Size, Image Size, Image Quality (For example, Lossless Compressed RAW (14-bit)), Device, Focal Length, Aperture, and Shutter Speed are provided.
  - [[Project]](http://loki.disi.unitn.it/RAISE/)
  - [[Download]](http://loki.disi.unitn.it/RAISE/download.html)
  - I write a python script [downloadRAISE.py](./RAISE/downloadRAISE.py) to download the dataset.

### Datasets that not explored

- [**[HdM HDR]**](https://www.hdm-stuttgart.de/vmlab/hdm-hdr-2014)
  - Reconstructed scene radiance in ALEXA-Wide-Gamut color space (80GB OpenEXR files)
  - All clips color graded for Rec.2020 primaries and 0.005-4000cd/m2 luminance (189GB TIFF files)

- HDR-EYE
  - https://www.epfl.ch/labs/mmspg/downloads/hdr-eye/
- [**[HDR+]**](http://www.hdrplusdata.org)
  - Curated subset (153 images)
  - Part 1 (2000 images)
  - Part 2 (1640 images)
  - <http://www.hdrplusdata.org/dataset.html>

- <https://www2.cs.sfu.ca/~colour/data/funt_hdr/>
- <http://www.hdrlabs.com/sibl/archive.html>

## Paper with code datasets

<https://paperswithcode.com/datasets>

<a href="#head">`Back To TOP`</a>
