import os

class Config:
    def __init__(self):
        directories = [
            './src',
            './src/utils',
            './src/decryption',
        ]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            init_file = os.path.join(directory, '__init__.py')
            if not os.path.exists(init_file):
                with open(init_file, 'w') as f:
                    f.write('# Package initialization\n')
                print(f"Created: {init_file}")
            else:     print(f"Already exists: {init_file}")