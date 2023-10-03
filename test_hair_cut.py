from hair_cut import hair_cut

def test_hair_cut():
    # Test case 1: Basic test case with provided input
    hairstyles1 = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
    prices1 = [30, 25, 40, 20, 20, 35, 50, 35]
    last_week1 = [2, 3, 5, 8, 4, 4, 6, 2]
    result1 = hair_cut(hairstyles1, prices1, last_week1)
    expected_output1 = (
        "Average Haircut Price: 31.88\n"
        "Average Daily Revenue: 155.00\n"
        "Total Revenue: 1085\n"
        "Prices reduced by 5: [25, 20, 35, 15, 15, 30, 45, 30]\n"
        "All cuts under 30: ['pixie', 'crew', 'bowl']"
    )
    assert result1 == expected_output1

    # Test case 2: All prices below 30
    hairstyles2 = ["style1", "style2", "style3"]
    prices2 = [25, 28, 29]
    last_week2 = [1, 2, 3]
    result2 = hair_cut(hairstyles2, prices2, last_week2)
    expected_output2 = (
        "Average Haircut Price: 27.33\n"
        "Average Daily Revenue: 24.00\n"
        "Total Revenue: 168\n"
        "Prices reduced by 5: [20, 23, 24]\n"
        "All cuts under 30: ['style1', 'style2', 'style3']"
    )
    assert result2 == expected_output2








