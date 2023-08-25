

def check_solution(positions: list[tuple[int,int]]) -> bool:
    # frow == srow -> false
    # fcol == scol -> false
    # abs(srow - frow) = abs(fcol - scol) -> false
    
    for i, (frow, fcol) in enumerate(positions): # (0, (x, y)), (1, ())
        for j,(srow,scol) in enumerate(positions):
            if i == j:
                continue
            if frow == srow or fcol == scol or abs(srow - frow) == abs(fcol - scol):
                return False
    return True