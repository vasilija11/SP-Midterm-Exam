# SP-Midterm-Exam

#### Task 1.
Find the mean value of the `special` integer numbers provided by the user input. The number is considered `special` if 
it divisible by 3 but not divisible by 5. User should be allowed to input numbers until `=` sign is entered as input. 
After `=` is entered program should print mean value of the entered `special` numbers. 

**Note:** It is not allowed to use list/arrays or `sum()` in order to solve this task.

#### Task 2.
Write the recursive function that will form a patterns starting from positive integer number N with step M.
Function should print numbers in descending order starting from N with step M until it becomes negative or zero.
After it becomes negative or zero it should return back to the originating number N with same step M.

**Examples:**
N = 15
M = 5
Output: 15 10 5 0 5 10 15

**Note:** It is not allowed to use loops to solve this task.

#### Task 3.
Write a class `Person` that has general attributes about person like `name, surname, date of birth, address`.
Override `__str__` function in order to print `name` and the `surname` of the person.

Write a class `Employee` that extends the `Person` class and adds attributes `company`, `position`, `years_employed` and
`base_salary`.
`Employee` class should override `__str__` method and print the data about the company and position.
`Employee` class should have method `get_salary()` that returns actually salary of the employee
by adding `1%` of the base salary on top of the base salary for each year spent in company.
`Employee` class should have method `get_tax()` that returns how much tax should be paid for
the employee by using formula `actual salary + 70% of the actual salary`.
`Employee` class should have class variable `num_of_employees` that keeps track about the
number of existing employees.

Write a class `Freelancer` that extends the `Person` class and adds attributes `skills` and `reviews`.
Both `skills` and `reviews` should be lists. List `skills` represents list of the skills offered by Freelancer.
List `reviews` represents quality marks (review starts) valued from `1 - 5` for each project done by Freelancer.
`Freelancer` class should override `__str__` method and print the skill set and average rating for the Freelancer.
`Frellancer` class should have method `get_rating()` that returns average rating based on all reviews.

#### Task 4.
Write a most efficient function `insert()` that inserts integer number into the already sorted array.
After the insertion the array should stay sorted. Explain your approach in comments. Calculate complexity
for your algorithm considering worst case scenario - give answer in comments.

### Task 5.
Write a script that calculates `sum` of the `products` of the elements on the `main` and the `secondary` matrix diagonal. 
Calculate algorithm complexity - give answer in comments. 
