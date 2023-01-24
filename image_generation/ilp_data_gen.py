import itertools
import random

from dilpst.src.ilp_problem import ILPProblem
from scene import CLEVRObject, CLEVRSize, CLEVRColor, CLEVRShape, CLEVRMaterial

def ilp_problem2scenes(ilp_problem):
    # an example is a list of clevr objects
    pos_scenes = [objects2scene(x) for x in ilp_problem.pos_examples]
    neg_scenes = [objects2scene(x) for x in ilp_problem.neg_examples]
    bk_scenes = [objects2scene(x) for x in ilp_problem.backgrounds]

def objects2scene(x):
    pass

"""
full attributes
colors = ["cyan","blue","yellow","purple","red","green","gray","brown"]
shapes = ["sphere","cube","cylinder"]
sizes = ["large","small"]
materials = ["rubber","metal"]
"""

colors = ["red", "gray", "cyan", "yellow"]
shapes = ["sphere"]
sizes = ["large"]
materials = ["metal"]

def gen_all_properties():
    xs = itertools.product(colors, shapes, sizes, materials)
    ys = []
    for x in xs:
        color = CLEVRColor(x[0])
        shape = CLEVRShape(x[1])
        size = CLEVRSize(x[2])
        material = CLEVRMaterial(x[3])
        obj = CLEVRObject(color=color, shape=shape, size=size, material=material)
        ys.append(obj)
    return ys


def random_choices(ls, k):
    if k == 0:
        return []
    else:
        return [random.choice(ls) for i in range(k)]


def get_sublist(ls):
    if len(ls) == 1:
        return [ls] + [[]]
    else:
        return [ls] + get_sublist(ls[1:])

def get_ilp_problem(name, n):
    if name == "member":
        return MemberProblem(n)
    elif name == "delete":
        return DeleteProblem(n)
    elif name == "append":
        return AppendProblem(n)
    elif name == "sort":
        return SortProblem(n)


class MemberProblem(ILPProblem):
    def __init__(self, n=30, noise_rate=0.0, max_len=3, min_len=3):
        self.name = "member"
        self.pos_examples = []
        self.neg_examples = []
        self.backgrounds = []
        self.init_clauses = []
        #p_ = Predicate('.', 1)
        #false = Atom(p_, [Const('__F__')])
        #true = Atom(p_, [Const('__T__')])
        #self.facts = [false, true]
        self.lang = None
        self.noise_rate = noise_rate
        self.n = n
        self.max_len = max_len
        self.min_len = min_len
        #self.symbols = list('abc')
        self.symbols = gen_all_properties()

        # init dataset
        self.get_pos_examples()
        self.get_neg_examples()
        self.get_backgrounds()

    def get_pos_examples(self):
        i = 0
        while len(self.pos_examples) < self.n:
            n = random.randint(self.min_len, self.max_len)
            x = random.choice(self.symbols)
            ls = random_choices(self.symbols, k=n)
            if x in ls:
                self.pos_examples.append(([x], ls))
                #term1 = Const(x)
                #term2 = list_to_term(ls, self.funcs[0])
                #atom = Atom(self.preds[0], [term1, term2])
                #self.pos_examples.append(atom)

    def get_neg_examples(self):
        i = 0
        while i < self.n:
            n = random.randint(1, self.max_len)
            # 長さnで満たすもの出すまで繰り返し
            flag = True
            while flag:
                x = random.choice(self.symbols)
                ls = random_choices(self.symbols, n)
                if not x in ls:
                    self.neg_examples.append(([x], ls))
                    #atom = Atom(self.preds[0], [
                    #            Const(x), list_to_term(ls, self.funcs[0])])
                    #self.neg_examples.append(atom)
                    i += 1
                    flag = False

    def get_backgrounds(self):
        # pass
        #self.backgrounds.append(Atom(self.preds[0], [Const('*'), Const('*')]))
        for s in self.symbols:
            self.backgrounds.append(([s], [s]))
            #atom = Atom(self.preds[0], [
            #            Const(s), list_to_term([s], self.funcs[0])])
            #self.backgrounds.append(atom)
        #     self.backgrounds.append(atom)
        # for s in self.symbols:
        #    self.backgrounds.append(Atom(self.preds[0], [Const(s), Const(s)]))

    def get_clauses(self):
        clause1 = Clause(Atom(self.preds[0], [Var('X'), Var('Y')]), [])
        self.clauses = [clause1]

    def get_facts(self):
        terms = []
        for i in range(1, self.max_len+1):
            i_len_list = list(itertools.product(self.symbols, repeat=i))
            for l in i_len_list:
                term = list_to_term(l, self.funcs[0])
                terms.append(term)
        # generate facts
        args1 = [term for term in terms if term.max_depth() <= 0]
        args2 = [term for term in terms]
        for pair in list(itertools.product(args1, args2)):
            self.facts.append(Atom(self.preds[0], list(pair)))

    def get_templates(self):
        self.templates = [RuleTemplate(body_num=1, const_num=0),
                          RuleTemplate(body_num=0, const_num=0)]

    def get_language(self):
        self.preds = [Predicate('member', 2)]
        self.funcs = [FuncSymbol('f', 2)]
        self.consts = [Const(x) for x in self.symbols]
        self.lang = Language(preds=self.preds, funcs=self.funcs,
                             consts=self.consts)



