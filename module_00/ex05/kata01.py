kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

print(f'''Python was created by {kata['Python']}
Ruby was created by {kata.get('Ruby')}
PHP was created by {kata['PHP']}''')
