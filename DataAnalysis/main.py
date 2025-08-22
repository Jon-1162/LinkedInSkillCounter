import pandas as pd

from linkedinjobs_csv2stats import coOccurrence, getSkillAllInstancesSumCount, getSkillCounts



def main():
    getSkillCounts()
    getSkillAllInstancesSumCount()
    coOccurrence()

if __name__ == "__main__":
    main()
    