def society_name(names):
 secret_name = ''.join(sorted([name[0] for name in names]))
 return secret_name

print(society_name(["Rupin","Riya","Lakshmi"]))
print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))