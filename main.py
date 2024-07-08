# # main.py

# # Import necessary modules
import argparse
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

def main(args):
    """
    Main function to execute the script functionality.
    """
    # logger.info("Script started with arguments: %s", args)

    # Your code here
    # Example: print a greeting message
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Description of your script.")
    parser.add_argument('-n', '--name', type=str, default="World", help='Name to greet')
    
    args = parser.parse_args()
    
    # Call the main function
    main(args)