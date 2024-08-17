import argparse
import sys
from sqlalchemy import create_engine
from utils.config import Config
from utils.models.general_models import Base
from processors.example_event_processor import models as example_models

def main(config_path):
    try:
        # Load the configuration
        config = Config.from_yaml_file(config_path)
        
        # Create SQLAlchemy engine
        engine = create_engine(config.server_config.postgres_connection_string)
        
        # Create all tables in the database
        Base.metadata.create_all(engine)
        example_models.Base.metadata.create_all(engine)
        
        print("Database tables created successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create database tables based on the provided configuration.")
    parser.add_argument("-c", "--config", help="Path to config file", required=True)
    args = parser.parse_args()
    
    main(args.config)
