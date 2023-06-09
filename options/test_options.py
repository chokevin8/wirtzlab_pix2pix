from .base_options import BaseOptions


class TestOptions(BaseOptions):
    """This class includes test_pix2pix options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)  # define shared options
        parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
        parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
        parser.add_argument('--phase', type=str, default='test_pix2pix', help='train, val, test_pix2pix, etc')
        # Dropout and Batchnorm has different behavioir during training and test_pix2pix.
        parser.add_argument('--eval', action='store_true', help='use eval mode during test_pix2pix time.')
        parser.add_argument('--num_test', type=int, default=50, help='how many test_pix2pix images to run')
        # rewrite devalue values
        parser.set_defaults(model='test_pix2pix')
        # To avoid cropping, the load_size should be the same as crop_size
        parser.set_defaults(load_size=parser.get_default('crop_size'))
        self.isTrain = False
        return parser
