import subprocess


def run_command():
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(
            ["bash", "101-200/192.sh"], check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"


def main():
    """Main function to run the shell command and print the output."""
    output = run_command()
    print(output)


if __name__ == "__main__":
    main()
