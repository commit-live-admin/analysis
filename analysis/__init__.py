import sys

from analysis.app import analyze

if __name__ == "__main__":
    # env = "prod"
    # accessToken = "60f126597ce4dccd7e716ed4ecf79c7b52a1d4c5"
    # hash = "hash"
    # titleSlugTestCase = "fsdse-title-slug"
    # filePath =  "/Users/sangam/Documents/greyatom/analysis/analysis/module.py"

    env = sys.argv[1]
    accessToken = sys.argv[2]
    hash = sys.argv[3]
    titleSlugTestCase = sys.argv[4]
    filePath = sys.argv[5]
    analyze(filePath, titleSlugTestCase, accessToken, env, hash)