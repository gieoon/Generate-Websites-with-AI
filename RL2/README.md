# Modified Version

This uses a RL generator, it performs 10 randomized actions, then a discriminator will assess this to see if it looks like a website or not.

The discriminator is also training simultaneously, so it is a moving target.
Value function is determined by discriminator.
State is the HTML

An external puppeteer server has been created to convert HTML into screenshots, which are then processed by the discriminator.

Generation = Code
Discrimination = Image

This simulates how a human would look at this.

## Self-publish as a paper on different generation methods
