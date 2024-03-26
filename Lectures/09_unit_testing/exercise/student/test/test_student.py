from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Mitko", {})
        self.student_with_courses = Student("Teodor", {"math": ["x + y = z"]})

    def test_correct_init(self):
        self.assertEqual("Mitko", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["x + y = z"]}, self.student_with_courses.courses)

    def test_enroll_with_course_already_in_courses_and_appending_notes(self):
        result = self.student_with_courses.enroll("math", ["Reaper", "The Black Lion"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"math": ["x + y = z", "Reaper", "The Black Lion"]}, self.student_with_courses.courses)

    def test_enroll_with_third_param_Y_string_equals_add_success(self):
        result = self.student.enroll("Sci-Fi", ["Hadrian", "Halfmortal"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Sci-Fi": ["Hadrian", "Halfmortal"]}, self.student.courses)

    def test_enroll_with_third_param_empty_string_equals_add_success(self):
        result = self.student.enroll("Fantasy", ["Gabriel", "The Black Lion"])

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Fantasy": ["Gabriel", "The Black Lion"]}, self.student.courses)

    def test_enroll_with_third_param_different_then_empty_string_or_Y(self):
        result = self.student.enroll("math", ["yes", "no"], "no")

        self.assertEqual("Course has been added.", result)
        self.assertEqual({"math": []}, self.student.courses)

    def test_add_notes_with_course_in_courses(self):
        result = self.student_with_courses.add_notes("math", "3 + 7 = 10")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"math": ["x + y = z", "3 + 7 = 10"]}, self.student_with_courses.courses)

    def test_add_notes_with_course_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "Tralala")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_course_exist(self):
        result = self.student_with_courses.leave_course("math")
        self.assertEqual("Course has been removed", result)

    def test_leave_course_course_not_found_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Fantasy")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
