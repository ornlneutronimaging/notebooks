import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from qtpy.QtWidgets import QVBoxLayout, QProgressBar

from __code.panoramic_stitching.mplcanvas import MplCanvas
from __code._utilities.parent import Parent
from __code.wave_front_dynamics import MAX_BIN_SIZE


class Initialization(Parent):

    def all(self):
        self.widgets()
        self.matplotlib()
        self.statusbar()

    def widgets(self):
        self.parent.ui.file_index_horizontalSlider.setMaximum(self.parent.nbr_files)
        self.parent.ui.file_index_value_label.setText(str(0))

        self.parent.ui.bin_value_horizontalSlider.setMinimum(1)
        self.parent.ui.bin_value_horizontalSlider.setMaximum(MAX_BIN_SIZE)

        self.parent.ui.recap_edges_widget.setEnabled(False)
        self.parent.ui.calculated_edges_widget.setEnabled(False)

        self.parent.ui.edge_calculation_file_index_slider.setMaximum(self.parent.nbr_files)

    def matplotlib(self):

        def _matplotlib(parent=None, widget=None):
            sc = MplCanvas(parent, width=5, height=4, dpi=100)
            toolbar = NavigationToolbar(sc, parent)
            layout = QVBoxLayout()
            layout.addWidget(toolbar)
            layout.addWidget(sc)
            widget.setLayout(layout)
            return sc

        self.parent.prepare_data_plot = _matplotlib(parent=self.parent,
                                                    widget=self.parent.ui.prepare_data_widget)
        self.parent.recap_edges_plot = _matplotlib(parent=self.parent,
                                                   widget=self.parent.ui.recap_edges_widget)
        self.parent.calculated_edges_plot = _matplotlib(parent=self.parent,
                                                        widget=self.parent.ui.calculated_edges_widget)

    def statusbar(self):
        self.parent.event_progress = QProgressBar(self.parent.ui.statusbar)
        self.parent.event_progress.setMinimumSize(20, 14)
        self.parent.event_progress.setMaximumSize(540, 100)
        self.parent.event_progress.setVisible(False)
        self.parent.ui.statusbar.addPermanentWidget(self.parent.event_progress)
