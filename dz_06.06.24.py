class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience
        self._classes_taught = []

    @property
    def name(self):
        return self._name

    @property
    def education(self):
        return self._education

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    def add_class(self, graider):
        self._classes_taught.append(graider)

    def remove_class(self):
        if self._classes_taught:
            return self._classes_taught.pop()
        else:
            return "Нет занятий у этого преподавателя"

teacher1 = Teacher("Ольга Петрова", "БГПУ", "15")
teacher1.add_class('1А')
teacher1.add_class('2Г')
print(teacher1.__getstate__())

teacher1.remove_class()
print(teacher1.__getstate__())
