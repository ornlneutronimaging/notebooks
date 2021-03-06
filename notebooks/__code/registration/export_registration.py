import numpy as np
import copy
from qtpy import QtGui
from skimage import transform
from scipy.ndimage.interpolation import shift

from NeuNorm.normalization import Normalization


class ExportRegistration:

    def __init__(self, parent=None, export_folder=''):
        self.parent = parent
        self.export_folder = export_folder

    def run(self):
        data_dict_raw = copy.deepcopy(self.parent.data_dict_raw)
        list_file_names = data_dict_raw['file_name']
        nbr_files = len(data_dict_raw['data'])

        self.parent.eventProgress.setMaximum(nbr_files)
        self.parent.eventProgress.setValue(0)
        self.parent.eventProgress.setVisible(True)

        for _row, _data in enumerate(data_dict_raw['data']):
            _filename = list_file_names[_row]
            if not _row == self.parent.reference_image_index:

                _xoffset = np.int(np.floor(np.float(self.parent.ui.tableWidget.item(_row, 1).text())))
                _yoffset = np.int(np.floor(np.float(self.parent.ui.tableWidget.item(_row, 2).text())))
                _rotation = np.float(self.parent.ui.tableWidget.item(_row, 3).text())

                _data_registered = self.registered_data(raw_data=_data,
                                                        xoffset=_xoffset,
                                                        yoffset=_yoffset,
                                                        rotation=_rotation)
            else:

                _data_registered = _data

            o_norm = Normalization()
            o_norm.load(data=_data_registered)
            # o_norm.data['sample']['metadata'] = [data_dict_raw['metadata'][_row]]
            o_norm.data['sample']['file_name'][0] = _filename
            # pprint.pprint(o_norm.data['sample'])
            # self.parent.testing_o_norm = o_norm

            o_norm.export(folder=self.export_folder, data_type='sample')

            self.parent.eventProgress.setValue(_row+1)
            QtGui.QApplication.processEvents()


        self.parent.eventProgress.setVisible(False)

    def registered_data(self, raw_data=[], xoffset=0, yoffset=0, rotation=0):

        _data = raw_data.copy()
        _data = transform.rotate(_data, rotation)
        _data = shift(_data, (yoffset, xoffset))

        return _data
