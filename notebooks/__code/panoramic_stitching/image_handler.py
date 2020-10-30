import numpy as np
from qtpy import QtGui
import pyqtgraph as pg

from __code._utilities.table_handler import TableHandler
from __code.panoramic_stitching.get import Get

COLOR_LOCK = QtGui.QColor(62, 13, 244, 100)
COLOR_UNLOCK = QtGui.QColor(255, 0, 0, 100)
COLOR_LINE_SEGMENT = QtGui.QColor(255, 0, 255)
LINE_SEGMENT_FONT = QtGui.QFont("Arial", 15)


class ImageHandler:

    def __init__(self, parent=None):
        self.parent = parent

    def update_contour_plot(self):
        if self.parent.contour_image_roi_id:
            self.parent.ui.image_view.removeItem(self.parent.contour_image_roi_id)

        o_table = TableHandler(table_ui=self.parent.ui.tableWidget)
        row_selected = o_table.get_row_selected()
        name_of_file_selected = o_table.get_item_str_from_cell(row=row_selected, column=0)

        o_get = Get(parent=self.parent)
        folder_selected = o_get.get_combobox_folder_selected()
        offset_dictionary = self.parent.offset_dictionary[folder_selected]

        roi = {'x0': offset_dictionary[name_of_file_selected]['xoffset'],
               'y0': offset_dictionary[name_of_file_selected]['yoffset']}

        if row_selected == 0:
            _color = COLOR_LOCK
        else:
            _color = COLOR_UNLOCK

        if roi:
            _pen = QtGui.QPen()
            _pen.setColor(_color)
            _pen.setWidthF(0.01)
            _roi_id = pg.ROI([roi['x0'], roi['y0']],
                             [self.parent.image_width, self.parent.image_height],
                             pen=_pen, scaleSnap=True,
                             movable=False)
            self.parent.ui.image_view.addItem(_roi_id)
            self.parent.contour_image_roi_id = _roi_id

    def update_current_panoramic_image(self):

        _view = self.parent.ui.image_view.getView()
        _view_box = _view.getViewBox()
        _state = _view_box.getState()

        first_update = False
        if self.parent.histogram_level is None:
            first_update = True
        _histo_widget = self.parent.ui.image_view.getHistogramWidget()
        self.parent.histogram_level = _histo_widget.getLevels()

        o_get = Get(parent=self.parent)
        folder_selected = o_get.get_combobox_folder_selected()

        data_dictionary = self.parent.data_dictionary[folder_selected]
        offset_dictionary = self.parent.offset_dictionary[folder_selected]

        max_yoffset, max_xoffset = self.get_max_offset(folder_selected=folder_selected)

        image_height = self.parent.image_height
        image_width = self.parent.image_width

        _color = None

        panoramic_image = None
        for _file_index, _file in enumerate(data_dictionary.keys()):

            if _file_index == 0:
                panoramic_image = np.zeros((max_yoffset + image_height, max_xoffset + image_width))

            _image = data_dictionary[_file].data
            is_visible = offset_dictionary[_file]['visible']
            if not is_visible:
                continue

            if _file_index == 0:
                panoramic_image[0:image_height, 0:image_width] = _image
            else:
                xoffset = offset_dictionary[_file]['xoffset']
                yoffset = offset_dictionary[_file]['yoffset']

                panoramic_image[yoffset: yoffset+image_height, xoffset: xoffset+image_width] = _image

        self.parent.panoramic_images[folder_selected] = panoramic_image

        _image = np.transpose(panoramic_image)
        # _image = self._clean_image(_image)
        self.parent.ui.image_view.setImage(_image)
        self.parent.current_live_image = _image
        _view_box.setState(_state)

        if not first_update:
            _histo_widget.setLevels(self.parent.histogram_level[0],
                                    self.parent.histogram_level[1])

    def get_max_offset(self, folder_selected=None):
        offset_dictionary = self.parent.offset_dictionary[folder_selected]

        list_xoffset = [offset_dictionary[_key]['xoffset'] for _key in offset_dictionary.keys()]
        list_yoffset = [offset_dictionary[_key]['yoffset'] for _key in offset_dictionary.keys()]

        return np.int(np.max(list_yoffset)), np.int(np.max(list_xoffset))

    def update_from_to_roi(self, state=False):

        if state:
            from_to_roi = self.parent.from_to_roi
            x0 = from_to_roi['x0']
            y0 = from_to_roi['y0']
            x1 = from_to_roi['x1']
            y1 = from_to_roi['y1']
            _pen = QtGui.QPen()
            _pen.setColor(COLOR_LINE_SEGMENT)
            _pen.setWidthF(1)
            _line_segment = pg.LineSegmentROI(positions=[[x0, y0], [x1, y1]],
                                              pen=_pen,
                                              )
            self.parent.ui.image_view.addItem(_line_segment)
            self.parent.from_to_roi_id = _line_segment
            _line_segment.sigRegionChanged.connect(self.parent.from_to_line_segment_changed)

            _text_from = pg.TextItem(text="from")
            _text_from.setPos(x0, y0)
            _text_from.setFont(LINE_SEGMENT_FONT)
            self.parent.from_label_id = _text_from

            _text_to = pg.TextItem(text="to")
            _text_to.setPos(x1, y1)
            _text_to.setFont(LINE_SEGMENT_FONT)
            self.parent.to_label_id = _text_to

            self.parent.ui.image_view.addItem(_text_from)
            self.parent.ui.image_view.addItem(_text_to)

        else:
            if self.parent.from_to_roi_id:
                if self.parent.contour_image_roi_id:
                    self.parent.ui.image_view.removeItem(self.parent.from_to_roi_id)

    def update_from_to_line_label_changed(self):
        from_to_roi = self.parent.from_to_roi
        x0 = from_to_roi['x0']
        y0 = from_to_roi['y0']
        x1 = from_to_roi['x1']
        y1 = from_to_roi['y1']

        self.parent.from_label_id.setPos(x1, y1)
        self.parent.to_label_id.setPos(x0, y0)
