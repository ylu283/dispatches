import os
from dispatches_sample_data import rts_gmlc
from dispatches.case_studies.renewables_case.double_loop_utils import read_rts_gmlc_wind_inputs


rtsgmlc_path = rts_gmlc.source_data_path
this_file_path = os.path.dirname(os.path.realpath(__file__))
# default some options
shortfall = 500
prescient_options = {
        # "data_path":"gtep/data/123_Bus_Coal/Prescient",
        "Input_format":"rts-gmlc",
        "simulate_out_of_sample":False,
        "run_sced_with_persistent_forcast_errors": False,
        # "output_directory":"gtep/data/123_Bus_Coal/Prescient/results",
        "start_date": "01-01-2035",
        "num_days":365,
        "sced_horizon": 24,
        "ruc_mipgap": 0.01,
        "reserve_factor":0.0,
        "deterministic_ruc_solver": "gurobi_persistent",
        "sced_solver":"gurobi",
        "sced_frequency_minutes":60,
        "ruc_horizon":48,
        "compute_market_settlements":True,
        "monitor_all_contingencies": False,
        "output_solver_logs": False,
        "price_threshold": 1000,
        "contingency_price_threshold": 5,
        "reserve_price_threshold":None,
        "sced_network_type": "btheta",
        "ruc_network_type":"btheta",
        "enforce_sced_shutdown_ramprate":False,
        }

# read the wind capacity factor dataframe and make a NPP capacity factor in the same format
# this is for the perfect forecaster
wind_generator = "303_WIND_1"
NPP_df = read_rts_gmlc_wind_inputs(rts_gmlc.source_data_path, wind_generator)
NPP_df.columns = ["121_NUCLEAR_1-RTCF", "121_NUCLEAR_1-DACF"]
NPP_df["121_NUCLEAR_1-RTCF"] = 1.0
NPP_df["121_NUCLEAR_1-DACF"] = 1.0