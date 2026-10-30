from cases_ctp_def import ctp_cases


def all_cases():
    cs = ctp_cases()
    try:
        from cases_other_def import other_cases
        cs += other_cases()
    except ImportError:
        pass
    return cs
