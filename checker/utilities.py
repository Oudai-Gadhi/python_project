def classify (score):
    if score >= 9.0:
        return f"\033[{91}mCRITICAL\033[0m"
    elif score >= 7.0:
        return f"\033[{93}mHIGH\033[0m"
    elif score >= 4.0:
        return f"\033[{33}mMEDIUM\033[0m"
    elif score >= 0.1:
        return f"\033[{32}mLOW\033[0m"
    else:
        return f"\033[{25}mNONE\033[0m"


