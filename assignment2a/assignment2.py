#!/usr/bin/env python3
#Author: Yelianny Zabala
#Author ID: yzabala-pellicer@myseneca.ca

import argparse

import os, sys

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."

    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # Make this entry for human-readable. Check the docs to make it a True/False option.
    parser.add_argument("program", type=str, nargs='?', help="if a program is specified, show memory use of all associated processes. Show only total use if not.")
    args = parser.parse_args()
    return args

def percent_to_graph(percent: float, length: int=20) -> str:
    "turns a percent 0.0 - 1.0 into a bar graph"
    pass

def get_sys_mem() -> int:
    "return total system memory (used or available) in kB"
    # open the meminfo file to accomplish the task!
    pass

def get_avail_mem() -> int:
    "return total memory that is currently in use"
    # open the meminfo file to accomplish the task!
    pass

def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    # please use os.popen('pidof <app>') to accomplish the task!
    pass

def rss_mem_of_pid(proc_id: str) -> int:
    "given a process id, return the Resident memory used"
    # for a process, open the smaps file and return the total of each
    # Rss line.
    pass

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB'] # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
      result /= 1024
      suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program: # not program name is specified.
      pass
    else:
      pass