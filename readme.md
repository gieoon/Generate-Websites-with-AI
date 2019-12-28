# Generating Websites with Machine Learning
The goal is to generate the skeleton of a website through human-directed machine learning

## Process
1. Generate website from 10 steps
2. Let human choose which one they like more
3. Add in a GAN with OpenCV to detect websites which go towards the one the human likes more.
4. Done

## Technical Hurdles
There are numerous challenges
- How to create dynamically updating HTML? Is this done by rendering a template? Or after human intervention there's a GET request?

## What to consider
There are many ways of treating this problem, which is what makes it fun
- What sort of input? Is it a language model only looking at the code? 
- Is it a reinforcement learning solution?
- Can we use a GAN to generate tasks, but does this mean that we need a dataset of images of websites to train a CNN (Discriminator) on?
- Is it possible to have minimal human feedback to generate something that's in the 'area' of a website
- Is it possible to do this purely using code without any form of image recognition? Using HTML XML to generate more HTML XML, and have it judged by a human who looks at the webpage? Or do we need to (at some point) insert an image recognition system, either using OpenCV or a pre-trained CNN?

# Similar areas
There are other areas that are similar in trying to generate websites, but most of these have not formed complete solution, or at least not an open-source one. That's why I think this is something interesting to work on, and would value your input

## Sources
- [FloydHub] (https://blog.floydhub.com/an-introduction-to-q-learning-reinforcement-learning/)
- [Amunategui](https://amunategui.github.io/reinforcement-learning/index.html)
