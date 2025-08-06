import pandas as pd

from linkedinjobs_csv2stats import getSkillAllInstancesSumCount, getSkillCounts



def main():
    # df = pd.read_csv('linkedinjobs.csv')
    getSkillCounts()
    getSkillAllInstancesSumCount()

if __name__ == "__main__":
    
    main()