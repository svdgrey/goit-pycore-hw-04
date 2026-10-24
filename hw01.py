
# Calculate the total and average salary of employees from a specified file.
# Each line in the file contains an employee's name and salary separated by a comma.
# parameters:
#   path: the path to the employee data file.
# The function returns a tuple containing employees total and average salary, or raises an exception if an error occurs.
def total_salary(path: str) -> tuple[int, float]:
    with open(path, "r", encoding='utf-8') as emps_file:
        salary_total = 0    
        employees_count = 0
        for line_number, line in enumerate(emps_file, start=1):
            line = line.rstrip("\r\n")
            try:
                _, employee_salary = line.split(',')
                employee_salary = int(employee_salary)
                employees_count += 1
                salary_total += employee_salary
            except ValueError as e:
                raise ValueError(f"Invalid employee record at line {line_number}: {line}") from e

        if employees_count == 0:
            raise ValueError("No employee's salary records found.")

        salary_average = salary_total / employees_count  

        return salary_total, salary_average



# Example usage:
def main():
    try:

        # У завданні є певна неоднозначність щодо точності представлення результату.
        # Критерії оцінювання вимагають:
        #   "Функція повинна точно обчислювати загальну та середню суми."
        # Водночас очікуваний результат наведено без дробової частини:
        #   "Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000"
        #   
        # Тому я вирішив обчислювати середню зарплату як float, щоб зберегти
        # дробову частину результату ділення, якщо вона є.
        # Для відображення результату використовую формат із двома знаками після коми.

        total, average = total_salary("assets/salaries.txt")
        
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.2f}")
    except FileNotFoundError as e:
        print(f"Salary file not found: {e}")
    except ValueError as e:
        print(f"Salary file is corrupted (invalid data): {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
