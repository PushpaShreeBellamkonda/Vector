# union
s={5,8,2,9,7}
t={4,7,8,9,1,6}
print(s|t)
print(t|s)
print(s.union(t))
s.update(t)
print(s)
t.update(s)
print(t)
print(s&t)

# intersection
print("Intersection")
print(s.intersection(t))
print(t.intersection(s))
s.intersection_update(t)
print(s)
t.intersection_update(s)
print(t)

# Difference
print("Difference")
print(s-t)
print(t-s)
print(s.difference(t))
print(t.difference(s))
s.difference_update(t)
print(s)
t.difference_update(s)
print(t)

# symmetry
print("symmetry")
print(s^t)
print(t^s)
print(s.symmetric_difference(t))
print(t.symmetric_difference(s))
s.symmetric_difference_update(t)
print(s)
t.symmetric_difference_update(s)
print(t)

# subset
print("subset")
print(t. issubset(s))
print(t<s)

# Disjoint sets
print("disjoint")
print(s.isdisjoint(t))
print(t.isdisjoint(s))