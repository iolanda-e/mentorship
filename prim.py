import math

#1 Check if number is prime

def prime( x):
    if x<2:
        return 0
    if x==2:
        return 1
    if x%2==0:
        return 0
    for i in range(3, int(math.sqrt(x)),2):
        if x%i==0:
            return 0
    return 1

#2 Check if string is a palindrome

def palindrome(sir):
    return sir==sir[::-1]


#3 Get highest common denominator for 2 numbers

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)


#4 Reverse words in a sentence

def reverse_words(sir):
    words=sir.split()
    rev_words=[]
    for i in range(len(words)-1, -1, -1):
        rev_words.append(words[i])
    return ' '.join(rev_words)


#5 Reverse each word in a sentence

def reverse_each_word(sir):
    words=sir.split()
    rev_words=[]
    for i in range(len(words)):
        rev_words.append(words[i][::-1])
    return ' '.join(rev_words)

#6 Bubble sort for lists

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
    return lista


#7 Merge sort a list using slicing

def merge_sort(lista):
    if len(lista)<=1:
        return lista
    mid=len(lista)//2
    st=merge_sort(lista[:mid])
    dr=merge_sort(lista[mid:])

    return interclasare(st,dr)

def interclasare(st,dr):
    result=[]
    i=0
    j=0
    while i<len(st) and j<len(dr):
        if st[i]<dr[j]:
            result.append(st[i])
            i+=1
        else:
            result.append(dr[j])
            j+=1

    result.extend(st[i:])
    result.extend(dr[j:])
    return result



#8 N-th fibonacci, N-th prime number, N-th factorial (modulo very big number)

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


def eratostene(limita):
    prim=[1 for _ in range (limita)]
    prim[0]=prim[1]=0

    for i in range(2, limita):
        if prim[i]:
            for j in range(i*i, limita, i):
                prim[j]=0
    result=[]
    for i in range(limita):
        if prim[i]:
            result.append(i)
    return result

def n_prim(n):
    prim=eratostene(n*10)
    return prim[n-1]

def n_fact(n, mod):
    result=1
    for i in range(2, n+1):
        result=result*i%mod
    return result

#print(n_fact(100, 10**9 + 7))

#9 Letter and word frequency for all text in a file

def frequency(file):
    with (open(file) as reader):
        text=reader.read().lower()
        words=text.split()
        words=[w.strip('. ,') for w in words]
        word_frecv={}
        letter_frecv={}
        for w in words:
            word_frecv[w]=word_frecv.get(w,0)+1
        for ch in text:
            if ch.isalpha():
                letter_frecv[ch]=letter_frecv.get(ch,0)+1
    print(word_frecv)
    print(letter_frecv)

#10 Explicit power implementation with log n time complexity

def power(x, y ):
    if y==0:
        return 1
    else:
        if y%2==0:
             return power(x, y/2)*power(x, y/2)
        else:
            return x * power(x, (y-1)/2) * power(x, (y-1)/2)

#11 Trie tree using nested dictionaries


def insert(trie, word):
    node=trie
    for letter in word:
        if letter not in node:
            node[letter]={}
        node=node[letter]
    node['#']=True

def search(trie, word):
    node=trie
    for letter in word:
        if letter not in node:
            return False
        node = node[letter]
    return '#' in node

trie = {}

insert(trie, "car")
insert(trie, "cart")
insert(trie, "cat")
insert(trie, "do")
insert(trie, "door")

print(search(trie, "do"))

#print(power(3,5))
#frequency("text.txt")
#print(n_prim(5))
#print(fibonacci(6))
#print(merge_sort([1,7,3,6,3,6,-3,4]))
#print(bubble_sort([1,7,3,6,3,6,-3,4]))
#print(reverse_each_word("ana are mere"))
#print(reverse_words("ana are mere"))
#print(gcd(10, 45))
#print(palindrome("ana"))
#print(prime(2))