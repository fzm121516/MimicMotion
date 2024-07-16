import os
import subprocess


def run_inference(yaml_file):
    command = f"python inference.py --inference_config {yaml_file}"
    subprocess.run(command, shell=True)


def main():
    configs_dir = "configs"
    yaml_files = [f for f in os.listdir(configs_dir) if f.endswith('.yaml')]

    for yaml_file in yaml_files:
        yaml_path = os.path.join(configs_dir, yaml_file)
        run_inference(yaml_path)


if __name__ == "__main__":
    main()
