letter = ''' Dear <|Name|>,
 You are selected!
 <|Date|> '''

print(letter.replace("<|Name|>", "Anamika").replace("<|Date|>","24 October 2025"))