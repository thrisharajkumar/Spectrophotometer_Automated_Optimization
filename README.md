# Spectrophotometer_Automated_Optimization-
The production optimization algorithm is designed to schedule over 250 lipstick shades efficiently. It considers the delta E values of the shades, which is calculated using the formula delta E = sqrt(a2+b2+L2). The algorithm also uses a greedy approach to schedule the shades from lightest to darkest and vice versa, based on the demand plan.


![image](https://github.com/thrisharajkumar/Spectrophotometer_Automated_Optimization-/assets/85435379/adacd285-af7c-4374-a9a8-e1684751360b)
<img width="458" alt="image" src="https://github.com/thrisharajkumar/Spectrophotometer_Automated_Optimization-/assets/85435379/d658ca0f-bae7-47d8-b288-19f43210caab">

Utilized Python programming language, leveraging Pandas for data manipulation.
Executed the algorithm on platforms such as Jupyter Lab and Visual Studio Code for efficient development and deployment. 
--> 3 files are uploaded in the Jupyter lab folder along with the Python file. One Excel file consists of the Delta X values of all the shades in the form of a symmetric matrix, and another Excel file contains the Lightest to darkest shades, and the Production Plan for the week file. 
--> The program traverses/reads through the files and produces an Excel file as the output as well as displays it on the screen.
--> The program uses the greedy algorithm. It takes the lightest color shade from the production plan and finds the smallest delta-x value among the other shades in the plan and loops this step until all the shades are sorted.
--> This program helps to optimize the production OEE and changeover time by outputting the optimized shades for over 250+ shades.

<img width="257" alt="image" src="https://github.com/thrisharajkumar/Spectrophotometer_Automated_Optimization-/assets/85435379/35ea9f12-0f71-45e0-a75f-1b8e5b7adf23">
