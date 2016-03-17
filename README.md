# Overview

sc2ReplayAnalyzer is a tKinter GUI-based program which gets information from a StarCraft II replay file, using the sc2reader library.



# Getting Started

There are two ways to load a replay file. Both start with the file menu, in the top left.

### Load Replay
The first choice is "Load Replay". This is used to load a locally-saved replay file. The default directory is the working directory for the program, though replays can be loaded from anywhere on the system.

Simply, navigate to where the replay file is saved and open it.

### Import from GGTracker
The second choice is "Import from GGTracker". (http://www.ggtracker.com) This option prompts the user for a GGTracker ID.

To get a user ID from a player's profile on GGTracker, navigate to the profile page. The user ID is the set of numbers contained in the URL.

  e.g. (http://ggtracker.com/players/1455/nocek), the user ID would be "1455".
  
Simply enter the user ID in the prompt, and the program grabs the replay file for the most recent ranked, 1v1 match the player has uploaded.

As soon as the replay file has been loaded, or grabbed from GGTracker, the UI will be automatically updated with info and stats contained within the file.

