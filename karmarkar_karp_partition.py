
from  multi_set import MultiSet
from  reverse_priority_queue import ReversePriorityQueue

def karmarkar_karp_partition(numbers):

    heap = ReversePriorityQueue()

    for value in numbers:
        heap_value = (value, value)
        heap.put(heap_value)

    while(heap.qsize() > 1):
        a = heap.get()
        b = heap.get()
        print("a = {}\nb = {}".format(a, b))

        diff = (a[0] - b[0], a[1] - b[1])

        heap.put(diff)

    return heap.get()

def main():

    multi = MultiSet(10,5)

    print(multi.set)

    a = karmarkar_karp_partition(multi.set)

    print(a)

if __name__ == "__main__":
    main()

# int karmarkarKarpPartition(int[] baseArr) {	
#     // create max heap	
#     PriorityQueue<Integer> heap = new PriorityQueue<Integer>(baseArr.length, REVERSE_INT_CMP);

#     for (int value : baseArr) {		
#         heap.add(value);	
#     }

#     while(heap.size() > 1) {
#         int val1 = heap.poll();	
#         int val2 = heap.poll();	
#         heap.add(val1 - val2);
#     }

#     return heap.poll();
# }