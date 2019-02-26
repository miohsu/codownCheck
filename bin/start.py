import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import main

if __name__ == '__main__':
    main.main()
