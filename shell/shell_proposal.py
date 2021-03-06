from random import random, randint
from orcamentos.core.models import Proposal, Category, Work, Person, Employee, Seller, NumLastProposal
from shell.gen_random_values import gen_string, gen_date, gen_decimal

status_list = ('c', 'elab', 'p', 'co', 'a')

REPEAT = 100

# Return min id of work
try:
    min_work_pk = Work.objects.order_by('pk')[0].pk
except IndexError:
    min_work_pk = None

# Return max id of work
try:
    max_work_pk = Work.objects.latest('pk').id
except Work.DoesNotExist:
    max_work_pk = None

for i in range(1, REPEAT + 1):
    c = randint(1, 8)
    category = Category.objects.get(pk=c)
    description = gen_string(30)
    w = randint(min_work_pk, max_work_pk)
    work = Work.objects.get(pk=w)
    p = randint(1, 50)
    person = Person.objects.get(pk=p)
    e = randint(1, 9)
    employee = Employee.objects.get(pk=e)
    s = randint(1, 3)
    seller = Seller.objects.get(pk=s)
    sl = randint(0, 4)
    status = status_list[sl]
    if status == 'co' or status == 'a':
        date_conclusion = gen_date(min_year=2015, max_year=2015)
        price = gen_decimal(9, 2)
    else:
        date_conclusion = None
        price = 0
    obj = Proposal(
        num_prop=i,
        type_prop='R',
        num_type_prop=0,
        category=category,
        description=description,
        work=work,
        person=person,
        employee=employee,
        seller=seller,
        status=status,
        date_conclusion=date_conclusion,
        price=price,
    )
    obj.save()

num_last_proposal = NumLastProposal.objects.get(pk=1)
num_last_proposal.num_last_prop = REPEAT
num_last_proposal.save()
print('%d Proposals salvo com sucesso.' % REPEAT)
