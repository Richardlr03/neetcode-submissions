class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        no_eat = 0
        while no_eat < len(students) and students:
            if students[0] == sandwiches[0]:
                no_eat = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                no_eat += 1
                students.append(students.pop(0))

        return len(students)