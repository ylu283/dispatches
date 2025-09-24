import os
from dispatches.improved_pt.prescient_sweep.base_prescient_options import prescient_options
from prescient.simulator import Prescient

ercot_path = os.path.join(os.getcwd(), "..", "..", "..", "..", "..", "idaes-gtep/gtep/data/123_Bus_Coal/Prescient")

prescient_options["output_directory"] = f"base_pcm_ERCOT"
prescient_options["data_path"] = ercot_path
Prescient().simulate(**prescient_options)
