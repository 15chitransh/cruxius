#list return sum
class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        list=[]
        s=len(numbers)
        for i in range(0,s):
            for j in range(0,s):
                if (numbers[i]+numbers[j]) ==target_sum:
                   list.append((i,j))
                   #print str(names)[1:-1]

                
        
        return print(*list,sep="\n")
print(TwoSum.find_two_sum([1, 3, 5, 7, 9], 12))