import argparse
from lib.cli import main_menu  # use main_menu instead of run_cli

def main():
    parser = argparse.ArgumentParser(description="Influencer Authenticity Decay Tracker CLI")
    parser.add_argument('--run', action='store_true', help="Run the CLI")
    args = parser.parse_args()

    if args.run:
        main_menu()

if __name__ == "__main__":
    main()
