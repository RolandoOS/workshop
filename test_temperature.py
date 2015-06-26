import temperature as tmp

def test_f_to_k():
    assert tmp.f_to_k(32)==273.15
    assert tmp.f_to_k(212)==373.15
