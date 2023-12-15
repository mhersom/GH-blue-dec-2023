"""
Wednesday Coding Exercise
"""

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
counter = 0
sum = 0.0

for connect in connections:
    if connect[1] == 'Rome':
        counter += 1
        sum += connect[2]

print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes')
