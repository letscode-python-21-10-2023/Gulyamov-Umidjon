"""Получите кортеж VLANов со строки:"""

config_sw1 = 'switchport trunk allowed vlan 10,20,30,40,50,70'
config_sw2 = 'switchport trunk allowed vlan 80,90,10,45,50,100'
nums1 = config_sw1.split()[-1].split(',')
nums2 = config_sw2.split()[-1].split(',')
set1, set2 = set(nums1), set(nums2)
print(tuple(set1.intersection(set2)))
print(tuple(set1.difference(set2)))
print(tuple(set1.symmetric_difference(set2)))
print(tuple(set1.union(set2)))
