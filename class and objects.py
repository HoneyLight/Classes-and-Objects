class Student:
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, new_name):
        return "the name of the user is", new_name

    def change_age(self, new_age):
        return "the new age is", int(new_age)

    def add_track(self, new_track):
        return "the new track is", new_track

    def get_score(self):
        return "the new score is", self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())
