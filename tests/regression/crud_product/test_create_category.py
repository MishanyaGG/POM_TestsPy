from queryDatabase.categories import Categories

def test_Exist_Category(driver):
    category = Categories()
    
    # TODO: привести к принципу пестицидов
    
    # Негативный сценарий
    assert category.isExistCategoryByName("Тест") == False
    
    # Позитивный сценарий
    assert category.isExistCategoryByName("Животные") == False