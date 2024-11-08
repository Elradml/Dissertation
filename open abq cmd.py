import os
import subprocess

print("Start")
def run_inp(input_path):
    input_name = os.path.basename(input_path)

    job_name = os.path.splitext(input_name)[0]
    abaqus_command = f'abaqus job={job_name} inp="{input_path}"'
    
    try:
        subprocess.run(abaqus_command, shell = True, check = True)
        print(f"Job {job_name} completed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error running job {job_name}")
        print(e)

name = "TexGen_generated_test.inp"
run_inp(name) 

print("Finish")