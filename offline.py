import glob
import os
import pickle
from PIL import Image
from feature_extractor import FeatureExtractor

fe = FeatureExtractor()

for img_path in sorted(glob.glob('static/img/*.jpg')):
    try:
        print(img_path)
        img = Image.open(img_path)  # PIL image
        feature = fe.extract(img)
        feature_path = 'static/feature/' + os.path.splitext(os.path.basename(img_path))[0] + '.pkl'
        pickle.dump(feature, open(feature_path, 'wb'))
    except Exception as inst:
        print(img_path)
        print(inst)


