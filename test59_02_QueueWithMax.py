# -*- coding:utf-8 -*-


class Queue(object):

    def __init__(self):
        self.elem = []

    def push_back(self,x):
        self.elem.append(x)

    def pop_front(self):
        self.elem.reverse()
        self.elem.pop()
        self.elem.reverse()

    def max_value(self):
        # write code here
        if not self.elem :
            return []

        max_num = max(self.elem[0:len(self.elem)])
        return max_num


if __name__=="__main__":
    q=Queue()
    q.push_back(1)
    q.push_back(2)
    q.push_back(3)
    q.push_back(4)
    print(q.elem)
    q.pop_front()
    print(q.elem)
    print(q.max_value())



