import os
from pathlib import Path
import subprocess
import sys

def run_cli_command(command, output_file):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        stdoutFileName  = output_file+"Stdout.txt"
        with open(stdoutFileName, 'w') as file:
            file.write(result.stdout)

        stderrFileName  = output_file+"Stdrr.txt"
        with open(stderrFileName, 'w') as file:
            file.write(result.stderr)

        print(f"output saved to {stdoutFileName} and {stderrFileName}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    output_file = None
    tpcc_directory = None
    bookkeeper_metadata_uri = None

    if len(sys.argv) == 4:
        output_file = sys.argv[1]
        tpcc_path = sys.argv[2]
        bookkeeper_metadata_uri = sys.argv[3]
 

    if output_file is None or len(output_file) < 1:
        print("Usage: python3 leanstore_runner.py <output file names> <tpcc_directory> <bookkeeper_metadata_uri>")
        sys.exit(1)

    if tpcc_path is None:
        print("Usage: python3 leanstore_runner.py <output file names> <tpcc_directory> <bookkeeper_metadata_uri>")
        sys.exit(1)
    
    if bookkeeper_metadata_uri is None:
        print("Usage: python3 leanstore_runner.py <output file names> <tpcc_directory> <bookkeeper_metadata_uri>")
        sys.exit(1)



    os.chdir(Path(tpcc_path))
    
    command = f"./tpcc --tpcc_warehouse_count=1 --notpcc_warehouse_affinity --worker_threads=4 --pp_threads=16 --free_pct=1 --contention_split --xmerge --warmup_for_seconds=1 --run_for_seconds=2 --isolation_level=si --bookkeeper_jar_directories=../../bookkeeper-wal/target:../../bookkeeper-wal/target/maven-dependencies  --wal_pwrite=true --profile_latency=true --csv_path={output_file} --wal_variant=0 --bookkeeper_metadata_uri={bookkeeper_metadata_uri}"
    run_cli_command(command, output_file)

