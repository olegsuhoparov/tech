import string
from .generator import generate_string, generate_letter, alphanum_str, random_num

separators = [" ", ".", ",", ")", "]", "(", "[", "?", "!", "/", "\\", "'", "%", "^", "*", "_", ":", ";", "`", "~", "№"]

positive_suit = ("awe maria . gde mama mia .,nb][ ", "awe maria . gde mama mia", "awe maria . gde mama mia ",
                 "awe maria . gde mama mia    ", "awe maria . gde mama miam", "awe maria . gde mama miYAa",
                 "awe maria . gde mamaamiam ",
                 "aworhmrktorpekthkeoeltlgd", "aworhmrkt      t               ", "    ", "123123284755883929194556512",
                 generate_letter(string.printable), alphanum_str(2, 25), alphanum_str(2, 45, ru=True),
                 generate_string(string.ascii_letters, 25, 45), alphanum_str(45, 9999),
                 generate_string(string.printable, 45, 9999), "Everybody knows that cats likes",
                 "Volvo released a new car with the following spec: V6 236HP. It will cost $22647 and going to be...")

positive_suit_with_length = (
    (alphanum_str(11, 29), random_num(14, 26)), (alphanum_str(11, 29, ru=True), random_num(7, 11)),
    (alphanum_str(11, 29), random_num(29, 35)), (alphanum_str(65, 74), random_num(72, 81)))

negative_suit = ("", 124, ("ut", "ooh"), -2.4, ["dt@", 23, {"awek": 2351}], None, True)
