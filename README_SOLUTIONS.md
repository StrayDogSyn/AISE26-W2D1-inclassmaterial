# W2D1 Breakout Assignments - Solution Guide

This directory contains complete solutions for both breakout assignments from Week 2, Day 1.

## Files Included

- `breakout1_solution.py` - Complete solution for JSON to CSV conversion
- `breakout2_solution.py` - Complete solution for OpenWeather API CLI app
- `requirements.txt` - Python package dependencies
- `api_key.txt.template` - Template for API key file
- `README_SOLUTIONS.md` - This file

## Setup Instructions

### Install Dependencies

```powershell
# Make sure you're in the correct directory
cd c:\Users\EHunt\Repos\AISE\AISE-Curriculum-Weekly\AISE26-W2D1-inclassmaterial

# Install required packages
pip install -r requirements.txt
```

## Breakout 1: JSON to CSV Converter

### Features
- Unzips aircraft.zip archive automatically
- Processes all JSON files in the extracted directory
- Handles errors gracefully (invalid JSON, missing fields)
- Creates a well-formatted CSV file with headers
- Provides detailed progress feedback

### Usage

```powershell
python breakout1_solution.py
```

### Best Practices Implemented
1. **Type hints** - All functions have type annotations
2. **Docstrings** - Comprehensive documentation for all functions
3. **Error handling** - Try-except blocks for all file operations
4. **Separation of concerns** - Each function has a single responsibility
5. **User feedback** - Clear status messages throughout execution
6. **Path handling** - Uses os.path for cross-platform compatibility
7. **File modes** - Proper use of 'r' (read), 'w' (write) modes

### Expected Output
Creates `aircraft.csv` with columns:
- manufacturer
- model
- introduced
- length_ft
- top_speed_mph
- number_of_engines

## Breakout 2: OpenWeather API CLI App

### Features

#### Basic Mode (Required)
- Prompts user for city name
- Fetches weather data from OpenWeather API
- Displays temperature and weather condition
- Handles errors gracefully (invalid city, network issues, API errors)
- Allows user to quit with 'q'

#### Extended Mode (Bonus)
- `location <city>` - Set current location and display weather
- `get <detail>` - Retrieve specific weather data without API call
  - Supported details: time, temperature, feelslike, pressure, sealevel, windspeed, winddirection, windgust, humidity, visibility
- `log` - Save session history to log.txt
- `help` - Display comprehensive help menu
- `quit` - Exit the program

### Setup

1. Get your OpenWeather API key:
   - Create a free account at https://home.openweathermap.org
   - Navigate to API keys section
   - Copy your API key

2. Create API key file:
   ```powershell
   # Copy the template
   cp api_key.txt.template api_key.txt
   
   # Edit api_key.txt and paste your actual API key
   notepad api_key.txt
   ```

### Usage

```powershell
python breakout2_solution.py
```

When prompted, choose:
- `1` for Simple mode (basic requirements)
- `2` for Extended mode (with bonus features)

### Examples

**Simple Mode:**
```
Please input a city (or q to quit): New York
```

**Extended Mode:**
```
>>> location Paris
>>> get temperature
>>> get windspeed
>>> log
>>> quit
```

### Best Practices Implemented
1. **Class-based design** - WeatherApp class encapsulates all functionality
2. **API key management** - Stored in separate file (not hardcoded)
3. **Error handling** - Comprehensive exception handling for all scenarios
4. **User experience** - Clear prompts, formatted output, help menu
5. **Logging** - Session logging capability
6. **API efficiency** - Caches weather data to minimize API calls
7. **Input validation** - Handles empty input, invalid commands
8. **Type hints** - All methods have type annotations
9. **Docstrings** - Complete documentation for all methods
10. **DRY principle** - No code duplication

### Error Handling Scenarios
- Invalid API key
- City not found
- Network connection issues
- Timeout errors
- Missing API key file
- Empty input
- Invalid commands
- Missing weather data fields

## Reflection Questions

### Breakout 1
1. **Issues encountered**: The script handles JSON parsing errors and missing fields gracefully
2. **File modes**:
   - `r` (read): Opens file for reading only
   - `w` (write): Creates new file or overwrites existing (used for CSV)
   - `a` (append): Adds to end of existing file
   - `x` (exclusive): Creates new file, fails if exists

### Breakout 2
1. **Error prediction**: 
   - Typos in city names
   - Empty input
   - Network issues
   - Invalid API key
   - Rate limiting (60 calls/min)
   
2. **API key management**:
   - Stored in separate file (not in code)
   - File should be added to .gitignore
   - Never commit API keys to version control
   - Consider using environment variables for production
   - Rotate keys if accidentally exposed

## Code Quality Features

Both solutions demonstrate:
- ✅ PEP 8 style compliance
- ✅ Comprehensive error handling
- ✅ Type hints for all functions/methods
- ✅ Detailed docstrings
- ✅ Single responsibility principle
- ✅ Clear variable names
- ✅ User-friendly output
- ✅ Commented code where needed
- ✅ Modular design
- ✅ Professional structure

## Testing Recommendations

### Breakout 1
- Test with valid aircraft.zip
- Test with corrupted JSON files
- Test with missing fields
- Test with empty directory

### Breakout 2
- Test with valid city names
- Test with invalid city names
- Test with no internet connection
- Test with invalid API key
- Test all 'get' commands
- Test log functionality

## Additional Notes

- Both solutions use defensive programming practices
- Error messages are user-friendly and actionable
- Code is production-ready with proper documentation
- Solutions exceed assignment requirements with bonus features
