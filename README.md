# Hangman Game Animal Edition

[Link To App](https://lsws.herokuapp.com/)

## UX

### User Demographic

This Python Terminal Program was created for:

- A fictional bakery that needs to keep track of stock of each item to avoid having to throw away unsold inventory while still maximizing sales.

### User Stories

#### As a user of the program I expect

- To be able to input sales figures at the end of the day.
- To get calculated values of next days inventory recommendations.
- To receive feedback if my input is invalid.

### User Goals

- Input correct sales data and receive recommended inventory numbers for the next day based on past sales figures.

### Requirements

A python terminal program that is made completely with python and contains various advanced functionalities.

### Planning

The project steps listed below:

- User inputs values for the market
- If valid:
  - Values get stored in sales figures
    - Next markets value gets calculated and printed to the terminal
- If Invalid:

  - Error is printed to the terminal and the program expects a new, valid input.

    Errors are either if the values are not numbers, or if there are not exactly 6 comma separated values

### Design

The design of the project is nonextistant given the command line interface of the console. The formatting of the text and prompts have been written out in a way to make it clear and easy to follow, with the help of spacing.

## Features

### Console Program

![Initial](/readme-imgs/initial.png)

The above image shows the intial prints in the console window:

![Valid](/readme-imgs/valid.png)

The above image shows the console prints from a valid input:

![InvalidL](/readme-imgs/invalidl.png)

The above image shows the console prints from an invalid input with letter:

![InvalidN](/readme-imgs/invalidn.png)

The above image shows the console prints from an invalid input with wrong amount of values:

### Google Sheets

#### Sales Figures

![Sales](/readme-imgs/sales.png)

Image above shows the sales figures that are being input by the user through the program.

#### Surplus

![Surplus](/readme-imgs/surplus.png)

Image above shows the surplus for each sandwich, calulation stock - sales for the day, negative numbers means sold more than stock we calculated.

#### Stock

![Stock](/readme-imgs/stock.png)

Image above shows the stock sheet, the stock is calculated by the averages of the sales from the last 5 entries with a 10% increase to encourage more sales and then rounded to the closes whole number.

### Features Left to Implement

- A way to print surplus from the console.
- Ability to delete an entry if incorrect values were added.

## Technologies used

- [Python](https://www.python.org/)

## Testing

### Tests Executed

Test exectued to ensure that the program is running as is intended.

- Ensuring that the input validators accurately validates the input to the program
- Test that all the different statements print correctly.

### Validator Testing

- Using a python linter in the workspace, there were no issues found.

### Unfixed Bugs

All known bugs have been squashed

## Development and Deployment

The development of this code was done exclusively in GitPod, with the changes being tracked and pushed on GitHub. The initial template of the project was made by the Code Institute

The live version of the project is deployed on Heroku for the time being following the steps outlined by the Code Institute

The link to the hosted program on heroku can be found [here](https://lsws.herokuapp.com/)
