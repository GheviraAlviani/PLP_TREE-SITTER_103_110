(string) @string
(number) @number
(boolean) @constant.builtin
["=" "!=" ">" "<" ">=" "<="] @operator
["and" "or" "not" "in" "contains"] @keyword
(comparison field: (identifier) @property)
(in_expression field: (identifier) @property)
(contains_expression field: (identifier) @property)