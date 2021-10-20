# FiveK how-to
> author : Jinwang Pan cs_pjw@163.com


FiveK dataset can be downloaded for its official website: 

[https://data.csail.mit.edu/graphics/fivek/](https://data.csail.mit.edu/graphics/fivek/)

The downloaded dataset contains RAW images from different devices. To generate the experts retouched images, you need to download Adobe Lightroom. There is a detailed tutorial from [yuanming-hu/exposure](https://github.com/yuanming-hu/exposure) titled [Preparing data for the MIT Adobe FiveK Dataset with Lightroom](https://github.com/yuanming-hu/exposure/wiki/Preparing-data-for-the-MIT-Adobe-FiveK-Dataset-with-Lightroom)

After generating your own specified dataset. you may need split it into 'training set', 'eval set' and 'test set'. A script is here for script dataset. [split_dataset.py](./split_dataset.py)

To get the minimal image size in the generated images, you can check it with [checksize.py](./checksize.py).

To pre-crop the images for training your model, you can use [cropfivek.py](./cropfivek.py).