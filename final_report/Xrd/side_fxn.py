def _align(*sns):
    str_ = ""

    for sn in sns:
        if len(sn[0]) < sn[1]:
            n_ = sn[1] - len(sn[0])
            str_ += sn[0] + " " * n_

    return str_
