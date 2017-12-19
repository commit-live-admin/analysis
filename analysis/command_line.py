import sys
from analysis.app import analyze


def main():
    # env = "local"
    # accessToken = "0e431a22f0161e935fbf98791adb1880c96a635e"
    # hash = "cb717033-29eb-4b07-ba85-a0240551bc48"
    # titleSlugTestCase = "numpy_advanced_project:q01_get_total_deliveries_players"
    # filePath =  "/Users/sangam/Documents/greyatom/analysis/analysis/module.py"

    env = sys.argv[1]
    accessToken = sys.argv[2]
    hash = sys.argv[3]
    titleSlugTestCase = sys.argv[4]
    filePath = sys.argv[5]
    analyze(filePath, titleSlugTestCase, accessToken, env, hash)


main()