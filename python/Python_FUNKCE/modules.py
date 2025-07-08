#the first way
#import function_greetings as a
#import function_guessing as b

#a.greeting("Medvěd")

#b.user_guessing_game(str(13),"stop")
#-----------------------------------------------
#the second way
from tests.test_saucedemo_shop.my_modules.function_greetings import greeting
from tests.test_saucedemo_shop.my_modules.function_guessing import user_guessing_game, name, Test

greeting("Medvěd")
user_guessing_game(str(13),"stop")
print(name)
print(Test.a)
test_obj = Test()
print(test_obj.a)