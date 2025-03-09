# Proxy

class College:
    def studyInCollege(self):
        print("College study")


class CollegeProxy:
    def __init__(self):
        self.college = College()
        self.feeBalance = 1000
        self.college = None

    def studyInCollege(self):
        # print("Proxy in action. Checking to see if the college is available")
        # self.college.studyInCollege()
        print("Proxy in action. Checking to see if the balance of student is clear or not...")
        if self.feeBalance <= 500:
            # If the balance is less than 500, let him study.
            self.college = College()
            self.college.studyInCollege()
        else:

            # Otherwise, don't instantiate the college object.
            print("Your fee balance is greater than 500, first pay the fee")

# """main method"""
#
# if __name__ == "__main__":
#
#     # Instantiate the Proxy
#     collegeProxy = CollegeProxy()
#
#     # Client attempting to study in the college at the default balance of 1000.
#     # Logically, since he / she cannot study with such balance,
#     # there is no need to make the college object.
#     collegeProxy.studyInCollege()
#
#     # Altering the balance of the student
#     collegeProxy.feeBalance = 100
#
#     # Client attempting to study in college at the balance of 100. Should succeed.
#     collegeProxy.studyInCollege()

# Usage
collegeProxy = CollegeProxy()
collegeProxy.studyInCollege()
collegeProxy.feeBalance = 100
collegeProxy.studyInCollege()