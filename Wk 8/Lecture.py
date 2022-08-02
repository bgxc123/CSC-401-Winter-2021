class Queue:
    def __init__(self,lst=[]):
        self.q = list(lst) #prevent two lists from being the same
    def __repr__(self):
        return f'Queue({self.q})'
    def enqueue(self,item):
        self.q.append(item)
    def dequeue(self):
        return self.q.pop(0)
    def __getitem__(self,index):
        return self.q[index]
    def __len__(self):
        return len(self.q)
    def __eq__(self,other):
        return self.q == other.q
    def __add__(self,other):
        return Queue(self.q + other.q) #return new queue, not list
    
class MyList(list):
    #override repr
    def __repr__(self):
        ans = '['
        for item in self:
            ans += repr(item) + ','
        return ans[:-1] + ']'
    #added method
    def apply(self,func):
        for i in range(len(self)):
            self[i] = func(self[i])
    
            
    
