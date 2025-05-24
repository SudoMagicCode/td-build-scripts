import subprocess
import os
import shutil


import td_builder.build_settings
import td_builder.env_var_utils
import td_builder.gitVersion
import td_builder.read_td_log

artifact_dir_name = "artifacts"
targets_dir_name = "targets"
dist_info_name = "dist_info.json"
build_settings_file = "buildSettings.json"

dist_info: dict = {}


def main():
    print('> creating release...')


if __name__ == "__main__":
    main()
