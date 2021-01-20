# Image Enhancement

[comment]:<> (Anchor for Back to top)
<a id="head"/>

A list of image enhancement resources collected by [jinwang pan](https://github.com/eeerpjw)

## Low Light Enhancement
Follow the link [low light enhancement](low-light/README.md)


## Contrast Enhancement
- [**SICE**] Learning a Deep Single Image Contrast Enhancer from Multi-Exposure Images (TIP 2018) [[PDF]](http://www4.comp.polyu.edu.hk/~cslzhang/paper/SICE.pdf) [[Caffe code]](https://github.com/csjcai/SICE) [[Dataset]](https://github.com/csjcai/SICE)
- Unpaired Image Enhancement Featuring Reinforcement-Learning-Controlled Image Editing Software (AAAI 2020) [[PDF]](https://arxiv.org/pdf/1912.07833.pdf) [[Python code]](https://github.com/satoshi-kosugi/Unpaired-Image-Enhancement) based on [chainer_spiral](https://github.com/DwangoMediaVillage/chainer_spiral)
- [**DPED**] DSLR-Quality Photos on Mobile Devices with Deep Convolutional Network (ICCV 2017)[[Project page]](https://people.ee.ethz.ch/~ihnatova/)

## Multi-Exposure Fusion
- [**EEMEFN**] EEMEFN: Low-Light Image Enhancement via Edge-Enhanced Multi-Exposure Fusion Network (AAAI 2020) [[Project page]](https://zjuvag.org/publications/eemefn/)


## Tone Mapping

## HDR reconstruction
- Single-Image HDR Reconstruction by Learning to Reverse the Camera Pipeline （CVPR2020）[[Project page]](https://alex04072000.github.io/SingleHDR/) [[TensorFlow code]](https://github.com/alex04072000/SingleHDR) [[Very Large Dataset]](https://alex04072000.github.io/SingleHDR/)

### Multi-image HDR reconstruction

- Recovering High Dynamic Range Radiance Maps from Photographs (SIGGRAPH 1997)
- Burst photography for high dynamic range and low-light imaging on mobile cameras (ACM TOG 2016) [[PDF]](https://people.csail.mit.edu/hasinoff/pubs/HasinoffEtAl16-hdrplus.pdf) [[supp]](http://graphics.stanford.edu/papers/hdrp/hasinoff-hdrplus-sigasia16-supp.pdf)
- Deep Snapshot HDR Imaging Using Multi-Exposure Color Filter Array (ACVV 2020) [[Project page]](http://www.ok.sc.e.titech.ac.jp/res/DSHDR/) [[PDF]](http://www.ok.sc.e.titech.ac.jp/res/DSHDR/data/ACCV2020.pdf) 



### single image HDR reconstruction

- [**UnModNet**] UnModNet: Learning to Unwrap a Modulo Image for High Dynamic Range Imaging (NeurIPS 2020) [[PyTorch code]](https://github.com/fourson/UnModNet)

- [**ExpandNet**] ExpandNet: A Deep Convolutional Neural Network for High Dynamic Range Expansion from Low Dynamic Range Content (CGF 2018) [[PyTorch code]](https://github.com/dmarnerides/hdr-expandnet)

- [**DrTMO**] Deep reverse tone mapping (TOG 2017） [[Project page]](http://www.cgg.cs.tsukuba.ac.jp/~endo/projects/DrTMO/)

- [**HDRCNN**] HDR image reconstruction from a single exposure using deep CNNs (TOG 2017） [[Tensorflow code]](https://github.com/gabrieleilertsen/hdrcnn)

- [**MRF-based**] Unbounded high dynamic range photography using a modulo camera (ICCP 2015 Best Paper) [[Project page]](https://web.media.mit.edu/~hangzhao/modulo.html)

### Tools

[HDR Toolbox for processing High Dynamic Range (HDR) images into MATLAB and Octave](https://github.com/banterle/HDR_Toolbox)

## Underwater Image Enhancement


## Datasets
Follow the link [Datasets](Datasets/README.md)

## Metrics

1. **SSIM**
2. **PSNR**
3. **NIQE** [[code]](https://github.com/csjunxu/Bovik_NIQE_SPL2013)
4. **HDR-VDP** [[code]](http://hdrvdp.sourceforge.net/wiki/)
5. **LOE**
6. **VIF**







## Related Researchers
- [Lei Zhang](http://www4.comp.polyu.edu.hk/~cslzhang/)
  
- [Kede Ma](https://ece.uwaterloo.ca/~k29ma/)
  - MEF 
  - Image Quality Assessment 
- [Wenqi Ren(任文琦)](https://sites.google.com/site/renwenqi888/)
  - low-light, Dehazing, Deraining
  - Underwater image enhancement
- [Chongyi Li(李重仪)](https://li-chongyi.github.io)
  - image and video restoration and enhancement: 1) images and videos captured in adverse weather (hazy, foggy, sandy, dusty, rainy, snowy day), 2) or special circumstances (underwater, weak illumination), 3) general photo enhancement, 4) image/depth super-resolution.
  - Salient object detection: 1) RGB-D salient object detection, 2) remote sensing image salient object detection.

## News


- [HDR+: Low Light and High Dynamic Range photography in the Google Camera App](https://ai.googleblog.com/2014/10/hdr-low-light-and-high-dynamic-range.html) Monday, October 27, 2014
- [Introducing the HDR+ Burst Photography Dataset](https://ai.googleblog.com/2018/02/introducing-hdr-burst-photography.html) Monday, February 12, 2018








<a href="#head">`Back To TOP`</a>