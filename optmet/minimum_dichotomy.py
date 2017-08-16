from optmet.function import Function, Domain


def find_minimum_dichotomy(func: Function, epsilon: float, delta: float) -> float:
    assert func.domain

    a0, b0 = func.domain
    domain_length = abs(func.domain)

    assert epsilon > 0
    assert delta > 0
    assert b0 > a0
    assert delta < domain_length

    next_domain = func.domain

    while domain_length > epsilon:
        a0, b0 = next_domain
        domain_length = abs(next_domain)

        domain_median = next_domain.median()
        x1 = domain_median - delta
        x2 = domain_median + delta
        y1 = func(x1)
        y2 = func(x2)

        if y1 < y2:
            next_domain = Domain(a0, x2)
        elif y1 > y2:
            next_domain = Domain(x1, b0)
        else:
            next_domain = Domain(x1, x2)

    return domain_median
