from pathlib import Path
from qtpy.QtWidgets import QFileDialog
import numpy as np
from collections import OrderedDict

from __code.file_handler import make_ascii_file, read_bragg_edge_fitting_ascii_format


class ImportHandler:

	def __init__(self, parent=None):
		self.parent = parent

	def run(self):
		working_dir = str(Path(self.parent.working_dir).parent)
		ascii_file = QFileDialog.getOpenFileName(self.parent,
		                                         caption="Select ASCII file",
		                                         directory=working_dir,
		                                         filter="ASCII (*.txt)")

		if ascii_file[0]:
			self.parent.full_reset_of_ui()
			self.parent.block_table_ui(True)

			self.parent.is_file_imported = True
			result_of_import = read_bragg_edge_fitting_ascii_format(full_file_name=str(ascii_file[0]))
			self.parent.bragg_edge_range = result_of_import['metadata']['bragg_edge_range']
			self.parent.ui.distance_detector_sample.setText(result_of_import['metadata']['distance_detector_sample'])
			self.parent.ui.detector_offset.setText(result_of_import['metadata']['detector_offset'])
			self.create_fitting_input_dictionary_from_imported_ascii_file(result_of_import)
			self.parent.tof_array_s = self.parent.fitting_input_dictionary['xaxis']['tof'][0] * 1e-6
			self.parent.lambda_array = self.parent.fitting_input_dictionary['xaxis']['lambda'][0]
			self.parent.index_array = self.parent.fitting_input_dictionary['xaxis']['index'][0]

			self.parent.ui.statusbar.showMessage("{} has been imported!".format(ascii_file), 10000)  # 10s
			self.parent.ui.statusbar.setStyleSheet("color: green")

			self.parent.disable_left_part_of_selection_tab()
			self.parent.ui.info_message_about_cyan.setVisible(False)
			self.parent.update_profile_of_bin_slider_widget()
			self.parent.update_selection_plot()
			self.parent.update_vertical_line_in_profile_plot()

			self.parent.ui.tabWidget.setTabEnabled(1, self.parent.is_fit_infos_loaded())
			self.parent.ui.tabWidget.setEnabled(True)
			self.parent.ui.actionExport.setEnabled(True)

			if result_of_import.get('metadata').get('fitting_procedure_started', False):
				self.parent.fit_that_selection_pushed_by_program(initialize_region=False)

			self.parent.block_table_ui(False)
			self.parent.update_fitting_plot()

	def create_fitting_input_dictionary_from_imported_ascii_file(self, result_of_import):
		self.parent.fitting_input_dictionary = {}

		metadata = result_of_import['metadata']
		self.parent.working_dir = metadata['base_folder']
		self.parent.bragg_edge_range = metadata['bragg_edge_range']

		columns_roi = metadata['columns']

		data = result_of_import['data']
		tof_array = np.array(data['tof'])
		# self.tof_array = tof_array
		index_array = np.array(data['index'])
		lambda_array = np.array(data['lambda'])
		rois_dictionary = OrderedDict()
		for col in np.arange(3, len(columns_roi) + 3):
			str_col = str(col)
			rois_dictionary[col - 3] = {'profile': np.array(data[str_col]),
			                            'x0'     : columns_roi[str_col]['x0'],
			                            'y0'     : columns_roi[str_col]['y0'],
			                            'width'  : columns_roi[str_col]['width'],
			                            'height' : columns_roi[str_col]['height'],
			                            }
		xaxis_dictionary = {'index' : (index_array, self.parent.xaxis_label['index']),
		                    'lambda': (lambda_array, self.parent.xaxis_label['lambda']),
		                    'tof'   : (tof_array, self.parent.xaxis_label['tof'])}
		self.parent.fitting_input_dictionary = {'xaxis': xaxis_dictionary,
		                                        'rois' : rois_dictionary}

		self.parent.kropff_fitting_range['high'] = metadata['kropff_high']
		self.parent.kropff_fitting_range['low'] = metadata['kropff_low']
		self.parent.kropff_fitting_range['bragg_peak'] = metadata['kropff_bragg_peak']
