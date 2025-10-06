JTC Program: AISE 25
Lesson Plan: File I/O & External Data
Type: Breakout Session
W2D1 Breakout #1
Version Date: Oct 6, 2025

## Breakout Session #1: Converting and saving JSON entries to a table

Duration: 30 minutes

**Instructions**: Unzip the aircraft zipfile, read in each JSON entry, and convert them to a single comma-delimited .csv file called 'aircraft.csv' with the columns "manufacturer", "model", "introduced", "length_ft", "top_speed_mph", and "number_of_engines".

**Steps**:
- Use the zipfile module (or your OS) to unzip the aircraft.zip archive.
- Traverse the archive with os module (os.listdir) and load each JSON file into memory with the json module.
- Create a new tabular file (use w mode) called aircraft.csv with the csv module (csv.writer). Write the header row (csv.writerow) and then a row with the data from each JSON file.
- If any errors arise, handle them gracefully or (bonus) correct them.

**Expected Outcome**:
- A nicely formatted csv file containing the contents of each provided JSON file
- Experience working with JSON and tabular formats in Python

Example output .csv contents:
  ```csv
    Airbus,A350-900,2015,219.2,652.0,2
    
    Boeing,747-100,1970,231.8,583,4
    
    Cessna,172 Skyhawk,1956,27.2,188,1
    
    Aérospatiale/BAC,Concorde,1976,202.4,1354,4
    
    Embraer,E175,2005,103.8,545,2
  ```

**Reflection Questions**:
- Did you encounter any issues with the files? How did you correct them?
- What is the difference between the modes of file open (r, w, a, x)? Which did you use?
