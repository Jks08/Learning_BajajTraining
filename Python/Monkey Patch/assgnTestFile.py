class emp:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def bonus_to_give(self,bonus=0.1):
        self.bonus = bonus
        return self.bonus

    def gross_salary(self):
        return "Gross Salary after Bonus of " + str(self.bonus) + " is: " + str(self.salary + self.salary*self.bonus)