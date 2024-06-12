from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class xBD(BaseSegDataset):

    METAINFO = dict(
        classes=('no_dmg', 'minor_dmg', 'major_dmg', 'destroyed'),
        palette=[[128, 64, 128], [244, 35, 232], [70, 70, 70], [102, 102, 156]])

    def __init__(self, img_suffix='.png', seg_map_suffix='.png', **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)