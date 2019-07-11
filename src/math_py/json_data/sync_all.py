from json_data import write_problems
from json_data import write_tasks
from json_data import write_summary_concepts
from json_data import write_summary_qtypes

def main():
    write_problems.main()
    write_tasks.main()
    write_summary_concepts.main()
    write_summary_qtypes.main()

if __name__ == '__main__': 
    main()