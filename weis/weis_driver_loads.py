import os
from weis import weis_main

## File management
run_dir = os.path.dirname( os.path.realpath(__file__) )
fname_wt_input = os.path.join("IEA-15-240-RWT-CFDpolars_Feb25.yaml")
fname_modeling_options = os.path.join(run_dir, "modeling_options.yaml")
fname_analysis_options = os.path.join(run_dir, "analysis_options.yaml")

# Run WEIS for real now
wt_opt, modeling_options, opt_options = weis_main(fname_wt_input, 
                                                  fname_modeling_options, 
                                                  fname_analysis_options)
