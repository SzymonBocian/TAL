
from queue import PriorityQueue
 
class ReversePriorityQueue(PriorityQueue):

    def put(self, tup):
        # print("tup = {}".format(tup))
        newtup = tup[0] * -1, tup[1]
        PriorityQueue.put(self, newtup)

    def get(self):
        tup = PriorityQueue.get(self)
        newtup = tup[0] * -1, tup[1]
        return newtup

def main():
    pass


if __name__ == "__main__":
    main()