def delete(a, ls):
    result = []
    count = 0
    for x in ls:
        if a == x and count == 0:
            count += 1
            next
        else:
            result.append(x)
    return result


class AppendProblem(ILPProblem):
    def __init__(self, n=50, noise_rate=0.0, max_len=3, min_len=3):
        self.name = "append"
        self.pos_examples = []
        self.neg_examples = []
        self.backgrounds = []
        self.init_clauses = []
        self.lang = None
        self.noise_rate = noise_rate
        self.n = n
        self.max_len = max_len
        self.min_len = min_len
        #self.symbols = list('abc')
        self.symbols = gen_all_properties()

        # init dataset
        self.get_pos_examples()
        self.get_neg_examples()
        self.get_backgrounds()

    def get_pos_examples(self):
        i = 0
        while len(self.pos_examples) < self.n:
            a1 = random.choice(self.symbols)

            n2 = random.randint(self.min_len-1, int(self.max_len)-1)
            ls2 = random_choices(self.symbols, k=n2)

            self.pos_examples.append(([a1], ls2, [a1] + ls2))
            i += 1

    def get_neg_examples(self):
        i = 0
        while i < self.n:
            a1 = random.choice(self.symbols)

            n2 = random.randint(self.min_len-1, int(self.max_len)-1)
            ls2 = random_choices(self.symbols, k=n2)
            n3 = random.randint(self.min_len, int(self.max_len))
            ls3 = random_choices(self.symbols, k=n3)
            if [a1] + ls2 != ls3:
                self.neg_examples.append(([a1], ls2, ls3))
                i += 1


    def get_backgrounds(self):
        for s in self.symbols:
            self.backgrounds.append(([], [], []))

    def get_clauses(self):
        clause1 = Clause(
            Atom(self.preds[0], [Var('X'), Var('Y'), Var('Z')]), [])
        self.clauses = [clause1]

    def get_facts(self):
        pass

    def get_templates(self):
        self.templates = [RuleTemplate(body_num=1, const_num=0),
                          RuleTemplate(body_num=0, const_num=1)]

    def get_language(self):
        self.preds = [Predicate('append', 3)]
        self.funcs = [FuncSymbol('f', 2)]
        self.consts = [Const(x) for x in self.symbols]
        self.lang = Language(preds=self.preds, funcs=self.funcs,
                             consts=self.consts)


