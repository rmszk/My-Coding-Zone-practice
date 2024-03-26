info = {
    "name" : "Rao Muhammad Shahroz Khan",
    "father" : "Rao Abdul Munim Khan",
    "age" : 23,
    "number" : "03028124650",
    "subject" : {
        "phy" : 97,
        "chem" : 80,
        "math" : 70
    }
}
print(info)
print(info.keys())   #return all keys
print(info.values()) #return all values
print(info.items())  #returns all (key,val) pairs as tuple
pairs = list(info.items())
print(pairs[0])
print(info.get("subject")) #return the key according to value
info.update({"City" : "Shahdadpur"})      #insert the specified items to the dictionary
print(info)

#----Question : Store following word meanings in a pyhton dictionary-----#
word_meaning = {
    "table" : ["a Piece of turniture", "list of fact & Figure "],
    "cat" : "a small animal"
}
print(word_meaning)
print(word_meaning.keys())

#-----Question : you are given a list of subjects foe students. Assume one classroom is required for 1 subject.How many classroom are needed by all students.
subject = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
    }
print(type(subject))
print(len(subject))


subject = {}
key1 = input("Enter a 1st subject Name : ")
mark1 = int(input("Enter a 1st "+key1+" subject Mark :"))
key2 = input("Enter a 2nd Subject Name : ")
mark2 = int(input("Enter a 2nd "+key2+" Subject Mark : "))

subject.update({key1 : mark1})
subject.update({key2 : mark2})
print(subject)
print(subject.keys())



set = {(9,9.0)}

val1  = 9
val2  = 9.0

#set.update(val2,val1)
print(set)
print(type(set))