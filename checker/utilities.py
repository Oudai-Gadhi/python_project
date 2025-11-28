# checker/utilities.py

def classify(score):
    score = float(score)
    if score >= 9.0:
        return "\033[91mCRITICAL\033[0m"  # Red
    elif score >= 7.0:
        return "\033[93mHIGH\033[0m"      # Yellow
    elif score >= 4.0:
        return "\033[33mMEDIUM\033[0m"    # Orange/Brown
    elif score >= 0.1:
        return "\033[92mLOW\033[0m"       # Green
    else:
        return "\033[90mNONE\033[0m"      # Gray


