import os
import numpy as np

this_file_path = os.path.dirname(os.path.realpath(__file__))


def submit_job(index, pem_pmax_ratio, pem_bid):
    # create a directory to save job scripts
    job_scripts_dir = os.path.join(this_file_path, "sim_job_scripts")
    if not os.path.isdir(job_scripts_dir):
        os.mkdir(job_scripts_dir)

    file_name = os.path.join(job_scripts_dir, f"test_re_pcm_sweep_bid_{pem_bid}_{index}.sh")
    with open(file_name, "w") as f:
        f.write(
            "#!/bin/bash\n"
            + "#$ -M ylu28@nd.edu\n"
            + "#$ -m ae\n"
            + "#$ -q long\n"
            + f"#$ -N base_PCM_sim\n"
            + "conda activate /users/ylu28/dispatches\n"
            + "export LD_LIBRARY_PATH=~/.conda/envs/dispatches/lib:$LD_LIBRARY_PATH \n"
            + "module load gurobi/10.0.2\n"
            + "module load ipopt/3.14.2 \n"
            + f"python ./base_pcm_simulation.py"
        )
    os.system(f"qsub {file_name}")


if __name__ == "__main__":
    
    # fix the pem/wind generator power ratio at 0.15. change the price from 50 to 100
    idx = 1
    pem_bid = [50, 60, 70, 80, 90, 100]
    pem_pmax_ratio = 0.15
    for i in pem_bid:
        index = idx
        idx += 1    
        submit_job(index, pem_pmax_ratio, i)