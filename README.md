# Triangle567
# Assignment Description
The objective of this assignment is for you to (a) develop a set of tests for an existing triangle classification program, (b) use those tests to find and fix defects in that program, and (c) report on your testing results for the Triangle problem
# Author
Kensay Sato
# Honor Pledge
I pledge my honor that I have abided by the Stevens Honor System.
# Summary

# Test Report 1

| Test ID               | Input       | Expected Result | Actual Result  | Pass or Fail |
|-----------------------|-------------|-----------------|----------------|--------------|
| test_equilateral | 1, 1, 1 | Equilateral | InvalidInput | Fail |
| test_invalid_1 | 1, 1, 2 | Invalid | InvalidInput | Fail |
| test_invalid_2 | 0, 0, 0 | Invalid | InvalidInput | Fail |
| test_invalid_3 | -1, -1, -1 | Invalid | InvalidInput | Fail |
| test_invalid_4 | 1, 10, 12 | Invalid | InvalidInput | Fail |
| test_isosceles_1 | 2, 2, 3 | Isosceles | InvalidInput | Fail |
| test_isosceles_2 | 5, 5, 8 | Isosceles | InvalidInput | Fail |
| test_right_triangle_1 | 3, 4, 5 | Right | InvalidInput | Fail |
| test_right_triangle_2 | 5, 12, 13 | Right | InvalidInput | Fail |
| test_right_triangle_3 | 6, 8, 10 | Right | InvalidInput | Fail |
| test_scalene_1 | 6, 7, 8 | Scalene | InvalidInput | Fail |
| test_scalene_2 | 10, 12, 15 | Scalene | InvalidInput | Fail |
| test_triangle_inequality_1 | 10, 1, 1 | Invalid | InvalidInput | Fail |
| test_triangle_inequality_2 | 1, 10, 1 | Invalid | InvalidInput | Fail |
| test_triangle_inequality_3 | 1, 1, 10 | Invalid | InvalidInput | Fail |
| test_right_triangle_1 | 3, 4, 5 | Right | Right | Pass |
| test_right_triangle_2 | 5, 12, 13 | Right | Right | Pass |
| test_right_triangle_3 | 6, 8, 10 | Right | Right | Pass |
| test_equilateral | 1, 1, 1 | Equilateral | Equilateral | Pass |
| test_isosceles_1 | 2, 2, 3 | Isosceles | Isosceles | Pass |
| test_isosceles_2 | 5, 5, 8 | Isosceles | Isosceles | Pass |
| test_scalene_1 | 6, 7, 8 | Scalene | Scalene | Pass |
| test_scalene_2 | 10, 12, 15 | Scalene | Scalene | Pass |
| test_invalid_1 | 1, 1, 2 | NotATriangle | NotATriangle | Pass |
| test_invalid_2 | 0, 0, 0 | InvalidInput | InvalidInput | Pass |
| test_invalid_3 | -1, -1, -1 | InvalidInput | InvalidInput | Pass |
| test_invalid_4 | 1, 10, 12 | NotATriangle | NotATriangle | Pass |
| test_non_numeric_1 | 'a', 3, 4 | TypeError | TypeError | Pass |
| test_non_numeric_2 | 3, 'b', 5 | TypeError | TypeError | Pass |
| test_non_numeric_3 | 3, 4, 'c' | TypeError | TypeError | Pass |
| test_non_numeric_4 | [1, 2, 3], 4, 5 | TypeError | TypeError | Pass |
| test_non_numeric_5 | None, 4, 5 | TypeError | TypeError | Pass |
| test_non_numeric_6 | 3.0, "4.0", 5.0 | TypeError | TypeError | Pass |
| test_triangle_inequality_1 | 10, 1, 1 | NotATriangle | NotATriangle | Pass |
| test_triangle_inequality_2 | 1, 10, 1 | NotATriangle | NotATriangle | Pass |
| test_triangle_inequality_3 | 1, 1, 10 | NotATriangle | NotATriangle | Pass |


# Test Report 2

| Test ID               | Input       | Expected Result | Actual Result  | Pass or Fail |
|-----------------------|-------------|-----------------|----------------|--------------|
| test_right_triangle_1 | 3, 4, 5     | Right           | Right          | Pass         |
| test_right_triangle_2 | 5, 12, 13   | Right           | Right          | Pass         |
| test_right_triangle_3 | 6, 8, 10    | Right           | Right          | Pass         |
| test_equilateral       | 1, 1, 1     | Equilateral     | Equilateral    | Pass         |
| test_isosceles_1       | 2, 2, 3     | Isosceles       | Isosceles      | Pass         |
| test_isosceles_2       | 5, 5, 8     | Isosceles       | Isosceles      | Pass         |
| test_scalene_1         | 6, 7, 8     | Scalene         | Scalene        | Pass         |
| test_scalene_2         | 10, 12, 15  | Scalene         | Scalene        | Pass         |
| test_invalid_1         | 1, 1, 2     | NotATriangle    | NotATriangle   | Pass         |
| test_invalid_2         | 0, 0, 0     | InvalidInput    | InvalidInput   | Pass         |
| test_invalid_3         | -1, -1, -1  | InvalidInput    | InvalidInput   | Pass         |
| test_invalid_4         | 1, 10, 12   | NotATriangle    | NotATriangle   | Pass         |
| test_non_numeric_1     | 'a', 3, 4   | TypeError       | TypeError      | Pass         |
| test_non_numeric_2     | 3, 'b', 5   | TypeError       | TypeError      | Pass         |
| test_non_numeric_3     | 3, 4, 'c'   | TypeError       | TypeError      | Pass         |
| test_non_numeric_4     | [1, 2, 3], 4, 5 | TypeError   | TypeError      | Pass         |
| test_non_numeric_5     | None, 4, 5  | TypeError       | TypeError      | Pass         |
| test_non_numeric_6     | 3.0, "4.0", 5.0 | TypeError   | TypeError      | Pass         |
| test_triangle_inequality_1 | 10, 1, 1 | NotATriangle  | NotATriangle   | Pass         |
| test_triangle_inequality_2 | 1, 10, 1 | NotATriangle  | NotATriangle   | Pass         |
| test_triangle_inequality_3 | 1, 1, 10 | NotATriangle  | NotATriangle   | Pass         |

# Final Report

|                 | **Test Run 1** | **Test Run 2** |
|-----------------|------------|------------|
| **Tests Planned** | 35         | 20         |
| **Tests Executed**| 35         | 20         |
| **Tests Passed**  | 15         | 20         |
| **Defects Found** | assuming c was the largest input, comparing b to itself, having a floating semi colon | None       |
| **Defects Fixed** | all        | None       |

# Reflection

I learned that sometimes programs come in differently than I would've initially wanted to function to be set up. I realized that it is more important to fix whats given, than to create a new solution because of the overhead that gives when working with larger systems.

[![<KensayS>](https://circleci.com/gh/<KensayS>
/<Triangle567>.svg?style=svg)](https://app.circleci.com/pipelines/github
/<KensayS>/<Triangle567>?branch=main&filter=all)