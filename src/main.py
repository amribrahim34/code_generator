import argparse
import logging
import traceback
import sys
from src.generators.code_generator import CodeGenerator

# Set up logging to write to a file
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='code_generator.log',
    filemode='w'
)

# Also print to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def main():
    parser = argparse.ArgumentParser(description="Generate code based on a schema.")
    parser.add_argument("--schema", required=True, help="Path to the input schema file")
    parser.add_argument("--input-type", required=True, choices=["json", "yaml"], help="Type of input schema")
    parser.add_argument("--config", required=True, help="Path to the configuration file")
    args = parser.parse_args()

    # logging.info(f"Starting code generation with schema: {args.schema}")
    
    try:
        logging.info("Initializing CodeGenerator...")
        generator = CodeGenerator(args.config)
        
        logging.info("Generating code...")
        generated_code = generator.generate(args.schema)
        
        logging.info(f"Generated code: {generated_code}")
        
        logging.info("Saving files...")
        generator.save_to_files(generated_code)
        
        logging.info("Code generation completed")
    except Exception as e:
        # logging.error(f"An error occurred: {str(e)}")
        logging.error("Traceback:")
        logging.error(traceback.format_exc())

if __name__ == "__main__":
    main()