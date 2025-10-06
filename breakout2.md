JTC Program: AISE 25
Lesson Plan: File I/O & External Data
Type: Breakout Session
W2D1 Breakout #2
Version Date: Oct 6, 2025

## Breakout Session #2: Interacting with the OpenWeather API via a command line app

Duration: 30 minutes

**Instructions**: Build a simple command line interface that lets us query the OpenWeather API

**Steps**:
Create an API key (at least one per group)
1. Create a (free) account: https://home.openweathermap.org
2. Find your key on openweathermap.org. Add it to a local text file.

- Load your key into a Python script.
Use input to prompt the user for the name of a city ("`Please input a city (or q to quit): `").
- If the user enters `q`, quit the program. Otherwise, attempt to retrieve the weather for that city via the OpenWeather API.
- If it works, display the temperature and main weather type (e.g. `clear`) to the user and exit the program. If the attempt to retrieve the weather for the user's location fails, display the resulting error and prompt the user again.
- Take turns testing the app and adding features to prevent crashes.

**Expected Outcome:**
- Experience creating, managing and using API keys
- A robust and simple command line loop with control flow based on user input

**Reflection Questions:**
- What errors did you predict your users would cause? Are any error states particularly difficult to deal with?
- How did you manage your API key? What considerations are important when dealing with API keys?

**Bonus:**
#### Extending our command line program

The basic application contains a loop which loads the API key from a local .env file, prints a welcome message, and prompts the user for input. Extend the application with the following commands:

`location`: Sets the location at which weather is queried. When a new location is successfully set, display the time of day, temperature and "main" weather description. *This is the only time the API should be queried! You have a max of 60 calls/min*

`get`: Retrives and displays specific requested data from the currently set location such as "time", "sea level", "temperature", "pressure", "feelslike", "windspeed", "winddirection" and "windgust." Implement at least 4 of these. This interface should be as human readable and as forgiving as possible and may have as many additional features features as you like, as long as you explain how to use it with the help command (see below). 

The program should have three additional commands:

`log`: Record the entire output of the program's run so far to a text file in the current working directory called "log.txt."

`help`: Prints instructions on how to use the program.

`quit`: Ends the program.
