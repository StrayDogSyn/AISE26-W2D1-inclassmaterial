"""
JTC Program: AISE 25
W2D1 Breakout #1: Converting and saving JSON entries to a table

This script unzips an aircraft.zip file, reads JSON files from the extracted directory,
and converts them into a single CSV file with specified columns.

Author: Solution
Date: Oct 6, 2025
"""

import json
import csv
import os
import zipfile
from pathlib import Path
from typing import Dict, List, Optional


def unzip_aircraft_data(zip_path: str = "aircraft.zip", extract_to: str = "aircraft_data") -> str:
    """
    Unzip the aircraft.zip archive to a specified directory.
    
    Args:
        zip_path: Path to the zip file
        extract_to: Directory to extract files to
        
    Returns:
        Path to the extracted directory
        
    Raises:
        FileNotFoundError: If zip file doesn't exist
        zipfile.BadZipFile: If file is not a valid zip file
    """
    try:
        # Check if zip file exists
        if not os.path.exists(zip_path):
            raise FileNotFoundError(f"Zip file not found: {zip_path}")
        
        # Create extraction directory if it doesn't exist
        os.makedirs(extract_to, exist_ok=True)
        
        # Extract all files from the zip archive
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"✓ Successfully extracted {zip_path} to {extract_to}/")
        
        return extract_to
        
    except zipfile.BadZipFile:
        print(f"✗ Error: {zip_path} is not a valid zip file")
        raise
    except Exception as e:
        print(f"✗ Error extracting zip file: {e}")
        raise


def load_json_file(file_path: str) -> Optional[Dict]:
    """
    Load and parse a single JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Dictionary containing JSON data, or None if error occurs
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError as e:
        print(f"✗ Warning: Invalid JSON in {file_path}: {e}")
        return None
    except Exception as e:
        print(f"✗ Warning: Could not read {file_path}: {e}")
        return None


def extract_aircraft_data(json_data: Dict) -> Optional[Dict[str, any]]:
    """
    Extract required fields from aircraft JSON data.
    
    Args:
        json_data: Dictionary containing aircraft data
        
    Returns:
        Dictionary with extracted fields, or None if required fields are missing
    """
    try:
        # Define the required fields for our CSV
        required_fields = {
            'manufacturer': json_data.get('manufacturer', ''),
            'model': json_data.get('model', ''),
            'introduced': json_data.get('introduced', ''),
            'length_ft': json_data.get('length_ft', ''),
            'top_speed_mph': json_data.get('top_speed_mph', ''),
            'number_of_engines': json_data.get('number_of_engines', '')
        }
        
        return required_fields
        
    except Exception as e:
        print(f"✗ Warning: Error extracting data: {e}")
        return None


def process_aircraft_files(data_dir: str) -> List[Dict[str, any]]:
    """
    Process all JSON files in the data directory.
    
    Args:
        data_dir: Directory containing JSON files
        
    Returns:
        List of dictionaries containing aircraft data
    """
    aircraft_list = []
    
    # Get all files in the directory
    try:
        files = os.listdir(data_dir)
    except FileNotFoundError:
        print(f"✗ Error: Directory not found: {data_dir}")
        return aircraft_list
    
    # Filter for JSON files only
    json_files = [f for f in files if f.endswith('.json')]
    
    if not json_files:
        print(f"✗ Warning: No JSON files found in {data_dir}")
        return aircraft_list
    
    print(f"\nProcessing {len(json_files)} JSON files...")
    
    # Process each JSON file
    for filename in json_files:
        file_path = os.path.join(data_dir, filename)
        
        # Load JSON data
        json_data = load_json_file(file_path)
        
        if json_data:
            # Extract required fields
            aircraft_data = extract_aircraft_data(json_data)
            
            if aircraft_data:
                aircraft_list.append(aircraft_data)
                print(f"  ✓ Processed: {filename}")
            else:
                print(f"  ✗ Skipped: {filename} (missing required fields)")
        else:
            print(f"  ✗ Skipped: {filename} (invalid JSON)")
    
    return aircraft_list


def write_csv_file(aircraft_data: List[Dict[str, any]], output_file: str = "aircraft.csv") -> bool:
    """
    Write aircraft data to a CSV file.
    
    Args:
        aircraft_data: List of dictionaries containing aircraft data
        output_file: Path to output CSV file
        
    Returns:
        True if successful, False otherwise
    """
    # Define CSV column headers
    headers = ['manufacturer', 'model', 'introduced', 'length_ft', 'top_speed_mph', 'number_of_engines']
    
    try:
        # Open file in write mode (will create or overwrite)
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            # Create CSV writer object
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            
            # Write header row
            writer.writeheader()
            
            # Write data rows
            writer.writerows(aircraft_data)
            
        print(f"\n✓ Successfully created {output_file} with {len(aircraft_data)} entries")
        return True
        
    except Exception as e:
        print(f"\n✗ Error writing CSV file: {e}")
        return False


def main():
    """
    Main function to orchestrate the JSON to CSV conversion process.
    """
    print("=" * 60)
    print("Aircraft Data Converter: JSON to CSV")
    print("=" * 60)
    
    # Step 1: Unzip the aircraft archive
    try:
        data_dir = unzip_aircraft_data()
    except Exception:
        print("\n✗ Failed to unzip aircraft data. Exiting.")
        return
    
    # Step 2: Process all JSON files
    aircraft_data = process_aircraft_files(data_dir)
    
    if not aircraft_data:
        print("\n✗ No valid aircraft data found. Exiting.")
        return
    
    # Step 3: Write data to CSV file
    success = write_csv_file(aircraft_data)
    
    if success:
        print("\n" + "=" * 60)
        print("✓ Conversion completed successfully!")
        print("=" * 60)
    else:
        print("\n✗ Conversion failed.")


if __name__ == "__main__":
    main()
