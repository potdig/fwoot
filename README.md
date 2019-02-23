# fwoot

## Feature
This tool displays Twitter's web intent page using text of music info from title bar of Foobar2000.
Format is fixed now: `Now Playing: {music_info}`

## Usage
### Settings on Foobar2000
First, you have to make window title of Foobar2000 available for fwoot.
+ Select [File]-[Preferences] from menu
+ Select [Display]-[Default User Interface] in the tree of preferences window
+ Change "Window title" setting like this: `[%title%] [/ %artist%] ['['%album% [Tr. %tracknumber%]']'] - foobar2000` (IMPORTANT: Include fixed string ` - foobar2000` !! This tool finds window of Foobar200 with this string.)

### Using tool
+ Execute fwoot.exe
+ Push "Tweet" button on browser

## Features considering to add
- Text format customization
