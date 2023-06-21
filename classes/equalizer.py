import tensorflow as tf
import cv2
import numpy as np

class HistogramEqualizer:
    def __init__(self, mode='grayscale'):
        self.mode = mode

    @tf.function
    def equalize(self, image):
        def scale_channel(im, c):
            im = tf.cast(im[..., c], tf.int32)
            histo = tf.histogram_fixed_width(im, [0, 255], nbins=256)

            nonzero = tf.where(tf.not_equal(histo, 0))
            nonzero_histo = tf.reshape(tf.gather(histo, nonzero), [-1])
            step = (tf.reduce_sum(nonzero_histo) - nonzero_histo[-1]) // 255

            def build_lut(histo, step):
                lut = (tf.cumsum(histo) + (step // 2)) // step
                lut = tf.concat([[0], lut[:-1]], 0)
                return tf.clip_by_value(lut, 0, 255)

            result = tf.cond(
                tf.equal(step, 0), lambda: im,
                lambda: tf.gather(build_lut(histo, step), im))
            return tf.cast(result, tf.uint8)

        if self.mode == 'grayscale':
            image = scale_channel(image, 0)
            return tf.cast(image, tf.float32)
        elif self.mode == 'rgb':
            s1 = scale_channel(image, 0)
            s2 = scale_channel(image, 1)
            s3 = scale_channel(image, 2)
            image = tf.stack([s1, s2, s3], -1)
            return tf.cast(image, tf.float32)

    def process_image(self, img_path):
        # Read the image, equalize and return
        img = cv2.imdecode(np.fromstring(img_path.read(), np.uint8), cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        enhanced_img = self.equalize(img)
        return enhanced_img
