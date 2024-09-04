import argparse
import logging
from typing import Dict, Any
import sys
import os

# Adjust the path to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.core.code_generator import CodeGenerator
from src.configuration.config_manager import ConfigManager
from src.utilities.file_utils import read_json_file, write_json_file

class CommandLineInterface:
    def __init__(self):
        self.parser = self._create_argument_parser()
        self.config_manager = ConfigManager("config/default_config.json")
        self.logger = self._setup_logger()

    def _create_argument_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="Code Generator CLI")
        parser.add_argument("--schema", required=True, help="Path to the input schema JSON file")
        parser.add_argument("--config", default="config/default_config.json", help="Path to the configuration JSON file")
        parser.add_argument("--output", default="output", help="Output directory for generated code")
        parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Set the logging level")
        return parser

    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger("CodeGeneratorCLI")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def run(self):
        args = self.parser.parse_args()
        
        # Set logging level
        self.logger.setLevel(args.log_level)

        # Load and update configuration
        self.config_manager.load_config()
        self.config_manager.update_config({
            "schema_path": args.schema,
            "output_directory": args.output
        })
        self.config_manager.validate_config()

        # Initialize CodeGenerator
        code_generator = CodeGenerator(self.config_manager)

        try:
            # Generate code
            self.logger.info("Starting code generation...")
            generated_code = code_generator.generate()
            self.logger.info(f"Code generation completed. {len(generated_code)} files generated.")

            # Save generated code
            self.logger.info("Saving generated files...")
            code_generator.save_to_files(generated_code)
            self.logger.info(f"Files saved to {args.output}")

            # Generate documentation (if applicable)
            if self.config_manager.get_config().get("generate_documentation", False):
                self.logger.info("Generating documentation...")
                documentation = code_generator.generate_documentation()
                documentation_path = os.path.join(args.output, "documentation.md")
                write_json_file(documentation_path, documentation)
                self.logger.info(f"Documentation saved to {documentation_path}")

            self.logger.info("Code generation process completed successfully.")
        except Exception as e:
            self.logger.error(f"An error occurred during code generation: {str(e)}")
            sys.exit(1)

def main():
    cli = CommandLineInterface()
    cli.run()

if __name__ == "__main__":
    main()