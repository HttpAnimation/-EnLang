# random.value

random.value allows you to generate random data of a specified length within your EKG code.

## Importing
To import random.value, add the following to your EKG file:
```ekg
get random.value
```

## Usage
To use random.value, add the line:
```ekg
random.value length
```
Replace `length` with the desired length of the random data you want to generate.

## Example
Here is an example of how to generate random data:
```ekg
get random.value
get say

say Here's a random string: 
say + random.value 10
```
In this example, a random string of 10 characters will be generated and printed out.