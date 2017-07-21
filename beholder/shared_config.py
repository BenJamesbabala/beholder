PLUGIN_NAME = 'beholder'
TAG_NAME = 'beholder-frame'
SUMMARY_FILENAME = 'frame.summary'
CONFIG_FILENAME = 'config.pkl'
SECTION_INFO_FILENAME = 'section-info.pkl'

DEFAULT_CONFIG = {
    'values': 'trainable_variables',
    'mode': 'variance',
    'scaling': 'layer',
    'window_size': 15,
    'FPS': 10,
    'is_recording': False
}

SECTION_HEIGHT = 128
IMAGE_WIDTH = 512 + 256

TB_WHITE = 245
