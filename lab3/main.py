import LupaPupa

worker1 = LupaPupa.Pupa(100)
worker2 = LupaPupa.Lupa(100)
accountant = LupaPupa.Accountant()

# Accountant methods test
accountant.get_worker_salary(worker1)
accountant.give_salary(worker1)
accountant.set_worker_salary(worker1, 150)
accountant.give_salary(worker1)

# Worker methods check
worker1.cash
worker2.cash
worker1._do_work("in1.txt", "in2.txt")
worker2._do_work("in1.txt", "in2.txt")
accountant.give_salary(worker1)
accountant.give_salary(worker2)
worker1.cash
worker2.cash





