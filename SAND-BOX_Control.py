import os
import subprocess

def enable_sandbox():
    os.system('DISM /Online /Enable-Feature /FeatureName:"Containers-DisposableClientVM" /All')
    print("sandbox enable.")

def disable_sandbox():
    os.system('DISM /Online /Disable-Feature /FeatureName:"Containers-DisposableClientVM"')
    print("sandbox disabled.")

def Check_the_status():
    command = 'DISM /Online /Get-FeatureInfo /FeatureName:"Containers-DisposableClientVM"'
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            print("Command executed successfully.\n")
            print(result.stdout)
        else:
            print("error occurred while executing the command.")
            print(result.stderr)
    except FileNotFoundError:
        print("DISM command not found. Make sure you have the necessary tools installed.")

def main():
    while True:
        print("==================================================")
        print("E:enable/D:disabled/S:Check Please choose.")
        choice = input("Select (E/D/S) or enter Q to exit:").upper()
        print("==================================================")

        if choice == 'E':
            enable_sandbox()
        elif choice == 'D':
            disable_sandbox()
        elif choice == 'S':
            Check_the_status()
        elif choice == 'Q':
            print("EXIT")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
