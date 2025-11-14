import os

class Config:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src_dir = os.path.join(current_dir, "src")

        directories = [
            src_dir,
            os.path.join(src_dir, "utils"),
            os.path.join(src_dir, "decryption"),
        ]

        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            init_file = os.path.join(directory, '__init__.py')
            if not os.path.exists(init_file):
                with open(init_file, 'w') as f:
                    f.write('# Package initialization\n')

if __name__ == "__main__":
    Config()