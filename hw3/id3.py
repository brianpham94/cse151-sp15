from collections import namedtuple, defaultdict
from math import log

data_train = open('hw3train.txt').readlines()
data_test = open('hw3test.txt').readlines()

Flower = namedtuple('Flower', ['p_width', 'p_length', 's_width', 's_length', 
                               'species'])

flowers = [Flower(*elm.split()) for elm in data_train]

def is_impure(ls):
    for num in [x[-1] for x in ls]:
        if num != ls[0][-1]:
            return True
    return False

def is_pure(ls):
    return not is_impure(ls)

def entropy(ls,idx=-1):
    label_counts = {}
    for label in set([lab[idx] for lab in ls]):
        label_counts[label] = [x[idx] for x in ls].count(label)

    return sum([-1 * float(x)/len(ls) * log(float(x)/len(ls), 2) for x 
        in label_counts.values()])

def info_gain(attr, data):
    attr_counts = {}
    ent_sub = 0.0
    for atr in set([at[attr] for at in data]):
        attr_counts[atr] = [a[attr] for a in data].count(attr)

    for val in attr_counts.keys():
        p = attr_counts/len(data)
        ent_sub += p * entropy([elm for elm in data if elm[attr] == val])

    return entropy(data) - ent_sub

def best_feature(data):
    ENT = entropy(data)
    feature_num = 4

def build_tree(data):
    if is_pure(data):
        return data[0].species
    best_feature(data)

build_tree(flowers)

''' Bonus code saving for later
    h = defaultdict(lambda: {})
    for x in data:
        for field in x._fields:
            if getattr(x,field) not in h[field]:
                h[field][getattr(x,field)] = 1
            else:
                h[field][getattr(x,field)] += 1
    print h
'''
