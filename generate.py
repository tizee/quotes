# File: generate.py
# Description: A script for converting quotes in jsonc format to other format
# Author: tizee
# Email: 33030965+tizee@users.noreply.github.com
# Github: https://github.com/tizee/quotes.git

# -*- coding: utf-8 -*-

import glob
import json
import os
import subprocess
import sys
from pathlib import Path
from pprint import pprint

QUOTES_DIR = os.path.join(os.getcwd(), "quotes")
OUTPUT_DIR = os.path.join(os.getcwd(), "output")


class Config:
    """Config"""

    debug = False
    supported_tools = ["fortune"]
    tools = []

    def __init__(self):
        return None

    def verbose(self):
        print(
            """Config:
        debug: {}
        tools:
        {}
        """.format(self.debug, "\n".join([x for x in self.tools]))
        )

    def parse_arguments(self, args):
        for arg in args:
            if arg == "--debug":
                self.debug = True
            elif arg in self.supported_tools:
                self.tools.append(arg)
            else:
                pprint(f"invalid argument {arg}")
                sys.exit(1)
        if self.debug:
            self.verbose()
        return self

    def convert(self, tool):
        if tool not in self.supported_tools:
            return

        os.makedirs(OUTPUT_DIR, exist_ok=True)
        for file_path in glob.glob(os.path.join(QUOTES_DIR, "*.json")):
            file_name = Path(file_path).stem
            if self.debug:
                print(f"open {file_name}")
            with open(file_path) as fd:
                data = json.load(fd)
                for tool in self.tools:
                    if tool == "fortune":
                        convert_fortune(file_name, data, self.debug)
                        print(f"✅ process {file_name} for fortune")


# convert json to fortune strings format
def convert_fortune(file_name, json_data: dict, debug=False):
    fortune_lines = []
    quotes = json_data.get("quotes")
    for quote in quotes:
        content = quote.get("quote")
        source = quote.get("source")
        line = f"{content}\n  --  {source}\n%\n"
        fortune_lines.append(line)
        if debug:
            print("before ->")
            pprint(quote)
            print("after ->")
            pprint(line)
    file_path = os.path.join(OUTPUT_DIR, "fortune", file_name)
    data_file_path = os.path.join(OUTPUT_DIR, "fortune", file_name + ".dat")
    os.makedirs(os.path.join(OUTPUT_DIR, "fortune"), exist_ok=True)
    with open(file_path, "w+") as fd:
        fd.writelines(fortune_lines)
    result = subprocess.run(
        ["strfile", file_path, data_file_path], capture_output=True, text=True
    )
    if debug:
        print(f"strfile -> {result.stdout}")


def main(argv=None):
    if len(argv) <= 1:
        print(
            """usage: {} [cli] --debug
        available cli formats:
        fortune
        """.format("generate.py")
        )
    config = Config()
    config.parse_arguments(argv[1:])
    for tool in config.tools:
        config.convert(tool)


if __name__ == "__main__":
    main(sys.argv)


# vim:set et sw=4 ts=4 tw=80 ft=python:
