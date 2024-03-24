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