### Coding Challenge Guidelines
* You can choose any programming language (we’d suggest choosing your strongest)
* You can use the internet, but please don’t look up or copy an existing solution—we want to see how you work
* This isn’t a race, but please track your time so you can tell us how long it took you
* Please don’t spend any longer than 90 minutes total

### Evaluation Criteria
Write a library for generating random PIN codes. You probably know what a PIN code is; it’s a short sequence of numbers, often used as a passcode for bank cards.

* The library should export a function that returns a batch of 1,000 PIN codes in random order
* Each PIN code in the batch should be unique
* Each PIN should be:
* 4 digits long
* Two consecutive digits should not be the same (e.g. 1156 is invalid)
* Three consecutive digits should not be incremental (e.g. 1236 is invalid)
* The library should have automated tests.
