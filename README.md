# note_data_to_instrument
An application that reads note data from for example a .mid file and plays a musical instrument

It currently only reads .mid files right now, if you can get it to read .mxl(sheet music files), .it, .mod, .s3m, .xm files, please add those features in note_data_to_instrument.py.

It only supports synthesizers right now, (for example a square wave or sine wave generator).

It works on raspberry pi right now but I have no idea if it works on raspberry pi clones like the orange pi or if it works on other computers with GPIO ports.

If you want to use an arduino you have to use the files from the version 2 folder because I still have version 1 on here for people who may want it and you have to run and send the note_data_to_instrument_arduino_driver file to the arduino 1st then run note_data_to_instrument.

To use 128 note support you have to use the files from the version 3 folder or later.

To use Mod Support you must use the version 4 folder and to run mods you need to put the mod file in your home directory, project folder or both, whichever works for you. The mod must be called note_data_to_instrument_mod.lua.

Sometimes with raspberry pi you may need to connect a battery between the gpio pin and synth.

<a href="https://github.com/Daniel-Hanrahan-Tools-and-Games/note_data_to_instrument_mod">Example Mod Repository Page</a>

It works on arduino uno right now but I have no idea if it works on other arduino boards.

<a href="https://github.com/Daniel-Hanrahan-Tools-and-Games/note_data_to_instrument">Repository Page</a>

<a href="https://daniel-hanrahan-tools-and-games.github.io/">Home Page</a>




GNU GPL v3.0 Conditional Exceptions to use MPL 2.0

If the following condition is met, the licensing rules for content covered by GNU GPL v3.0 are modified as described below:

Condition:

The developer is distributing, porting, or integrating the software with platforms or environments that impose requirements incompatible with GPL-3.0, including but not limited to:
- proprietary or non-redistributable SDKs
- confidential hardware or platform documentation
- legally required confidentiality obligations preventing full GPL redistribution
- safety-regulated or certified systems where full GPL redistribution cannot be satisfied

Effect on licensing:

- Content covered by GNU GPL v3.0: May instead be used under the Mozilla Public License 2.0.

These exceptions apply **only when the condition above is met**.






Contributors needed.