class DeleteProblem(ILPProblem):
    def __init__(self, n=50, noise_rate=0.0, max_len=3, min_len=3):
        self.name = "delete"
        self.pos_examples = []
        self.neg_examples = []
        self.backgrounds = []
        self.init_clauses = []
        self.lang = None
        self.noise_rate = noise_rate
        self.n = n
        self.max_len = max_len
        self.min_len = min_len
        #self.symbols = list('abc')
        self.symbols = gen_all_properties()

        # init dataset
        self.get_pos_examples()
        self.get_neg_examples()
        self.get_backgrounds()

    def get_pos_examples(self):
        i = 0
        while len(self.pos_examples) < self.n:
            a1 = random.choice(self.symbols)

            n2 = random.randint(self.min_len, int(self.max_len))
            ls2 = random_choices(self.symbols, k=n2)
            if a1 in ls2:
                self.pos_examples.append(([a1], ls2, delete(a1, ls2)))
                i += 1

    def get_neg_examples(self):
        i = 0
        while i < self.n:
            a1 = random.choice(self.symbols)

            n2 = random.randint(self.min_len, int(self.max_len))
            ls2 = random_choices(self.symbols, k=n2)
            n3 = random.randint(self.min_len-1, int(self.max_len)-1)
            ls3 = random_choices(self.symbols, k=n3)
            if a1 in ls2 and delete(a1, ls2) != ls3:
                self.neg_examples.append(([a1], ls2, ls3))
                i += 1

    def get_backgrounds(self):
        for s in self.symbols:
            self.backgrounds.append(([s], [s], []))

    def get_clauses(self):
        clause1 = Clause(
            Atom(self.preds[0], [Var('X'), Var('Y'), Var('Z')]), [])
        self.clauses = [clause1]

    def get_facts(self):
        pass

    def get_templates(self):
        self.templates = [RuleTemplate(body_num=1, const_num=0),
                          RuleTemplate(body_num=0, const_num=1)]

    def get_language(self):
        self.preds = [Predicate('delete', 3)]
        self.funcs = [FuncSymbol('f', 2)]
        self.consts = [Const(x) for x in self.symbols]
        self.lang = Language(preds=self.preds, funcs=self.funcs,
                             consts=self.consts)



class SortProblem(ILPProblem):
    def __init__(self, n=50, noise_rate=0.0, max_len=3, min_len=3):
        self.name = "sort"
        self.pos_examples = []
        self.neg_examples = []
        self.backgrounds = []
        self.init_clauses = []
        self.lang = None
        self.noise_rate = noise_rate
        self.n = n
        self.max_len = max_len
        self.min_len = min_len
        #self.symbols = list('abc')
        self.symbols = gen_all_properties()

        # init dataset
        self.get_pos_examples()
        self.get_neg_examples()
        self.get_backgrounds()

    def get_pos_examples(self):
        i = 0
        while len(self.pos_examples) < self.n:
            a1 = random.choice(self.symbols)

            n1 = random.randint(self.min_len, self.max_len)
            ls = random_choices(self.symbols, k=n1)
            ls_sorted = sorted(ls)

            self.pos_examples.append((ls, ls_sorted))
            i += 1


    def get_neg_examples(self):
        i = 0
        while i < self.n:
            n1 = random.randint(self.min_len, self.max_len)
            ls1 = random_choices(self.symbols, k=n1)
            ls2 = random_choices(self.symbols, k=n1)
            if sorted(ls1) != ls2:
                self.neg_examples.append((ls1, ls2))
                i += 1

    def get_backgrounds(self):
        for s in self.symbols:
            #atom = Atom(self.preds[0], [Const(s), list_to_term(
            #    [s], self.funcs[0]), Const('*')])
            self.backgrounds.append(([s], [s], []))
        #atom = Atom(self.preds[0], [Const('*'), Const('*'), Const('*')])
        # self.backgrounds.append(atom)

    def get_clauses(self):
        clause1 = Clause(
            Atom(self.preds[0], [Var('X'), Var('Y'), Var('Z')]), [])
        self.clauses = [clause1]

    def get_facts(self):
        pass

    def get_templates(self):
        self.templates = [RuleTemplate(body_num=1, const_num=0),
                          RuleTemplate(body_num=0, const_num=1)]

    def get_language(self):
        self.preds = [Predicate('delete', 3)]
        self.funcs = [FuncSymbol('f', 2)]
        self.consts = [Const(x) for x in self.symbols]
        self.lang = Language(preds=self.preds, funcs=self.funcs,
                             consts=self.consts)
