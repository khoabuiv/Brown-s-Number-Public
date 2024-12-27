# Purpose
The purpose of this project is to measure the influence of Paul Brown on American football. To do this, we introduce the Paul Brown's number, inspired by the Erdos' number in mathematics, to measure how close is a coach to Paul Brown. 

## Introduction
The mathematician Paul Erdos was one of the prolific mathematicians of the 20th century. He published more papers than any other mathematician in history outpacing even the great Euler. To measure his influence, mathematicians defined an Erdos number to be how close a person to a collaboration with Paul Erdos. For example: 
- Erdos number 0: Erdos himself 
- Erdos number 1: Someone who wrote an article with Erdos 
- Erdos number 2: Someone who wrote an article with a person who has Erdos number 1
And so on. 

### What is the Brown's Number?
Inspired by Erdos number, I define the Brown's number to be how close a coach is to Paul Brown. So for example:
- Brown number 0: Paul Brown himself 
- Brown number 1: Someone coached with Paul Brown on a team 
- Brown number 2: Someone coached with a coach who coached with Paul Brown
And so on to infinity. To note, an undefined Paul Brown's number would be someone who never coached with.

## Methodology
To find the Brown's number, we gather the coaching data from [pro-football-reference](https://www.pro-football-reference.com/). We then analyze the data to build out our database of the Paul Brown's number. The steps is as follow:
1. Pull the data from pro-football-references using the get_coaches.py using the list of teams participated in the NFL from 1946 to 2023.
2. Clean the data using the cleaning_data.py script to get the coaches' names, their positions, their records, what team they coached for, and what year? 
3. Analyze the data using the data_analysis.py script. 

## Data Usage
We credited all the data to pro-football-reference, and that the data used in this project is solely focus on educational and entertainment focuses. 

