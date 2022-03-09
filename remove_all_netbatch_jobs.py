!/usr/bin/env python3.7.4

import os

"""
The script will remove ALL your netbatch jobs
Useful to release netbatch queue if regression is stuck 
"""

JOBS_FILE = "nb_jobs_file"
USER_NAME = os.environ["USER"]
NB_COMMAND = f"nbstatus jobs --tar iil_normal --fi jobid,status,qslot::32,submittime,starttime 'user=~\"{USER_NAME}\"&&status=~\"Run\"' > {JOBS_FILE} "

os.system(NB_COMMAND)
#print(NB_COMMAND)

jobs_file = open(JOBS_FILE, 'r')
jobs_list = []
for line in jobs_file:
    if line.split()[0].isnumeric() == True:# extract jobs id
        jobs_list.append(line.split()[0])

print(f"starting to remove {len(jobs_list)} jobs from netbatch")
#print(jobs_list)
for job_id in jobs_list:
    os.system(f"nbjob remove --tar iil_normal {job_id}")
    #print(f"nbjob remove --tar iil_normal {job_id}")

print("finish to remove all your netbatch jobs!")
