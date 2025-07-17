original_string = " hello"
reversed_string = reversed(original_string)
print (reversed_string)

original_string = "hello"
reversed_string = ''.join (reversed(original_string))
print(reversed_string)

original_string = "hello"
reversed_string = reversed (original_string)
reversed_string_using_loop = ''
for i in reversed_string:
    reversed_string_using_loop  = reversed_string_using_loop + i
    print (reversed_string_using_loop)

def reverse_string(word):
    return ''.join(reversed(word))
def test_reverse_string():
    input_str = "TripleTen"
    reversed_str = reverse_string (input_str)
    assert reversed_str == "neTelpirT"

def reverse_string(word):
    return ''.join(reversed(word))
def test_reverse_string():
    input_str = "UrbanRoutes"
    reversed_str = reverse_string(input_str)
    assert reversed_str == 'setuoRnabrU'
    print ("test Passed !" + input_str + " ' s reverse is" + reversed_str)

def reverse_sting(word):
    return "".join (reversed (word))
def test_reverse_string():
    input_str = "TripleTen"
    reversed_str = reverse_string(input_str)
    assert reversed_str =="neTelpirT"
    print("test Passed !" + input_str + " ' s reverse is" + reversed_str)