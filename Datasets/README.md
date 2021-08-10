# Dataset
[comment]:<> (Anchor for Back to top)
<a id="head"/>

## Paper with code datasets
https://paperswithcode.com/datasets

## Low Light Enhancement
- [[LOL]](https://daooshee.github.io/BMVC2018website/)

- [[SICE]](https://github.com/csjcai/SICE)

- [[GladNet]](https://daooshee.github.io/fgworkshop18Gladnet/)

- [[vip-lowlight]](https://uwaterloo.ca/vision-image-processing-lab/research-demos/vip-lowlight-dataset)
    - 8 pics
    - .png
    - no-pair
    - low-light denoising

- [[ReNOIR]](http://adrianbarburesearch.blogspot.com/p/renoir-dataset.html)
    - 500 pics and 120 scenes
    - 12-bit RAW and aligned
    - no-pair
    - low-light denoising
    - three cameras: Cannon T3i, Cannon S90 and a Xiaomi MI3 mobile phone

- [[SID]](http://vladlen.info/publications/learning-see-dark/)
    - The file name contains the image information. For example, in "10019_00_0.033s.RAF", the first digit "1" means it is from the test set ("0" for training set and "2" for validation set); "0019" is the image ID; the following "00" is the number in the sequence/burst; "0.033s" is the exposure time 1/30 seconds.
    - misalignment with the ground-truth for image 10034, 10045, 10172
    - [github](https://github.com/cchen156/Learning-to-See-in-the-Dark)

- [[ExDark]](https://github.com/cs-chan/Exclusively-Dark-Image-Dataset)
    - Exclusively Dark (ExDARK) dataset 分类和目标检测

- [[MIT-Adobe FiveK]](https://data.csail.mit.edu/graphics/fivek)
    - 5,000 images
    - DNG format
    - Learning Photographic Global Tonal Adjustment with a Database of Input / Output Image Pairs (with ~4% low light images)
    - [[Project Site]](http://people.csail.mit.edu/vladb/photoadjust/)
-[[DNIM (Day-Night Matching)]](http://users.umiacs.umd.edu/~hzhou/dnim.html)
    - There are 17 image sequences containing 1722 images in total with the time stamp for each of these images
    - Evaluating Local Features for Day-Night Matching
    - N. Jacobs, N. Roman and R. Pless. Consistent temporal variations in many outdoor scenes. In: CVPR (2007)
    - H. Zhou, T. Sattler and D. Jacobs. Evaluating Local Features for Day-Night Matching. In: ECCV workshop (2016)

- [[L3F Dataset]](https://mohitlamba94.github.io/L3Fnet/)
    - TODO 

- [[Image-Adaptive-3DLUT Dataset]](https://github.com/HuiZeng/Image-Adaptive-3DLUT)
    - TODO

- [AgLLNet Dataset](http://www.phi-ai.org/project/AgLLNet/default.htm)
    - Synthetic data

### Datasets for Test
- [[VV]](https://sites.google.com/site/vonikakis/datasets/challenging-dataset-for-enhancement)
    - 24 images
    - Busting image enhancement and tone-mapping algorithms: A collection of the most challenging cases

- [[DICM]](http://mcl.korea.ac.kr/projects/LDR/LDR_TEST_IMAGES_DICM.zip)
    - 69 images

- [[LIME]](https://drive.google.com/open?id=0BwVzAzXoqrSXb3prWUV1YzBjZzg)
    - 10 images
    - [[project page]](https://sites.google.com/view/xjguo/lime)

- [[NPE]](http://blog.sina.com.cn/s/blog_a0a06f190101cvon.html)
    - 84 images
    - The download link maybe unavaliable. Thanks to [baidut/BIMEF](https://github.com/baidut/BIMEF). The dataset can be found in the google drive link [[BIMEF folder]](https://drive.google.com/drive/folders/0B_FjaR958nw_djVQanJqeEhUM1k) （datasets_NPE-ex1.zip、datasets_NPE-ex2.zip、datasets_NPE-ex3.zip）

- [[MEF]](http://ivc.uwaterloo.ca/database/MEF/MEF-Database.php)



## Contrast Enhancement
- [[Contrast Enhancement based on Layered Difference Representation of 2D Histograms]](http://mcl.korea.ac.kr/projects/LDR/)
    - 500 from [Berkeley Segmentation Data Set and Benchmarks 500 (BSDS500)](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html#bsds500)
    - 24 from [Kodak Lossless True Color Image Suite](http://r0k.us/graphics/kodak/)
    - 7 of 4.2.0x from [The USCI-SIPI Image Database, Volume 3: Miscellaneous](http://sipi.usc.edu/database/database.php?volume=misc)
    - 69 captured images from commercial digital cameras: [DICM(15.3MB)](http://mcl.korea.ac.kr/projects/LDR/LDR_TEST_IMAGES_DICM.zip)
    - 4 synthetic images: [Download (445 kB)](http://mcl.korea.ac.kr/projects/LDR/LDR_TEST_IMAGES_SYNTHETIC.zip)


## Multi-exposure Image Dataset
- [[SICE]](https://github.com/csjcai/SICE)


## HDR reconstruction
### Single Frame

- [[NTIRE 2021 HDR]](https://competitions.codalab.org/competitions/28161)
    - The NTIRE 2021 HDR was built for the first challenge on high-dynamic range (HDR) imaging that was part of the New Trends in Image Restoration and Enhancement (NTIRE) workshop, held in conjunction with CVPR 2021. The challenge aims at estimating a HDR image from one or multiple respective low-dynamic range (LDR) observations, which might suffer from under- or over-exposed regions and different sources of noise. The challenge is composed by two tracks: In Track 1 only a single LDR image is provided as input, whereas in Track 2 three differently-exposed LDR images with inter-frame motion are available. In both tracks, the ultimate goal is to achieve the best objective HDR reconstruction in terms of PSNR with respect to a ground-truth image, evaluated both directly and with a canonical tone mapping operation.

- [[SingleHDR]](https://github.com/alex04072000/SingleHDR)
    - Single-Image HDR Reconstruction by Learning to Reverse the Camera Pipeline （CVPR2020）
    - [[Project]](https://alex04072000.github.io/SingleHDR/)



###  Multiple Frames
- [[NTIRE 2021 HDR]](https://competitions.codalab.org/competitions/28161)
    - The NTIRE 2021 HDR was built for the first challenge on high-dynamic range (HDR) imaging that was part of the New Trends in Image Restoration and Enhancement (NTIRE) workshop, held in conjunction with CVPR 2021. The challenge aims at estimating a HDR image from one or multiple respective low-dynamic range (LDR) observations, which might suffer from under- or over-exposed regions and different sources of noise. The challenge is composed by two tracks: In Track 1 only a single LDR image is provided as input, whereas in Track 2 three differently-exposed LDR images with inter-frame motion are available. In both tracks, the ultimate goal is to achieve the best objective HDR reconstruction in terms of PSNR with respect to a ground-truth image, evaluated both directly and with a canonical tone mapping operation.

- [[Kalantari SIG17HDR]](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/)
    - Deep High Dynamic Range Imaging of Dynamic Scenes (SIGGRAPH 2017) 
    - [[Project]](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/)
    - [Dataset] [[Test set 405MB]](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/PaperData/SIGGRAPH17_HDR_Testset.zip) [[Training set 1.95GB]](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/PaperData/SIGGRAPH17_HDR_Trainingset.zip)
    - [[MATLAB Caffe Code]](https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/PaperData/SIGGRAPH17_HDR_Code_v1.0.zip)

- [[Deep-Deghosting-HDR]](https://val.cds.iisc.ac.in/HDR/ICCP19/)
    - A Fast, Scalable, and Reliable Deghosting Method for Extreme Exposure Fusion (ICCP 2019)
    - [[Project page]](https://val.cds.iisc.ac.in/HDR/ICCP19/)
    - [[TensorFlow code]](https://github.com/rajat95/Deep-Deghosting-HDR)
    - [[Training set]](https://www.kaggle.com/dataset/558d6f7da370e99824685b50488d9cb86fef812d31d68b9a64ec751b238978a6) [[Test set]](https://www.kaggle.com/dataset/a9c5c05e9d5bf0de30009eb0714b461867c8e4a7ebc1288d705644827e27501f)

- Sensor-Realistic Synthetic Data Engine for Multi-Frame High Dynamic Range Photography (CVPRW2020)
    - NTIRE'2O: Sensor-realistic Synthetic Data Engine for Multi-frame High Dynamic Range Photography
    - [[GitHub with no code]](https://github.com/nadir-zeeshan/sensor-realistic-synthetic-data)
    - [[synthetic Dataset]](https://drive.google.com/drive/folders/1Sr2Jth4DT8K7dwviGsMhfDuc1d53XX0Z)

### Video
- High Speed and HDR Datasets
    - High Speed and High Dynamic Range Video with an Event Camera (TPAMI 2019)
    - [[Project]](http://rpg.ifi.uzh.ch/E2VID.html)
    - [[PyTorch code]](https://github.com/uzh-rpg/rpg_e2vid)
    - [[Paper]](http://rpg.ifi.uzh.ch/docs/TPAMI19_Rebecq.pdf)
    - [[Dataset]](http://rpg.ifi.uzh.ch/E2VID.html)

### Datasets that not explored
- [[HdM HDR]](https://www.hdm-stuttgart.de/vmlab/hdm-hdr-2014)
    - Reconstructed scene radiance in ALEXA-Wide-Gamut color space (80GB OpenEXR files)
    - All clips color graded for Rec.2020 primaries and 0.005-4000cd/m2 luminance (189GB TIFF files)
    - 德国的FTP服务器，下不下来

- [[HDR+]](http://www.hdrplusdata.org)
    - Curated subset (153 images)
    - Part 1 (2000 images)
    - Part 2 (1640 images)
    - http://www.hdrplusdata.org/dataset.html




## Underwater Image Enhancement








<a href="#head">`Back To TOP`</a>

