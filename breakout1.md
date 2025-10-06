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

**Reflection Questions**:
- Did you encounter any issues with the files? How did you correct them?
- What is the difference between the modes of file open (r, w, a, x)? Which did you use?
