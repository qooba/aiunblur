from fastai.basic_train import load_learner
from fastai.vision.image import open_image, Image
import torchvision.transforms as tfms
import __mp_main__

class FeatureLoss: ...

__mp_main__.FeatureLoss=FeatureLoss

class UnblurService:
    def __init__(self):
        self.learn=load_learner('/models','unblur.pkl')

    def process(self, image):
        img = open_image(image)
        crop_size = max(img.size)
        uncrop_left, uncrop_top, uncrop_right, uncrop_bottom = (0,0,0,0)

        o_h,o_w = img.size
        print(o_w,o_h)
        if o_w > o_h:
            # TRAGET 256x256 !!!! TODO
            uncrop_top=int((o_w-o_h)*0.5*256/crop_size)
            uncrop_bottom=int(256-uncrop_top)
            uncrop_right=256
        else:
            uncrop_left=int((o_h-o_w)*0.5*256/crop_size)+1
            uncrop_right=int(256-uncrop_left)-1
            uncrop_bottom=256

        print(uncrop_left,uncrop_top,uncrop_right,uncrop_bottom)
        img=img.crop_pad((crop_size,crop_size), padding_mode='zeros')
        p,img_hr,b = self.learn.predict(img)
        print(img_hr.size)
        return tfms.ToPILImage()(img_hr.data).convert("RGB").crop((uncrop_left, uncrop_top, uncrop_right, uncrop_bottom))
