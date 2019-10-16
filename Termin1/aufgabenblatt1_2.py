# erstellen der liste und entscheidung des indices
liste = list(range(1,10))
index = int(input("select an index"))

# aufteilen der liste
begin_list = liste[:index]
element = liste[index]
end_list = liste[(index+1):]

#zusammenfuegen der liste
result = begin_list[::-1]
result.append(element)
result.extend(end_list[::-1])

print(result)