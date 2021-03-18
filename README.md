# Project Constraints
- Shelter holds at most 30 dogs
- Food needs by size Small=10; medium=20; large=30
- Can have remaining food from last month
- When ordering, make sure at least 20% extra food on hand (???Requirment/example is slightly ambigous???)
<br>
<br>

# Running the code
### Prereqs
- Python 3(may run on previous versions but has not been tested)
- ... There may be others as my machine has been used quite a bit in the past. Let me know if something else is required and we can add it to the doc. 
<br>
### Running the code
- To make things easy I have made both the unit test and the function runnable on its own. There is some conditional code at the bottom of the Food.py file that will only run when running that script directly. Without conditionalizting the input on Food.py, the unit test would have to pass through those inputs which is undersirable based on my understanding of the excercise. It is nice to be able to experiement with the function though :)
    - ```python3 Food.py```
<br>

### Running the tests
- You can run the tests with either of the following comamnd line arguaments when in the project directory 
    - ```python3 FoodTests.py```
    - ```python3 -m unittest FoodTests.py```
<br>
<br>

# Test / Edge / Error Cases
- Provided test case: 5=small, 3=medium, 7=large, leftover=17 >>> order 363.6(Appears to be wrong)
- No dogs in shelter: You don't need to order food if no dogs are in the shelter(not handled in the code)
- Leftover exceeds current needed food: You don't need to order food if the leftover amount exceeds the required amount plus the extra(handled by returning 0, could be handled with messaging)
- Food packaging tiers: There may be a minimum order amount or a packaging size increment to take into account(not handled in the code)
- Dog counts must be positive and whole numbers: Handled with exceptions
- Leftover qty must be postive and a float or int: Handled with exceptions
- Incorrect parameter count provided: Handled with exceptions

<br>
<br>

# Notes & Caveats
- The test case provided in the write up appears to be incorrect(https://prnt.sc/10p8whv). I don't think it is possible to end up with a decimal if you are multiplying factors of 10 by 20%. I was able to get the same order amount by multiplying the current food supply by 20% as well but that doesn't make sense based on the problem statement. The leftover food is just the leftover food. The extra required is based on each dog type(https://prnt.sc/10p90q3)
- function run count not tested. planned at integration level.
- Admittedaly the way I have implimented type checking and the subsequent tests to support it are not best practice and could be improved.
<br>
<br>
