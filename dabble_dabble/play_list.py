
test_subject = ['joe morningstar', 'lilly sadhouse', 'mary minow', 'frank epee']


#variant one
capitalizer = lambda x: x.upper()
sub_upper = list(map(capitalizer, test_subject))

print sub_upper

#variant_two (shortest)
sub_upper2 = [x.upper() for x in test_subject]
print sub_upper2

#variant_three
sub_upper3 = []
for x in test_subject:
    sub_upper3.append(x.upper())

print sub_upper3