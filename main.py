import argparse
import json
import yaml
from pathlib import Path

from src.generator import CodeGenerator

def load_config(config_path):
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_file}")
    
    with config_file.open('r') as file:
        if config_file.suffix == '.json':
            return json.load(file)
        elif config_file.suffix in ['.yml', '.yaml']:
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported configuration file format: {config_file.suffix}")

def parse_input(input_file, input_type):
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    with input_path.open('r') as file:
        input_data = json.load(file)
    
    if input_type == 'json':
        return input_data  # Return the entire schema
    else:
        raise ValueError(f"Unsupported input type: {input_type}")

def main():
    parser = argparse.ArgumentParser(description="Laravel Code Generator")
    parser.add_argument("input_file", help="Path to the input file (JSON)")
    parser.add_argument("--input-type", choices=['json'], default='json',
                        help="Type of the input file (default: json)")
    parser.add_argument("--config", default="src/config/config.json",
                        help="Path to the configuration file (default: src/config/config.json)")
    parser.add_argument("--output", help="Directory to store generated files")
    args = parser.parse_args()

    try:
        # Load configuration
        config = load_config('./src/config/config.json')
        
        # Override output directory if specified in command line
        if args.output:
            config['output_directory'] = args.output

        # Parse input
        schema = parse_input(args.input_file, args.input_type)

        # Initialize code generator
        generator = CodeGenerator(config)

        # Generate code
        generated_files = generator.generate(schema)

        # Save generated files
        output_dir = Path(config['output_directory'])
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for file_path, content in generated_files.items():
            full_path = output_dir / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            with full_path.open('w') as file:
                file.write(content)

        print(f"Code generation complete. Files written to {output_dir}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()