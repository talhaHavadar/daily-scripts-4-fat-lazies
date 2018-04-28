#coding: utf-8
import itertools
import builtins
import re

class BioStr(str):
    def insert_char_to(self, c, index):
        """
        Returns a newly created strıng so string itself wont be effected from this change
        """
        return self[:index] + c + self[index:]

    def count_iter(self, s):
        count = start = 0
        while True:
            start = self.find(s, start) + 1
            if start > 0:
                count+=1
            else:
                return count

BIO_CHARS = ["A", "G", "C", "T"]

def get_type2_of(s):
    results = set()
    for c in itertools.combinations(s, len(s) - 1):
        results.add(BioStr("".join(c)))
    return list(results)

def get_type3_of(s):
    bstr = BioStr(s)
    results = set()
    for i in range(len(bstr) + 1):
        for c in BIO_CHARS:
            results.add(bstr.insert_char_to(c, i))
    return list(results)

def main(test_cases):
    for case in test_cases:
        S, L = case.split(" ")
        L = BioStr(L)
        type2_list = get_type2_of(S)
        type3_list = get_type3_of(S)
        type2_count = type3_count = 0
        for s in type2_list:
            type2_count += L.count_iter(s)
        for s in type3_list:
            type3_count += L.count_iter(s)
        print(L.count_iter(S), type2_count, type3_count)
        
if __name__ == '__main__':
    test_cases = list()
    while True:
        case = input()
        if case is "0":
            break
        test_cases.append(case)
    main(test_cases)
    
