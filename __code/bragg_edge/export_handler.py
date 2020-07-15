from pathlib import Path
from qtpy.QtWidgets import QFileDialog
import numpy as np

from __code.bragg_edge.get import Get
from __code.file_handler import make_ascii_file
from __code.bragg_edge.bragg_edge_peak_fitting_gui_utility import GuiUtility


class ExportHandler:

	def __init__(self, parent=None):
		self.parent = parent

	def configuration(self):
		# bring file dialog to locate where the file will be saved
		base_folder = Path(self.parent.working_dir)
		directory = str(base_folder.parent)
		_export_folder = QFileDialog.getExistingDirectory(self.parent,
		                                                  directory=directory,
		                                                  caption="Select Output Folder",
		                                                  options=QFileDialog.ShowDirsOnly)

		if _export_folder:
			data, metadata = self.get_data_metadata_from_selection_tab()

			# collect initial selection size (x0, y0, width, height)
			o_get = Get(parent=self.parent)
			[x0, y0, x1, y1, width, height] = o_get.selection_roi_dimension()

			name_of_ascii_file = ExportHandler.makeup_name_of_profile_ascii_file(base_name=str(base_folder.name),
			                                                                     export_folder=_export_folder,
			                                                                     x0=x0, y0=y0,
			                                                                     width=width,
			                                                                     height=height)

			make_ascii_file(metadata=metadata,
			                data=data,
			                output_file_name=name_of_ascii_file,
			                dim='1d')

			self.parent.ui.statusbar.showMessage("{} has been created!".format(name_of_ascii_file), 10000)  # 10s
			self.parent.ui.statusbar.setStyleSheet("color: green")

	@staticmethod
	def makeup_name_of_profile_ascii_file(base_name="default",
	                                      export_folder="./",
	                                      x0=None, y0=None, width=None, height=None):
		"""this will return the full path name of the ascii file to create that will contain all the profiles
		starting with the selection box and all the way to the minimal size"""
		full_base_name = "full_set_of_shrinkable_region_profiles_from_" + \
		                 "x{}_y{}_w{}_h{}_for_folder_{}.txt".format(x0, y0, width, height, base_name)
		return str(Path(export_folder) / full_base_name)

	def get_data_metadata_from_selection_tab(self):
		base_folder = Path(self.parent.working_dir)
		o_get = Get(parent=self.parent)

		index_axis, _ = o_get.specified_x_axis(xaxis='index')
		tof_axis, _ = o_get.specified_x_axis(xaxis='tof')
		lambda_axis, _ = o_get.specified_x_axis('lambda')
		fitting_peak_range = self.parent.bragg_edge_range
		distance_detector_sample = str(self.parent.ui.distance_detector_sample.text())
		detector_offset = str(self.parent.ui.detector_offset.text())

		dict_regions = o_get.all_russian_doll_region_full_infos()
		metadata = ExportHandler.make_metadata(base_folder=base_folder,
		                                       fitting_peak_range=fitting_peak_range,
		                                       dict_regions=dict_regions,
		                                       distance_detector_sample=distance_detector_sample,
		                                       detector_offset=detector_offset)
		self.add_fitting_infos_to_metadata(metadata)

		metadata.append("#")
		metadata.append("#File Index, TOF(micros), lambda(Angstroms), ROIs (see above)")
		data = ExportHandler.format_data(col1=index_axis,
		                                 col2=tof_axis,
		                                 col3=lambda_axis,
		                                 dict_regions=dict_regions)

		return data, metadata

	def add_fitting_infos_to_metadata(self, metadata):
		o_tab = GuiUtility(parent=self.parent)
		fitting_algorithm_used = o_tab.get_tab_selected(tab_ui=self.parent.ui.tab_algorithm)
		# fitting_rois = self.fitting_rois
		fitting_flag = True if self.parent.fitting_peak_ui else False
		metadata.append("#fitting procedure started: {}".format(fitting_flag))
		metadata.append("#fitting algorithm selected: {}".format(fitting_algorithm_used))
		# kropff
		for _key in self.parent.kropff_fitting_range.keys():
			metadata.append("#kropff {} selection range: [{}, {}]".format(_key,
			                                                              self.parent.kropff_fitting_range[_key][0],
			                                                              self.parent.kropff_fitting_range[_key][1]))

	@staticmethod
	def make_metadata(base_folder=None, fitting_peak_range=None, dict_regions=None,
	                  distance_detector_sample="", detector_offset=""):
		metadata = ["#base folder: {}".format(base_folder)]
		metadata.append("#fitting peak range in file index: [{}, {}]".format(fitting_peak_range[0],
		                                                                     fitting_peak_range[1]))
		metadata.append("#distance detector-sample: {}".format(distance_detector_sample))
		metadata.append("#detector offset: {}".format(detector_offset))
		for _key in dict_regions.keys():
			_entry = dict_regions[_key]
			x0 = _entry['x0']
			y0 = _entry['y0']
			width = _entry['width']
			height = _entry['height']
			metadata.append("#column {} -> x0:{}, y0:{}, width:{}, height:{}".format(_key + 3,
			                                                                         x0, y0,
			                                                                         width, height))
		return metadata

	@staticmethod
	def format_data(col1=None, col2=None, col3=None, dict_regions=None):
		if col1 is None:
			return []

		data = []
		profile_length = len(dict_regions[0]['profile'])
		for _row_index in np.arange(profile_length):
			list_profile_for_this_row = []
			for _key in dict_regions.keys():
				_profile = dict_regions[_key]['profile']
				list_profile_for_this_row.append(str(_profile[_row_index]))
			_col1 = col1[_row_index]
			_col2 = col2[_row_index]
			_col3 = col3[_row_index]
			data.append("{}, {}, {}, ".format(_col1, _col2, _col3) + ", ".join(list_profile_for_this_row))
		return data

