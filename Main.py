import random, timeit

##
## 여기에 세 가지 정렬함수를 위한 코드를...
##
def quick_sort(A, first, last):
		global Qc
		global Qs
		if first >= last: return
		left, right = first+1, last
		pivot = A[first]
		while left <= right:
				while left <= last and A[left] < pivot:
					left += 1 
					Qc+=1

				while right > first and A[right] >= pivot:
					right -= 1 
					Qc+=1

				if left <= right: # swap A[left] and A[right]
					A[left], A[right] = A[right], A[left]
					left += 1
					right -= 1 
					Qs+=1
    # place pivot at the right place
		A[first], A[right] = A[right], A[first]
		quick_sort(A, first, right-1)
		quick_sort(A, right+1, last)

def merge_sort(A, first, last): # merge sort A[first] ~ A[last]
		global Mc
		global Ms
		if first >= last: return
		middle = (first+last)//2
		merge_sort(A, first, middle)
		merge_sort(A, middle+1, last)
		B = []
		i = first
		j = middle+1
		while i <= middle and j <= last:
			if A[i] <= A[j]:
				Mc+=1
				B.append(A[i])
				i += 1
			else:
				B.append(A[j])
				j += 1

		for i in range(i, middle+1): B.append(A[i])
		for j in range(j, last+1): B.append(A[j])
		for k in range(first, last+1): 
			A[k] = B[k-first]
			Ms+=1
			
def heapify(A,k,n): 
		global Hc
		global Hs
		largest=k
		left_index=2*k+1
		right_index=2*k+2
		if left_index<n and A[left_index]>A[largest]:
			largest=left_index
			Hc+=1
		if right_index<n and A[right_index]>A[largest]:
			Hc+=1
			largest=right_index
		if largest!=k:
			A[largest],A[k]=A[k],A[largest]
			Hs+=1
			heapify(A,largest,n)
	
		
def heap_sort(A):
		global Hc
		global Hs
		n = len(A)	
		for i in range(len(A)//2-1, -1, -1):
			heapify(A,i,n)
		for i in range(n-1,0,-1):
			A[0],A[i]=A[i],A[0]
			Hs+=1
			heapify(A,0,i)
		return A

# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환 횟수 저장
#

Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
