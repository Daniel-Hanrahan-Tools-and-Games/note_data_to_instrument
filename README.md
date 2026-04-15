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





CC BY-SA 4.0 and GNU GPL v3.0 Conditional Exceptions to use PolyForm Noncommercial and CC BY-NC 4.0

The PolyForm Noncommercial License (and Creative Commons
Attribution-NonCommercial 4.0 International for non-code
content) may be used as an alternative only when the combined
work is subject to binding legal, contractual, or platform-
imposed restrictions that prohibit commercial use.

Such restrictions may arise from third-party licenses,
distribution platforms, or other enforceable legal terms that
make commercial use of the combined work not legally permitted.

Content covered by the primary license (e.g., source code or
other covered material) remains governed by that license.

Content not covered by the primary license (e.g., assets,
documentation, or other non-code materials) is governed by
CC BY-NC 4.0, unless otherwise stated.

This alternative applies only to the extent necessary to
comply with such restrictions.




CC BY-SA 4.0 and GNU GPL v3.0 Conditional Exceptions to use PolyForm Strict and CC BY-NC-ND 4.0

The PolyForm Strict License may be used as an alternative
license only when the combined work is subject to binding
legal, contractual, or platform-imposed restrictions that
require both non-commercial use and prohibit the creation of
derivative works as part of the distribution terms.

Such restrictions may arise from third-party licenses,
distribution platforms, or other enforceable legal terms that
impose both non-commercial and no-derivatives requirements on
the combined work.

Content covered by the primary license (e.g., source code or
other covered material) remains governed by that license.

Content not covered by the primary license (e.g., assets,
documentation, or other non-code materials) is governed by
Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International (CC BY-NC-ND 4.0), unless otherwise stated.

This alternative applies only to the extent necessary to
comply with such restrictions.





Contributors needed.
