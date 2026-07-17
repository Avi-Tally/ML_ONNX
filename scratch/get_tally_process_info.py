import subprocess

try:
    # Run wmic to get commandline of tally.exe
    output = subprocess.check_output(
        'wmic process where "name=\'tally.exe\'" get ExecutablePath, CommandLine',
        shell=True,
        text=True
    )
    print("Tally Process Info:")
    print(output)
except Exception as e:
    print(f"Error: {e}")
