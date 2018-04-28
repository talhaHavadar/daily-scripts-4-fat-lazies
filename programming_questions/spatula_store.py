"""
Selling Spatulas Problem

Still I need to do some improvements and bugfixes
"""
from sys import float_info
MINIMUM_FLOAT = -float_info.max

class Sale(object):
    def __init__(self, start, profit):
        self.start, self.profit = start, profit
        self.previous = None
        self.next = None
    
    def net_profit_from_openning(self):
        if self.previous:
            return self.net_profit_related_to_previous() + self.previous.net_profit_from_openning()
        return self.profit

    def net_profit_related_to_previous(self):
        if self.previous:
            return self.profit - self.cost_between(self.previous)
        return self.profit

    def cost_between(self, sale):
        if self.start > sale.start:
            return (self.start - sale.start + 1) * 0.08
        else:
            return (sale.start - self.start + 1) * 0.08            

    def __str__(self):
        return "{start=%s, profit=%s}" % (self.start, self.profit)

    def __repr__(self):
        return "{start=%s, profit=%s}" % (self.start, self.profit)

class Store(object):
    
    def __init__(self):
        self.head = None
        self.tail = None

    def add_sale(self, sale):
        if self.head is None:
            self.head = sale
            self.tail = sale
        else:
            self.tail.next = sale
            sale.previous = self.tail
            self.tail = sale
    
    def __get_best_profit__(self, computations):
        max_profit = MINIMUM_FLOAT
        best_profit_candidates = list()

        for computation in computations:
            l = computation["list"]
            duration = l[-1].start - l[0].start
            if len(l) == 1:
                computation["total_profit"] -= 0.08
            elif len(l) > 1:
                computation["total_profit"] += 0.08
            
            if computation["total_profit"] > max_profit:
                max_profit = computation["total_profit"]
                computation["period_length"] = 1 if duration == 0 else duration
                best_profit_candidates.append(computation)
            elif computation["total_profit"] == max_profit:
                computation["period_length"] = 1 if duration == 0 else duration
                best_profit_candidates.append(computation)

        best_profit_candidates = sorted(best_profit_candidates, key=lambda x: x["list"][0].start) 
        return min(best_profit_candidates, key=lambda x: x["period_length"])        
        
    def compute_profit_periods(self):
        node = self.head

        computations = [{"list": [], "total_profit": None}]
        computation_list = 0
        while node:
            if not computations[computation_list]["list"]:
                computations[computation_list]["list"].append(node)
                computations[computation_list]["total_profit"] = node.profit
                node = node.next
                continue

            new_profit = computations[computation_list]["total_profit"] + node.net_profit_related_to_previous()
            
            if new_profit < node.profit:
                if computations[computation_list]["total_profit"] < node.profit:
                    if computations[computation_list]["list"] and node.previous.start != computations[computation_list]["list"][-1].start:
                        computations.append({"list": [], "total_profit": None})
                        computation_list += 1
                    computations[computation_list]["list"] = [node]
                    computations[computation_list]["total_profit"] = node.profit
            elif new_profit >= computations[computation_list]["total_profit"]:
                if computations[computation_list]["list"] and node.previous.start != computations[computation_list]["list"][-1].start:
                        computations.append({"list": [], "total_profit": None})
                        new_profit = node.profit
                        computation_list += 1
                computations[computation_list]["list"].append(node)
                computations[computation_list]["total_profit"] = new_profit

            node = node.next
        return self.__get_best_profit__(computations)

def main(stores):
    for store in stores:
        profit = store.compute_profit_periods()
        if profit["total_profit"] <= 0:
            print("no profit")
        else:
            print("%.2f" % profit["total_profit"], profit["list"][0].start, profit["list"][-1].start)

if __name__ == '__main__':
    stores = []
    while True:
        sales_count = int(input())
        if sales_count == 0:
            break
        store = Store()
        for i in range(sales_count):
            start_time, profit = str(input()).split(" ")
            store.add_sale(Sale(int(start_time), float(profit)))
        stores.append(store)
    
    main(stores)